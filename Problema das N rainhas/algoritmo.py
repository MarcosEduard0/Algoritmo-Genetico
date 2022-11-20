from populacao import Populacao
from populacaoBinaria import PopulacaoBinaria


def algoritmoGeneticoBinario(total_geration, n_populacao, n_individuo, p_cross, p_mut, elitismo=False):
    melhores = []
    media, geracao = [], [0, ]
    populacao = PopulacaoBinaria(
        n_populacao, n_individuo, p_cross, p_mut, elitismo)
    melhores.append(populacao.melhorIndividuo.fitness)
    media.append(populacao.media)
    for i in range(total_geration):
        populacao = PopulacaoBinaria(
            n_populacao, n_individuo, p_cross, p_mut, elitismo, populacao.popIntermediaria)
        melhores.append(populacao.melhorIndividuo.fitness)
        media.append(populacao.media)
        geracao.append(i+1)

    print('Melhor individuo da última geração: {}\nAdaptação: {}'.format(
        populacao.melhorIndividuo.binario, populacao.melhorIndividuo.fitness))
    return geracao, melhores, media


def algoritmoGenetico(total_geration, n_populacao, n_individuo, p_cross, p_mut, elitismo=False):
    melhores = []
    media, geracao = [], [0, ]
    populacao = Populacao(n_populacao, n_individuo, p_cross, p_mut, elitismo)
    melhores.append(populacao.melhorIndividuo.fitness)
    media.append(populacao.media)
    for i in range(total_geration):
        populacao = Populacao(
            n_populacao, n_individuo, p_cross, p_mut, elitismo, populacao.popIntermediaria)
        melhores.append(populacao.melhorIndividuo.fitness)
        media.append(populacao.media)
        geracao.append(i+1)

    print('Melhor individuo da última geração: {}\nAdaptação: {}'.format(
        populacao.melhorIndividuo.rainhas, populacao.melhorIndividuo.fitness))
    return geracao, melhores, media
