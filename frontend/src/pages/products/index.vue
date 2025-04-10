<script setup lang="ts">
  import { useApi } from '@/composables/useApi';

  const $api = useApi()
  const isLoading = ref(true)

  const servicesData = ref<Array<any>|null>(null)
  const totalData = ref<any|null>(null)
  const totalPagesCount = ref(0)
  const currentPage = ref(1)

  const headers = [
    { title: 'Наименование категории', key: 'product_category_name' },
    { title: 'Размер', key: 'product_length_cm' },
    { title: 'Количество фотографий', key: 'product_photos_qty' },
    { title: 'ABC', key: 'abc' },
    { title: 'XYZ', key: 'xyz' },
  ]

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
            <template #item.product_category_name="{ item }">
              <div class="d-flex align-center gap-x-4" style="min-width: 250px; line-height: 1.2;">
                <div class="d-flex flex-column">
                  <a class="text-capitalize"
                    style="white-space: wrap;"
                  >
                    {{ item.product_category_name }}
                </a>
                  <span class="text-body-2">
                    {{ item.product_id }}
                  </span>
                </div>
              </div>
            </template>

            <!-- category -->
            <template #item.abc="{ item }">
              <VChip color="success" class="text-uppercase">
                A
              </VChip>
            </template>

            <template #item.xyz="{ item }">
              <VChip color="primary" class="text-uppercase">
                X
              </VChip>
            </template>

            <template #item.product_photos_qty="{ item }">
              <div class="text-center">
                {{ item.product_photos_qty }}
              </div>
            </template>

            <template #item.product_length_cm="{ item }">
              <div class="text-center">
                {{ item.product_length_cm }}
                x
                {{ item.product_height_cm }}
                x
                {{ item.product_width_cm }}
              </div>
            </template>

            <!-- Actions -->
            <template #item.actions="{ item }">
              <!-- <IconBtn>
                <VIcon icon="ri-edit-2-fill" :to="'/account/service/' + item.id" />
              </IconBtn> -->
              <VBtn  icon="ri-edit-2-fill" :to="'/customers/' + item.id" variant="plain" />
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
    </VCol>

  </VRow>
</template>
