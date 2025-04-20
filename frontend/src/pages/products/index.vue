<script setup lang="ts">
  import { useApi } from '@/composables/useApi';
import ProductsTable from '@/views/customers/ProductsTable.vue';

  const $api = useApi()
  const isLoading = ref(true)

  const servicesData = ref<Array<any>|null>(null)
  const totalData = ref<any|null>(null)
  const totalPagesCount = ref(0)
  const currentPage = ref(1)


  const loadData = (isResetPage = true) => {
    if (isResetPage) {
      currentPage.value = 1
    }
    isLoading.value = true
    let url = '/api/products/?page=' + currentPage.value
    $api.get(url)
      .then(response => {
        totalData.value = response.data
        servicesData.value = response.data.results
        totalPagesCount.value = response.data.total_pages
        isLoading.value = false
      })
  }

  const gotoPage = (pageNumber: number) => {
    currentPage.value = pageNumber
    loadData(false)
  }

  onMounted(() => {
    loadData()
  })
</script>

<template>
  <VRow>
    <VCol cols="12">
      <VCard title="Товары интернет магазина">
        <!-- <VCardText>
          You can show a dense version of the table by using the <code>density</code> prop.
        </VCardText> -->
        
        <VDivider class="mt-4" />

        <ProductsTable
          :current-page="currentPage"
          :is-loading="isLoading"
          :services-data="servicesData"
         />

         <VPagination v-if="totalPagesCount"
            @update:model-value="gotoPage"
            :model-value="currentPage"
            active-color="primary"
            :length="totalPagesCount"
            :total-visible="$vuetify.display.xs ? 1 : Math.min(totalPagesCount, 5)"
            class="my-8"
          />
        </VCard>
    </VCol>

  </VRow>
</template>
