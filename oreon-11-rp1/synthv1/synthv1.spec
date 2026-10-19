%global source0_hash d73acaec384a4042f7c6d325847f34bd78f6d3410b47a188302cd7985f0903bc
%global        namespace org.rncbc
Summary:        A 4-oscillator subtractive polyphonic synthesizer
Name:          synthv1
Version:       1.5.0
Release:        1%{?dist}
URL:           https://%{name}.sourceforge.io/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:        synthv1-nostrip.patch
License:       GPL-2.0-or-later
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(lv2)
# /oreon:deps
%description
%{name} is a 4-oscillator subtractive polyphonic synthesizer with stereo fx.

%package -n lv2-%{name}
Summary:       An LV2 port of synthv1
Requires:      lv2 >= 1.2.0
%description -n lv2-%{name}
An LV2 plugin of the synthv1 subtractive synthesizer

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{namespace}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{namespace}.%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n lv2-synthv1 -f %{oreon_filedir}/lv2-synthv1.list

%changelog

%autochangelog
