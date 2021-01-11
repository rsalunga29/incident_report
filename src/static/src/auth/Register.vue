<template>
  <ValidationObserver v-slot="{ invalid, validated }">
    <div class="columns is-flex is-flex-direction-column is-align-items-center">
      <div
        class="column is-4"
        style="margin-top: -3.25rem;"
      >
        <div class="card has-background-light">
          <div class="card content p-3">
            <ValidationProvider
              name="name"
              rules="required"
              immediate
            >
              <b-field
                label="Full Name"
                slot-scope="{ errors, valid }"
                :type="valid ? 'is-success' : ''"
              >
                <b-input
                  type="name"
                  v-model="name"
                  :validation-message="errors[0]"
                />
              </b-field>
            </ValidationProvider>

            <ValidationProvider
              name="email"
              rules="required|email"
              immediate
            >
              <b-field
                label="Email"
                class="mt-3"
                slot-scope="{ errors, valid }"
                :type="valid ? 'is-success' : ''"
              >
                <b-input
                  type="email"
                  v-model="email"
                  :validation-message="errors[0]"
                />
              </b-field>
            </ValidationProvider>

            <ValidationProvider
              name="password"
              rules="required"
              immediate
            >
              <b-field
                label="Password"
                class="mt-3"
                slot-scope="{ errors, valid }"
                :type="valid ? 'is-success' : ''"
              >
                <b-input
                  type="password"
                  v-model="password"
                  :validation-message="errors[0]"
                />
              </b-field>
            </ValidationProvider>

            <b-button
              type="is-success is-fullwidth mt-3"
              :disabled="invalid || !validated"
              @click="register"
            >Register</b-button>

            <p class="is-size-7 has-text-centered mt-2">
              Already have an account?
              <router-link to="/auth/login">Login now</router-link>.
            </p>
          </div>
        </div>
      </div>
    </div>
  </ValidationObserver>
</template>

<script>
import { ValidationObserver, ValidationProvider, extend } from 'vee-validate';
import { required, email } from 'vee-validate/dist/rules';

extend('email', email);
extend('required', {
  ...required,
  message: 'This field is required.',
});

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },

  data() {
    return {
      name: '',
      email: '',
      password: '',
    };
  },

  methods: {
    register() {
      this.$store.dispatch('auth/register', {
        name: this.name,
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>
