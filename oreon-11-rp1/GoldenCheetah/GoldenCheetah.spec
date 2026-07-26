%global source0_hash none

#For git snapshots, set to 0 to use release instead:
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
Version:        3.6
# Release:        0.19.%%{commitdate}git%%{shortcommit0}%%{?dist}
Release:        0.36.RC4%%{?dist}
%else
Version:        3.7.1
Release:        3%{?dist}
%endif
Summary:        Cycling Performance Software
Epoch:          1
License:        GPL-3.0-only
URL:            http://www.goldencheetah.org/
%if 0%{?usesnapshot}
Source0:        https://github.com/GoldenCheetah/GoldenCheetah/archive/refs/tags/v3.6%{?gc_rc}.tar.gz#/%{name}-%{version}%{?gc_rc}.tar.gz
%else
# Source0:        https://github.com/GoldenCheetah/GoldenCheetah/archive/refs/tags/v%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source0:        https://github.com/GoldenCheetah/GoldenCheetah/archive/refs/tags/v3.7-SP1.tar.gz#/%{name}-%{version}.tar.gz
%endif
Source1:        %{name}.desktop
# https://github.com/GoldenCheetah/GoldenCheetah/issues/2690
Source2:        %{name}.appdata.xml
# Use Qwt Widget Library
Patch0:         %{name}-3.7-qwtconfig.pri.patch
Patch1:         %{name}_bison-3.8.patch

BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Help)
BuildRequires:  pkgconfig(Qt6Bluetooth)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6WebChannel)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6QmlModels)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  lmfit-devel
BuildRequires:  libkml-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttranslations
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  R-core-devel
BuildRequires:  R-Rcpp-devel
BuildRequires:  R-RInside-devel
BuildRequires:  python3-devel
BuildRequires:  gsl-devel
BuildRequires:  make
Requires:       hicolor-icon-theme

# qt6-qtwebengine-devel is missing on ppc64, ppc64le, s390x CPU architectures.
ExclusiveArch:  %{qt6_qtwebengine_arches}

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
# Create translation files.
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

#icons
for size in 256 48 32 16; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
  magick doc/web/logo.jpg -resize ${size} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files data
%{_datadir}/%{name}

%files doc
%doc doc/user/*.pdf

%changelog
%autochangelog
