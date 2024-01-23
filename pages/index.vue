<script setup>
</script>

<style lang="scss">
    #description{
        font-size: 1.5em;
    }

    @media (max-width: 576px) { 
        #description{
            font-size: 1.1em;
            padding: 1rem 1rem;
        }
    }
</style>

<template>
	<IContainer>
        <IRow id="description">
            <IColumn>
                <p>The &#127918; <b>Open Source Game Development (OSGD) Collection</b> is a curated list of freely available open-source game development resources that anyone can access. The purpose of the list is to serve as a central repository of open-source game development projects for anyone to discover, use, or contribute to.</p>
            </IColumn>
        </IRow>
		<Section category="Engines"></Section>
		<Section category="Code"></Section>
		<Section category="Art"></Section>
		<Section category="Audio"></Section>
		<Section category="Design"></Section>
        <Section category="Games"></Section>
    </IContainer>
</template>