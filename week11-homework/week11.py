import scanpy as sc
from matplotlib.pyplot import rc_context

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()
sc.tl.pca(adata)
sc.pl.pca(adata)


# do it again with filtering
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
 Make variable names (in this case the genes) unique
adata.var_names_make_unique()
sc.pp.recipe_zheng17(adata)
sc.tl.pca(adata)
with rc_context({'figure.figsize': (4, 4)}):
    sc.pl.pca(adata)

# lieden cluster and umap/tsne
sc.pp.neighbors(adata)
sc.tl.umap(adata,maxiter=1000)
sc.tl.leiden(adata)
sc.pl.umap(adata, color=['leiden'])
sc.tl.tsne(adata)
sc.pl.tsne(adata, color=['leiden'])

# get the genes that describe each cluster
sc.tl.rank_genes_groups(adata,'leiden',method='logreg')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)
sc.tl.rank_genes_groups(adata,'leiden',method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)


#Tsne of marker genes (mostly from https://www.nature.com/articles/s41467-021-20892-3)
sc.pl.tsne(adata, color="Npy")#neuron
sc.pl.tsne(adata, color="Itm2a")#endothelial
sc.pl.tsne(adata, color="Ccl4")#microglia
sc.pl.tsne(adata, color="Clu")#astrocyte
sc.pl.tsne(adata, color="Cspg4")#pericyte
sc.pl.tsne(adata, color="Olig2")#oligodendrite


#find which cluster numbers coorespond to my cell types
marker_genes_dict = {
    'Neuron': ['Npy'],
    'Endothelial': ['Itm2a'],
    'Microglia': ['Ccl4'],
    'Astrocyte': ['Clu'],
    'c': ['Cspg4'],
    'Oligodendrite': ['Olig2'],}

sc.tl.leiden(adata, key_added='clusters', resolution=0.5)
with rc_context({'figure.figsize': (5, 5)}):
    sc.pl.tsne(adata, color='clusters', add_outline=True, legend_loc='on data',
               legend_fontsize=12, legend_fontoutline=2,frameon=False,
               title='clustering of cells', palette='Set1')

sc.pl.dotplot(adata, marker_genes_dict, 'clusters', dendrogram=True)



#Tsne labelling clusters and cell types they coorespond to
cluster2annotation = {
     '0': '',
     '1': '',
     '2': 'Astrocyte',
     '3': 'Neuron',
     '4': '',
     '5': '',
     '6': '',
     '7': '',
     '8': '',
     '9': '',
     '10': '',
     '11': 'Oligodendrite',
     '12': '',
     '13': 'Endothelial',
     '14': 'Pericyte',
     '15': 'Microglia',
     '16': '',
     }

adata.obs['cell type'] = adata.obs['clusters'].map(cluster2annotation).astype('category')
sc.pl.tsne(adata, color='cell type', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2)

















