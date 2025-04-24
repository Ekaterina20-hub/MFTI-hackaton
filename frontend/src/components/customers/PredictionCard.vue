<template>
  <h2 class="h2 text-center my-8">
    Предсказание повторной покупки с помощью машинного обучения
  </h2>

  <template  v-for="predict in predictsData.predicts">
    <v-row class="mb-4">
      <v-col cols="12" md="6">
        <v-card outlined>
          <v-card-text class="text-center">
            <div class="text-h6 mb-2">Вероятность повторной покупки</div>
            <v-progress-circular
              :rotate="-90"
              :size="150"
              :width="15"
              :model-value="predictionProbability(predict)"
              color="primary"
              class="mb-2"
            >
              <span class="text-h4">{{ predictionProbability(predict) }}%</span>
            </v-progress-circular>
            <div class="text-caption">Модель: {{ predict.mlmodel.name }}</div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card outlined>
          <v-card-text>
            <div class="text-h6 mb-3">Метрики модели</div>
            <VChip label color="success" class="mr-2">
              Recall: {{ predict.mlmodel.recall_true }}%
            </VChip>
            <v-chip label color="primary" class="mr-2">
              Precision: {{ predict.mlmodel.precision_true }}%
            </v-chip>
            <v-chip label color="warning" class="mr-2">
              F1: {{ predict.mlmodel.f1_true }}%
            </v-chip>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Факторы влияния -->
    <v-card outlined class="mb-4">
      <v-card-title>
        Ключевые факторы влияния
        <div class="text-sm text-disabled">
          * Значимость факторов может превышать 100%, так как SHAP анализ показывает вклад в логарифм шансов, а не в вероятность.
        </div>
      </v-card-title>
      <v-card-text>
        <div v-for="(factor, index) in topFactors(predict)" :key="index" class="mb-3">
          <div class="d-flex justify-space-between mb-1">
            <span>
              {{ factor.name }}
              <span v-if="factor.property_value">({{ factor.property_value }})</span>
            </span>
            <span>{{ (factor.value * 100).toFixed(1) }}%</span>
          </div>
          <v-progress-linear
            :model-value="factor.value * 100"
            height="10"
            rounded
            color="primary"
            :max="factorMaximum(predict)"
          ></v-progress-linear>
        </div>
      </v-card-text>
    </v-card>
    <VDivider class="my-8" />

  </template>
  
  <!-- Все свойства -->
  <v-expansion-panels class="mb-4">
    <v-expansion-panel title="Все параметры клиента, используемые в предсказании">
      <v-expansion-panel-text>
        <v-list>
          <v-list-item
            v-for="(prop, index) in properties"
            :key="index"
          >
            <template v-slot:prepend>
              <v-icon icon="ri-question-line"></v-icon>
            </template>
            <v-list-item-title>{{ prop.name }}</v-list-item-title>
            <v-list-item-subtitle>
              {{ formatValue(prop.value) }}
            </v-list-item-subtitle>
          </v-list-item>
        </v-list>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script setup lang="ts">
import { computed } from 'vue';

interface Property {
  key: string
  name: string
  value: any
}

interface MLModel {
  name: string
  precision_true: number
  recall_true: number
  f1_true: number
  precision_false: number
  is_active: boolean
  is_main: boolean
}

interface Prediction {
  mlmodel: MLModel
  proba: number[]
  interpretations: {
    key: string
    name: string
    value: number
  }[][]
}

interface Props {
  predictsData: {
    properties: Property[]
    predicts: Prediction[]
  }
}

const props = defineProps<Props>()

const properties = computed(() => props.predictsData.properties)
const topFactors = computed(() => (predict: any) => {
  const factors = predict.interpretations[0]
  factors.forEach((factor: any) => {
    factor.property_value = properties.value.find(x => x.key == factor.key)?.value
  })
  return factors
})
const factorMaximum = computed(() => (predict: any) => {
  if (!topFactors.value || !topFactors.value(predict).length) {
    return 100
  }
  const values = topFactors.value(predict).map((x: any) => Math.floor(100 * x.value))
  return Math.max(...values)
})

const predictionProbability = computed(() => (predict: any) => {
  return (predict.proba[0] * 100).toFixed(1)
})

const formatValue = (value: any) => {
  if (typeof value === 'number') {
    return value.toFixed(value % 1 === 0 ? 0 : 2)
  }
  return value
}
</script>

<style scoped>
.prediction-card {
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.v-progress-circular {
  transition: all 0.5s ease;
}
</style>
