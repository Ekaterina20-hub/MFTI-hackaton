<script setup lang="ts">

  import { useApi } from '@/composables/useApi';
import LoyaltyFilterDialog from '@/views/customers/LoyaltyFilterDialog.vue';

  import avatar1 from '@images/avatars/avatar-1.png';
import avatar2 from '@images/avatars/avatar-2.png';
import avatar3 from '@images/avatars/avatar-3.png';
import avatar4 from '@images/avatars/avatar-4.png';
import avatar5 from '@images/avatars/avatar-5.png';
import avatar6 from '@images/avatars/avatar-6.png';
import avatar7 from '@images/avatars/avatar-7.png';
import avatar8 from '@images/avatars/avatar-8.png';

  const $api = useApi()
  const isLoading = ref(true)
  const processingId = ref<number|null>(null)
  const servicesData = ref<Array<any>|null>(null)
  const totalData = ref<any|null>(null)
  const totalPagesCount = ref(0)
  const currentPage = ref(1)
  const MLModels = ref<Array<any>|null>(null)
  const mainMLModel = ref<any|null>(null)
  const metricaFilter = ref<any|null>(null)
  const loyaltyFilterDialog = ref<typeof LoyaltyFilterDialog|null>(null)

  const headers = [
    { title: 'Клиент', key: 'customer_unique_id' },
    { title: 'Штат', key: 'state_code' },
    { title: 'Всего заказов', key: 'orders_total' },
    { title: 'Последняя активность', key: 'last_activity' },
    { title: 'Actions', key: 'actions', sortable: false },
  ]

  const loadData = (isResetPage = true) => {
    if (isResetPage) {
      currentPage.value = 1
    }
    isLoading.value = true
    let url = '/api/customers/?page=' + currentPage.value
    console.log('metricaFilter.value', metricaFilter.value)
    if (metricaFilter.value) {
      url += '&threshold=' + metricaFilter.value.threshold
    }
    $api.get(url)
      .then(response => {
        totalData.value = response.data
        response.data.results.forEach((item: any) => {
          item.photo = getRundomPhoto()
        })
        servicesData.value = response.data.results
        // servicesData.value = []
        totalPagesCount.value = response.data.total_pages
        isLoading.value = false
      })
    $api.get('/api/ml-models/list')
      .then(response => {
        MLModels.value = response.data
        mainMLModel.value = MLModels.value?.find(x => x.is_main)
      })
  }

  const getRundomPhoto = () => {
    const photos = [avatar1, avatar2, avatar3, avatar4, avatar5, avatar6, avatar7, avatar8]
    return photos[Math.floor(Math.random() * photos.length)]
  }

  const isLoadedButEmpty = computed(() => {
    return !isLoading.value && (servicesData.value != null && !servicesData.value.length)
  })

  const gotoPage = (pageNumber: number) => {
    currentPage.value = pageNumber
    loadData(false)
  }

  const openFilterDialog = () => {
    loyaltyFilterDialog.value?.open(
      metricaFilter.value ? metricaFilter.value.recall : null
    )
  }

  onMounted(() => {
    loadData()
  })

</script>

<template>
  <VCard class="mb-6">

    <div class="d-flex flex-wrap items-center gap-4 ma-6">
      <h3>Клиенты интернет-магазина</h3>
      <VSpacer />
      <div class="d-flex gap-4 flex-wrap align-center">

        <VBtn
          :color="metricaFilter ? 'success' : 'primary'"
          prepend-icon="ri-search-line"
          :disabled="!mainMLModel"
          :loading="!mainMLModel"
          @click="openFilterDialog"
        >
          {{ metricaFilter 
            ? `Лояльность: массовость: ${metricaFilter.recall}%, точность: ${metricaFilter.precision}%` 
            : 'Фильтрация по уровню лояльности' }}
        </VBtn>
      </div>
    </div>

    <VDivider class="mt-4" />

    <VDataTableServer
      :items-per-page="15"
      :page="currentPage"
      :headers="headers"
      :items="servicesData ?? []"
      :loading="isLoading"
      :items-length="servicesData?.length ?? 0"
      class="text-no-wrap"
      :disable-sort="true"
      no-data-text="Клиенты не найдены"
    >
      <template #item.customer_unique_id="{ item }">
        <div class="d-flex align-center gap-x-4" style="min-width: 250px; line-height: 1.2;">
          <VAvatar
            size="38"
            variant="tonal"
            rounded
            :image="item.photo"
          />
          <div class="d-flex flex-column">
            <RouterLink :to="'/customers/' + item.id"
              style="white-space: wrap;"
            >
              {{ item.fullname }}
            </RouterLink>
            <span class="text-body-2">
              {{ item.customer_unique_id }}
            </span>
          </div>
        </div>
      </template>

      <!-- category -->
      <template #item.state_code="{ item }">
        <VChip class="text-uppercase">
          {{ item.state_code }}
        </VChip>
      </template>

      <template #item.orders_total="{ item }">
        <div class="text-center">
          {{ item.orders_total }}
        </div>
      </template>

      <template #item.actions="{ item }">
        <VBtn  icon="ri-eye-fill" :to="'/customers/' + item.id" variant="plain" />
      </template>
      <template #bottom>
      </template>
    </VDataTableServer>

    <VPagination v-if="totalPagesCount"
      @update:model-value="gotoPage"
      :model-value="currentPage"
      active-color="primary"
      :length="totalPagesCount"
      :total-visible="$vuetify.display.xs ? 1 : Math.min(totalPagesCount, 5)"
      class="my-8"
    />

  </VCard>

  <LoyaltyFilterDialog v-if="mainMLModel"
    ref="loyaltyFilterDialog"
    :main-m-l-model="mainMLModel"
    @update-search="metricaFilter = $event; loadData()"
  />
</template>
