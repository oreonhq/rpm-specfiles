%global source0_hash 169b1dff508287ae03fbbb16155663cefffdc640b718ca21ace4cb57553d60c4
%global usesnapshot 0
%if 0%{?usesnapshot}
%global commit0 0d979f9fb90b0676c0e6d93b2b952afda6622de9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%global commitdate 20220713
%global gc_rc          -RC4
%endif
Name:           GoldenCheetah
%if 0%{?usesnapshot}
Version:        3.8
Release:        3%{?dist}
%else
Version:        3.7.1
Release:        3%{?dist}
%endif
Summary:        Cycling Performance Software
Epoch:          1
License:        GPL-3.0-only
URL:            http://www.goldencheetah.org/
%if 0%{?usesnapshot}
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v3.8.tar.gz#/%{name}-%{version}.tar.gz
%else
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v3.8.tar.gz#/%{name}-%{version}.tar.gz
%endif
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         %{name}-3.7-qwtconfig.pri.patch
Patch1:         %{name}_bison-3.8.patch
Requires:       hicolor-icon-theme
ExclusiveArch:  %{qt6_qtwebengine_arches}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  R-RInside-devel
BuildRequires:  R-Rcpp-devel
BuildRequires:  R-core-devel
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  libappstream-glib
BuildRequires:  libkml-devel
BuildRequires:  lmfit-devel
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Bluetooth)
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Help)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6QmlModels)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WebChannel)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qttranslations
# /oreon:deps
%description
#Golden Cheetah is a program for cyclists: 
- download and import activities from most popular bike computers from CycleOps,
  SRM, Polar, Garmin and others;
- analyze, track and review performance data and metrics;
- train indoors with real-time monitoring supporting trainers from Racermate,
  Tacx and any ANT+ device; 
- Golden Cheetah is free software and distributed under the GPL.

%package data
Summary:       Icons and translation files for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}
%description data
This package contains icons and translation files.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep

%if 0%{?usesnapshot}
%autosetup -p1 -n %{name}-%{version}%{?gc_rc}
%else
%autosetup -p1 -n %{name}-3.7-SP1
%endif

# fixes W: spurious-executable-perm
find . -type f  \( -name "*.cpp" -o -name "*.h" \) -exec chmod a-x {} \;

%build

lrelease-qt6 src/Resources/translations/*.ts
%{_qt6_qmake} %{_qt6_qmake_flags}
%make_build
%install
mkdir -p %{buildroot}%{_bindir}/
cp -p %{_builddir}/%{buildsubdir}/src/GoldenCheetah %{buildroot}%{_bindir}/
desktop-file-install                        \
--dir=%{buildroot}%{_datadir}/applications  \
%{SOURCE1}
install -Dm644 %{SOURCE2} %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
install -d -m 0755 %{buildroot}%{_datadir}/%{name}/translations
install -m 0644 src/Resources/translations/gc_{es,nl,zh-tw,pt-br,pt,ru,it,cs,ja,de,sv,fr,zh-cn}.qm \
        %{buildroot}%{_datadir}/%{name}/translations
for size in 256 48 32 16; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
  magick doc/web/logo.jpg -resize ${size} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
%find_lang %{name} --all-name --with-qt
%oreon_autofiles GoldenCheetah-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles GoldenCheetah-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n GoldenCheetah-data -f %{oreon_filedir}/GoldenCheetah-data.list
%files -n GoldenCheetah-doc -f %{oreon_filedir}/GoldenCheetah-doc.list

%changelog

%autochangelog
