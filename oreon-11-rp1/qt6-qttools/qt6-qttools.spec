# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9ea75af35c512f7e09e61c8c3af3997f13b4d43bb099cf43fcec470126b4041e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global qt_module qttools

%global examples 1
%global metainfo 1

Summary: Qt6 - QtTool components
Name:    qt6-qttools
Version: 6.11.2
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

Patch1: qdoc-support-newer-clang.patch

Patch10: qttools-llvm22-qdoc-fixes.patch

Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop

Source31: io.qt.Designer.metainfo.xml
Source32: io.qt.Linguist.metainfo.xml
Source33: io.qt.qdbusviewer.metainfo.xml

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/file
BuildRequires: appstream
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-private-devel%{?_isa}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: libzstd-devel

Requires: %{name}-common = %{version}-%{release}

%description
%{summary}.

%package common
Summary: Common files for %{name}
BuildArch: noarch

%description common
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs-designer%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-designercomponents%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-help%{?_isa} = %{version}-%{release}
Requires: qt6-doctools = %{version}-%{release}
Requires: qt6-designer = %{version}-%{release}
Requires: qt6-linguist = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package libs-designer
Summary: Qt6 Designer runtime library
Requires: %{name}-common = %{version}-%{release}
%description libs-designer
%{summary}.

%package libs-designercomponents
Summary: Qt6 Designer Components runtime library
Requires: %{name}-common = %{version}-%{release}
%description libs-designercomponents
%{summary}.

%package libs-help
Summary: Qt6 Help runtime library
Requires: %{name}-common = %{version}-%{release}
%description libs-help
%{summary}.

%package -n qt6-assistant
Summary: Documentation browser for Qt6
Requires: %{name}-common = %{version}-%{release}
%description -n qt6-assistant
%{summary}.

%package -n qt6-designer
Summary: Design GUIs for Qt6 applications
Requires: %{name}-libs-designer%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-designercomponents%{?_isa} = %{version}-%{release}
%description -n qt6-designer
%{summary}.

%package -n qt6-linguist
Summary: Qt6 Linguist Tools
Requires: %{name}-common = %{version}-%{release}
Provides: qt6-qttools-linguist = %{version}-%{release}
%description -n qt6-linguist
Tools to add translations to Qt6 applications.

%package -n qt6-qdbusviewer
Summary: D-Bus debugger and viewer
Requires: %{name}-common = %{version}-%{release}
%{?_qt6:Requires: %{_qt6}%{?_isa} >= %{_qt6_version}}
%description -n qt6-qdbusviewer
QDbusviewer can be used to inspect D-Bus objects of running programs
and invoke methods on those objects.

%package -n qt6-doctools
Summary: Qt6 doc tools package
%description -n qt6-doctools
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}-common = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep
%oreon_sha256
%setup -q -n %{qt_module}-everywhere-src-%{qt_version}

%patch -P1 -p1 -b .llvm22
%patch -P10 -p1 -b .llvm22-qdoc-fixes

%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build

%install
%cmake_install

rm -rf %{buildroot}%{_qt6_archdatadir}/objects-RelWithDebInfo

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --vendor="qt6" \
  %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23}

%if 0%{?metainfo}
install -Dm0644 -t %{buildroot}%{_metainfodir} \
  %{SOURCE31} %{SOURCE32} %{SOURCE33}
appstreamcli validate --no-net --explain %{buildroot}%{_metainfodir}/*.xml
%endif

install -m644 -p -D src/assistant/assistant/images/assistant.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/assistant-qt6.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/assistant-qt6.png
install -m644 -p -D src/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/designer-qt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer-qt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer-qt6.png
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/linguist-qt6.png
done

mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
   assistant|designer|lcheck|lconvert|linguist|lrelease|lrelease-pro|ltext2id|lupdate|lupdate-pro|pixeltool| \
   qdbus|qdbusviewer| \
   qtplugininfo|qdistancefieldgenerator|qdoc|qtdiag)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt6
      ln -sv ${i} ${i}-qt6
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

%check
pushd %{buildroot}%{_datadir}/icons
for RES in $(ls hicolor); do
  for APP in designer assistant linguist qdbusviewer; do
    if [ -e hicolor/$RES/apps/${APP}*.* ]; then
      file hicolor/$RES/apps/${APP}*.* | grep "$(echo $RES | sed 's/x/ x /')"
    fi
  done
done
popd

%files
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_bindir}/qdbus-qt6
%{_qt6_bindir}/qdbus
%{_qt6_bindir}/qdbus-qt6
%{_qt6_libdir}/libQt6UiTools.so.6*

%files common
%license LICENSES/LGPL*

%files  libs-designer
%{_qt6_libdir}/libQt6Designer.so.6*
%dir %{_qt6_libdir}/cmake/Qt6Designer/
%{_qt6_plugindir}/designer/*

%files  libs-designercomponents
%{_qt6_libdir}/libQt6DesignerComponents.so.6*

%files  libs-help
%{_qt6_libdir}/libQt6Help.so.6*

%files -n qt6-assistant
%{_bindir}/assistant-qt6
%{_qt6_bindir}/assistant*
%{_datadir}/applications/*assistant.desktop
%{_datadir}/icons/hicolor/*/apps/assistant*.*

%files -n qt6-doctools
%{_bindir}/qdoc*
%{_qt6_bindir}/qdoc*
%{_bindir}/qdistancefieldgenerator*
%{_qt6_bindir}/qdistancefieldgenerator*
%{_qt6_libexecdir}/qhelpgenerator*
%{_qt6_libexecdir}/qtattributionsscanner*

%files -n qt6-designer
%{_bindir}/designer*
%{_qt6_bindir}/designer*
%{_datadir}/applications/*designer.desktop
%{_datadir}/icons/hicolor/*/apps/designer*.*
%if 0%{?metainfo}
%{_metainfodir}/io.qt.Designer.metainfo.xml
%endif

%files -n qt6-linguist
%{_bindir}/linguist*
%{_qt6_bindir}/linguist*
%{_datadir}/qt6/phrasebooks/*.qph
%{_datadir}/applications/*linguist.desktop
%{_datadir}/icons/hicolor/*/apps/linguist*.*
%{_bindir}/lcheck*
%{_bindir}/lconvert*
%{_bindir}/lrelease*
%{_bindir}/ltext2id*
%{_bindir}/lupdate*
%{_qt6_bindir}/lcheck*
%{_qt6_bindir}/lconvert*
%{_qt6_bindir}/lrelease*
%{_qt6_bindir}/ltext2id*
%{_qt6_bindir}/lupdate*
%if 0%{?metainfo}
%{_metainfodir}/io.qt.Linguist.metainfo.xml
%endif

%files -n qt6-qdbusviewer
%{_bindir}/qdbusviewer*
%{_qt6_bindir}/qdbusviewer*
%{_datadir}/applications/*qdbusviewer.desktop
%{_datadir}/icons/hicolor/*/apps/qdbusviewer*.*
%if 0%{?metainfo}
%{_metainfodir}/io.qt.qdbusviewer.metainfo.xml
%endif

%files devel
%{_bindir}/pixeltool*
%{_bindir}/qtdiag*
%{_bindir}/qtplugininfo*
%{_qt6_bindir}/pixeltool*
%{_qt6_bindir}/qtdiag*
%{_qt6_bindir}/qtplugininfo*
%{_qt6_headerdir}/QtQDocCatch/
%{_qt6_headerdir}/QtQDocCatchConversions/
%{_qt6_headerdir}/QtQDocCatchGenerators/
%{_qt6_headerdir}/QtDesigner/
%{_qt6_headerdir}/QtDesignerComponents/
%{_qt6_headerdir}/QtHelp/
%{_qt6_headerdir}/QtUiPlugin
%{_qt6_headerdir}/QtUiTools/
%{_qt6_headerdir}/QtTools/
%{_qt6_libdir}/libQt6Designer*.so
%{_qt6_libdir}/libQt6Help.so
%{_qt6_libdir}/libQt6UiTools.so
%{_qt6_libdir}/libQt6Designer*.prl
%{_qt6_libdir}/libQt6Help.prl
%{_qt6_libdir}/libQt6UiTools.prl
%dir %{_qt6_libdir}/cmake/Qt6Designer
%dir %{_qt6_libdir}/cmake/Qt6DesignerComponentsPrivate
%dir %{_qt6_libdir}/cmake/Qt6DesignerPrivate
%dir %{_qt6_libdir}/cmake/Qt6Help/
%dir %{_qt6_libdir}/cmake/Qt6HelpPrivate
%dir %{_qt6_libdir}/cmake/Qt6Linguist
%dir %{_qt6_libdir}/cmake/Qt6LinguistTools
%dir %{_qt6_libdir}/cmake/Qt6QDocCatchConversionsPrivate
%dir %{_qt6_libdir}/cmake/Qt6QDocCatchGeneratorsPrivate
%dir %{_qt6_libdir}/cmake/Qt6QDocCatchPrivate
%dir %{_qt6_libdir}/cmake/Qt6Tools/
%dir %{_qt6_libdir}/cmake/Qt6ToolsTools/
%dir %{_qt6_libdir}/cmake/Qt6UiPlugin/
%dir %{_qt6_libdir}/cmake/Qt6UiToolsPrivate
%{_qt6_libdir}/cmake/Qt6/FindWrapLibClang.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtToolsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Designer/*.cmake
%{_qt6_libdir}/cmake/Qt6DesignerComponentsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6DesignerPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Help/*.cmake
%{_qt6_libdir}/cmake/Qt6HelpPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Linguist/*.cmake
%{_qt6_libdir}/cmake/Qt6LinguistTools/*.cmake
%{_qt6_libdir}/cmake/Qt6QDocCatchConversionsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6QDocCatchGeneratorsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6QDocCatchPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Tools/*.cmake
%{_qt6_libdir}/cmake/Qt6ToolsTools/*.cmake
%{_qt6_libdir}/cmake/Qt6UiPlugin/*.cmake
%{_qt6_libdir}/cmake/Qt6UiTools/
%{_qt6_libdir}/cmake/Qt6UiToolsPrivate/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_qdoccatch_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_qdoccatchconversions_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_qdoccatchgenerators_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_designer.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_designer_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_designercomponents_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_help.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_help_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_linguist.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_tools_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_uiplugin.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_uitools.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_uitools_private.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc


%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
%autochangelog
