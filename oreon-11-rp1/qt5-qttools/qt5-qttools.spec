%global source0_hash none

%global qt_module qttools

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

#global bootstrap 1

%if ! 0%{?bootstrap}
## don't enable until crasher fixed: https://bugzilla.redhat.com/show_bug.cgi?id=1470778
#global webkit 1
%endif

Summary: Qt5 - QtTool components
Name:    qt5-qttools
Version: 5.15.18
Release: 4%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
## upstream patches
## repo: https://invent.kde.org/qt/qt/qttools
## branch: kde/5.15
## git format-patch v5.15.16-lts-lgpl
Patch1: 0001-Ensure-FileAttributeSetTable-is-filled-ordered-so-we.patch
Patch2: 0002-Drop-superfluous-network-dependency-from-assistant-h.patch
Patch3: 0003-qdoc-Ensure-the-generated-temporary-header-file-is-c.patch

# help lrelease/lupdate use/prefer qmake-qt5
# https://bugzilla.redhat.com/show_bug.cgi?id=1009893
Patch102: qttools-opensource-src-5.13.2-runqttools-with-qt5-suffix.patch

# 32-bit MIPS needs explicit -latomic
Patch104: qttools-opensource-src-5.7-add-libatomic.patch
# Link against libclang-cpp.so
# 
Patch105: Link-against-libclang-cpp.so-instead-of-the-clang-co.patch

Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop

BuildRequires: make
# %%check needs cmake (and don't want to mess with cmake28)
%if 0%{?fedora} || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
BuildRequires: cmake
%endif
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/file
BuildRequires: qt5-rpm-macros >= %{version}

BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtbase-static >= %{version}
BuildRequires: qt5-qtdeclarative-static >= %{version}
BuildRequires: pkgconfig(Qt5Qml)
# libQt5DBus.so.5(Qt_5_PRIVATE_API)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%if 0%{?bootstrap}
%global no_examples CONFIG-=compile_examples
Obsoletes: %{name}-examples < %{version}-%{release}
%else
# for qdoc
BuildRequires: clang-devel llvm-devel
%endif

Requires: %{name}-common = %{version}-%{release}

%description
%{summary}.

%package common
Summary: Common files for %{name}
BuildArch: noarch
Obsoletes: qt5-qttools-libs-clucene < 5.9.0
%if ! 0%{?webkit}
Obsoletes: qt5-designer-plugin-webkit < 5.9.0
%endif
%description common
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs-designer%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-designercomponents%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-help%{?_isa} = %{version}-%{release}
Requires: qt5-doctools = %{version}-%{release}
Requires: qt5-designer = %{version}-%{release}
Requires: qt5-linguist = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package static
Summary: Static library files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
%{summary}.

%package libs-designer
Summary: Qt5 Designer runtime library
Requires: %{name}-common = %{version}-%{release}
%description libs-designer
%{summary}.

%package libs-designercomponents
Summary: Qt5 Designer Components runtime library
Requires: %{name}-common = %{version}-%{release}
%description libs-designercomponents
%{summary}.

%package libs-help
Summary: Qt5 Help runtime library
Requires: %{name}-common = %{version}-%{release}
# when split happened
Conflicts: qt5-tools < 5.4.0-0.2
%description libs-help
%{summary}.

%package -n qt5-assistant
Summary: Documentation browser for Qt5
Requires: %{name}-common = %{version}-%{release}
%description -n qt5-assistant
%{summary}.

%package -n qt5-designer
Summary: Design GUIs for Qt5 applications
Requires: %{name}-libs-designer%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-designercomponents%{?_isa} = %{version}-%{release}
%description -n qt5-designer
%{summary}.

%if 0%{?webkit}
%package -n qt5-designer-plugin-webkit
Summary: Qt5 designer plugin for WebKit
BuildRequires: pkgconfig(Qt5WebKitWidgets)
Requires: %{name}-libs-designer%{?_isa} = %{version}-%{release}
%description -n qt5-designer-plugin-webkit
%{summary}.
%endif

%package -n qt5-linguist
Summary: Qt5 Linguist Tools
Requires: %{name}-common = %{version}-%{release}
%description -n qt5-linguist
Tools to add translations to Qt5 applications.

%package -n qt5-qdbusviewer
Summary: D-Bus debugger and viewer
Requires: %{name}-common = %{version}-%{release}
%{?_qt5:Requires: %{_qt5}%{?_isa} >= %{_qt5_version}}
%description -n qt5-qdbusviewer
QDbusviewer can be used to inspect D-Bus objects of running programs
and invoke methods on those objects.

%package -n qt5-doctools
Summary: Qt5 doc tools package
Provides: qt5-qdoc = %{version}
Obsoletes: qt5-qdoc < 5.8.0
Provides: qt5-qhelpgenerator = %{version}
Obsoletes: qt5-qhelpgenerator < 5.8.0
Provides: qt5-qtattributionsscanner = %{version}
Obsoletes: qt5-qtattributionsscanner < 5.8.0
Requires: qt5-qtattributionsscanner = %{version}

%description -n qt5-doctools
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}-common = %{version}-%{release}
%description examples
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{qt_module}-everywhere-src-%{version}
%autopatch -M 99 -p1
%patch -P102 -p1 -b ..runqttools-with-qt5-suffix.patch

%ifarch %{mips32}
%patch -P104 -p1 -b .libatomic
%endif
%patch -P105 -p1 -b .libclang-cpp


%build
# TODO: Please submit an issue to upstream (rhbz#2381396)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{qmake_qt5} \
  CONFIG+=disable_external_rpath \
  %{?no_examples}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

# Add desktop files, --vendor=... helps avoid possible conflicts with qt3/qt4
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --vendor="qt5" \
  %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23}

# icons
install -m644 -p -D src/assistant/assistant/images/assistant.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/assistant-qt5.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/assistant-qt5.png
install -m644 -p -D src/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/designer-qt5.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer-qt5.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer-qt5.png
# linguist icons
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/linguist-qt5.png
done

# hardlink files to {_bindir}, add -qt5 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt5_bindir}
for i in * ; do
  case "${i}" in
   assistant|designer|lconvert|linguist|lrelease|lupdate|lprodump|pixeltool|qcollectiongenerator|qdbus|qdbusviewer|qhelpconverter|qhelpgenerator|qtplugininfo|qtattributionsscanner)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt5
      ln -sv ${i} ${i}-qt5
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

## Qt5Designer.pc references non-existent Qt5UiPlugin.pc, remove the reference for now
sed -i -e 's| Qt5UiPlugin||g' %{buildroot}%{_qt5_libdir}/pkgconfig/Qt5Designer.pc


## work-in-progress... -- rex
%if 0%{?fedora} || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%check
# TODO: Please submit an issue to upstream (rhbz#2381396)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# verify validity of Qt5Designer.pc
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig:$PKG_CONFIG_PATH
pkg-config --print-requires --print-requires-private Qt5Designer
export CMAKE_PREFIX_PATH=%{buildroot}%{_qt5_prefix}:%{buildroot}%{_prefix}
export PATH=%{buildroot}%{_qt5_bindir}:%{_qt5_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt5_libdir}
mkdir tests/auto/cmake/%{_target_platform}
pushd tests/auto/cmake/%{_target_platform}
cmake ..
ctest --output-on-failure ||:
popd


# check icon resolutions
pushd %{buildroot}%{_datadir}/icons
for RES in $(ls hicolor); do
  for APP in designer assistant linguist qdbusviewer; do
    if [ -e hicolor/$RES/apps/${APP}*.* ]; then
      file hicolor/$RES/apps/${APP}*.* | grep "$(echo $RES | sed 's/x/ x /')"
    fi
  done
done
popd

%endif


%files
%{_bindir}/qdbus-qt5
%{_bindir}/qtpaths
%{_qt5_bindir}/qdbus
%{_qt5_bindir}/qdbus-qt5
%{_qt5_bindir}/qtpaths

%files common
%license LICENSE.LGPL*

%ldconfig_scriptlets libs-designer

%files  libs-designer
%{_qt5_libdir}/libQt5Designer.so.5*
%dir %{_qt5_libdir}/cmake/Qt5Designer/

%ldconfig_scriptlets libs-designercomponents

%files  libs-designercomponents
%{_qt5_libdir}/libQt5DesignerComponents.so.5*

%ldconfig_scriptlets libs-help

%files  libs-help
%{_qt5_libdir}/libQt5Help.so.5*

%if 0%{?rhel} && 0%{?rhel} <= 7 || (0%{?oreon} >= 11)
%post -n qt5-assistant
touch --no-create %{_datadir}/icons/hicolor ||:

%posttrans -n qt5-assistant
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

%postun -n qt5-assistant
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
fi
%endif

%files -n qt5-assistant
%{_bindir}/assistant-qt5
%{_qt5_bindir}/assistant*
%{_datadir}/applications/*assistant.desktop
%{_datadir}/icons/hicolor/*/apps/assistant*.*

%if 0%{?rhel} && 0%{?rhel} <= 7 || (0%{?oreon} >= 11)
%post -n qt5-doctools
touch --no-create %{_datadir}/icons/hicolor ||:

%posttrans -n qt5-doctools
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

%postun -n qt5-doctools
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
fi
%endif

%files -n qt5-doctools
%{_bindir}/qdoc*
%{_qt5_bindir}/qdoc*
%{_bindir}/qdistancefieldgenerator*
%{_bindir}/qhelpgenerator*
%{_qt5_bindir}/qdistancefieldgenerator*
%{_qt5_bindir}/qhelpgenerator*
%{_bindir}/qtattributionsscanner-qt5
%{_qt5_bindir}/qtattributionsscanner*

%if 0%{?rhel} && 0%{?rhel} <= 7 || (0%{?oreon} >= 11)
%post -n qt5-designer
touch --no-create %{_datadir}/icons/hicolor ||:

%posttrans -n qt5-designer
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database -q &> /dev/null ||:

%postun -n qt5-designer
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
fi
%endif

%files -n qt5-designer
%{_bindir}/designer*
%{_qt5_bindir}/designer*
%{_datadir}/applications/*designer.desktop
%{_datadir}/icons/hicolor/*/apps/designer*.*
%dir %{_qt5_libdir}/cmake/Qt5DesignerComponents
%{_qt5_libdir}/cmake/Qt5DesignerComponents/Qt5DesignerComponentsConfig*.cmake

%if 0%{?webkit}
%files -n qt5-designer-plugin-webkit
%{_qt5_plugindir}/designer/libqwebview.so
%{_qt5_libdir}/cmake/Qt5Designer/Qt5Designer_QWebViewPlugin.cmake
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7 || (0%{?oreon} >= 11)
%post -n qt5-linguist
touch --no-create %{_datadir}/icons/hicolor ||:

%posttrans -n qt5-linguist
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database -q &> /dev/null ||:

%postun -n qt5-linguist
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
fi
%endif

%files -n qt5-linguist
%{_bindir}/linguist*
%{_qt5_bindir}/linguist*
# phrasebooks used by linguist
%{_qt5_datadir}/phrasebooks/
%{_datadir}/applications/*linguist.desktop
%{_datadir}/icons/hicolor/*/apps/linguist*.*
# linguist friends
%{_bindir}/lconvert*
%{_bindir}/lrelease*
%{_bindir}/lupdate*
%{_bindir}/lprodump*
%{_qt5_bindir}/lconvert*
%{_qt5_bindir}/lrelease*
%{_qt5_bindir}/lupdate*
%{_qt5_bindir}/lprodump*
# cmake config
%dir %{_qt5_libdir}/cmake/Qt5LinguistTools/
%{_qt5_libdir}/cmake/Qt5LinguistTools/Qt5LinguistToolsConfig*.cmake
%{_qt5_libdir}/cmake/Qt5LinguistTools/Qt5LinguistToolsMacros.cmake

%if 0%{?rhel} && 0%{?rhel} <= 7 || (0%{?oreon} >= 11)
%post -n qt5-qdbusviewer
touch --no-create %{_datadir}/icons/hicolor ||:

%posttrans -n qt5-qdbusviewer
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

%postun -n qt5-qdbusviewer
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
fi
%endif

%files -n qt5-qdbusviewer
%{_bindir}/qdbusviewer*
%{_qt5_bindir}/qdbusviewer*
%{_datadir}/applications/*qdbusviewer.desktop
%{_datadir}/icons/hicolor/*/apps/qdbusviewer*.*

%files devel
%{_bindir}/pixeltool*
%{_bindir}/qcollectiongenerator*
#{_bindir}/qhelpconverter*
%{_bindir}/qtdiag*
%{_bindir}/qtplugininfo*
%{_qt5_bindir}/pixeltool*
%{_qt5_bindir}/qtdiag*
%{_qt5_bindir}/qcollectiongenerator*
#{_qt5_bindir}/qhelpconverter*
%{_qt5_bindir}/qtplugininfo*
%{_qt5_headerdir}/QtDesigner/
%{_qt5_headerdir}/QtDesignerComponents/
%{_qt5_headerdir}/QtHelp/
%{_qt5_headerdir}/QtUiPlugin
%{_qt5_libdir}/libQt5Designer*.prl
%{_qt5_libdir}/libQt5Designer*.so
%{_qt5_libdir}/libQt5Help.prl
%{_qt5_libdir}/libQt5Help.so
%{_qt5_libdir}/Qt5UiPlugin.la
%{_qt5_libdir}/libQt5UiPlugin.prl
%{_qt5_libdir}/cmake/Qt5Designer/Qt5DesignerConfig*.cmake
%dir %{_qt5_libdir}/cmake/Qt5Help/
%{_qt5_libdir}/cmake/Qt5Help/Qt5HelpConfig*.cmake
%{_qt5_libdir}/cmake/Qt5UiPlugin/
%{_qt5_libdir}/pkgconfig/Qt5Designer.pc
%{_qt5_libdir}/pkgconfig/Qt5Help.pc
%{_qt5_libdir}/pkgconfig/Qt5UiPlugin.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_designer.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_designer_private.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_designercomponents_private.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_help.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_help_private.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_uiplugin.pri
# putting these here for now, new stuff in 5.14, review for accuracy -- rdieter
%{_qt5_libdir}/cmake/Qt5AttributionsScannerTools/
%{_qt5_libdir}/cmake/Qt5DocTools/

%files static
%{_qt5_headerdir}/QtUiTools/
%{_qt5_libdir}/libQt5UiTools.*a
%{_qt5_libdir}/libQt5UiTools.prl
%{_qt5_libdir}/cmake/Qt5UiTools/
%{_qt5_libdir}/pkgconfig/Qt5UiTools.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_uitools.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_uitools_private.pri

%if ! 0%{?no_examples:1}
%files examples
%{_qt5_examplesdir}/
%{_qt5_plugindir}/designer/*
%dir %{_qt5_libdir}/cmake/Qt5Designer
%{_qt5_libdir}/cmake/Qt5Designer/Qt5Designer_*
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-4
- Import
