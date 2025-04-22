<template>
  <h2 class="h2 text-center my-8">
    Предсказание повторной покупки с помощью машинного обучения
  </h2>
  <v-row class="mb-4">
    <v-col cols="12" md="6">
      <v-card outlined>
        <v-card-text class="text-center">
          <div class="text-h6 mb-2">Вероятность повторной покупки</div>
          <v-progress-circular
            :rotate="-90"
            :size="150"
            :width="15"
            :model-value="predictionProbability"
            color="primary"
            class="mb-2"
          >
            <span class="text-h4">{{ predictionProbability }}%</span>
          </v-progress-circular>
          <div class="text-caption">Модель: {{ activeModel.name }}</div>
        </v-card-text>
      </v-card>
    </v-col>

    <v-col cols="12" md="6">
      <v-card outlined>
        <v-card-text>
          <div class="text-h6 mb-3">Метрики модели</div>
          <VChip label color="success" class="mr-2">
            Recall: {{ activeModel.recall_true }}%
          </VChip>
          <v-chip label color="primary" class="mr-2">
            Precision: {{ activeModel.precision_true }}%
          </v-chip>
          <v-chip label color="warning" class="mr-2">
            F1: {{ activeModel.f1_true }}%
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
      <div v-for="(factor, index) in topFactors" :key="index" class="mb-3">
        <div class="d-flex justify-space-between mb-1">
          <span>{{ factor.name }}</span>
          <span>{{ (factor.value * 100).toFixed(1) }}%</span>
        </div>
        <v-progress-linear
          :model-value="factor.value * 100"
          height="10"
          rounded
          :max="factorMaximum"
        ></v-progress-linear>
      </div>
    </v-card-text>
  </v-card>

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

const activeModel = computed(() => props.predictsData.predicts[0].mlmodel)
const predictionProbability = computed(() => (props.predictsData.predicts[0].proba[0] * 100).toFixed(1))
const properties = computed(() => props.predictsData.properties)
const topFactors = computed(() => props.predictsData.predicts[0].interpretations[0])
const factorMaximum = computed(() => {
  if (!topFactors.value || !topFactors.value.length) {
    return 100
  }
  const values = topFactors.value.map(x => Math.floor(100 * x.value))
  return Math.max(...values)
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
