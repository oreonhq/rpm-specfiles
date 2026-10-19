%global source0_hash 391907d3f8e1cfcfe2c1fd2b1e93cfbda852425abba8f83db32b406bb0467443
%global         namespace org.rncbc
Name:           padthv1
Version:        0.9.91
Release:        1%{?dist}
Summary:        An old-school polyphonic additive synthesizer
License:        GPL-2.0-or-later
URL:            https://%{name}.sourceforge.io/
Source0:        https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         %{name}-nostrip.patch
Requires:       hicolor-icon-theme
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
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(lv2)
# /oreon:deps
%description
%{name} is an old-school polyphonic additive synthesizer with stereo effects.
%{name} is based on the PADsynth algorithm by Paul Nasca,
as a special variant of additive synthesis.
This is the standalone Jack version.

%package -n     lv2-%{name}
Summary:        LV2 port of an old-school polyphonic additive synthesizer
Requires:       lv2 >= 1.8.1
%description -n lv2-%{name}
%{name} is an old-school polyphonic additive synthesizer with stereo effects.
%{name} is based on the PADsynth algorithm by Paul Nasca,
as a special variant of additive synthesis.
This is the LV2 version.

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
%files -n lv2-padthv1 -f %{oreon_filedir}/lv2-padthv1.list

%changelog

%autochangelog
