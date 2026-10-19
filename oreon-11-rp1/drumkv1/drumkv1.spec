%global source0_hash 7fe6a110ce558bf21110e91e299bc5ee117e6dbefdd01ffd1b8e48b5811c2698
%global        namespace org.rncbc
Summary:        An old-school drum-kit sampler
Name:          drumkv1
Version:       1.5.0
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           https://%{name}.sourceforge.io
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:        drumkv1-nostrip.patch
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
BuildRequires:  pkgconfig(sndfile)
# /oreon:deps
%description
%{name} is an old-school all-digital drum-kit sampler synthesizer with
stereo fx.

%package -n lv2-%{name}
Summary:       An LV2 port of %{name}
Requires:      lv2
%description -n lv2-%{name}
An LV2 plugin of the %{name} synth

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
%files -n lv2-drumkv1 -f %{oreon_filedir}/lv2-drumkv1.list

%changelog

%autochangelog
