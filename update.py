#!/usr/bin/python

stations = \
{
    # somafm.com
    'http://somafm.com/bagel.pls':            'by-name/somafm.com/bagel.pls',
    'http://somafm.com/beatblender.pls':      'by-name/somafm.com/beatblender.pls',
    'http://somafm.com/bootliquor.pls':       'by-name/somafm.com/bootliquor.pls',
    'http://somafm.com/brfm.pls':             'by-name/somafm.com/brfm.pls',
    'http://somafm.com/cliqhop.pls':          'by-name/somafm.com/cliqhop.pls',
    'http://somafm.com/covers.pls':           'by-name/somafm.com/covers.pls',
    'http://somafm.com/digitalis.pls':        'by-name/somafm.com/digitalis.pls',
    'http://somafm.com/doomed.pls':           'by-name/somafm.com/doomed.pls',
    'http://somafm.com/dronezone.pls':        'by-name/somafm.com/dronezone.pls',
    'http://somafm.com/dubstep.pls':          'by-name/somafm.com/dubstep.pls',
    'http://somafm.com/folkfwd.pls':          'by-name/somafm.com/folkfwd.pls',
    'http://somafm.com/groovesalad.pls':      'by-name/somafm.com/groovesalad.pls',
    'http://somafm.com/illstreet.pls':        'by-name/somafm.com/illstreet.pls',
    'http://somafm.com/indiepop.pls':         'by-name/somafm.com/indiepop.pls',
    'http://somafm.com/lush.pls':             'by-name/somafm.com/lush.pls',
    'http://somafm.com/missioncontrol.pls':   'by-name/somafm.com/missioncontrol.pls',
    'http://somafm.com/poptron.pls':          'by-name/somafm.com/poptron.pls',
    'http://somafm.com/secretagent.pls':      'by-name/somafm.com/secretagent.pls',
    'http://somafm.com/sf1033.pls':           'by-name/somafm.com/sf1033.pls',
    'http://somafm.com/sonicuniverse192.pls': 'by-name/somafm.com/sonicuniverse192.pls',
    'http://somafm.com/spacestation.pls':     'by-name/somafm.com/spacestation.pls',
    'http://somafm.com/suburbsofgoa.pls':     'by-name/somafm.com/suburbsofgoa.pls',
    'http://somafm.com/sxfm.pls':             'by-name/somafm.com/sxfm.pls',
    'http://somafm.com/thetrip.pls':          'by-name/somafm.com/thetrip.pls',
    'http://somafm.com/u80s192.pls':          'by-name/somafm.com/u80s192.pls',

    # di.fm
    'http://listen.di.fm/public3/ambient.pls':            'by-name/di.fm/ambient.pls',
    'http://listen.di.fm/public3/bigroomhouse.pls':       'by-name/di.fm/bigroomhouse.pls',
    'http://listen.di.fm/public3/breaks.pls':             'by-name/di.fm/breaks.pls',
    'http://listen.di.fm/public3/chillout.pls':           'by-name/di.fm/chillout.pls',
    'http://listen.di.fm/public3/chilloutdreams.pls':     'by-name/di.fm/chilloutdreams.pls',
    'http://listen.di.fm/public3/chiptunes.pls':          'by-name/di.fm/chiptunes.pls',
    'http://listen.di.fm/public3/classiceurodance.pls':   'by-name/di.fm/classiceurodance.pls',
    'http://listen.di.fm/public3/classiceurodisco.pls':   'by-name/di.fm/classiceurodisco.pls',
    'http://listen.di.fm/public3/classictechno.pls':      'by-name/di.fm/classictechno.pls',
    'http://listen.di.fm/public3/classictrance.pls':      'by-name/di.fm/classictrance.pls',
    'http://listen.di.fm/public3/classicvocaltrance.pls': 'by-name/di.fm/classicvocaltrance.pls',
    'http://listen.di.fm/public3/club.pls':               'by-name/di.fm/club.pls',
    'http://listen.di.fm/public3/clubdubstep.pls':        'by-name/di.fm/clubdubstep.pls',
    'http://listen.di.fm/public3/cosmicdowntempo.pls':    'by-name/di.fm/cosmicdowntempo.pls',
    'http://listen.di.fm/public3/darkdnb.pls':            'by-name/di.fm/darkdnb.pls',
    'http://listen.di.fm/public3/deephouse.pls':          'by-name/di.fm/deephouse.pls',
    'http://listen.di.fm/public3/deepnudisco.pls':        'by-name/di.fm/deepnudisco.pls',
    'http://listen.di.fm/public3/deeptech.pls':           'by-name/di.fm/deeptech.pls',
    'http://listen.di.fm/public3/discohouse.pls':         'by-name/di.fm/discohouse.pls',
    'http://listen.di.fm/public3/djmixes.pls':            'by-name/di.fm/djmixes.pls',
    'http://listen.di.fm/public3/drumandbass.pls':        'by-name/di.fm/drumandbass.pls',
    'http://listen.di.fm/public3/dubstep.pls':            'by-name/di.fm/dubstep.pls',
    'http://listen.di.fm/public3/eclectronica.pls':       'by-name/di.fm/eclectronica.pls',
    'http://listen.di.fm/public3/electro.pls':            'by-name/di.fm/electro.pls',
    'http://listen.di.fm/public3/epictrance.pls':         'by-name/di.fm/epictrance.pls',
    'http://listen.di.fm/public3/eurodance.pls':          'by-name/di.fm/eurodance.pls',
    'http://listen.di.fm/public3/funkyhouse.pls':         'by-name/di.fm/funkyhouse.pls',
    'http://listen.di.fm/public3/futuresynthpop.pls':     'by-name/di.fm/futuresynthpop.pls',
    'http://listen.di.fm/public3/glitchhop.pls':          'by-name/di.fm/glitchhop.pls',
    'http://listen.di.fm/public3/goapsy.pls':             'by-name/di.fm/goapsy.pls',
    'http://listen.di.fm/public3/handsup.pls':            'by-name/di.fm/handsup.pls',
    'http://listen.di.fm/public3/hardcore.pls':           'by-name/di.fm/hardcore.pls',
    'http://listen.di.fm/public3/harddance.pls':          'by-name/di.fm/harddance.pls',
    'http://listen.di.fm/public3/hardstyle.pls':          'by-name/di.fm/hardstyle.pls',
    'http://listen.di.fm/public3/house.pls':              'by-name/di.fm/house.pls',
    'http://listen.di.fm/public3/latinhouse.pls':         'by-name/di.fm/latinhouse.pls',
    'http://listen.di.fm/public3/liquiddnb.pls':          'by-name/di.fm/liquiddnb.pls',
    'http://listen.di.fm/public3/liquiddubstep.pls':      'by-name/di.fm/liquiddubstep.pls',
    'http://listen.di.fm/public3/lounge.pls':             'by-name/di.fm/lounge.pls',
    'http://listen.di.fm/public3/mainstage.pls':          'by-name/di.fm/mainstage.pls',
    'http://listen.di.fm/public3/minimal.pls':            'by-name/di.fm/minimal.pls',
    'http://listen.di.fm/public3/oldschoolacid.pls':      'by-name/di.fm/oldschoolacid.pls',
    'http://listen.di.fm/public3/progressive.pls':        'by-name/di.fm/progressive.pls',
    'http://listen.di.fm/public3/progressivepsy.pls':     'by-name/di.fm/progressivepsy.pls',
    'http://listen.di.fm/public3/psychill.pls':           'by-name/di.fm/psychill.pls',
    'http://listen.di.fm/public3/russianclubhits.pls':    'by-name/di.fm/russianclubhits.pls',
    'http://listen.di.fm/public3/soulfulhouse.pls':       'by-name/di.fm/soulfulhouse.pls',
    'http://listen.di.fm/public3/spacemusic.pls':         'by-name/di.fm/spacemusic.pls',
    'http://listen.di.fm/public3/techhouse.pls':          'by-name/di.fm/techhouse.pls',
    'http://listen.di.fm/public3/techno.pls':             'by-name/di.fm/techno.pls',
    'http://listen.di.fm/public3/trance.pls':             'by-name/di.fm/trance.pls',
    'http://listen.di.fm/public3/tribalhouse.pls':        'by-name/di.fm/tribalhouse.pls',
    'http://listen.di.fm/public3/ukgarage.pls':           'by-name/di.fm/ukgarage.pls',
    'http://listen.di.fm/public3/umfradio.pls':           'by-name/di.fm/umfradio.pls',
    'http://listen.di.fm/public3/vocalchillout.pls':      'by-name/di.fm/vocalchillout.pls',
    'http://listen.di.fm/public3/vocaltrance.pls':        'by-name/di.fm/vocaltrance.pls',

    # divbyzero.de
    'http://divbyzero.de/chill.pls': 'by-name/divbyzero.de/ambient-and-downbeat.pls',
    'http://divbyzero.de/mix.pls':   'by-name/divbyzero.de/mixes-and-livesets.pls',
    'http://divbyzero.de/va.pls':    'by-name/divbyzero.de/progressive.pls',
    'http://divbyzero.de/old.pls':   'by-name/divbyzero.de/goa.pls',

    # radio23.cz
    'http://stream1.radio23.cz/1ch128.m3u': 'by-name/radio23.cz/ch1-tekno.m3u',
    'http://stream1.radio23.cz/2ch128.m3u': 'by-name/radio23.cz/ch2-breakbeat.m3u',
    'http://stream1.radio23.cz/3ch128.m3u': 'by-name/radio23.cz/ch3-psytrance.m3u',
    'http://stream1.radio23.cz/4ch128.m3u': 'by-name/radio23.cz/ch4-dnb.m3u',
    'http://stream1.radio23.cz/5ch128.m3u': 'by-name/radio23.cz/ch5-hardcore.m3u',
    'http://stream1.radio23.cz/live.m3u':   'by-name/radio23.cz/ch-live.m3u',

    # rozhlas.cz
    'http://www.play.cz/radio/cro1-128.mp3.m3u':         'by-name/rozhlas.cz/1.m3u',
    'http://www.play.cz/radio/cro2-128.mp3.m3u':         'by-name/rozhlas.cz/2.m3u',
    'http://www.play.cz/radio/cro3-128.mp3.m3u':         'by-name/rozhlas.cz/3.m3u',
    'http://www.play.cz/radio/cro7-128.mp3.m3u':         'by-name/rozhlas.cz/7.m3u',
    'http://www.play.cz/radio/crobrno128.mp3.m3u':       'by-name/rozhlas.cz/brno.m3u',
    'http://www.play.cz/radio/crocb128.mp3.m3u':         'by-name/rozhlas.cz/cb.m3u',
    'http://www.play.cz/radio/croddur-128.mp3.m3u':      'by-name/rozhlas.cz/ddur.m3u',
    'http://www.play.cz/radio/crohk128.mp3.m3u':         'by-name/rozhlas.cz/hk.m3u',
    'http://www.play.cz/radio/crojuniormaxi128.mp3.m3u': 'by-name/rozhlas.cz/juniormaxi.m3u',
    'http://www.play.cz/radio/crojuniormini128.mp3.m3u': 'by-name/rozhlas.cz/juniormini.m3u',
    'http://www.play.cz/radio/crokv128.mp3.m3u':         'by-name/rozhlas.cz/kv.m3u',
    'http://www.play.cz/radio/croliberec128.mp3.m3u':    'by-name/rozhlas.cz/liberec.m3u',
    'http://www.play.cz/radio/crool128.mp3.m3u':         'by-name/rozhlas.cz/ol.m3u',
    'http://www.play.cz/radio/croov128.mp3.m3u':         'by-name/rozhlas.cz/ov.m3u',
    'http://www.play.cz/radio/cropardubice128.mp3.m3u':  'by-name/rozhlas.cz/pardubice.m3u',
    'http://www.play.cz/radio/croplus128.mp3.m3u':       'by-name/rozhlas.cz/plus.m3u',
    'http://www.play.cz/radio/croplzen128.mp3.m3u':      'by-name/rozhlas.cz/plzen.m3u',
    'http://www.play.cz/radio/croregina128.mp3.m3u':     'by-name/rozhlas.cz/regina.m3u',
    'http://www.play.cz/radio/croregion128.mp3.m3u':     'by-name/rozhlas.cz/region.m3u',
    'http://www.play.cz/radio/crosever128.mp3.m3u':      'by-name/rozhlas.cz/sever.m3u',
    'http://www.play.cz/radio/crovysocina128.mp3.m3u':   'by-name/rozhlas.cz/vysocina.m3u',
    'http://www.play.cz/radio/crowave-128.mp3.m3u':      'by-name/rozhlas.cz/wave.m3u',

    'http://www.bassdrive.com/v2/streams/BassDrive.pls':  'by-name/bassdrive.pls',
    'http://www.dirtlabaudio.com/listen.m3u':             'by-name/dirt-lab-audio.m3u',
}

import os
import os.path
import urllib2
import contextlib

def download_playlist(url, dest):
    if not os.path.isdir(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))

    with contextlib.closing(urllib2.urlopen(url)) as i, open(dest, 'w') as o:
        while True:
            chunk = i.read(8192)
            if not chunk:
                break
            o.write(chunk)

for (url, dest) in sorted(stations.iteritems()):
    print '{0} -> {1}'.format(url, dest)
    download_playlist(url, dest)
