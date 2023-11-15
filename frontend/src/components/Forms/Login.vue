<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useVuelidate } from '@vuelidate/core'
  import { email, required, minLength } from '@vuelidate/validators'
  import axios from 'axios'
  import { useAppStore } from '@/store/app'

  const appStore = useAppStore()
  const router = useRouter()

  const showPassword = ref(false)

  const fields = ref({ email: '', password: '' })

  const rules = {
    email: { required, email },
    password: { required, minLengthValue: minLength(8) }
  }

  const v$ = useVuelidate(rules, fields)

  const submit = async () => {
    const isValid = await v$.value.$validate()
    if (!isValid) return

    localStorage.removeItem('token')
    axios.defaults.headers.Authorization = ''

    const formData = {
      email: fields.value.email.toLowerCase(),
      password: fields.value.password
    }
    axios
      .post('/api/v1/token/login', formData)
      .then(({ data }) => {
        const token = data.auth_token

        appStore.user.token = token
        appStore.isLoggedIn = true
        axios.defaults.headers.Authorization = 'Token ' + token
        localStorage.setItem('token', token)

        router.push('/account')
      })
      .catch((error) => {
        alert(error)
        console.log(error)
      })
  }
</script>

<template>
  <v-form>
    <v-row>
      <v-col>
        <v-text-field
          v-model="fields.email"
          :error-messages="v$.email.$errors.map((e:any) => e.$message)"
          label="Email"
          variant="solo-filled"
          @keyup.native.enter="submit"
          @input="v$.email.$touch"
          @blur="v$.email.$touch"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          v-model="fields.password"
          :error-messages="v$.password.$errors.map((e:any) => e.$message)"
          label="Password"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :type="showPassword ? 'text' : 'password'"
          variant="solo-filled"
          @keyup.native.enter="submit"
          @click:append="showPassword = !showPassword"
          @input="v$.password.$touch"
          @blur="v$.password.$touch"
        />
      </v-col>
    </v-row>

    <v-btn
      variant="text"
      class="me-4"
      to="/register"
    >
      Register
    </v-btn>
    <v-btn
      variant="text"
      class="me-4"
      @click.prevent="submit"
    >
      Login
    </v-btn>
  </v-form>
</template>
