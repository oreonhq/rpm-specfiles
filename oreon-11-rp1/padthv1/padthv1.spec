%global source0_hash 391907d3f8e1cfcfe2c1fd2b1e93cfbda852425abba8f83db32b406bb0467443

%global         namespace org.rncbc

Name:           padthv1
Version:        0.9.91
Release:        4%{?dist}
Summary:        An old-school polyphonic additive synthesizer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://%{name}.sourceforge.io/
Source0:        https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Patch requested upstream https://sourceforge.net/p/padthv1/tickets/1/
Patch0:         %{name}-nostrip.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

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

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{namespace}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{namespace}.%{name}.metainfo.xml

%files
%license LICENSE
%doc README
%{_bindir}/%{name}_jack
%{_datadir}/applications/%{namespace}.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{namespace}.%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/%{namespace}.%{name}.application-x-%{name}-preset.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_metainfodir}/%{namespace}.%{name}.metainfo.xml
%{_datadir}/mime/packages/%{namespace}.%{name}.xml
%{_datadir}/%{name}

%files -n       lv2-%{name}
%license LICENSE
%doc README
%{_libdir}/lv2/%{name}.lv2/

%changelog
%autochangelog
