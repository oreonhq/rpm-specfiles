%global source0_hash 8dab8f3611496486a470ad5f115ceea584f36bc22a2b8b6f6ebdbafbb8160693
%global qt_module qttools
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
%global metainfo 1
Summary:        Qt6 - QtTool components
Name:    qt6-qttools
Version: 6.12.0
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
%else
Source0:        https://download.qt.io/a%{prerelease}hive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%endif
Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop
Source31: io.qt.Designer.metainfo.xml
Source32: io.qt.Linguist.metainfo.xml
Source33: io.qt.qdbusviewer.metainfo.xml
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires: %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/file
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libzstd-devel
BuildRequires:  llvm-devel
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtdeclarative
BuildRequires:  qt6-qtdeclarative-static
BuildRequires:  qt6-rpm-macros
# /oreon:deps
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

%package static
Summary: Static library files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}}

%build

%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_qt6_libdir}/objects-RelWithDebInfo
rm -rf %{buildroot}%{_qt6_archdatadir}/objects-RelWithDebInfo
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --vendor="qt6" \
  %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23}
%if 0%{?metainfo}
install -Dm0644 -t %{buildroot}%{_metainfodir} \
  %{SOURCE31} %{SOURCE32} %{SOURCE33}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
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
%oreon_autofiles qt6-assistant usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt6-designer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt6-linguist usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt6-qdbusviewer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt6-doctools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n qt6-qttools-common -f %{oreon_filedir}/qt6-qttools-common.list
%files -n qt6-qttools-devel -f %{oreon_filedir}/qt6-qttools-devel.list
%files -n qt6-qttools-static -f %{oreon_filedir}/qt6-qttools-static.list
%files -n qt6-qttools-libs-designer -f %{oreon_filedir}/qt6-qttools-libs-designer.list
%files -n qt6-qttools-libs-designercomponents -f %{oreon_filedir}/qt6-qttools-libs-designercomponents.list
%files -n qt6-qttools-libs-help -f %{oreon_filedir}/qt6-qttools-libs-help.list
%files -n qt6-assistant -f %{oreon_filedir}/qt6-assistant.list
%files -n qt6-designer -f %{oreon_filedir}/qt6-designer.list
%files -n qt6-linguist -f %{oreon_filedir}/qt6-linguist.list
%files -n qt6-qdbusviewer -f %{oreon_filedir}/qt6-qdbusviewer.list
%files -n qt6-doctools -f %{oreon_filedir}/qt6-doctools.list
%files -n qt6-qttools-examples -f %{oreon_filedir}/qt6-qttools-examples.list

%changelog

%autochangelog
