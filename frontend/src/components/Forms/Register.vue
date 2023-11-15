<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useVuelidate } from '@vuelidate/core'
  import { email, required, minLength } from '@vuelidate/validators'
  import axios from 'axios'

  const router = useRouter()

  const isValid = ref(false)
  const showPassword = ref(false)
  // const dateMenuOpen = ref(false)

  const fields = ref({
    name: null,
    surname: null,
    age: null,
    dob: null,
    phone: null,
    address: null,
    city: null,
    email: null,
    password: null
  })

  const rules = {
    name: { required, minLengthValue: minLength(3) },
    surname: { required, minLengthValue: minLength(3) },
    // dob: { required },
    // phone: { required, minLengthValue: minLength(8) },
    // address: { required, minLengthValue: minLength(3) },
    // city: { required, minLengthValue: minLength(3) },
    email: { required, email },
    password: { required, minLengthValue: minLength(8) }
  }

  const v$ = useVuelidate(rules, fields)

  const register = async () => {
    const isValid = await v$.value.$validate()
    if (!isValid) return

    const formData = {
      email: fields.value.email,
      password: fields.value.password,
      first_name: fields.value.name,
      last_name: fields.value.surname
    }

    axios
      .post('/api/v1/users/', formData)
      .then(() => {
        alert('Registeration successful')
        router.push('/login')
      })
      .catch((error) => {
        alert(error)
        console.log(error)
      })
  }
</script>

<template>
  <v-form v-model="isValid">
    <v-row>
      <v-col>
        <v-text-field
          v-model="fields.name"
          :error-messages="v$.name.$errors.map((e:any) => e.$message)"
          label="Name"
          variant="solo-filled"
          @input="v$.name.$touch"
          @blur="v$.name.$touch"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          v-model="fields.surname"
          :error-messages="v$.surname.$errors.map((e:any) => e.$message)"
          label="Surname"
          variant="solo-filled"
          @input="v$.surname.$touch"
          @blur="v$.surname.$touch"
        />
      </v-col>
    </v-row>
    <!-- <v-row>
      <v-col>
        <v-menu
          v-model="dateMenuOpen"
          max-width="290px"
          min-width="290px"
          transition="scale-transition"
        >
          <template #activator="{ props }">
            <v-text-field
              v-model="fields.dob"
              v-bind="props"
              slot="activator"
              label="Date of Birth"
              variant="solo-filled"
              readonly
            />
          </template>
          <v-date-picker
            v-model="fields.dob"
            no-title
            @input="dateMenuOpen = false"
          />
        </v-menu>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          v-model="fields.address"
          :error-messages="v$.address.$errors.map((e:any) => e.$message)"
          label="Address"
          variant="solo-filled"
          @input="v$.address.$touch"
          @blur="v$.address.$touch"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          v-model="fields.city"
          :error-messages="v$.city.$errors.map((e:any) => e.$message)"
          label="City"
          variant="solo-filled"
          @input="v$.city.$touch"
          @blur="v$.city.$touch"
        />
      </v-col>
    </v-row> -->
    <v-row>
      <v-col>
        <v-text-field
          v-model="fields.email"
          :error-messages="v$.email.$errors.map((e:any) => e.$message)"
          label="Email"
          variant="solo-filled"
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
          @click:append="showPassword = !showPassword"
          @input="v$.password.$touch"
          @blur="v$.password.$touch"
        />
      </v-col>
    </v-row>
    <v-btn
      variant="text"
      class="me-4"
      @click="register"
    >
      Register
    </v-btn>
  </v-form>
</template>
