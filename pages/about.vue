<script>
export default {
    data() {
        return {
            open: ['2.0']
        };
    }
};
</script>

<template>
	<IContainer>
        <IRow>
            <IColumn class="content">
                <div class="d3">About the OSGD</div>
        
                <div>
                    <p>Hello there, fellow developer!</p>
                    <p>My name's <b>Andrew</b>, and I'm the curator of the <b>Open Source Game Development Collection</b>, abbreviated as the OSGD. I created the OSGD to be a centralized, clean, and easily accessible collection of free and open source game development projects, applications, and material. But ultimately, the main issue I wanted to solve was <i>discoverability</i>. It is suprisingly hard to discover new repositories and projects on GitHub without any prior knowledge of what you're looking for. That's what I want to OSGD to help solve - to help bring cool new projects into the spotlight and make them easily accessible to all game devs.</p>
                    <p>The OSGD, of course, is also free and open-source. If you'd like to contribute to the site or want to suggest an addition to the list, I'd certainly appreciate the help! To do so, check out our <a href="contribute">contribution page</a>.</p>
                    <p>Want to know more about me? Feel free to check out my <a href="https://kiptoke.com" target="_blank">personal website</a>.</p>
                </div>

                <h2>What's Next?</h2>
                <div>
                    <p>I have plenty more ideas and future plans to make the OSGD a better, more useful, and more accessible site for all developers. Planned additions include:</p>
                    <ul>
                        <li>Adding in functionality for non-GitHub repositories</li>
                        <li>Adding a full list of all repositories that can be sorted and filtered</li>
                        <li>Color-coding for the specific categories</li>
                        <li>Learning how to properly make a CSS grid, for once</li>
                        <li>Better metrics visualization - project activity, OS availability, etc</li>
                        <li>Improving performance of the main page</li>
                    </ul>  
                </div>
                
                <h1>OSGD Changelog</h1>
                <ICollapsible size="sm" v-model="open">
                    <ICollapsibleItem name="2.0">
                        <template #header><div><b>Version 2.0</b> - <i>January 22, 2024</i></div></template>
                        <ul>
                            <li>
                                Completely re-vamped the site with Vue 3 and a new backend - a project I've been procrastinating on for <b>TWO YEARS</b>
                                <ul>
                                    <li>Previously the site was updated with a Python script that ran every day via GitHub Actions - this required a JSON file to be pushed to the repo, which would then trigger an automated build. If you're wondering why this project has <i>860+</i> commits, that's why...</li>
                                    <li>Now, the site runs off Supabase, which hosts a PostgreSQL table of the repositories.</li>
                                    <li>We also now have it so that the site checks GitHub on page load, so now you'll have the most accurate data.</li>
                                </ul>
                            </li>
                            <li>Replaced the UI component library from Bootstrap to Inkline.</li>
                            <li>Pruned some old repositories that no longer exist.</li>
                            <li>Added in new entries.</li>
                            <li>Removed link to Twitter.</li>
                            <li>If you're visiting for the 2024 Global Game Jam, hello!</li>
                        </ul>
                    </ICollapsibleItem>
                    <ICollapsibleItem name="1.1">
                        <template #header><div><b>Version 1.1</b> - <i>March 28, 2022</i></div></template>
                        <ul>
                            <li>Added in new entries</li>
                            <li>Fixed navbar menu not working in mobile</li>
                            <li>Better readability on mobile devices</li>
                            <li>Updated "What's Next" priorities</li>
                            <li>If you're visiting from the Open Source Roundtable at GDC 2022, hello!</li>
                        </ul>
                    </ICollapsibleItem>
                    <ICollapsibleItem name="1.0">
                        <template #header><div><b>Version 1.0</b> - <i>February 23, 2022</i></div></template>
                        <ul>
                            <li>Added in initial list of repositories</li>
                            <li>Created basic site layout</li>
                            <li>The OSGD goes live!</li>
                        </ul>
                    </ICollapsibleItem>
                </ICollapsible>
            </IColumn>
        </IRow>
    </IContainer>
</template>