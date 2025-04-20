export const routes = [
  { path: '/' },
  {
    path: '/',
    component: () => import('@/layouts/default.vue'),
    children: [
      {
        path: '',
        component: () => import('@/pages/dashboard.vue'),
      },
      {
        path: 'analyzes/datalens/general',
        component: () => import('@/pages/analyzes/datalens/general.vue'),
      },
      {
        path: 'analyzes/abc-xyz',
        component: () => import('@/pages/analyzes/abc-xyz.vue'),
      },
      {
        path: 'analyzes/datalens/xyz',
        component: () => import('@/pages/analyzes/datalens/xyz.vue'),
      },
      {
        path: 'analyzes/datalens/abc',
        component: () => import('@/pages/analyzes/datalens/abc.vue'),
      },
      {
        path: 'analyzes/rfm',
        component: () => import('@/pages/analyzes/rfm.vue'),
      },
      {
        path: 'analyzes/geolocation',
        component: () => import('@/pages/analyzes/geolocation.vue'),
      },
      {
        path: 'analyzes/cohort',
        component: () => import('@/pages/analyzes/cohort.vue'),
      },
      {
        path: 'analyzes/nlp',
        component: () => import('@/pages/analyzes/nlp.vue'),
      },
      {
        path: 'analyzes/cluster',
        component: () => import('@/pages/analyzes/cluster.vue'),
      },
      {
        path: 'analyzes/k-means',
        component: () => import('@/pages/analyzes/k-means.vue'),
      },
      {
        path: 'ml-models/time-machine',
        component: () => import('@/pages/ml-models/time-machine.vue'),
      },
      {
        path: 'customers',
        component: () => import('@/pages/customers/index.vue'),
      },
      {
        path: 'about/dataset',
        component: () => import('@/pages/about/dataset.vue'),
      },

      {
        path: 'customers/:id',
        component: () => import('@/pages/customers/[id].vue'),
      },
      {
        path: 'typography',
        component: () => import('@/pages/typography.vue'),
      },
      {
        path: 'icons',
        component: () => import('@/pages/icons.vue'),
      },
      {
        path: 'cards',
        component: () => import('@/pages/cards.vue'),
      },
      {
        path: 'products',
        component: () => import('@/pages/products/index.vue'),
      },
      {
        path: 'form-layouts',
        component: () => import('@/pages/form-layouts.vue'),
      },
    ],
  },
  {
    path: '/',
    component: () => import('@/layouts/blank.vue'),
    children: [
      {
        path: 'login',
        component: () => import('@/pages/login.vue'),
      },
      {
        path: 'register',
        component: () => import('@/pages/register.vue'),
      },
      {
        path: '/:pathMatch(.*)*',
        component: () => import('@/pages/[...error].vue'),
      },
    ],
  },
]
