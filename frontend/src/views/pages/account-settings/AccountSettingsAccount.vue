<script lang="ts" setup>
import AbcAnalysisCard from '@/components/analyzes/AbcAnalysisCard.vue';
import ProductsTable from '@/views/customers/ProductsTable.vue';
import avatar1 from '@images/avatars/avatar-1.png';

const $props = defineProps({
  customerProfile: {
    type: Object,
    default: null
  }
})

const accountData = {
  avatarImg: avatar1,
  firstName: 'john',
  lastName: 'Doe',
  email: 'johnDoe@example.com',
  org: 'ThemeSelection',
  phone: '+1 (917) 543-9876',
  address: '123 Main St, New York, NY 10001',
  state: 'New York',
  zip: '10001',
  country: 'USA',
  language: 'English',
  timezone: '(GMT-11:00) International Date Line West',
  currency: 'USD',
}

const refInputEl = ref<HTMLElement>()

const accountDataLocal = ref(structuredClone(accountData))
const isAccountDeactivated = ref(false)

const resetForm = () => {
  accountDataLocal.value = structuredClone(accountData)
}

// changeAvatar function
const changeAvatar = (file: Event) => {
  const fileReader = new FileReader()
  const { files } = file.target as HTMLInputElement

  if (files && files.length) {
    fileReader.readAsDataURL(files[0])
    fileReader.onload = () => {
      if (typeof fileReader.result === 'string')
        accountDataLocal.value.avatarImg = fileReader.result
    }
  }
}

// reset avatar image
const resetAvatar = () => {
  accountDataLocal.value.avatarImg = accountData.avatarImg
}

const timezones = [
  '(GMT-11:00) International Date Line West',
  '(GMT-11:00) Midway Island',
  '(GMT-10:00) Hawaii',
  '(GMT-09:00) Alaska',
  '(GMT-08:00) Pacific Time (US & Canada)',
  '(GMT-08:00) Tijuana',
  '(GMT-07:00) Arizona',
  '(GMT-07:00) Chihuahua',
  '(GMT-07:00) La Paz',
  '(GMT-07:00) Mazatlan',
  '(GMT-07:00) Mountain Time (US & Canada)',
  '(GMT-06:00) Central America',
  '(GMT-06:00) Central Time (US & Canada)',
  '(GMT-06:00) Guadalajara',
  '(GMT-06:00) Mexico City',
  '(GMT-06:00) Monterrey',
  '(GMT-06:00) Saskatchewan',
  '(GMT-05:00) Bogota',
  '(GMT-05:00) Eastern Time (US & Canada)',
  '(GMT-05:00) Indiana (East)',
  '(GMT-05:00) Lima',
  '(GMT-05:00) Quito',
  '(GMT-04:00) Atlantic Time (Canada)',
  '(GMT-04:00) Caracas',
  '(GMT-04:00) La Paz',
  '(GMT-04:00) Santiago',
  '(GMT-03:30) Newfoundland',
  '(GMT-03:00) Brasilia',
  '(GMT-03:00) Buenos Aires',
  '(GMT-03:00) Georgetown',
  '(GMT-03:00) Greenland',
  '(GMT-02:00) Mid-Atlantic',
  '(GMT-01:00) Azores',
  '(GMT-01:00) Cape Verde Is.',
  '(GMT+00:00) Casablanca',
  '(GMT+00:00) Dublin',
  '(GMT+00:00) Edinburgh',
  '(GMT+00:00) Lisbon',
  '(GMT+00:00) London',
]

const currencies = [
  'USD',
  'EUR',
  'GBP',
  'AUD',
  'BRL',
  'CAD',
  'CNY',
  'CZK',
  'DKK',
  'HKD',
  'HUF',
  'INR',
]
</script>

<template>
  <VRow>
    <VCol cols="12">
      <VCard title="Информация о клиенте">
        <v-progress-linear
          :active="!customerProfile"
          :indeterminate="!customerProfile"
          color="primary"
          absolute
          bottom
          :height="3"
        ></v-progress-linear>

        <VCardText v-if="customerProfile" class="d-flex">

          <div class="d-flex mr-auto">
            <!-- 👉 Avatar -->
            <VAvatar
              rounded="lg"
              size="100"
              class="me-6"
              :image="accountDataLocal.avatarImg"
            />

            <!-- 👉 Upload Photo -->
            <div class="d-flex flex-column justify-center gap-1">
              <h3 class="h3 mb-0">
                {{ customerProfile.fullname }}
                <sup class="text-sm text-disabled">Имя генерируется случайно</sup>
              </h3>

              <p class="text-body-1 mb-0">
                {{ customerProfile.customer_unique_id }}
              </p>
              <p class="text-primary">
                Последняя активность: {{ customerProfile.last_activity }}
              </p>
            </div>
          </div>
          <div>
            <VChip color="success">Всего заказов: {{ customerProfile.orders_total }}</VChip>
          </div>
          </VCardText>

        <VDivider />

        <VCardTitle v-if="customerProfile" class="mt-4">
          Основные параметры:
        </VCardTitle>
        <VCardText v-if="customerProfile">

          <AbcAnalysisCard :abc-analysis="customerProfile.abc_analysis" />

          <h4 class="h4 mt-4 mb-2">Купленные товары:</h4>

          <ProductsTable 
            :current-page="1"
            :services-data="customerProfile.products"
            :is-loading="false"
          />

        </VCardText>
      </VCard>
    </VCol>
  </VRow>
</template>
