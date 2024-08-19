from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
def home(request):
    return render(request, 'converter/home.html',)

def Rus(request):
    return render(request, 'converter/Rus.html',)



def resultRus(request):
    ustanovkamango = int(request.GET['ustanovkamango'].replace(" ", ""))
    narezka = int(request.GET['narezka'].replace(" ", ""))
    vent = int(request.GET['vent'].replace(" ", ""))
    teh = int(request.GET['teh'].replace(" ", ""))
    freez = int(request.GET['freez'].replace(" ", ""))
    package = int(request.GET['package'].replace(" ", ""))
    itogo = ustanovkamango + narezka + vent + teh + freez + package
    arenda = int(request.GET['arenda'].replace(" ", ""))
    kolsotr = int(request.GET['kolsotr'].replace(" ", ""))
    zp = int(request.GET['zp'].replace(" ", ""))
    smenmes = int(request.GET['smenmes'].replace(" ", ""))
    smenchas = int(request.GET['smenchas'].replace(" ", ""))
    itogo2 = zp * kolsotr + arenda
    stoimsmeni = round(itogo2 / smenmes)
    stsir1 = int(request.GET['stsir1'].replace(" ", ""))
    loadequip = int(request.GET['loadequip'].replace(" ", ""))
    exitcomplproduct = int(request.GET['exitcomplproduct'])
    timecikl = int(request.GET['timecikl'])
    kolcikl = round(60 / int(timecikl))
    porcup = int(request.GET['porcup'])
    kolporcikl = round(loadequip * (exitcomplproduct / 100) * 1000 / porcup)
    kolporcchas = kolporcikl * kolcikl
    sebestpor = round(int(loadequip) * stsir1 / kolporcikl)
    stEE = int(request.GET['stEE'])
    maxpot = int(request.GET['maxpot'])
    kef = request.GET['kef']
    stwater = int(request.GET['stwater'])
    raswater = request.GET['raswater']
    stnoschas = round(maxpot * float(kef) * stEE + (stwater * float(raswater)))
    stnoscikl = round(stnoschas / kolcikl)
    ctnospor = round(stnoscikl / kolporcikl, 2)
    upak = int(request.GET['upak'])
    sto = int(request.GET['sto'].replace(" ", ""))
    stodvapyat = int(request.GET['stodvapyat'].replace(" ", ""))
    stopyatdes = int(request.GET['stopyatdes'].replace(" ", ""))
    stosempesyat = int(request.GET['stosempesyat'].replace(" ", ""))
    dvesti = int(request.GET['dvesti'].replace(" ", ""))
    porcsmen40 = round(kolporcchas * 0.4 * int(smenchas))
    porcsmen50 = round(kolporcchas * 0.5 * int(smenchas))
    porcsmen60 = round(kolporcchas * 0.6 * int(smenchas))
    porcsmen70 = round(kolporcchas * 0.7 * int(smenchas))
    porcsmen80 = round(kolporcchas * 0.8 * int(smenchas))
    sbsproducsmen40 = int(porcsmen40) * (int(sebestpor) + int(upak) + int(ctnospor)) + int(stoimsmeni)
    sbsproducsmen50 = int(porcsmen50) * (int(sebestpor) + int(upak) + int(ctnospor)) + int(stoimsmeni)
    sbsproducsmen60 = int(porcsmen60) * (int(sebestpor) + int(upak) + int(ctnospor)) + int(stoimsmeni)
    sbsproducsmen70 = int(porcsmen70) * (int(sebestpor) + int(upak) + int(ctnospor)) + int(stoimsmeni)
    sbsproducsmen80 = int(porcsmen80) * (int(sebestpor) + int(upak) + int(ctnospor)) + int(stoimsmeni)
    sbsporc40 = round(sbsproducsmen40 / porcsmen40)
    sbsporc50 = round(sbsproducsmen50 / porcsmen50)
    sbsporc60 = round(sbsproducsmen60 / porcsmen60)
    sbsporc70 = round(sbsproducsmen70 / porcsmen70)
    sbsporc80 = round(sbsproducsmen80 / porcsmen80)
    siresmen40 = round(int(porcsmen40) * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siresmen50 = round(int(porcsmen50) * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siresmen60 = round(int(porcsmen60) * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siresmen70 = round(int(porcsmen70) * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siresmen80 = round(int(porcsmen80) * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siremes40 = int(siresmen40) * int(smenmes)
    siremes50 = int(siresmen50) * int(smenmes)
    siremes60 = int(siresmen60) * int(smenmes)
    siremes70 = int(siresmen70) * int(smenmes)
    siremes80 = int(siresmen80) * int(smenmes)
    marza100_40 = porcsmen40 * int(sto) - sbsproducsmen40
    if marza100_40 < 0:
        marza100_40 = 'Убыток'
        prodrubporc100_40 = 'Убыток'
    else:
        prodrubporc100_40 = round(itogo / int(marza100_40) / int(smenmes) * 30)
        marza100_40 = '{0:,}'.format(marza100_40).replace(',', ' ')
        prodrubporc100_40 = '{0:,}'.format(prodrubporc100_40).replace(',', ' ')
    marza100_50 = porcsmen50 * int(sto) - sbsproducsmen50
    if marza100_50 < 0:
        marza100_50 = 'Убыток'
        prodrubporc100_50 = 'Убыток'
    else:
        prodrubporc100_50 = round(itogo / int(marza100_50) / int(smenmes) * 30)
        marza100_50 = '{0:,}'.format(marza100_50).replace(',', ' ')
        prodrubporc100_50 = '{0:,}'.format(prodrubporc100_50).replace(',', ' ')
    marza100_60 = porcsmen60 * int(sto) - sbsproducsmen60
    if marza100_60 < 0:
        marza100_60 = 'Убыток'
        prodrubporc100_60 = 'Убыток'
    else:
        prodrubporc100_60 = round(itogo / int(marza100_60) / int(smenmes) * 30)
        marza100_60 = '{0:,}'.format(marza100_60).replace(',', ' ')
        prodrubporc100_60 = '{0:,}'.format(prodrubporc100_60).replace(',', ' ')
    marza100_70 = porcsmen70 * int(sto) - sbsproducsmen70
    if marza100_70 < 0:
        marza100_70 = 'Убыток'
        prodrubporc100_70 = 'Убыток'
    else:
        prodrubporc100_70 = round(itogo / int(marza100_70) / int(smenmes) * 30)
        marza100_70 = '{0:,}'.format(marza100_70).replace(',', ' ')
        prodrubporc100_70 = '{0:,}'.format(prodrubporc100_70).replace(',', ' ')
    marza100_80 = porcsmen80 * int(sto) - sbsproducsmen80
    if marza100_80 < 0:
        marza100_80 = 'Убыток'
        prodrubporc100_80 = 'Убыток'
    else:
        prodrubporc100_80 = round(itogo / int(marza100_80) / int(smenmes) * 30)
        marza100_80 = '{0:,}'.format(marza100_80).replace(',', ' ')
        prodrubporc100_80 = '{0:,}'.format(prodrubporc100_80).replace(',', ' ')
    marza125_40 = porcsmen40 * int(stodvapyat) - sbsproducsmen40
    if marza125_40 < 0:
        marza125_40 = 'Убыток'
        prodrubporc125_40 = 'Убыток'
    else:
        prodrubporc125_40 = round(itogo / int(marza125_40) / int(smenmes) * 30)
        marza125_40 = '{0:,}'.format(marza125_40).replace(',', ' ')
        prodrubporc125_40 = '{0:,}'.format(prodrubporc125_40).replace(',', ' ')
    marza125_50 = porcsmen50 * int(stodvapyat) - sbsproducsmen50
    if marza125_50 < 0:
        marza125_50 = 'Убыток'
        prodrubporc125_50 = 'Убыток'
    else:
        prodrubporc125_50 = round(itogo / int(marza125_50) / int(smenmes) * 30)
        marza125_50 = '{0:,}'.format(marza125_50).replace(',', ' ')
        prodrubporc125_50 = '{0:,}'.format(prodrubporc125_50).replace(',', ' ')
    marza125_60 = porcsmen60 * int(stodvapyat) - sbsproducsmen60
    if marza125_60 < 0:
        marza125_60 = 'Убыток'
        prodrubporc125_60 = 'Убыток'
    else:
        prodrubporc125_60 = round(itogo / int(marza125_60) / int(smenmes) * 30)
        marza125_60 = '{0:,}'.format(marza125_60).replace(',', ' ')
        prodrubporc125_60 = '{0:,}'.format(prodrubporc125_60).replace(',', ' ')
    marza125_70 = porcsmen70 * int(stodvapyat) - sbsproducsmen70
    if marza125_70 < 0:
        marza125_70 = 'Убыток'
        prodrubporc125_70 = 'Убыток'
    else:
        prodrubporc125_70 = round(itogo / int(marza125_70) / int(smenmes) * 30)
        marza125_70 = '{0:,}'.format(marza125_70).replace(',', ' ')
        prodrubporc125_70 = '{0:,}'.format(prodrubporc125_70).replace(',', ' ')
    marza125_80 = porcsmen80 * int(stodvapyat) - sbsproducsmen80
    if marza125_80 < 0:
        marza125_80 = 'Убыток'
        prodrubporc125_80 = 'Убыток'
    else:
        prodrubporc125_80 = round(itogo / int(marza125_80) / int(smenmes) * 30)
        marza125_80 = '{0:,}'.format(marza125_80).replace(',', ' ')
        prodrubporc125_80 = '{0:,}'.format(prodrubporc125_80).replace(',', ' ')
    marza150_40 = porcsmen40 * int(stopyatdes) - sbsproducsmen40
    if marza150_40 < 0:
        marza150_40 = 'Убыток'
        prodrubporc150_40 = 'Убыток'
    else:
        prodrubporc150_40 = round(itogo / int(marza150_40) / int(smenmes) * 30)
        marza150_40 = '{0:,}'.format(marza150_40).replace(',', ' ')
        prodrubporc150_40 = '{0:,}'.format(prodrubporc150_40).replace(',', ' ')
    marza150_50 = porcsmen50 * int(stopyatdes) - sbsproducsmen50
    if marza150_50 < 0:
        marza150_50 = 'Убыток'
        prodrubporc150_50 = 'Убыток'
    else:
        prodrubporc150_50 = round(itogo / int(marza150_50) / int(smenmes) * 30)
        marza150_50 = '{0:,}'.format(marza150_50).replace(',', ' ')
        prodrubporc150_50 = '{0:,}'.format(prodrubporc150_50).replace(',', ' ')
    marza150_60 = porcsmen60 * int(stopyatdes) - sbsproducsmen60
    if marza150_60 < 0:
        marza150_60 = 'Убыток'
        prodrubporc150_60 = 'Убыток'
    else:
        prodrubporc150_60 = round(itogo / int(marza150_60) / int(smenmes) * 30)
        marza150_60 = '{0:,}'.format(marza150_60).replace(',', ' ')
        prodrubporc150_60 = '{0:,}'.format(prodrubporc150_60).replace(',', ' ')
    marza150_70 = porcsmen70 * int(stopyatdes) - sbsproducsmen70
    if marza150_70 < 0:
        marza150_70 = 'Убыток'
        prodrubporc150_70 = 'Убыток'
    else:
        prodrubporc150_70 = round(itogo / int(marza150_70) / int(smenmes) * 30)
        marza150_70 = '{0:,}'.format(marza150_70).replace(',', ' ')
        prodrubporc150_70 = '{0:,}'.format(prodrubporc150_70).replace(',', ' ')
    marza150_80 = porcsmen80 * int(stopyatdes) - sbsproducsmen80
    if marza150_80 < 0:
        marza150_80 = 'Убыток'
        prodrubporc150_80 = 'Убыток'
    else:
        prodrubporc150_80 = round(itogo / int(marza150_80) / int(smenmes) * 30)
        marza150_80 = '{0:,}'.format(marza150_80).replace(',', ' ')
        prodrubporc150_80 = '{0:,}'.format(prodrubporc150_80).replace(',', ' ')
    marza175_40 = porcsmen40 * int(stosempesyat) - sbsproducsmen40
    if marza175_40 < 0:
        marza175_40 = 'Убыток'
        prodrubporc175_40 = 'Убыток'
    else:
        prodrubporc175_40 = round(itogo / int(marza175_40) / int(smenmes) * 30)
        marza175_40 = '{0:,}'.format(marza175_40).replace(',', ' ')
        prodrubporc175_40 = '{0:,}'.format(prodrubporc175_40).replace(',', ' ')
    marza175_50 = porcsmen50 * int(stosempesyat) - sbsproducsmen50
    if marza175_50 < 0:
        marza175_50 = 'Убыток'
        prodrubporc175_50 = 'Убыток'
    else:
        prodrubporc175_50 = round(itogo / int(marza175_50) / int(smenmes) * 30)
        marza175_50 = '{0:,}'.format(marza175_50).replace(',', ' ')
        prodrubporc175_50 = '{0:,}'.format(prodrubporc175_50).replace(',', ' ')
    marza175_60 = porcsmen60 * int(stosempesyat) - sbsproducsmen60
    if marza175_60 < 0:
        marza175_60 = 'Убыток'
        prodrubporc175_60 = 'Убыток'
    else:
        prodrubporc175_60 = round(itogo / int(marza175_60) / int(smenmes) * 30)
        marza175_60 = '{0:,}'.format(marza175_60).replace(',', ' ')
        prodrubporc175_60 = '{0:,}'.format(prodrubporc175_60).replace(',', ' ')
    marza175_70 = porcsmen70 * int(stosempesyat) - sbsproducsmen70
    if marza175_70 < 0:
        marza175_70 = 'Убыток'
        prodrubporc175_70 = 'Убыток'
    else:
        prodrubporc175_70 = round(itogo / int(marza175_70) / int(smenmes) * 30)
        marza175_70 = '{0:,}'.format(marza175_70).replace(',', ' ')
        prodrubporc175_70 = '{0:,}'.format(prodrubporc175_70).replace(',', ' ')
    marza175_80 = porcsmen80 * int(stosempesyat) - sbsproducsmen80
    if marza175_80 < 0:
        marza175_80 = 'Убыток'
        prodrubporc175_80 = 'Убыток'
    else:
        prodrubporc175_80 = round(itogo / int(marza175_80) / int(smenmes) * 30)
        marza175_80 = '{0:,}'.format(marza175_80).replace(',', ' ')
        prodrubporc175_80 = '{0:,}'.format(prodrubporc175_80).replace(',', ' ')
    marza200_40 = porcsmen40 * int(dvesti) - sbsproducsmen40
    if marza200_40 < 0:
        marza200_40 = 'Убыток'
        prodrubporc200_40 = 'Убыток'
    else:
        prodrubporc200_40 = round(itogo / int(marza200_40) / int(smenmes) * 30)
        marza200_40 = '{0:,}'.format(marza200_40).replace(',', ' ')
        prodrubporc200_40 = '{0:,}'.format(prodrubporc200_40).replace(',', ' ')
    marza200_50 = porcsmen50 * int(dvesti) - sbsproducsmen50
    if marza200_50 < 0:
        marza200_50 = 'Убыток'
        prodrubporc200_50 = 'Убыток'
    else:
        prodrubporc200_50 = round(itogo / int(marza200_50) / int(smenmes) * 30)
        marza200_50 = '{0:,}'.format(marza200_50).replace(',', ' ')
        prodrubporc200_50 = '{0:,}'.format(prodrubporc200_50).replace(',', ' ')
    marza200_60 = porcsmen60 * int(dvesti) - sbsproducsmen60
    if marza200_60 < 0:
        marza200_60 = 'Убыток'
        prodrubporc200_60 = 'Убыток'
    else:
        prodrubporc200_60 = round(itogo / int(marza200_60) / int(smenmes) * 30)
        marza200_60 = '{0:,}'.format(marza200_60).replace(',', ' ')
        prodrubporc200_60 = '{0:,}'.format(prodrubporc200_60).replace(',', ' ')
    marza200_70 = porcsmen70 * int(dvesti) - sbsproducsmen70
    if marza200_70 < 0:
        marza200_70 = 'Убыток'
        prodrubporc200_70 = 'Убыток'
    else:
        prodrubporc200_70 = round(itogo / int(marza200_70) / int(smenmes) * 30)
        marza200_70 = '{0:,}'.format(marza200_70).replace(',', ' ')
        prodrubporc200_70 = '{0:,}'.format(prodrubporc200_70).replace(',', ' ')
    marza200_80 = porcsmen80 * int(dvesti) - sbsproducsmen80
    if marza200_80 < 0:
        marza200_80 = 'Убыток'
        prodrubporc200_80 = 'Убыток'
    else:
        prodrubporc200_80 = round(itogo / int(marza200_80) / int(smenmes) * 30)
        marza200_80 = '{0:,}'.format(marza200_80).replace(',', ' ')
        prodrubporc200_80 = '{0:,}'.format(prodrubporc200_80).replace(',', ' ')
    ustanovkamango = '{0:,}'.format(ustanovkamango).replace(',', ' ')
    narezka = '{0:,}'.format(narezka).replace(',', ' ')
    vent = '{0:,}'.format(vent).replace(',', ' ')
    teh = '{0:,}'.format(teh).replace(',', ' ')
    freez = '{0:,}'.format(freez).replace(',', ' ')
    package = '{0:,}'.format(package).replace(',', ' ')
    itogo = '{0:,}'.format(itogo).replace(',', ' ')
    arenda = '{0:,}'.format(arenda).replace(',', ' ')
    zp = '{0:,}'.format(zp).replace(',', ' ')
    itogo2 = '{0:,}'.format(itogo2).replace(',', ' ')
    stoimsmeni = '{0:,}'.format(stoimsmeni).replace(',', ' ')
    stsir1 = '{0:,}'.format(stsir1).replace(',', ' ')
    porcsmen40 = '{0:,}'.format(porcsmen40).replace(',', ' ')
    porcsmen50 = '{0:,}'.format(porcsmen50).replace(',', ' ')
    porcsmen60 = '{0:,}'.format(porcsmen60).replace(',', ' ')
    porcsmen70 = '{0:,}'.format(porcsmen70).replace(',', ' ')
    porcsmen80 = '{0:,}'.format(porcsmen80).replace(',', ' ')
    sbsproducsmen40 = '{0:,}'.format(sbsproducsmen40).replace(',', ' ')
    sbsproducsmen50 = '{0:,}'.format(sbsproducsmen50).replace(',', ' ')
    sbsproducsmen60 = '{0:,}'.format(sbsproducsmen60).replace(',', ' ')
    sbsproducsmen70 = '{0:,}'.format(sbsproducsmen70).replace(',', ' ')
    sbsproducsmen80 = '{0:,}'.format(sbsproducsmen80).replace(',', ' ')
    sbsporc40 = '{0:,}'.format(sbsporc40).replace(',', ' ')
    sbsporc50 = '{0:,}'.format(sbsporc50).replace(',', ' ')
    sbsporc60 = '{0:,}'.format(sbsporc60).replace(',', ' ')
    sbsporc70 = '{0:,}'.format(sbsporc70).replace(',', ' ')
    sbsporc80 = '{0:,}'.format(sbsporc80).replace(',', ' ')
    siresmen40 = '{0:,}'.format(siresmen40).replace(',', ' ')
    siresmen50 = '{0:,}'.format(siresmen50).replace(',', ' ')
    siresmen60 = '{0:,}'.format(siresmen60).replace(',', ' ')
    siresmen70 = '{0:,}'.format(siresmen70).replace(',', ' ')
    siresmen80 = '{0:,}'.format(siresmen80).replace(',', ' ')
    siremes40 = '{0:,}'.format(siremes40).replace(',', ' ')
    siremes50 = '{0:,}'.format(siremes50).replace(',', ' ')
    siremes60 = '{0:,}'.format(siremes60).replace(',', ' ')
    siremes70 = '{0:,}'.format(siremes70).replace(',', ' ')
    siremes80 = '{0:,}'.format(siremes80).replace(',', ' ')
    sto = '{0:,}'.format(sto).replace(',', ' ')
    stodvapyat = '{0:,}'.format(stodvapyat).replace(',', ' ')
    stopyatdes = '{0:,}'.format(stopyatdes).replace(',', ' ')
    stosempesyat = '{0:,}'.format(stosempesyat).replace(',', ' ')
    dvesti = '{0:,}'.format(dvesti).replace(',', ' ')
    return render(request, 'converter/resultRus.html', {'name1': ustanovkamango,
    'name2': narezka, 'name3': vent, 'name4': teh, 'name5': freez, 'name6': package,
    'name7': itogo, 'name8': arenda, 'name9': kolsotr, 'name10': zp,
    'name11': smenmes, 'name12': smenchas, 'name13': itogo2, 'name14': stoimsmeni,
    'name15': stsir1, 'name16': loadequip, 'name17': exitcomplproduct, 'name18': timecikl,
    'name19': kolcikl, 'name20': porcup, 'name21': kolporcikl, 'name22': kolporcchas,
    'name23': sebestpor, 'name24': stEE, 'name25': maxpot, 'name26': kef, 'name27': stwater,
    'name28': raswater, 'name29': stnoschas, 'name30': stnoscikl, 'name31': ctnospor,
    'name32': upak, 'name33': porcsmen40, 'name34': porcsmen50, 'name35': porcsmen60,
    'name36': porcsmen70, 'name37': porcsmen80, 'name38': sbsproducsmen40, 'name39': sbsproducsmen50,
    'name40': sbsproducsmen60, 'name41': sbsproducsmen70, 'name42': sbsproducsmen80, 'name43': sbsporc40,
    'name44': sbsporc50, 'name45': sbsporc60, 'name46': sbsporc70, 'name47': sbsporc80, 'name48': siresmen40,
    'name49': siresmen50, 'name50': siresmen60, 'name51': siresmen70, 'name52': siresmen80, 'name53': siremes40,
    'name54': siremes50, 'name55': siremes60, 'name56': siremes70, 'name57': siremes80, 'name58': marza100_40,
    'name59': marza100_50, 'name60': marza100_60, 'name61': marza100_70, 'name62': marza100_80, 'name63': marza125_40,
    'name64': marza125_50, 'name65': marza125_60, 'name66': marza125_70, 'name67': marza125_80, 'name68': marza150_40,
    'name69': marza150_50, 'name70': marza150_60, 'name71': marza150_70, 'name72': marza150_80, 'name73': marza175_40,
    'name74': marza175_50, 'name75': marza175_60, 'name76': marza175_70, 'name77': marza175_80, 'name78': marza200_40,
    'name79': marza200_50, 'name80': marza200_60, 'name81': marza200_70, 'name82': marza200_80,
    'name83': prodrubporc100_40, 'name84': prodrubporc100_50, 'name85': prodrubporc100_60, 'name86': prodrubporc100_70,
    'name87': prodrubporc100_80, 'name88': prodrubporc125_40, 'name89': prodrubporc125_50, 'name90': prodrubporc125_60,
    'name91': prodrubporc125_70, 'name92': prodrubporc125_80, 'name93': prodrubporc150_40, 'name94': prodrubporc150_50,
    'name95': prodrubporc150_60, 'name96': prodrubporc150_70, 'name97': prodrubporc150_80, 'name98': prodrubporc175_40,
    'name99': prodrubporc175_50, 'name100': prodrubporc175_60, 'name101': prodrubporc175_70, 'name102': prodrubporc175_80,
    'name103': prodrubporc200_40, 'name104': prodrubporc200_50, 'name105': prodrubporc200_60, 'name106': prodrubporc200_70,
    'name107': prodrubporc200_80, 'name108': sto, 'name109': stodvapyat, 'name110': stopyatdes, 'name111': stosempesyat,
    'name112': dvesti, })

def resultEng(request):
    ustanovkamango = int(request.GET['ustanovkamango'].replace(" ", ""))
    narezka = int(request.GET['narezka'].replace(" ", ""))
    vent = int(request.GET['vent'].replace(" ", ""))
    teh = int(request.GET['teh'].replace(" ", ""))
    freez = int(request.GET['freez'].replace(" ", ""))
    package = int(request.GET['package'].replace(" ", ""))
    itogo = ustanovkamango + narezka + vent + teh + freez + package
    arenda = int(request.GET['arenda'].replace(" ", ""))
    kolsotr = int(request.GET['kolsotr'].replace(" ", ""))
    zp = int(request.GET['zp'].replace(" ", ""))
    smenmes = int(request.GET['smenmes'].replace(" ", ""))
    smenchas = int(request.GET['smenchas'].replace(" ", ""))
    itogo2 = zp * kolsotr + arenda
    stoimsmeni = round(itogo2 / smenmes)
    stsir1 = int(request.GET['stsir1'].replace(" ", ""))
    loadequip = int(request.GET['loadequip'].replace(" ", ""))
    exitcomplproduct = int(request.GET['exitcomplproduct'])
    timecikl = int(request.GET['timecikl'])
    kolcikl = round(60 / int(timecikl))
    porcup = int(request.GET['porcup'])
    kolporcikl = round(loadequip * (exitcomplproduct / 100) * 1000 / porcup)
    kolporcchas = kolporcikl * kolcikl
    sebestpor = round(loadequip * stsir1 / kolporcikl, 1)
    stEE = float(request.GET['stEE'])
    maxpot = int(request.GET['maxpot'])
    kef = request.GET['kef']
    stwater = int(request.GET['stwater'])
    raswater = request.GET['raswater']
    stnoschas = round(maxpot * float(kef) * float(stEE) + (stwater * float(raswater)), 2)
    stnoscikl = round(stnoschas / kolcikl, 1)
    ctnospor = round(stnoscikl / kolporcikl, 2)
    upak = request.GET['upak']
    sto = float(request.GET['sto'].replace(" ", ""))
    stodvapyat = float(request.GET['stodvapyat'].replace(" ", ""))
    stopyatdes = float(request.GET['stopyatdes'].replace(" ", ""))
    stosempesyat = float(request.GET['stosempesyat'].replace(" ", ""))
    dvesti = float(request.GET['dvesti'].replace(" ", ""))
    porcsmen40 = round(kolporcchas * 0.4 * int(smenchas))
    porcsmen50 = round(kolporcchas * 0.5 * int(smenchas))
    porcsmen60 = round(kolporcchas * 0.6 * int(smenchas))
    porcsmen70 = round(kolporcchas * 0.7 * int(smenchas))
    porcsmen80 = round(kolporcchas * 0.8 * int(smenchas))
    sbsproducsmen40 = round(porcsmen40 * (sebestpor + float(upak) + ctnospor) + int(stoimsmeni))
    sbsproducsmen50 = round(porcsmen50 * (sebestpor + float(upak) + ctnospor) + int(stoimsmeni))
    sbsproducsmen60 = round(porcsmen60 * (sebestpor + float(upak) + ctnospor) + int(stoimsmeni))
    sbsproducsmen70 = round(porcsmen70 * (sebestpor + float(upak) + ctnospor) + int(stoimsmeni))
    sbsproducsmen80 = round(porcsmen80 * (sebestpor + float(upak) + ctnospor) + int(stoimsmeni))
    sbsporc40 = round(sbsproducsmen40 / porcsmen40)
    sbsporc50 = round(sbsproducsmen50 / porcsmen50)
    sbsporc60 = round(sbsproducsmen60 / porcsmen60)
    sbsporc70 = round(sbsproducsmen70 / porcsmen70)
    sbsporc80 = round(sbsproducsmen80 / porcsmen80)
    siresmen40 = round(porcsmen40 * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siresmen50 = round(porcsmen50 * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siresmen60 = round(porcsmen60 * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siresmen70 = round(porcsmen70 * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siresmen80 = round(porcsmen80 * int(porcup) / (int(exitcomplproduct) / 100) / 1000)
    siremes40 = round(int(siresmen40) * int(smenmes))
    siremes50 = round(int(siresmen50) * int(smenmes))
    siremes60 = round(int(siresmen60) * int(smenmes))
    siremes70 = round(int(siresmen70) * int(smenmes))
    siremes80 = round(int(siresmen80) * int(smenmes))
    marza100_40 = round(porcsmen40 * float(sto) - sbsproducsmen40)
    if marza100_40 < 0:
        marza100_40 = 'Loss'
        prodrubporc100_40 = 'Loss'
    else:
        prodrubporc100_40 = round(itogo / int(marza100_40) / int(smenmes) * 30)
        marza100_40 = '{0:,}'.format(marza100_40).replace(',', ' ')
        prodrubporc100_40 = '{0:,}'.format(prodrubporc100_40).replace(',', ' ')
    marza100_50 = round(porcsmen50 * float(sto) - sbsproducsmen50)
    if marza100_50 < 0:
        marza100_50 = 'Loss'
        prodrubporc100_50 = 'Loss'
    else:
        prodrubporc100_50 = round(itogo / int(marza100_50) / int(smenmes) * 30)
        marza100_50 = '{0:,}'.format(marza100_50).replace(',', ' ')
        prodrubporc100_50 = '{0:,}'.format(prodrubporc100_50).replace(',', ' ')
    marza100_60 = round(porcsmen60 * float(sto) - sbsproducsmen60)
    if marza100_60 < 0:
        marza100_60 = 'Loss'
        prodrubporc100_60 = 'Loss'
    else:
        prodrubporc100_60 = round(itogo / int(marza100_60) / int(smenmes) * 30)
        marza100_60 = '{0:,}'.format(marza100_60).replace(',', ' ')
        prodrubporc100_60 = '{0:,}'.format(prodrubporc100_60).replace(',', ' ')
    marza100_70 = round(porcsmen70 * float(sto) - sbsproducsmen70)
    if marza100_70 < 0:
        marza100_70 = 'Loss'
        prodrubporc100_70 = 'Loss'
    else:
        prodrubporc100_70 = round(itogo / int(marza100_70) / int(smenmes) * 30)
        marza100_70 = '{0:,}'.format(marza100_70).replace(',', ' ')
        prodrubporc100_70 = '{0:,}'.format(prodrubporc100_70).replace(',', ' ')
    marza100_80 = round(porcsmen80 * float(sto) - sbsproducsmen80)
    if marza100_80 < 0:
        marza100_80 = 'Loss'
        prodrubporc100_80 = 'Loss'
    else:
        prodrubporc100_80 = round(itogo / int(marza100_80) / int(smenmes) * 30)
        marza100_80 = '{0:,}'.format(marza100_80).replace(',', ' ')
        prodrubporc100_80 = '{0:,}'.format(prodrubporc100_80).replace(',', ' ')
    marza125_40 = round(porcsmen40 * float(stodvapyat) - sbsproducsmen40)
    if marza125_40 < 0:
        marza125_40 = 'Loss'
        prodrubporc125_40 = 'Loss'
    else:
        prodrubporc125_40 = round(itogo / int(marza125_40) / int(smenmes) * 30)
        marza125_40 = '{0:,}'.format(marza125_40).replace(',', ' ')
        prodrubporc125_40 = '{0:,}'.format(prodrubporc125_40).replace(',', ' ')
    marza125_50 = round(porcsmen50 * float(stodvapyat) - sbsproducsmen50)
    if marza125_50 < 0:
        marza125_50 = 'Loss'
        prodrubporc125_50 = 'Loss'
    else:
        prodrubporc125_50 = round(itogo / int(marza125_50) / int(smenmes) * 30)
        marza125_50 = '{0:,}'.format(marza125_50).replace(',', ' ')
        prodrubporc125_50 = '{0:,}'.format(prodrubporc125_50).replace(',', ' ')
    marza125_60 = round(porcsmen60 * float(stodvapyat) - sbsproducsmen60)
    if marza125_60 < 0:
        marza125_60 = 'Loss'
        prodrubporc125_60 = 'Loss'
    else:
        prodrubporc125_60 = round(itogo / int(marza125_60) / int(smenmes) * 30)
        marza125_60 = '{0:,}'.format(marza125_60).replace(',', ' ')
        prodrubporc125_60 = '{0:,}'.format(prodrubporc125_60).replace(',', ' ')
    marza125_70 = round(porcsmen70 * float(stodvapyat) - sbsproducsmen70)
    if marza125_70 < 0:
        marza125_70 = 'Loss'
        prodrubporc125_70 = 'Loss'
    else:
        prodrubporc125_70 = round(itogo / int(marza125_70) / int(smenmes) * 30)
        marza125_70 = '{0:,}'.format(marza125_70).replace(',', ' ')
        prodrubporc125_70 = '{0:,}'.format(prodrubporc125_70).replace(',', ' ')
    marza125_80 = round(porcsmen80 * float(stodvapyat) - sbsproducsmen80)
    if marza125_80 < 0:
        marza125_80 = 'Loss'
        prodrubporc125_80 = 'Loss'
    else:
        prodrubporc125_80 = round(itogo / int(marza125_80) / int(smenmes) * 30)
        marza125_80 = '{0:,}'.format(marza125_80).replace(',', ' ')
        prodrubporc125_80 = '{0:,}'.format(prodrubporc125_80).replace(',', ' ')
    marza150_40 = round(porcsmen40 * float(stopyatdes) - sbsproducsmen40)
    if marza150_40 < 0:
        marza150_40 = 'Loss'
        prodrubporc150_40 = 'Loss'
    else:
        prodrubporc150_40 = round(itogo / int(marza150_40) / int(smenmes) * 30)
        marza150_40 = '{0:,}'.format(marza150_40).replace(',', ' ')
        prodrubporc150_40 = '{0:,}'.format(prodrubporc150_40).replace(',', ' ')
    marza150_50 = round(porcsmen50 * float(stopyatdes) - sbsproducsmen50)
    if marza150_50 < 0:
        marza150_50 = 'Loss'
        prodrubporc150_50 = 'Loss'
    else:
        prodrubporc150_50 = round(itogo / int(marza150_50) / int(smenmes) * 30)
        marza150_50 = '{0:,}'.format(marza150_50).replace(',', ' ')
        prodrubporc150_50 = '{0:,}'.format(prodrubporc150_50).replace(',', ' ')
    marza150_60 = round(porcsmen60 * float(stopyatdes) - sbsproducsmen60)
    if marza150_60 < 0:
        marza150_60 = 'Loss'
        prodrubporc150_60 = 'Loss'
    else:
        prodrubporc150_60 = round(itogo / int(marza150_60) / int(smenmes) * 30)
        marza150_60 = '{0:,}'.format(marza150_60).replace(',', ' ')
        prodrubporc150_60 = '{0:,}'.format(prodrubporc150_60).replace(',', ' ')
    marza150_70 = round(porcsmen70 * float(stopyatdes) - sbsproducsmen70)
    if marza150_70 < 0:
        marza150_70 = 'Loss'
        prodrubporc150_70 = 'Loss'
    else:
        prodrubporc150_70 = round(itogo / int(marza150_70) / int(smenmes) * 30)
        marza150_70 = '{0:,}'.format(marza150_70).replace(',', ' ')
        prodrubporc150_70 = '{0:,}'.format(prodrubporc150_70).replace(',', ' ')
    marza150_80 = round(porcsmen80 * float(stopyatdes) - sbsproducsmen80)
    if marza150_80 < 0:
        marza150_80 = 'Loss'
        prodrubporc150_80 = 'Loss'
    else:
        prodrubporc150_80 = round(itogo / int(marza150_80) / int(smenmes) * 30)
        marza150_80 = '{0:,}'.format(marza150_80).replace(',', ' ')
        prodrubporc150_80 = '{0:,}'.format(prodrubporc150_80).replace(',', ' ')
    marza175_40 = round(porcsmen40 * float(stosempesyat) - sbsproducsmen40)
    if marza175_40 < 0:
        marza175_40 = 'Loss'
        prodrubporc175_40 = 'Loss'
    else:
        prodrubporc175_40 = round(itogo / int(marza175_40) / int(smenmes) * 30)
        marza175_40 = '{0:,}'.format(marza175_40).replace(',', ' ')
        prodrubporc175_40 = '{0:,}'.format(prodrubporc175_40).replace(',', ' ')
    marza175_50 = round(porcsmen50 * float(stosempesyat) - sbsproducsmen50)
    if marza175_50 < 0:
        marza175_50 = 'Loss'
        prodrubporc175_50 = 'Loss'
    else:
        prodrubporc175_50 = round(itogo / int(marza175_50) / int(smenmes) * 30)
        marza175_50 = '{0:,}'.format(marza175_50).replace(',', ' ')
        prodrubporc175_50 = '{0:,}'.format(prodrubporc175_50).replace(',', ' ')
    marza175_60 = round(porcsmen60 * float(stosempesyat) - sbsproducsmen60)
    if marza175_60 < 0:
        marza175_60 = 'Loss'
        prodrubporc175_60 = 'Loss'
    else:
        prodrubporc175_60 = round(itogo / int(marza175_60) / int(smenmes) * 30)
        marza175_60 = '{0:,}'.format(marza175_60).replace(',', ' ')
        prodrubporc175_60 = '{0:,}'.format(prodrubporc175_60).replace(',', ' ')
    marza175_70 = round(porcsmen70 * float(stosempesyat) - sbsproducsmen70)
    if marza175_70 < 0:
        marza175_70 = 'Loss'
        prodrubporc175_70 = 'Loss'
    else:
        prodrubporc175_70 = round(itogo / int(marza175_70) / int(smenmes) * 30)
        marza175_70 = '{0:,}'.format(marza175_70).replace(',', ' ')
        prodrubporc175_70 = '{0:,}'.format(prodrubporc175_70).replace(',', ' ')
    marza175_80 = round(porcsmen80 * float(stosempesyat) - sbsproducsmen80)
    if marza175_80 < 0:
        marza175_80 = 'Loss'
        prodrubporc175_80 = 'Loss'
    else:
        prodrubporc175_80 = round(itogo / int(marza175_80) / int(smenmes) * 30)
        marza175_80 = '{0:,}'.format(marza175_80).replace(',', ' ')
        prodrubporc175_80 = '{0:,}'.format(prodrubporc175_80).replace(',', ' ')
    marza200_40 = round(porcsmen40 * float(dvesti) - sbsproducsmen40)
    if marza200_40 < 0:
        marza200_40 = 'Loss'
        prodrubporc200_40 = 'Loss'
    else:
        prodrubporc200_40 = round(itogo / int(marza200_40) / int(smenmes) * 30)
        marza200_40 = '{0:,}'.format(marza200_40).replace(',', ' ')
        prodrubporc200_40 = '{0:,}'.format(prodrubporc200_40).replace(',', ' ')
    marza200_50 = round(porcsmen50 * float(dvesti) - sbsproducsmen50)
    if marza200_50 < 0:
        marza200_50 = 'Loss'
        prodrubporc200_50 = 'Loss'
    else:
        prodrubporc200_50 = round(itogo / int(marza200_50) / int(smenmes) * 30)
        marza200_50 = '{0:,}'.format(marza200_50).replace(',', ' ')
        prodrubporc200_50 = '{0:,}'.format(prodrubporc200_50).replace(',', ' ')
    marza200_60 = round(porcsmen60 * float(dvesti) - sbsproducsmen60)
    if marza200_60 < 0:
        marza200_60 = 'Loss'
        prodrubporc200_60 = 'Loss'
    else:
        prodrubporc200_60 = round(itogo / int(marza200_60) / int(smenmes) * 30)
        marza200_60 = '{0:,}'.format(marza200_60).replace(',', ' ')
        prodrubporc200_60 = '{0:,}'.format(prodrubporc200_60).replace(',', ' ')
    marza200_70 = round(porcsmen70 * float(dvesti) - sbsproducsmen70)
    if marza200_70 < 0:
        marza200_70 = 'Loss'
        prodrubporc200_70 = 'Loss'
    else:
        prodrubporc200_70 = round(itogo / int(marza200_70) / int(smenmes) * 30)
        marza200_70 = '{0:,}'.format(marza200_70).replace(',', ' ')
        prodrubporc200_70 = '{0:,}'.format(prodrubporc200_70).replace(',', ' ')
    marza200_80 = round(porcsmen80 * float(dvesti) - sbsproducsmen80)
    if marza200_80 < 0:
        marza200_80 = 'Loss'
        prodrubporc200_80 = 'Loss'
    else:
        prodrubporc200_80 = round(itogo / int(marza200_80) / int(smenmes) * 30)
        marza200_80 = '{0:,}'.format(marza200_80).replace(',', ' ')
        prodrubporc200_80 = '{0:,}'.format(prodrubporc200_80).replace(',', ' ')
    ustanovkamango = '{0:,}'.format(ustanovkamango).replace(',', ' ')
    narezka = '{0:,}'.format(narezka).replace(',', ' ')
    vent = '{0:,}'.format(vent).replace(',', ' ')
    teh = '{0:,}'.format(teh).replace(',', ' ')
    freez = '{0:,}'.format(freez).replace(',', ' ')
    package = '{0:,}'.format(package).replace(',', ' ')
    itogo = '{0:,}'.format(itogo).replace(',', ' ')
    arenda = '{0:,}'.format(arenda).replace(',', ' ')
    zp = '{0:,}'.format(zp).replace(',', ' ')
    itogo2 = '{0:,}'.format(itogo2).replace(',', ' ')
    stoimsmeni = '{0:,}'.format(stoimsmeni).replace(',', ' ')
    stsir1 = '{0:,}'.format(stsir1).replace(',', ' ')
    porcsmen40 = '{0:,}'.format(porcsmen40).replace(',', ' ')
    porcsmen50 = '{0:,}'.format(porcsmen50).replace(',', ' ')
    porcsmen60 = '{0:,}'.format(porcsmen60).replace(',', ' ')
    porcsmen70 = '{0:,}'.format(porcsmen70).replace(',', ' ')
    porcsmen80 = '{0:,}'.format(porcsmen80).replace(',', ' ')
    sbsproducsmen40 = '{0:,}'.format(sbsproducsmen40).replace(',', ' ')
    sbsproducsmen50 = '{0:,}'.format(sbsproducsmen50).replace(',', ' ')
    sbsproducsmen60 = '{0:,}'.format(sbsproducsmen60).replace(',', ' ')
    sbsproducsmen70 = '{0:,}'.format(sbsproducsmen70).replace(',', ' ')
    sbsproducsmen80 = '{0:,}'.format(sbsproducsmen80).replace(',', ' ')
    sbsporc40 = '{0:,}'.format(sbsporc40).replace(',', ' ')
    sbsporc50 = '{0:,}'.format(sbsporc50).replace(',', ' ')
    sbsporc60 = '{0:,}'.format(sbsporc60).replace(',', ' ')
    sbsporc70 = '{0:,}'.format(sbsporc70).replace(',', ' ')
    sbsporc80 = '{0:,}'.format(sbsporc80).replace(',', ' ')
    siresmen40 = '{0:,}'.format(siresmen40).replace(',', ' ')
    siresmen50 = '{0:,}'.format(siresmen50).replace(',', ' ')
    siresmen60 = '{0:,}'.format(siresmen60).replace(',', ' ')
    siresmen70 = '{0:,}'.format(siresmen70).replace(',', ' ')
    siresmen80 = '{0:,}'.format(siresmen80).replace(',', ' ')
    siremes40 = '{0:,}'.format(siremes40).replace(',', ' ')
    siremes50 = '{0:,}'.format(siremes50).replace(',', ' ')
    siremes60 = '{0:,}'.format(siremes60).replace(',', ' ')
    siremes70 = '{0:,}'.format(siremes70).replace(',', ' ')
    siremes80 = '{0:,}'.format(siremes80).replace(',', ' ')
    sto = '{0:,}'.format(sto).replace(',', ' ')
    stodvapyat = '{0:,}'.format(stodvapyat).replace(',', ' ')
    stopyatdes = '{0:,}'.format(stopyatdes).replace(',', ' ')
    stosempesyat = '{0:,}'.format(stosempesyat).replace(',', ' ')
    dvesti = '{0:,}'.format(dvesti).replace(',', ' ')
    return render(request, 'converter/resultEng.html', {'name1': ustanovkamango,
    'name2': narezka, 'name3': vent, 'name4': teh, 'name5': freez, 'name6': package,
    'name7': itogo, 'name8': arenda, 'name9': kolsotr, 'name10': zp,
    'name11': smenmes, 'name12': smenchas, 'name13': itogo2, 'name14': stoimsmeni,
    'name15': stsir1, 'name16': loadequip, 'name17': exitcomplproduct, 'name18': timecikl,
    'name19': kolcikl, 'name20': porcup, 'name21': kolporcikl, 'name22': kolporcchas,
    'name23': sebestpor, 'name24': stEE, 'name25': maxpot, 'name26': kef, 'name27': stwater,
    'name28': raswater, 'name29': stnoschas, 'name30': stnoscikl, 'name31': ctnospor,
    'name32': upak, 'name33': porcsmen40, 'name34': porcsmen50, 'name35': porcsmen60,
    'name36': porcsmen70, 'name37': porcsmen80, 'name38': sbsproducsmen40, 'name39': sbsproducsmen50,
    'name40': sbsproducsmen60, 'name41': sbsproducsmen70, 'name42': sbsproducsmen80, 'name43': sbsporc40,
    'name44': sbsporc50, 'name45': sbsporc60, 'name46': sbsporc70, 'name47': sbsporc80, 'name48': siresmen40,
    'name49': siresmen50, 'name50': siresmen60, 'name51': siresmen70, 'name52': siresmen80, 'name53': siremes40,
    'name54': siremes50, 'name55': siremes60, 'name56': siremes70, 'name57': siremes80, 'name58': marza100_40,
    'name59': marza100_50, 'name60': marza100_60, 'name61': marza100_70, 'name62': marza100_80, 'name63': marza125_40,
    'name64': marza125_50, 'name65': marza125_60, 'name66': marza125_70, 'name67': marza125_80, 'name68': marza150_40,
    'name69': marza150_50, 'name70': marza150_60, 'name71': marza150_70, 'name72': marza150_80, 'name73': marza175_40,
    'name74': marza175_50, 'name75': marza175_60, 'name76': marza175_70, 'name77': marza175_80, 'name78': marza200_40,
    'name79': marza200_50, 'name80': marza200_60, 'name81': marza200_70, 'name82': marza200_80,
    'name83': prodrubporc100_40, 'name84': prodrubporc100_50, 'name85': prodrubporc100_60, 'name86': prodrubporc100_70,
    'name87': prodrubporc100_80, 'name88': prodrubporc125_40, 'name89': prodrubporc125_50, 'name90': prodrubporc125_60,
    'name91': prodrubporc125_70, 'name92': prodrubporc125_80, 'name93': prodrubporc150_40, 'name94': prodrubporc150_50,
    'name95': prodrubporc150_60, 'name96': prodrubporc150_70, 'name97': prodrubporc150_80, 'name98': prodrubporc175_40,
    'name99': prodrubporc175_50, 'name100': prodrubporc175_60, 'name101': prodrubporc175_70, 'name102': prodrubporc175_80,
    'name103': prodrubporc200_40, 'name104': prodrubporc200_50, 'name105': prodrubporc200_60, 'name106': prodrubporc200_70,
    'name107': prodrubporc200_80, 'name108': sto, 'name109': stodvapyat, 'name110': stopyatdes, 'name111': stosempesyat,
    'name112': dvesti, })




