# pylint: skip-file
# flake8: noqa

import requests

# https://www.dwd.de/DE/service/impressum/impressum_node.html

BASEURL_RESPONSE = """
<!DOCTYPE html>
<html xml:lang="de" lang="de" class="no-js">
  <head>
   <meta http-equiv="X-UA-Compatible" content="IE=edge" /> 
   <base href="https://www.dwd.de/"/>
   <meta charset="utf-8">
   <meta name="viewport" content="width=320, minimum-scale=1.0, maximum-scale=1.0" />
    <title>Wetter und Klima - Deutscher Wetterdienst   -  Impressum</title>
    <meta name="generator" content="Government Site Builder"/>

    <script type="text/javascript">//<![CDATA[
      // i18n
        var PRINT_PAGE_TEXT = 'Seite drucken';
        var PRINT_TOOLTIP = 'Seite drucken (öffnet Dialog)';
        var MOBILENAVIGATION_JSON_URL = 'SiteGlobals/Functions/Navigation_Mobile/DE/mobile_navi_file.json?view=renderMobileNavigation';
        var MOBILENAVIGATION_ACTIVENODE = 'node20630';
        //constants
        var CLINKS;
        CLINKS = CLINKS || {};
        CLINKS['calendar'] = "SiteGlobals/Functions/Kalender/DE/Kalender.html";
        CLINKS['search'] = "SiteGlobals/Forms/Suche/Autosuggest_Formular.html";
        CLINKS['search.json'] = "SiteGlobals/Forms/Suche/Autosuggest_Formular.json";
        CLINKS['requirePath'] = "SiteGlobals/Functions/JavaScript_Optimierung2/_standardlsg";
        CLINKS['html5player'] = "SiteGlobals/Functions/JavaScript_Optimierung2/libs/jwplayer.html5.js?v=1";
        CLINKS['renderCityWeather.json?view=renderCityWeather'] = "SiteGlobals/Functions/CityWeather/RenderCityWeather.json?view=renderCityWeather";
        CLINKS['RenderWeatherStatus.html?view=renderWeatherStatus'] = "SiteGlobals/Functions/Unwetterwarnung/RenderWeatherStatus.html?view=renderWeatherStatus";
        CLINKS['CityWeatherCookiePath.value'] = "/SiteGlobals/";
        CLINKS['CityWeatherSprite.normal'] = "/SiteGlobals/StyleBundles/Bilder/Allgemein/staedtewetter.svg?__blob=normal&amp;v=1";
        CLINKS['ConsentBoxCookieExpiration.value'] = "360";
        CLINKS['inkas_wirkungsanalyse'] = "_config/ConsentBoxCookieExpiration.html";
        CLINKS['inkas_flaechenanalyse'] = "_config/ConsentBoxCookieExpiration.html";
        CLINKS['inkasstart'] = "_config/ConsentBoxCookieExpiration.html";
        CLINKS['inkas_wirkungsanalyse_en'] = "_config/ConsentBoxCookieExpiration.html";
        CLINKS['inkas_flaechenanalyse_en'] = "_config/ConsentBoxCookieExpiration.html";
        CLINKS['inkasstart_en'] = "_config/ConsentBoxCookieExpiration.html";
        CLINKS['svgInlineCSS'] = "SiteGlobals/Frontend/inkas/css/inkas-svg.css?v=2";
        CLINKS['inkasKomplett'] = "SiteGlobals/Frontend/inkas/js/inkasKomplett.js?v=1";
        CLINKS['config.inkasJson'] = "/inkasbackend/inkas/config.json";
        CLINKS['texts.inkasJson'] = "/inkasbackend/inkas/texts.json";
        CLINKS['zeitlichewirkung.inkasCSV'] = "/inkasbackend/inkas/zeitlichewirkung.csv";
        CLINKS['nrw/config-nrw.inkasJson'] = "/inkasbackend/inkas/nrw/config-nrw.json";
        CLINKS['nrw/texts-nrw.inkasJson'] = "/inkasbackend/inkas/nrw/texts-nrw.json";
        CLINKS.flashplayer = "/SiteGlobals/Functions/VideoPlayer/VideoPlayer.swf?__blob=value&amp;v=2";
        var RQNAMES;
        RQNAMES = RQNAMES || {};
        RQNAMES['app/modules/showbox.js'] = "app/modules/showbox%2Ejs";
        RQNAMES['../__enhanced.js'] = "../__enhanced%2Ejs";
        RQNAMES['../__modules.js'] = "../__modules%2Ejs";
        RQNAMES['Addon_UnwetterForm'] = "Addon_UnwetterForm";
        RQNAMES['Addon_mmenu'] = "Addon_mmenu";
        RQNAMES['Addon_MobileNavigations'] = "Addon_MobileNavigations";
        RQNAMES['Addon_Accordion'] = "Addon_Accordion";
        RQNAMES['Addon_Autosuggest'] = "Addon_Autosuggest";
        RQNAMES['Addon_StaedteWetter'] = "Addon_StaedteWetter";
        RQNAMES['Addon_GlossarPopup'] = "Addon_GlossarPopup";
        RQNAMES['Addon_Lightbox'] = "JQuery_PlugIn_Lightbox";
        RQNAMES['Addon_Lightbox_a11y'] = "JQuery_PlugIn_a11y";
        RQNAMES['jQuery_UI_Position'] = "JQuery_UI_Position";
        RQNAMES['jQuery_UI_Autocomplete'] = "JQuery_UI_Autocomplete";
        RQNAMES['jQuery_UI_Menu'] = "JQuery_UI_Menu";
        RQNAMES['libs/hammer.js'] = "libs/hammer%2Ejs";
        RQNAMES['libs/jquery.ui.mouse.js'] = "libs/jquery.ui.mouse%2Ejs";
        RQNAMES['libs/jquery.ui.slider.js'] = "libs/jquery.ui.slider%2Ejs";
        var LABELS;
        LABELS = LABELS || {};
        LABELS['MobilesMenueLaed'] = decodeURIComponent("Mobiles Men%C3%BC wird geladen. Bitte warten.");
        LABELS['MenueAusblenden'] = decodeURIComponent("Men%C3%BC ausblenden");
        LABELS['MenueEinblenden'] = decodeURIComponent("Men%C3%BC einblenden");
        LABELS['Schliessen'] = decodeURIComponent("Schlie%C3%9Fen");
        LABELS['MehrAnzeigen'] = decodeURIComponent("Mehr anzeigen");
        LABELS['TeilenUeberschrift'] = decodeURIComponent("In sozialen Medien teilen");
        LABELS['TeilenLink'] = decodeURIComponent("Diese Seite teilen");
        LABELS['InkasVergleichenButton'] = decodeURIComponent("Auswahl");
        LABELS['InkasVergleichEntfernenButton'] = decodeURIComponent("Auswahl aufheben");
        LABELS['TeilenEmailBodytext'] = decodeURIComponent("Sie erhalten diese E-Mail%2C weil Ihnen jemand einen Artikel auf www.dwd.de empfohlen hat%3A%0A%7Burl%7D");
      //]]>
    </script>


    <meta name="keywords" content="Impressum"/>    <meta name="description" content="Impressum des Auftritts"/>

    <meta name="og:image" content="/SiteGlobals/StyleBundles/Bilder/Allgemein/OpenGraphImage-DWD-Logo.jpg?__blob=normal&amp;v=3" />


    <link rel="canonical" href="https://www.dwd.de/DE/service/impressum/impressum_node.html"/>
    <link rel="copyright" href="" type="text/html" title="Impressum" />
    <link rel="glossary" href="" type="text/html" title="Glossar" />
    <link rel="help" href="" type="text/html" title="Hilfe" />
    <link rel="start" href="DE/Home/home_node.html" type="text/html" title="Homepage" />
    <link rel="contents" href="" type="text/html" title="&Uuml;bersicht" />
    <link rel="search" href="" type="text/html" title="Suche" />
    <link rel="shortcut icon" href="/SiteGlobals/StyleBundles/Bilder/favicon.ico?__blob=normal&amp;v=1" type="image/ico" />


<link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/screen/styles.css?v=20" type="text/css" media="screen" />
<link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/handheld/handheld_addon_mmenu.css?v=2" type="text/css" media="all and (max-width: 599px)" />
<link rel="stylesheet"  href="SiteGlobals/StyleBundles/CSS/screen/screen_addon_autosuggest.css?v=2" type="text/css" media ="projection, screen, handheld"  />
<link rel="stylesheet"  href="SiteGlobals/StyleBundles/CSS/screen/screen_addon_shariff.css?v=3" type="text/css" media ="projection, screen, handheld"  />
<link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/screen/materna_additional_stylesheet.css?v=99" type="text/css" media="screen" />
<link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/screen/mediaelementplayer.css?v=1" type="text/css" media="screen" />
<link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/screen/mediaelementplayer_additional.css?v=1" type="text/css" media="screen" />
<link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/screen/jquery.tablesorter.theme.default.css?v=1" type="text/css" media="screen" />
<!-- Additional IE/Win specific style sheet (Conditional Comments) --><!--[if IE 8]><link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/screen/ie8.css?v=1" type="text/css" media="screen, projection" /><![endif]-->
<!-- Additional IE/Win specific style sheet (Conditional Comments) --><!--[if lte IE 7]><link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/screen/ie6-7.css?v=1" type="text/css" media="projection, screen" /><![endif]-->
<!-- Additional IE/Win specific style sheet (Conditional Comments) --><!--[if lte IE 8]><link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/screen/screen_iew.css?v=1" type="text/css" media="projection, screen" /><![endif]-->
<link rel="stylesheet" href="SiteGlobals/StyleBundles/CSS/print/print.css?v=5" type="text/css" media="print" />
<link rel="stylesheet"  href="SiteGlobals/StyleBundles/CSS/screen/screen_addon_fontawesome.css?v=1" type="text/css" media ="projection, screen, handheld"  />



<!--[if IE 8]>
 <script src="SiteGlobals/Functions/JavaScript/__ie8.js.js?v=1"></script>
 <![endif]-->
 <!--[if ! lte IE 7]><!--> 
<!--
    <script src="SiteGlobals/Functions/JavaScript/__base.js.js?v=1"></script>
    <script src="SiteGlobals/Functions/JavaScript/__start.js.js?v=1"></script>
-->
    <script src="SiteGlobals/Functions/JavaScript_Optimierung2/__everything.js?v=13"></script>
 <!--<![endif]-->
<!--[if IE 8]>
        <script src="SiteGlobals/Functions/JavaScript/html5shiv.js.js?v=1"></script>
<![endif]-->
  </head>
  <body class=" no-header-bg  lang-de">


<a name="Start"></a>
 <div class="navSkip">
<ul>
   <li><a href="DE/service/impressum/impressum_node.html#Inhalt">Inhalt</a></li>
   <li><a href="DE/service/impressum/impressum_node.html#Hauptmenu">Hauptmenu</a></li>
   <li><a href="DE/service/impressum/impressum_node.html#Suche">Suche</a></li>
</ul>
</div>
 <header role="banner">


  <div id="top-bar" class="slot noWarning">
   <div class="row">
      <nav id="nav-meta" role="navigation">
        <h1>MetaNavigation</h1>
<a href="#" class="menu-button" title="Menü einblenden"><span>zum Haupt-</span>Menü</a>

<ul><li ><a href="DE/presse/presseseite_node.html" title="Presse">Pres­se</a></li><li ><a href="DE/service/kontakt/kontakt_node.html" title="Kontakt">Kon­takt</a></li><li ><a title="English" class="languageLink lang_en" href="EN/service/imprint/imprint_node.html" xml:lang="en" hreflang="en" lang="en">En</a></li><li  class="icon lang-s"><a href="DE/service/gebaerdensprache/gebaerdenSprache_node.html" title="Geb&#228;rdensprache">Ge­bär­den­spra­che</a></li><li  class="icon lang-e"><a href="DE/service/leichtesprache/leichte_sprache_home_node.html" title="Leichte Sprache">Leich­te Spra­che</a></li></ul>

      </nav>
<div class="weather weather-data">
     <p>
<a href="DE/wetter/wetterundklima_vorort/_node.html" title="Zum Städtewetter" alt="Zum Städtewetter">

      <span class="weather-location"></span>
      <span class="weather-icon icon-1"></span>
      <span class="weather-temp"></span>
</a>
     </p>
</div>
      <div class="search-btn">
         <a title="Suche einblenden" href="#">zur Suche</a>
      </div>



<div class="target-audience">
<form method="post">
<div class="select-box">
<fieldset>
<label for="select-box-id">Fachnutzer</label>

<select id="select-box-id" class="target" name="navigateTo">
<option>Fachnutzer</option>
              <option value='https://www.dwd.de/DE/fachnutzer/forschung_lehre/forschung_lehre_node.html' data-href='https://www.dwd.de/DE/fachnutzer/forschung_lehre/forschung_lehre_node.html'>Forschung und Lehre</option>
              <option value='https://www.dwd.de/DE/fachnutzer/freizeitgaertner/_node.html' data-href='https://www.dwd.de/DE/fachnutzer/freizeitgaertner/_node.html'>Freizeitgärtner</option>
              <option value='https://www.dwd.de/DE/fachnutzer/geoinformationswirtschaft/geoinformationswirtschaft_node.html' data-href='https://www.dwd.de/DE/fachnutzer/geoinformationswirtschaft/geoinformationswirtschaft_node.html'>Geoinformationswirtschaft</option>
              <option value='https://www.dwd.de/DE/fachnutzer/gesundheit/gesundheit_node.html' data-href='https://www.dwd.de/DE/fachnutzer/gesundheit/gesundheit_node.html'>Gesundheit</option>
              <option value='https://www.dwd.de/DE/fachnutzer/hobbymet/hobbymet_node.html' data-href='https://www.dwd.de/DE/fachnutzer/hobbymet/hobbymet_node.html'>Hobbymeteorologen</option>
              <option value='https://www.dwd.de/DE/fachnutzer/katastrophenschutz/katschutz_node.html' data-href='https://www.dwd.de/DE/fachnutzer/katastrophenschutz/katschutz_node.html'>Katastrophenschutz</option>
              <option value='https://www.dwd.de/DE/fachnutzer/landwirtschaft/landwirtschaft_node.html' data-href='https://www.dwd.de/DE/fachnutzer/landwirtschaft/landwirtschaft_node.html'>Land- und Forstwirtschaft</option>
              <option value='https://www.dwd.de/DE/fachnutzer/luftfahrt/luftfahrt_node.html' data-href='https://www.dwd.de/DE/fachnutzer/luftfahrt/luftfahrt_node.html'>Luftfahrt</option>
              <option value='https://www.dwd.de/DE/fachnutzer/schifffahrt/schifffahrt_node.html' data-href='https://www.dwd.de/DE/fachnutzer/schifffahrt/schifffahrt_node.html'>Schifffahrt</option>
              <option value='https://www.dwd.de/DE/fachnutzer/veranstalter/veranstalter_node.html' data-href='https://www.dwd.de/DE/fachnutzer/veranstalter/veranstalter_node.html'>Veranstalter</option>
              <option value='https://www.dwd.de/DE/fachnutzer/wasserwirtschaft/wasserwirtschaft_node.html' data-href='https://www.dwd.de/DE/fachnutzer/wasserwirtschaft/wasserwirtschaft_node.html'>Wasserwirtschaft</option>
</select>

<input type="submit" value="&gt;&gt;" class="non-js">

</fieldset>
</div>
</form>
</div>


<div class="weather weather-warning">
            <p class="no-warning">
            <a href="DE/wetter/warnungen/warnWetter_node.html" title="Zu den Wetterwarnungen" target="_blank">Kei­ne Un­wet­ter­war­nung</a>
            </p>
</div> 
   </div><!-- row -->
  </div><!-- slot -->
 
  <div id="search" class="slot extended">
   <div class="row">
    <div class="search-box" role="search">

<form name="ServicebereichSuche" action="SiteGlobals/Forms/Suche/Servicesuche_Formular.html" method="get" enctype="application/x-www-form-urlencoded">
  
  <input type="hidden" name="nn" value="20630"/>
  <input type="hidden" name="resourceId" value="13898" />
  <input type="hidden" name="input_" value="20630" />
  <input type="hidden" name="pageLocale" value="de" />
              
<span class="formLabel">
  <label for="f13898d20854">Suchtext </label></span>
            
  <input id="f13898d20854" name="templateQueryString" value="" title="Suchtext" type="text" placeholder="Suche ..." size="26" maxlength="100"/>
  <input id="f13898d22552" name="sortOrder" value="score desc" type="hidden"/>
            
  <input type="submit" name="submitButton" value="Suchen" class="submit" title="Suchen"/>


</form>
    </div>
   </div>
  </div>  

   <div id="nav" class="slot">
<div class="PrintLogo"><a href="DE/Home/home_node.html" id="anfang" title="Zur Startseite"><img src="/SiteGlobals/StyleBundles/Bilder/Farbschema/img/logo.png?__blob=normal&amp;v=3" alt="Government Site Builder Standardl&ouml;sung (Link zur Startseite)" /></a></div>
   <div class="row">
    <nav role="navigation">
     <h1 class="logo"><a href="DE/Home/home_node.html">Deutscher Wetterdienst <em>Wetter und Klima aus einer Hand</em></a></h1>    
     <section>
      <h1>Navigationsmenue</h1>
<ul class="level-1"><li class="has-flyout virgin "><a href="DE/wetter/wetter_node.html" title="Alles rund um das aktuelle Wetter und die Wettervorhersage">Wet­ter</a>
      <div class="flyout">
        <div class="flyout-box-group">
                <div class="flyout-box">
          <ul>
                <li><a href="DE/wetter/warnungen_gemeinden/warnWetter_node.html" title="Amtliche Warnungen aktuell">War­nun­gen</a></li>
                <li><a href="DE/wetter/wetterundklima_vorort/_node.html" title="lokale Wetter- und Klimawerte">Wet­ter und Kli­ma vor Ort</a></li>
                <li class="last"><a href="DE/wetter/vorhersage_aktuell/vhs_brd_node.html" title="aktuelle Wetterberichte f&#252;r die n&#228;chsten Tage f&#252;r Deutschland und die Bundesl&#228;nder">Wet­ter­be­rich­te</a></li>
                <li><a href="DE/wetter/wetter_weltweit/wetter_weltweit_node.html" title="aktuelle Wetterdaten und Vorhersagen weltweit">Wet­ter Eu­ro­pa und welt­weit</a></li>
                <li><a href="DE/wetter/schon_gewusst/schongewusst_node.html" title="Informationen &#252;ber den Erstellung von Wettervorhersagen, das DWD-Warnmanagement etc.">Schon ge­wusst?</a></li>
                <li class="last"><a href="DE/wetter/vorhersage_profis/vorhersageprofis_node.html" title="Wettervorhersagen f&#252;r Profis">Wet­ter­vor­her­sa­gen für Pro­fis</a></li>
          </ul></div></div></div></li><li class="has-flyout virgin "><a href="DE/klimaumwelt/klimaumwelt_node.html" title="Klima und Umwelt">Kli­ma und Um­welt</a>
      <div class="flyout">
        <div class="flyout-box-group">
                <div class="flyout-box">
          <ul>
                <li><a href="DE/klimaumwelt/klimawandel/klimawandel_node.html" title="Basisfakten zum Klimawandel">Ba­sis­fak­ten zum Kli­ma­wan­del</a></li>
                <li><a href="DE/klimaumwelt/klima-webdienste/_node.html" title="Klima-Webdienste">Kli­ma-Web­diens­te</a></li>
                <li class="last"><a href="DE/klimaumwelt/ku_beratung/ku_beratung_node.html" title="Klima- und Umweltberatung">Kli­ma- und Um­welt­be­ra­tung</a></li>
                <li><a href="DE/klimaumwelt/klimaueberwachung/klimaueberwachung_node.html" title="Klima&#252;berwachung">Kli­ma­über­wa­chung</a></li>
                <li class="last"><a href="DE/klimaumwelt/klimaforschung/klimaforschung_node.html" title="Klimaforschung">Kli­ma­for­schung</a></li>
          </ul></div></div></div></li><li class="has-flyout virgin "><a href="DE/forschung/forschung_node.html" title="Forschung">For­schung</a>
      <div class="flyout">
        <div class="flyout-box-group">
                <div class="flyout-box">
          <ul>
                <li><a href="DE/forschung/atmosphaerenbeob/atmosphaerenbeob_node.html" title="Atmosph&#228;renbeobachtung">At­mo­sphä­ren­be­ob­ach­tung</a></li>
                <li><a href="DE/forschung/wettervorhersage/wettervorhersage_node.html" title="Wettervorhersage">Wet­ter­vor­her­sa­ge</a></li>
                <li><a href="DE/forschung/klima_umwelt/klimaumwelt_node.html" title="Klima und Umwelt">Kli­ma und Um­welt</a></li>
                <li class="last"><a href="DE/forschung/forschungsprogramme/herz/herz_node.html" title="Hans-Ertel-Zentrum">Hans-Er­tel-Zen­trum</a></li>
                <li><a href="DE/forschung/forschungsprogramme/idea_s4s/idea_s4s_home_node.html" title="Italia &#8211; Deutschland science-4-services network in weather and climate ">IDEA-S4S Netz­werk</a></li>
                <li><a href="DE/forschung/forschungsprogramme/forschungsprogramme_node.html" title="DWD-Forschungsprogramme">DWD-For­schungs­pro­gram­me</a></li>
                <li><a href="DE/forschung/internationale_programme/internationale_programme_node.html" title="Internationale Programme">In­ter­na­tio­na­le Pro­gram­me</a></li>
                <li class="last"><a href="DE/forschung/projekte/projekte_node.html" title="Projekte">Pro­jek­te</a></li>
          </ul></div></div></div></li><li class="has-flyout virgin FlyoutLinks"><a href="DE/leistungen/_functions/Suche/Suche_Formular.html?nn=20630" title="Produkte und Leistungen des Deutschen Wetterdienstes">Leistungen</a></li><li class="has-flyout virgin FlyoutLinks"><a href="DE/derdwd/derdwd_node.html" title="Der Deutsche Wetterdienst - Aufgaben, Organisation, Standorte">Der DWD</a>
      <div class="flyout">
        <div class="flyout-box-group">
                <div class="flyout-box">
          <ul>
                <li><a href="DE/derdwd/aufgaben/aufgaben_node.html" title="Aufgaben">Auf­ga­ben</a></li>
                <li><a href="DE/derdwd/arbeitgeber/arbeitgeber_node.html" title="Arbeitgeber DWD">Ar­beit­ge­ber DWD</a></li>
                <li><a href="DE/derdwd/organisation/organisation_node.html" title="Organisation">Or­ga­ni­sa­ti­on</a></li>
                <li class="last"><a href="DE/derdwd/standorte/standorte_node.html" title="Standorte">Stand­orte</a></li>
                <li><a href="DE/derdwd/koop/koop_node.html" title="Zusammenarbeit">Zu­sam­men­ar­beit</a></li>
                <li><a href="DE/derdwd/messnetz/messnetz_node.html" title="Messnetz">Mess­netz</a></li>
                <li><a href="DE/derdwd/it/it_node.html" title="Informationstechnik">In­for­ma­ti­ons­tech­nik</a></li>
                <li class="last"><a href="DE/derdwd/bibliothek/bibliothek_node.html" title="Deutsche Meteorologische Bibliothek">Deut­sche Me­teo­ro­lo­gi­sche Bi­blio­thek</a></li>
          </ul></div></div></div></li>
</ul>
     </section>
    </nav>
   </div><!-- row -->
  </div><!-- slot -->   
 </header>

<main role="main" id="main">
 <div id="breadcrumbs" class="slot content">
   <div class="row">
    <nav role="navigation">
     <h1>Breadcrumb-<em> Menü</em></h1>
     <ul>
<li class="first"><a href="DE/Home/home_node.html" title="Startseite">Startseite</a></li>
     </ul>
    </nav>
   </div><!-- row -->
  </div><!-- slot -->

  <div class="slot content-sidebar">
   <div class="row">
         <section class="content">
    <div id="">
<div class="row text"><article class="article-full" role="article"><div class="intro">
<h1 class="isFirstInSlot">Impressum </h1></div><div class="body-text"><p><strong>Deutscher Wetterdienst</strong><br/>
<strong>Frankfurter Straße 135</strong><br/>
<strong>63067 Offenbach</strong><br/>
</p>

<p><br/>
<strong>Wetterdiensthotline: 0180 2 913 913</strong> *<br/>
<em><sub>*(Festnetzpreis 6 ct/Anruf, Mobilfunkpreise maximal 42 ct/min. innerhalb Deutschlands)</sub></em><br/>
</p>

<p><br/>
<strong><span lang="en-GB" xml:lang="en-GB">E-Mail</span>: info@dwd.de</strong><br/>
<strong>Internet: www.dwd.de</strong><br/>
</p>

<p><strong>Verantwortlich: Alexandros Bouras</strong></p>

<p>Die redaktionelle Verantwortung für die "Fachnutzer“-Seiten liegt bei der jeweiligen Fachabteilung.</p>

<p><strong>Kontoverbindung: </strong><br/>
Bundeskasse Halle – Deutsche Bundesbank Leipzig<br/>
<abbr title="International Bank Account Number">IBAN</abbr>: DE38 8600 0000 0086 0010 40<br/>
<abbr title="Bank-Identifizierungs-Code">BIC</abbr>: MARKDEFFXXX</p>

<p>Der Deutsche Wetterdienst ist eine teilrechtsfähige Anstalt des öffentlichen Rechts im Geschäftsbereich des Bundesministeriums für Digitales und Verkehr. <br/>
Vertretungsberechtigte Vorstandsmitglieder des Deutschen Wetterdienstes:</p>

<p>          </p>

<p>Prof. Dr. Sarah Jones (Präsidentin)<br/>
Norbert Wetter (Vizepräsident)<br/>
Dr. Renate Hagedorn<br/>
Tobias Fuchs<br/>
Klaus-Jürgen Schreiber </p>

<p>Das <a class="RichTextIntLink NavNode" href="DE/service/qm/qm_node.html" title="Qualitätsmanagement">Qualitätsmanagement</a> des <abbr title="Deutscher Wetterdienst">DWD</abbr> ist <a class="RichTextIntLink IMGObject" href="DE/derdwd/qm/bild_zertifikat_iso9001.html?nn=20630" target="_blank" rel="noopener noreferrer" title="Ausgestelltes Qualitätsmanagement Zertifikat: DIN EN ISO 9001 für den Deutschen Wetterdienst (Öffnet neues Fenster)">zertifiziert</a> nach <abbr title="Deutsches Institut für Normung">DIN</abbr> <abbr title="Euro Norm">EN</abbr> <abbr title="Internationale Organisation für Normung">ISO</abbr> 9001.</p>

<p>Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz:<br/>
DE 221793973 </p>
</div></article><div class="sectionRelated link-list"></div></div></div>
         </section>
    <div class="sidebar">
     <div class="row">
      <nav id="nav-sub" role="navigation">
       <section>
        <h1>Sub-Navigations-<em> Menü</em></h1>
<div class="navMain">
    <ul class="level-2">
      <li class="on " id="ServiceTree"><strong>Im­pres­s­um</strong>

</li>
      <li class=" " id="ServiceTree"><a href="DE/service/datenschutz/datenschutz_node.html" title="Datenschutz">Da­ten­schutz</a>

</li>
      <li class=" " id="ServiceTree"><a href="DE/service/disclaimer/disclaimer_node.html" title="Disclaimer">Disclai­mer</a>

</li>
      <li class=" " id="ServiceTree"><a href="DE/service/agb/agb_node.html" title="AGB">AGB</a>

</li>
      <li class=" " id="ServiceTree"><a href="DE/service/qm/qm_node.html" title="Qualit&#228;tsmanagement">QM</a>

</li>
      <li class=" " id="ServiceTree"><a href="DE/service/copyright/copyright_node.html" title="Copyright">Co­py­right</a>

</li>
      <li class="last " id="ServiceTree"><a href="DE/service/barrierefrei/barrierefrei_node.html" title="Erkl&#228;rung zur Barrierefreiheit">Er­klä­rung zur Bar­rie­re­frei­heit</a>

</li>
    </ul></div>
       </section>
      </nav>
    
     </div><!-- row -->
    </div><!-- sidebar -->

     </div><!-- row -->
</div><!-- content-sidebar -->

 <div class="slot content">
    
</div><!-- slot content -->

</main>
<script type="text/javascript">
<!--
window.rsConf = {general: {usePost: true}};
//-->
</script>

<script src="SiteGlobals/Functions/ReadSpeakerModul/ReadSpeakerSandbox/readspeakerScript.js?v=1&amp;pids=embhl" type="text/javascript"></script>



 <footer role="contentinfo" class="dwd-services">
<section class="materna-shariff-bar">
  <div class="row">
      <div class="materna-shariff subtle" data-lang="de">
        <a id="materna-shariff-bar-opener"><span>Diese Seite teilen</span></a>
      </div>
   </div>
</section>
  <section class="services">
   <div class="slot">
    <div class="row">
     <nav role="navigation">
      <h1>Service-Navigations-<em> Menü</em></h1>
      <ul>
<li class="service-1">
       <a href="DE/derdwd/bibliothek/bibliothek_node.html"  title="Deutsche Meteorologische Bibliothek"><span><span>Deutsche Meteorologische Bibliothek</span></span></a>
</li>
<li class="service-2">
       <a href="DE/presse/mediathek_socialmedia/mediathek_node.html"  title="Mediathek"><span><span>Mediathek</span></span></a>
</li>
<li class="service-3">
       <a class="external" href="/DE/service/lexikon/lexikon_node.html" title="Externer Link Wetter-Lexikon (Öffnet neues Fenster)" target="_blank" rel="noopener noreferrer"><span><span>Wetter-<br/>
Lexikon</span></span></a>
</li>
<li class="service-4">
       <a class="external" href="https://www.dwd-shop.de/" title="Externer Link WetterShop (Öffnet neues Fenster)" target="_blank" rel="noopener noreferrer"><span><span>WetterShop</span></span></a>
</li>
<li class="service-5">
       <a href="DE/derdwd/arbeitgeber/arbeitgeber_node.html"  title="Arbeitgeber DWD"><span><span>Arbeitgeber DWD</span></span></a>
</li>
      </ul>
     </nav>
    </div><!-- row -->
   </div><!-- slot -->
  </section>
</footer>
<footer role="contentinfo">
<section class="site-index">
   <h1>Inhatsverzeichnis</h1>
   <div class="slot">
    <div class="row">
         <nav class="box mod teaser type-2 link-list">
      <div class="teaser-box">
       <h1>DWD-Services</h1>
       <ul>
<li>
       <a href="DE/service/archiv/archiv_node.html"  title="Zum Archiv ''DWD Aktuell''">Zum Archiv &#039;&#039;DWD Aktuell&#039;&#039;</a>
</li>
<li>
       <a href="DE/service/termine/termine_node.html"  title="Termine, Veranstaltungen">Termine, Veranstaltungen</a>
</li>
<li>
       <a href="DE/service/dwd-apps/dwdapps_node.html"  title="DWD-Apps">DWD-Apps</a>
</li>
<li>
       <a href="DE/service/newsletter/newsletter_node.html"  title="Newsletter">Newsletter</a>
</li>
<li>
       <a href="DE/service/kurzadressen/kurzadressen_node.html"  title="Kurzadressen">Kurzadressen</a>
</li>
       </ul>
      </div>
     </nav>
     <nav class="box" role="navigation">
      <div class="box-box">
            <h1><a href="DE/wetter/wetter_node.html" title="Alles rund um das aktuelle Wetter und die Wettervorhersage">Wet­ter</a></h1>
            <ul id="footer-links-1">
              <li><a href="DE/wetter/warnungen_gemeinden/warnWetter_node.html"  title="Amtliche Warnungen aktuell"><span><span>Warnungen</span></span></a></li>
              <li><a href="DE/wetter/wetterundklima_vorort/_node.html"  title="lokale Wetter- und Klimawerte"><span><span>Wetter und Klima vor Ort</span></span></a></li>
              <li><a href="DE/wetter/vorhersage_aktuell/vhs_brd_node.html"  title="aktuelle Wetterberichte f&#252;r die n&#228;chsten Tage f&#252;r Deutschland und die Bundesl&#228;nder"><span><span>Wetterberichte</span></span></a></li>
              <li><a href="DE/wetter/wetter_weltweit/wetter_weltweit_node.html"  title="aktuelle Wetterdaten und Vorhersagen weltweit"><span><span>Wetter Europa und weltweit</span></span></a></li>
              <li><a href="DE/wetter/schon_gewusst/schongewusst_node.html"  title="Informationen &#252;ber den Erstellung von Wettervorhersagen, das DWD-Warnmanagement etc."><span><span>Schon gewusst?</span></span></a></li>
              <li><a href="DE/wetter/vorhersage_profis/vorhersageprofis_node.html"  title="Wettervorhersagen f&#252;r Profis"><span><span>Wettervorhersagen für Profis</span></span></a></li>
              </ul>
        </div><!-- box-box -->
     </nav><!-- box -->
     <nav class="box" role="navigation">
      <div class="box-box">
            <h1><a href="DE/klimaumwelt/klimaumwelt_node.html" title="Klima und Umwelt">Kli­ma und Um­welt</a></h1>
            <ul id="footer-links-2">
              <li><a href="DE/klimaumwelt/klimawandel/klimawandel_node.html"  title="Basisfakten zum Klimawandel"><span><span>Basisfakten zum Klimawandel</span></span></a></li>
              <li><a href="DE/klimaumwelt/klima-webdienste/_node.html"  title="Klima-Webdienste"><span><span>Klima-Webdienste</span></span></a></li>
              <li><a href="DE/klimaumwelt/ku_beratung/ku_beratung_node.html"  title="Klima- und Umweltberatung"><span><span>Klima- und Umweltberatung</span></span></a></li>
              <li><a href="DE/klimaumwelt/klimaueberwachung/klimaueberwachung_node.html"  title="Klima&#252;berwachung"><span><span>Klimaüberwachung</span></span></a></li>
              <li><a href="DE/klimaumwelt/klimaforschung/klimaforschung_node.html"  title="Klimaforschung"><span><span>Klimaforschung</span></span></a></li>
              </ul>
        </div><!-- box-box -->
     </nav><!-- box -->
     <nav class="box" role="navigation">
      <div class="box-box">
            <h1><a href="DE/forschung/forschung_node.html" title="Forschung">For­schung</a></h1>
            <ul id="footer-links-3">
              <li><a href="DE/forschung/atmosphaerenbeob/atmosphaerenbeob_node.html"  title="Atmosph&#228;renbeobachtung"><span><span>Atmosphärenbeobachtung</span></span></a></li>
              <li><a href="DE/forschung/wettervorhersage/wettervorhersage_node.html"  title="Wettervorhersage"><span><span>Wettervorhersage</span></span></a></li>
              <li><a href="DE/forschung/klima_umwelt/klimaumwelt_node.html"  title="Klima und Umwelt"><span><span>Klima und Umwelt</span></span></a></li>
              <li><a href="DE/forschung/forschungsprogramme/herz/herz_node.html"  title="Hans-Ertel-Zentrum"><span><span>Hans-Ertel-Zentrum</span></span></a></li>
              <li><a href="DE/forschung/forschungsprogramme/idea_s4s/idea_s4s_home_node.html"  title="Italia &#8211; Deutschland science-4-services network in weather and climate "><span><span>IDEA-S4S Netzwerk</span></span></a></li>
              <li><a href="DE/forschung/forschungsprogramme/forschungsprogramme_node.html"  title="DWD-Forschungsprogramme"><span><span>DWD-Forschungsprogramme</span></span></a></li>
              <li><a href="DE/forschung/internationale_programme/internationale_programme_node.html"  title="Internationale Programme"><span><span>Internationale Programme</span></span></a></li>
              <li><a href="DE/forschung/projekte/projekte_node.html"  title="Projekte"><span><span>Projekte</span></span></a></li>
              </ul>
        </div><!-- box-box -->
     </nav><!-- box -->
     <nav class="box" role="navigation">
      <div class="box-box">
            <h1><a href="DE/derdwd/derdwd_node.html" title="Der Deutsche Wetterdienst - Aufgaben, Organisation, Standorte">Der DWD</a></h1>
            <ul id="footer-links-4">
              <li><a href="DE/derdwd/aufgaben/aufgaben_node.html"  title="Aufgaben"><span><span>Aufgaben</span></span></a></li>
              <li><a href="DE/derdwd/arbeitgeber/arbeitgeber_node.html"  title="Arbeitgeber DWD"><span><span>Arbeitgeber DWD</span></span></a></li>
              <li><a href="DE/derdwd/organisation/organisation_node.html"  title="Organisation"><span><span>Organisation</span></span></a></li>
              <li><a href="DE/derdwd/standorte/standorte_node.html"  title="Standorte"><span><span>Standorte</span></span></a></li>
              <li><a href="DE/derdwd/koop/koop_node.html"  title="Zusammenarbeit"><span><span>Zusammenarbeit</span></span></a></li>
              <li><a href="DE/derdwd/messnetz/messnetz_node.html"  title="Messnetz"><span><span>Messnetz</span></span></a></li>
              <li><a href="DE/derdwd/it/it_node.html"  title="Informationstechnik"><span><span>Informationstechnik</span></span></a></li>
              <li><a href="DE/derdwd/bibliothek/bibliothek_node.html"  title="Deutsche Meteorologische Bibliothek"><span><span>Deutsche Meteorologische Bibliothek</span></span></a></li>
              </ul>
        </div><!-- box-box -->
     </nav><!-- box -->
    </div><!-- row -->
   </div><!-- slot -->
</section>
<section class="social-services">
   <div class="slot">
    <div class="row">
     <div class="box youtube">
      <div class="box-box">
       <a href="http://www.youtube.com/user/DWDderWetterdienst" target="_blank" rel="noopener noreferrer" title="Externer Link zur DWD-YouTube-Seite (Öffnet neues Fenster)">
        <span class="logo">You Tube</span>
        <p>
          Warn-Videos und viel mehr
        </p>
       </a>
      </div><!-- box-box -->
     </div><!-- box -->
     <div class="box facebook">
      <div class="box-box">
       <a href="https://www.facebook.com/DeutscherWetterdienst" target="_blank" rel="noopener noreferrer" title="Externer Link zur DWD-Facebook-Seite (Öffnet neues Fenster)">
        <span class="logo">Facebook</span>
        <p>
          Wetter und Klima aktuell und unterhaltend
        </p>
       </a>
      </div><!-- box-box -->
     </div><!-- box -->
     <div class="box flickr">
      <div class="box-box">
       <a href="http://www.flickr.com/deutscherwetterdienst" target="_blank" rel="noopener noreferrer" title="Externer Link zur DWD-Flickr-Seite (Öffnet neues Fenster)">
        <span class="logo">Flickr</span>
        <p>
          Wetter­phänomene vor der Kamera
        </p>
       </a>
      </div><!-- box-box -->
     </div><!-- box -->
     <div class="box twitter">
      <div class="box-box">
       <a href="https://www.dwd.de/DE/presse/mediathek_socialmedia/social_media_node.html" target="_blank" rel="noopener noreferrer" title="Link zur Social-Media-Seite des DWD (Öffnet neues Fenster)">
        <span class="logo">Twitter</span>
        <p>
          In bis zu 280 Zeichen Wetter und Klima weltweit
        </p>
       </a>
      </div><!-- box-box -->
     </div><!-- box -->
     <div class="box instagram">
      <div class="box-box">
       <a href="https://www.instagram.com/deutscherwetterdienst/" target="_blank" rel="noopener noreferrer" title="Externer Link zur DWD-Instagram-Seite (Öffnet neues Fenster)">
        <span class="logo">Instagram</span>
        <p>
          #ichliebewetter – Schnappschüsse und Videos
        </p>
       </a>
      </div><!-- box-box -->
     </div><!-- box -->
    </div><!-- row -->
   </div><!-- slot -->
</section>
<section class="legal">
   <div class="slot">
    <div class="row">
     <div class="box info">
      <div class="box-box">
       <p>
        Der Deutsche Wetterdienst ist eine Bundesoberbehörde im Geschäftsbereich des Bundesministeriums für Digitales und Verkehr.
       </p>
       <address>Deutscher Wetterdienst, Frankfurter Straße 135, 63067 Offenbach</address>
      </div><!-- box-box -->
     </div><!-- box -->
<div class="box links">
      <div class="box-box">
       <ul>
<li>
       <a href="DE/service/impressum/impressum_node.html"  title="Impressum">Impressum</a>
</li>
<li>
       <a href="DE/service/datenschutz/datenschutz_node.html"  title="Datenschutz">Datenschutz</a>
</li>
<li>
       <a href="DE/service/disclaimer/disclaimer_node.html"  title="Disclaimer">Disclaimer</a>
</li>
<li>
       <a href="DE/service/agb/agb_node.html"  title="AGB">AGB</a>
</li>
<li>
       <a href="DE/service/qm/qm_node.html"  title="Qualit&#228;tsmanagement">QM</a>
</li>
<li>
       <a href="DE/service/copyright/copyright_node.html"  title="Copyright">Copyright</a>
</li>
<li>
       <a href="DE/service/barrierefrei/barrierefrei_node.html"  title="Erkl&#228;rung zur Barrierefreiheit">Erklärung zur Barrierefreiheit</a>
</li>
       </ul>
      </div><!-- box-box -->
     </div><!-- box -->
    </div><!-- row -->
   </div><!-- slot -->
  </section>
 </footer>

 <!--[if ! lte IE 8]><!--> 
<!--
 <script type="text/javascript">
  preloader.modules = "SiteGlobals/Functions/JavaScript/__modules.js.js?v=3";
  preloader.enhanced= "SiteGlobals/Functions/JavaScript/__enhanced.js.js?v=4";
  preloader.everything = "SiteGlobals/Functions/JavaScript_Optimierung2/__everything.js?v=13";
  preloader.loadEverything = true;
 </script>
 <script src="SiteGlobals/Functions/JavaScript/__preload.js.js?v=1"></script>
-->

 <!--<![endif]-->

  </body>
</html>
"""

if __name__ == '__main__':
    r = requests.get('https://www.dwd.de/SiteGlobals/Forms/ThemaDesTages/ThemaDesTages_Formular.html', timeout=20)
    print(r.text)
    with open('dwd.html', 'w', encoding='UTF-8') as f:
        f.write(r.text)
    # print(BASEURL_RESPONSE)