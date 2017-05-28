
entrada = int(raw_input())
tempo_ = entrada

segundos = [3600, 60, 1]
tempo_final = []

for tempo in range(len(segundos)):
    tempo_final.append(int(tempo_ / segundos[tempo]))
    tempo_ = (tempo_ - (segundos[tempo] * tempo_final[tempo]))


print ("{0}:{1}:{2}".format(tempo_final[0],tempo_final[1],tempo_final[2]))
