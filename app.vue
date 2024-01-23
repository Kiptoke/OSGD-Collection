<template>
	<ILayoutHeader style="margin-bottom: 5ch">
		<Navigation/>
	</ILayoutHeader>
	<ILayoutContent>
		<NuxtPage></NuxtPage>
	</ILayoutContent>
	<ILayoutFooter>
		<OsgdFooter/>
	</ILayoutFooter>
</template>

<script setup lang="ts">
useHead({
  title: 'Open Source Game Dev Collection',
  meta: [
    { name: 'description', content: 'The Open Source Game Development (OSGD) Collection is a curated list of freely available open-source game development resources that anyone can access.' }
  ],
})
useSeoMeta({
  title: 'Open Source Game Dev Collection',
  ogTitle: 'Open Source Game Dev Collection',
  description: 'The Open Source Game Development (OSGD) Collection is a curated list of freely available open-source game development resources that anyone can access.',
  ogDescription: 'The Open Source Game Development (OSGD) Collection is a curated list of freely available open-source game development resources that anyone can access.'
})
</script>