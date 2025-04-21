<script setup lang="ts">

import { useApi } from '@/composables/useApi';

const $api = useApi()
const $emit = defineEmits()
const $props = defineProps({
  mainMLModel: {
    type: Object,
    required: true
  }
})

const isLoading = ref(false)
const lazytimer = ref<number | undefined | ReturnType<typeof setTimeout>>(undefined)
const isShowDialog = ref(false)
const customersCount = ref<number | null>(null)
const current = ref({
  recall: 0,
  precision: 0,
  f1: 0,
  threshold: 0.5
})

const open = (initRecall: number | null) => {
  initRecall = initRecall ? initRecall : $props.mainMLModel.recall_true
  if (!initRecall) {
    initRecall = 10
  }
  const recall = initRecall - (initRecall % 5)
  current.value.recall = recall
  isShowDialog.value = true
  changeMetrica(recall, Metrics.Recall)
}

const tickLabels = computed(() => {
  const result = {} as any
  let index = 0
  for (let i = 5; i <= 95; i += 5) {
    if ([5, 25, 50, 75, 95].includes(i)) {
      result[i] = i + '%'
    }
  }
  return result
})

const Metrics = {
  Precision: 'precision',
  Recall: 'recall'
}

const changeMetrica = (value: number, metrica: string) => {
  const offset = $props.mainMLModel.metrics_offset[metrica + 's']
  const item = offset.find((x: any) => Math.round(100 * x.target) == value)
  if (metrica == Metrics.Recall) {
    current.value.precision = Math.round(100 * item.precision)
  }
  if (metrica == Metrics.Precision) {
    current.value.recall = Math.round(100 * item.recall)
  }
  current.value.f1 = Math.round(100 * item.f1)
  current.value.threshold = item.threshold

  lazyUpdate()

}

const updateCount = () => {
  if (!current.value.threshold)
    isLoading.value = true
  $api.get('/api/ml-models/customers/count?threshold=' + current.value.threshold)
    .then(response => {
      customersCount.value = response.data.count
      console.log(response.data)
      isLoading.value = false
    })
}

const lazyUpdate = () => {
  isLoading.value = true
  clearTimeout(lazytimer.value)
  lazytimer.value = setTimeout(() => {
    clearTimeout(lazytimer.value)
    lazytimer.value = undefined
    updateCount()
  }, 750)
}

const updateSearch = () => {
  $emit('update-search', current.value)
  isShowDialog.value = false
}

const clearSearch = () => {
  $emit('update-search', null)
  isShowDialog.value = false
}

defineExpose({ open })
</script>

<template>
  <VDialog v-model="isShowDialog" max-width="500">
    <template v-slot:default="{ isActive }">
      <VCard title="Фильтрация по вероятности повторных покупок">
        <VCardText>
          <VRow>
            <!-- <VCol cols="12" sm="12">
                    Моделью ML для каждого покупателя было сделано предсказание от 01.08.2018 на предмет, совершит ли тот
                    покупку в обозримое не определённое время.
                  </VCol> -->
            <VCol cols="12" sm="12">
              <!-- TODO: в отдельный компонент -->
              <h4 class="h4 d-flex">
                <span class="mr-auto">Массовость (Recall)</span>
                <span class="font-weight-semibold text-xl"
                  :class="current.recall >= 10 ? 'text-success' : 'text-error'">{{ current.recall }}%</span>
              </h4>
              <div class="text-caption">Как много будущих покупателей получится извлечь</div>
              <VSlider v-model="current.recall" :min="5" :max="95" :step="5" thumb-label show-ticks="always"
                :ticks="tickLabels" :color="current.recall >= 10 ? 'success' : 'error'" class="mb-4"
                @update:modelValue="changeMetrica($event, Metrics.Recall)">
              </VSlider>
            </VCol>
            <VCol cols="12" sm="12">
              <h4 class="h4 d-flex">
                <span class="mr-auto">Точность соответствия (Precision)</span>
                <span class="font-weight-semibold text-xl"
                  :class="current.precision >= 20 ? 'text-primary' : 'text-error'">{{ current.precision }}%</span>
              </h4>
              <div class="text-caption">Какая часть действительно совершат повторную покупку</div>
              <VSlider v-model="current.precision" :min="5" :max="95" :step="5" thumb-label show-ticks="always"
                :ticks="tickLabels" class="mb-4" :color="current.precision >= 20 ? 'primary' : 'error'"
                validate-on="lazy input" @update:modelValue="changeMetrica($event, Metrics.Precision)">
              </VSlider>
            </VCol>
            <VCol cols="12" sm="12">
              <h4 class="h4 d-flex">
                <span class="mr-auto">Баланс модели (F1)</span>
                <span class="font-weight-semibold text-xl" :class="current.f1 >= 10 ? 'text-secondary' : 'text-error'">{{
                  current.f1 }}%</span>
              </h4>
              <div class="text-caption">Оценка баланса между массовостью и точностью прогноза</div>
              <VSlider v-model="current.f1" :min="5" :max="95" :step="5" thumb-label show-ticks="always"
                :ticks="tickLabels" class="mb-4" :color="current.f1 >= 10 ? 'secondary' : 'error'" readonly>
              </VSlider>
            </VCol>
          </VRow>
          <div class="text-right mt-10">
            <VBtn size="large" color="white" :disabled="isLoading" @click="clearSearch" class="mr-2">
              Очистить
            </VBtn>
            <VBtn size="large" :disabled="isLoading" :loading="isLoading" @click="updateSearch">
              Показать {{ customersCount }} клиентов
            </VBtn>
          </div>

        </VCardText>

      </VCard>
    </template>
  </VDialog>
</template>
