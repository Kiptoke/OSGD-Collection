<template>
	<IContainer>
        <IRow>
            <IColumn class="content">
                <div class="d3">Contribute to the OSGD</div>
                
                <p>The OSGD is an ever-evolving and changing site - I'm always on the lookout for cool new projects, and I'd be glad to get help from the larger game development community! If you have a suggestion of a new project to add to the OSGD, changes you'd like to see implemented in the site, or any adjustments to the OSGD overall, please feel free to open up an issue on the project's GitHub and let me know!</p>
                
                <h1>Changes to the OSGD List</h1>

                <p>Want to add, remove, or change an entry in the OSGD list? Then please feel free to create an issue in the OSGD's GitHub repository in order to do so! Note that all proposed changes to the OSGD are subject to review before being accepted.</p>
                <p>If you're interested in <i>adding</i> an entry into the OSGD, be sure to help me by placing the project into one of these 6 categories:</p>
                <ul>
                    <li><b>Game Engine</b></li>
                    <li><b>Code</b></li>
                    <li><b>Art</b></li>
                    <li><b>Audio</b></li>
                    <li><b>Design</b></li>
                    <li><b>Games</b></li>
                </ul>
                
                <p>Additionally, make sure that the project meets the OSGD requirements:</p>
                <ul>
                    <li>The project must be freely available to build and modify - having standalone paid version (like Aseprite) is fine, as long as people can freely access the repository and build their own version.</li>
                    <li>The project cannot directly be involved with cryptocurrency and/or NFTs.</li>
                    <li>The project's code must be hosted on GitHub.</li>
                </ul>
                
                <IAlert color="info" style="margin-bottom: 1.5em;">
                    <template #icon>
                        <IIcon name="ink-info" />
                    </template>
                    While not a <i>strict</i> requirement, I would prefer to include repositories with around 1000+ stars on GitHub. Usually, this is an indication that the project is active and supported by the community.
                </IAlert>
                
                <p><IButton color="primary" href="https://github.com/Kiptoke/OSGD-Collection/issues/new/choose">Submit a Change to the OSGD</IButton></p>

                <h1>Changes to the Website</h1>
                <p>Want to suggest a cool new feature or even help me develop the OSGD site? Feel free to take a look at the <a href="https://github.com/Kiptoke/OSGD-Collection/issues" target="_blank">issues page</a> in the OSGD repository. There, you can either take on a proposed change to the website under the <IBadge color="primary">Enhancement</IBadge> tag, or propose a change of your own!</p>
            </IColumn>
        </IRow>
    </IContainer>
</template>