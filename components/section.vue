<script setup>
    const props = defineProps({
        category: String
    })

    const supabase = useSupabaseClient()
    
    const { data: repos } = await useAsyncData(props.category, async () => {
        const { data } = await supabase.from('repoList').select().eq('category', props.category.toLowerCase())
        return data
    })
</script>

<template>
    <div class="d5">{{ category }}</div>
    <div class="grid-container">
        <template v-for="re in repos">
            <Gametile :repo=re class="grid-item"></Gametile>
        </template>
    </div>
</template>

<style scoped>
.grid-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-content: space-between;
  border: 1px solid gray;
  border-radius: 10px;
  margin-bottom: 2vh;
}
.grid-item {
  padding: 20px;
  flex-grow: 0;
}
</style>