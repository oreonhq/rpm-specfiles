%bcond pstoedit 1
# used only in RDF; Soprano has not been updated since Qt4
%bcond marble 0
%bcond visio 1
%bcond wpd 1
%bcond okular 1

#global external_lilypond_fonts 1

Name:    calligra 
Version: 26.04.1
Release: 1%{?dist}
Summary: An integrated office suite

License: GPL-2.0-or-later AND GPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND BSD-2-Clause
URL:     https://calligra.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/calligra-%{version}.tar.xz

## upstream patches

## upstreamable patches

## downstream patches
Patch200: calligra-disable_products.patch

# 
ExcludeArch: %{ix86}

BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: libappstream-glib

# kf6 deps
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DBusAddons)

# qt6 deps
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Sql)
%ifarch %{qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif
BuildRequires: cmake(Qt6DBus)

# other required deps
BuildRequires: perl-interpreter
BuildRequires: zlib-devel
BuildRequires: cmake(Qt6Keychain)
BuildRequires: boost-devel

# optional deps
BuildRequires: cmake(Imath)
BuildRequires: pkgconfig(gsl)
BuildRequires: cmake(Phonon4Qt6)
#BuildRequires: cmake(KF6CalendarCore)
#BuildRequires: cmake(KF6Contacts)
#BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KChart6)
BuildRequires: pkgconfig(eigen3)
BuildRequires: cmake(Qca-qt6)
%if %{with marble}
BuildRequires: cmake(Marble)
%endif
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(shared-mime-info)
%if %{with wpd}
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(libodfgen-0.1)
BuildRequires: pkgconfig(libwpd-0.10)
BuildRequires: pkgconfig(libwpg-0.3)
BuildRequires: pkgconfig(libwps-0.4)
%if %{with visio}
BuildRequires: pkgconfig(libvisio-0.1)
%endif
BuildRequires: pkgconfig(libetonyek-0.1)
%endif
BuildRequires: pkgconfig(poppler-qt6)
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(libgit2)

# -- The following OPTIONAL packages have not been found:
# * Qt6QmlCompilerPlusPrivate
# * Cauchy, Cauchy's M2MML, a Matlab/Octave to MathML compiler, <https://bitbucket.org/cyrille/cauchy>
#   Required for the matlab/octave formula tool
# * OOoSDK

Requires:  %{name}-words%{?_isa} = %{version}-%{release}
Requires:  %{name}-sheets%{?_isa} = %{version}-%{release}
Requires:  %{name}-stage%{?_isa} = %{version}-%{release}
Requires:  %{name}-karbon%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package data
Summary: Runtime support files for %{name}
%if %{undefined flatpak}
Requires: color-filesystem
%endif
%if 0%{?external_lilypond_fonts}
Requires: lilypond-emmentaler-fonts
%endif
Obsoletes: %{name}-core < 4
%if %{without okular}
Obsoletes: %{name}-okular-odpgenerator < %{version}-%{release}
Obsoletes: %{name}-okular-odtgenerator < %{version}-%{release}
%endif
BuildArch: noarch
%description data
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name}-data = %{version}-%{release}
%description libs
%{summary}.

%package l10n
Summary: Language files for calligra
# not *strictly* required, but helps ensure -l10n,-data, and other pkg versions match
Requires: %{name}-data = %{version}-%{release}
BuildArch: noarch
%description l10n
%{summary}.

%package  words
Summary:  An intuitive word processor application with desktop publishing features
Requires: %{name}-words-libs%{?_isa} = %{version}-%{release}
%description words
KWord is an intuitive word processor and desktop publisher application.
With it, you can create informative and attractive documents with
pleasure and ease.

%package  words-libs
Summary:  Runtime libraries for %{name}-words
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description words-libs
%{summary}.

%package  sheets 
Summary:  A fully-featured spreadsheet application
Requires: %{name}-sheets-libs%{?_isa} = %{version}-%{release}
%description sheets 
Tables is a fully-featured calculation and spreadsheet tool.  Use it to
quickly create and calculate various business-related spreadsheets, such
as income and expenditure, employee working hours…

%package  sheets-libs
Summary:  Runtime libraries for %{name}-sheets
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description sheets-libs
%{summary}.

%package  stage 
Summary:  A full-featured presentation program
Requires: %{name}-stage-libs%{?_isa} = %{version}-%{release}
%description stage 
Stage is a powerful and easy to use presentation application. You
can dazzle your audience with stunning slides containing images, videos,
animation and more.

%package  stage-libs
Summary:  Runtime libraries for %{name}-stage
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description stage-libs
%{summary}.

%package  karbon
Summary:  A vector drawing application
Requires: %{name}-karbon-libs%{?_isa} = %{version}-%{release}
%if %{with pstoedit}
# for karbon eps import filter
BuildRequires: pstoedit
Requires: pstoedit
%endif
%description karbon
Karbon is a vector drawing application with an user interface that is
easy to use, highly customizable and extensible. That makes Karbon a
great application for users starting to explore the world of vector
graphics as well as for artists wanting to create breathtaking vector
art.

Whether you want to create clipart, logos, illustrations or photorealistic
vector images – look no further, Karbon is the tool for you!

%package  karbon-libs
Summary:  Runtime libraries for %{name}-karbon
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description karbon-libs
%{summary}.

%if %{with okular}
%package  okular-odpgenerator
Summary:  OpenDocument presenter support for okular
BuildRequires: cmake(Okular6)
Requires: %{name}-stage-libs%{?_isa} = %{version}-%{release}
Requires: okular-part
Supplements: (%{name}-stage and okular)
%description okular-odpgenerator
%{summary}.

%package  okular-odtgenerator
Summary:  OpenDocument text support for okular
BuildRequires: cmake(Okular6)
Requires: %{name}-words-libs%{?_isa} = %{version}-%{release}
Requires: okular-part
Supplements: (%{name}-words and okular)
%description okular-odtgenerator
%{summary}.
%endif


%prep
%autosetup -p1


%build
%cmake_kf6 \
  -Wno-dev

%cmake_build


%install
%cmake_install

## unpackaged files
%if 0%{?external_lilypond_fonts}
rm -fv %{buildroot}%{_kf6_datadir}/calligra_shape_music/fonts/Emmentaler-14.ttf
%endif
rm -frv %{buildroot}%{_kf6_datadir}/locale/x-test/

%find_lang %{name} --all-name --with-html


%check
for appdata_file in %{buildroot}%{_kf6_metainfodir}/*.metainfo.xml ; do
appstream-util validate-relax --nonet ${appdata_file} ||:
done
for desktop_file in %{buildroot}%{_datadir}/applications/*.desktop ; do
desktop-file-validate ${desktop_file}  ||:
done


%files
%{_kf6_bindir}/calligraconverter
%{_kf6_bindir}/calligralauncher
%{_kf6_datadir}/applications/org.kde.calligra.desktop
%{_kf6_metainfodir}/org.kde.calligra.metainfo.xml

%files data
%doc AUTHORS README.md
%license COPYING*
%{_kf6_sysconfdir}/xdg/calligrasheetsrc
%{_kf6_sysconfdir}/xdg/calligrastagerc
%{_kf6_sysconfdir}/xdg/calligrawordsrc
%{_kf6_sysconfdir}/xdg/karbonrc
%{_datadir}/color/icc/calligra/
%{_kf6_datadir}/calligra/
%if ! 0%{?external_lilypond_fonts}
%{_kf6_datadir}/calligra_shape_music/fonts/Emmentaler-14.ttf
%endif
%{_kf6_datadir}/calligrasheets/
%{_kf6_datadir}/calligrastage/
%{_kf6_datadir}/calligrawords/
%{_kf6_datadir}/karbon/
%{_kf6_datadir}/config.kcfg/calligrasheets.kcfg
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/kxmlgui5/calligrasheets/
%{_kf6_datadir}/kxmlgui5/calligrastage/
%{_kf6_datadir}/kxmlgui5/calligrawords/
%{_kf6_datadir}/kxmlgui5/karbon/
%{_kf6_datadir}/mime/packages/calligra_svm.xml
%{_kf6_datadir}/mime/packages/wiki-format.xml

%files libs
%{_kf6_libdir}/libautocorrection.so*
%{_kf6_libdir}/libbasicflakes.so*
%{_kf6_libdir}/libflake.so*
%{_kf6_libdir}/libkoformula.so*
%{_kf6_libdir}/libkomain.so*
%{_kf6_libdir}/libkomsooxml.so*
%{_kf6_libdir}/libkoodf.so*
%{_kf6_libdir}/libkoodf2.so*
%{_kf6_libdir}/libkoodfreader.so*
%{_kf6_libdir}/libkopageapp.so*
%{_kf6_libdir}/libkoplugin.so*
%{_kf6_libdir}/libkostore.so*
%{_kf6_libdir}/libkotext.so*
%{_kf6_libdir}/libkotextlayout.so*
%{_kf6_libdir}/libkovectorimage.so*
%{_kf6_libdir}/libkowidgets.so*
%{_kf6_libdir}/libkowidgetutils.so*
%{_kf6_libdir}/libkowv2.so*
%{_kf6_libdir}/libkundo2.so*
%{_kf6_libdir}/libpigmentcms.so*
%{_kf6_libdir}/libRtfReader.so*
%dir %{_kf6_qtplugindir}/calligra/
%dir %{_kf6_qtplugindir}/calligra/colorspaces/
%{_kf6_qtplugindir}/calligra/colorspaces/kolcmsengine.so
%dir %{_kf6_qtplugindir}/calligra/dockers/
%{_kf6_qtplugindir}/calligra/dockers/calligra_docker_defaults.so
%{_kf6_qtplugindir}/calligra/dockers/calligra_docker_stencils.so
%dir %{_kf6_qtplugindir}/calligra/formatfilters/
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_eps2svgai.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_key2odp.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_kpr2odp.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_pdf2svg.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_vsdx2odg.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_wmf2svg.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_xfig2odg.so
%dir %{_kf6_qtplugindir}/calligra/pageapptools/
%{_kf6_qtplugindir}/calligra/pageapptools/kopabackgroundtool.so
%dir %{_kf6_qtplugindir}/calligra/parts/
%dir %{_kf6_qtplugindir}/calligra/shapefiltereffects/
%{_kf6_qtplugindir}/calligra/shapefiltereffects/calligra_filtereffects.so
%dir %{_kf6_qtplugindir}/calligra/shapes/
%ifarch %{qt6_qtwebengine_arches}
%{_kf6_qtplugindir}/calligra/shapes/braindump_shape_web.so
%endif
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_artistictext.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_chart.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_formula.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_music.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_paths.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_picture.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_plugin.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_text.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_threed.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_vector.so
%{_kf6_qtplugindir}/calligra/shapes/calligra_shape_video.so
%dir %{_kf6_qtplugindir}/calligra/textediting/
%{_kf6_qtplugindir}/calligra/textediting/calligra_textediting_autocorrect.so
%{_kf6_qtplugindir}/calligra/textediting/calligra_textediting_changecase.so
%{_kf6_qtplugindir}/calligra/textediting/calligra_textediting_spellcheck.so
%{_kf6_qtplugindir}/calligra/textediting/calligra_textediting_thesaurus.so
%dir %{_kf6_qtplugindir}/calligra/textinlineobjects/
%{_kf6_qtplugindir}/calligra/textinlineobjects/calligra_textinlineobject_variables.so
%dir %{_kf6_qtplugindir}/calligra/tools/
%{_kf6_qtplugindir}/calligra/tools/calligra_tool_basicflakes.so
%{_kf6_qtplugindir}/calligra/tools/calligra_tool_defaults.so
%{_kf6_plugindir}/propertiesdialog/calligradocinfopropspage.so
%{_kf6_plugindir}/thumbcreator/calligraimagethumbnail.so
%{_kf6_plugindir}/thumbcreator/calligrathumbnail.so

%files l10n -f %{name}.lang
# includes en/ docs, rename to -doc instead? -- rdieter
%{_kf6_datadir}/applications/calligra.desktop

%files sheets 
%{_kf6_bindir}/calligrasheets
%{_kf6_datadir}/applications/org.kde.calligra.sheets.desktop
%{_kf6_datadir}/kio/servicemenus/sheets_print.desktop
%{_kf6_datadir}/templates/.source/SpreadSheet.ods
%{_kf6_datadir}/templates/SpreadSheet.desktop
%{_kf6_metainfodir}/org.kde.calligra.sheets.metainfo.xml

%files sheets-libs
%{_libdir}/libcalligrasheetscore.so*
%{_libdir}/libcalligrasheetsengine.so*
%{_libdir}/libcalligrasheetspartlib.so*
%{_libdir}/libcalligrasheetsui.so*
%{_kf6_qtplugindir}/calligrasheets/
%{_kf6_qtplugindir}/calligra/parts/calligrasheetspart.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_applixspread2kspread.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_dbase2kspread.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_csv2sheets.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_gnumeric2sheets.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_kspread2tex.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_opencalc2sheets.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_qpro2sheets.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_sheets2csv.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_sheets2gnumeric.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_sheets2html.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_sheets2opencalc.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_xls2ods.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_xlsx2ods.so

%files stage 
#doc stage/AUTHORS stage/CHANGES
%{_bindir}/calligrastage
%{_kf6_datadir}/applications/org.kde.calligra.stage.desktop
%{_kf6_datadir}/kio/servicemenus/stage_print.desktop
%{_kf6_datadir}/templates/.source/Presentation.odp
%{_kf6_datadir}/templates/Presentation.desktop
%{_kf6_metainfodir}/org.kde.calligra.stage.metainfo.xml

%files stage-libs
%{_kf6_libdir}/libcalligrastageprivate.so*
%{_kf6_qtplugindir}/calligra/parts/calligrastagepart.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_ppt2odp.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_pptx2odp.so
%{_kf6_qtplugindir}/calligra/presentationeventactions/calligrastageeventactions.so
%{_kf6_qtplugindir}/calligra/textinlineobjects/kprvariables.so
%{_kf6_qtplugindir}/calligrastage/

%files karbon
%{_kf6_bindir}/karbon
%{_kf6_datadir}/applications/org.kde.calligra.karbon.desktop
%{_kf6_datadir}/kio/servicemenus/karbon_print.desktop
%{_kf6_datadir}/templates/.source/Illustration.odg
%{_kf6_datadir}/templates/Illustration.desktop
%{_kf6_metainfodir}/org.kde.calligra.karbon.metainfo.xml

%files karbon-libs
%{_kf6_libdir}/libkarboncommon.so*
%{_kf6_libdir}/libkarbonui.so*
%{_kf6_qtplugindir}/calligra/parts/karbonpart.so
%{_kf6_qtplugindir}/calligra/tools/karbon_tools.so
%{_kf6_qtplugindir}/karbon/
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_karbon1x2karbon.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_karbon2image.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_karbon2svg.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_karbon2wmf.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_pdf2odg.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_svg2karbon.so

%files words
%{_kf6_bindir}/calligrawords
%{_kf6_datadir}/applications/org.kde.calligra.words.desktop
%{_kf6_datadir}/applications/org.kde.calligrawords_ascii.desktop
%{_kf6_datadir}/kio/servicemenus/words_print.desktop
%{_kf6_datadir}/templates/.source/TextDocument.odt
%{_kf6_datadir}/templates/TextDocument.desktop
%{_kf6_metainfodir}/org.kde.calligra.words.metainfo.xml

%files words-libs
%{_kf6_libdir}/libwordsprivate.so*
%{_kf6_qtplugindir}/calligra/parts/calligrawordspart.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_applixword2odt.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_ascii2words.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_doc2odt.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_docx2odt.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_html2ods.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_odt2ascii.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_odt2docx.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_odt2epub2.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_odt2html.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_odt2mobi.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_odt2wiki.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_rtf2odt.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_wpd2odt.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_wpg2odg.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_wpg2svg.so
%{_kf6_qtplugindir}/calligra/formatfilters/calligra_filter_wps2odt.so

%if %{with okular}
%files okular-odpgenerator
%{_kf6_libdir}/libkookularGenerator_odp.so*
%{_kf6_qtplugindir}/okular_generators/okularGenerator_odp_calligra.so
%{_kf6_qtplugindir}/okular_generators/okularGenerator_powerpoint_calligra.so
%{_kf6_qtplugindir}/okular_generators/okularGenerator_pptx_calligra.so
%{_kf6_datadir}/applications/okularApplication_odp_calligra.desktop
%{_kf6_datadir}/applications/okularApplication_powerpoint_calligra.desktop
%{_kf6_datadir}/applications/okularApplication_pptx_calligra.desktop

%files okular-odtgenerator
%{_kf6_libdir}/libkookularGenerator_odt.so*
%{_kf6_qtplugindir}/okular_generators/okularGenerator_doc_calligra.so
%{_kf6_qtplugindir}/okular_generators/okularGenerator_docx_calligra.so
%{_kf6_qtplugindir}/okular_generators/okularGenerator_odt_calligra.so
%{_kf6_qtplugindir}/okular_generators/okularGenerator_powerpoint_calligra.so
%{_kf6_qtplugindir}/okular_generators/okularGenerator_rtf_calligra.so
%{_kf6_qtplugindir}/okular_generators/okularGenerator_wpd_calligra.so
%{_kf6_datadir}/applications/okularApplication_doc_calligra.desktop
%{_kf6_datadir}/applications/okularApplication_docx_calligra.desktop
%{_kf6_datadir}/applications/okularApplication_odt_calligra.desktop
%{_kf6_datadir}/applications/okularApplication_rtf_calligra.desktop
%{_kf6_datadir}/applications/okularApplication_wpd_calligra.desktop
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
