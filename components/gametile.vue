<script setup lang="ts">
    const props = defineProps({
        repo: {
            type: Object,
            required: true
        },
    });

    const supabase = useSupabaseClient()
    var repo = {
        "name": props.repo.name,
        "owner": props.repo.owner,
        "repo_url": "",
        "owner_url": "",
        "description": "test desc",
        "stars": 0,
        "issues": 0,
        "language": "JavaScript"
    }
    
    const { data: repList } = await useAsyncData(props.repo.name, async () => {
        const { data } = await supabase.from('repos').select().eq('name', props.repo.name)
        return data
    })

    if (repList.value?.length !== 0){
        const gitRepo = repList.value![0]
        
        const { data, error } = await useGithubData(`repos/${props.repo.owner}/${props.repo.name}`, {
            headers: {
                "If-Modified-Since": props.repo.last_read
            }
        })

        // Error handling
        //console.debug(`------ ${props.repo.name}, ${props.repo.owner} ------`)
        if (error.value !== null) {
            console.error(error.value)
        } else if (data.value === undefined) {
            repo = gitRepo
        } else if (data.value !== undefined) {
            //console.log(`${props.repo.name} loaded from GitHub`)
            repo = repositoryFormat(data.value)
            databaseUpdate(repo, false)
        }
    } else {
        const { data, error } = await useGithubData(`repos/${props.repo.owner}/${props.repo.name}`)

        // Error handling
        //console.debug(`------ ${props.repo.name}, ${props.repo.owner} ------`)
        if (error.value !== null) {
            console.error(error.value)
        } else if (data.value === undefined) {
            console.error(`${props.repo.name} unable to be loaded from GitHub`)
        } else if (data.value !== undefined) {
            //console.log(`${props.repo.name} loaded from GitHub for first time, pushing to database`)
            repo = repositoryFormat(data.value)
            databaseUpdate(repo, true)
        }
    }

    async function databaseUpdate(repo: any, write: boolean) {
        // Update `repos` database with repository information
        if (write) {
            const { error: read_error } = await useAsyncData(props.repo.name + "_insert", async () => {
                const { error } = await supabase.from('repos').insert(repo)
                return error
            })
            if (read_error.value !== null) {
                console.error(read_error.value)
            }
        } else {
            const { error } = await supabase.from('repos').update(repo).eq('name', props.repo.name)
            
            if (error !== null) {
                console.error(error)
            }
        }

        // Update `repoList` database with last_read information
        const date = new Date()
        const { error } = await supabase.from('repoList').update({ "last_read": date.toUTCString() }).eq('name', props.repo.name)
        
        if (error !== null) {
            console.error(error)
        }
    }

    function repositoryFormat(source: any) {
        return {
            "name": source.name,
            "owner": source.owner.login,
            "repo_url": source.html_url,
            "owner_url": source.owner.html_url,
            "description": source.description,
            "stars": source.watchers_count,
            "issues": source.open_issues_count,
            "language": source.language,
        }
    }

</script>

<style scoped>
    .link{
        text-decoration: none;
        color: inherit;
    }

    .stats{
        display: flex;
        justify-content: space-around;
        align-items: flex-end;
    }

    .card{
        height: 20em;
        width: 20em;
    }

    .truncate {
        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
</style>

<template>
    <ICard class="card" color="dark">
        <template #header>
            <h4><a :href="repo.repo_url" target="_blank" class="link">{{ repo.name }}</a></h4>
            <h6><a :href="repo.owner_url" target="_blank" class="link">{{ repo.owner }}</a></h6>
        </template>

        <p class="truncate">{{ repo.description }}</p>

        <template #footer>
            <div class="stats">
                <div>&#11088; {{ repo.stars }}</div>
                <div>&#128681; {{ repo.issues }}</div>
                <i-badge color="primary">{{repo.language}}</i-badge>
            </div>
        </template>
    </ICard>
</template>