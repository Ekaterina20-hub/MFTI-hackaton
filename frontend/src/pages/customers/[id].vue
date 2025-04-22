<script lang="ts" setup>
import CustomerAbout from '@/components/customers/CustomerAbout.vue';
import PredictionCard from '@/components/customers/PredictionCard.vue';
import ReviewItem from '@/components/reviews/ReviewItem.vue';
import { useApi } from '@/composables/useApi';
import ProductsTable from '@/views/customers/ProductsTable.vue';
import avatar1 from '@images/avatars/avatar-1.png';
import { useRoute } from 'vue-router';

const route = useRoute()

const $api = useApi()
const $route = useRoute()
const $router = useRouter()
const isLoading = ref(true)
const activeTab = ref(route.params.tab)
const customerProfile = ref<any|null>(null)
const customerId = ref<number|null>($route.params.id ? Number($route.params.id) : null)
const MLModels = ref<Array<any>|null>(null)
const mainMLModel = ref<any|null>(null)
const predictsData = ref<any|null>(null)

// tabs
const tabs = [
  { title: 'О клинете', icon: 'ri-group-line', tab: 'account' },
  // { title: 'Исследования', icon: 'ri-lock-line', tab: 'security' },
  // { title: 'Предсказания ML моделей', icon: 'ri-notification-3-line', tab: 'notification' },
]

const loadData = () => {
  isLoading.value = true
  // if (metricaFilter.value) {
  //   url += '&threshold=' + metricaFilter.value.threshold
  // }
  $api.get(`/api/customers/${customerId.value}/`)
    .then(response => {
      response.data.photo = avatar1
      customerProfile.value = response.data
      isLoading.value = false
    })
  $api.get('/api/ml-models/list')
    .then(response => {
      MLModels.value = response.data
      mainMLModel.value = MLModels.value?.find(x => x.is_main)
    })
  $api.get(`/api/customers/${customerId.value}/predict`)
    .then(response => {
      predictsData.value = response.data
    })

}

  onMounted(() => {
    loadData()
  })

</script>

<template>

  <CustomerAbout :customerProfile="customerProfile" />

  <div v-if="!predictsData" class="d-flex my-8 mx-auto">
    <VProgressCircular
      indeterminate
    />
    <label class="ml-2 mt-1">Загрузка предсказаний модели...</label>
  </div>

  <PredictionCard v-if="predictsData" :predictsData="predictsData" class="mb-6" />

  <VCard title="Купленные товары:" class="mb-6">
    <ProductsTable
      :current-page="1"
      :services-data="customerProfile?.products"
      :is-loading="isLoading"
    />
  </VCard>

  <VCard title="Отзывы покупателя:" class="mb-6">
    <VCardText v-if="customerProfile">
      <VList class="card-list d-flex flex-wrap">
        <ReviewItem v-for="review in customerProfile.reviews"
          :key="review.review_id"
          :review="review"
          :default-customer="customerProfile"
          style="max-width: 500px; min-width: 50%;"
        />
      </VList>
    </VCardText>
  </VCard>

</template>
