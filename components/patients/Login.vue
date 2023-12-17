<template>
  <section class="border border-cyan-600 my-12 mx-12 rounded-xl lg:mx-36">
    <div class="grid grid-cols-2 h-[750px]">
      <div class="image max-w-[700px] rounded-l-xl"></div>
      <div class="register flex flex-row px-6 max-w-[700px]">
        <div></div>
        <form
          class="mx-auto mt-6 flex flex-col items-center justify-around"
          @submit.prevent="chech_empty"
        >
          <h1 class="text-2xl text-gray-700">Pressure Sync Login</h1>
          <div class="flex flex-col gap-3 mx-auto mt-6">
            <UInput
              size="xl"
              color="cyan"
              placeholder="Email Address"
              icon="i-solar-letter-broken"
              v-model="login_user.email"
            />
            <UInput
              size="xl"
              color="cyan"
              placeholder="***"
              icon="i-solar-lock-password-bold-duotone"
              v-model="login_user.password"
            />
          </div>
          <div class="mt-12">
            <UButton
              class="bg-violet-400"
              icon="i-solar-map-arrow-right-bold-duotone"
              @click="login"
              :trailing="true"
            >
              Log In
            </UButton>
          </div>
          <div>Forgot Password?</div>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
let login_user = ref({ email: "", password: "" });

function ok_to_log() {
  let temp_user = visiting_user.value;
  if (temp_user.email === "" || temp_user.password === "") {
    console.log("either email or password is blank");
    return false;
  } else {
    return true;
  }
}

async function login() {
  try {
    let user = login_user.value;
    console.log(user);
    let response = await $fetch("http://localhost:8000/users/login", {
      method: "POST",
      body: JSON.stringify({ email: user.email, password: user.password }),
    });
    console.log({ email: user.email, password: user.password });
    console.log(response);
    if (response.code == 200) {
      navigateTo("/clients/123");
    } else {
      console.log("ridi");
    }
  } catch (error) {
    error ? console.log(error) : "";
  }

  let condition = false;
  if (!condition) {
  }
}
const headers = useRequestHeaders(["cookie"]);
async function login2() {
  console.log(headers);
  try {
    let user = login_user.value;
    console.log(user);
    let { data } = await useFetch("http://localhost:8000/users/login", {
      method: "POST",
      body: JSON.stringify({ email: user.email, password: user.password }),
      headers: { someheader: "mehrdad" },
    });
    console.log({ email: user.email, password: user.password });
  } catch (error) {
    error ? console.log(error) : "";
  }

  let condition = false;
  if (condition) {
  }
}
</script>

<style scoped>
.image {
  background-image: url("/login.jpeg");
  background-position: center;
  background-repeat: no-repeat;
}
</style>
