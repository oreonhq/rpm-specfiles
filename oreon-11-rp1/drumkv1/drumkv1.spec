%global source0_hash 5c95bddf2c01596a938d13c618e075e5cb5f351e126723f0fd93a633fca32fe4

%global        namespace org.rncbc

Summary:       An old-school drum-kit sampler
Name:          drumkv1
Version:       0.9.91
Release:       4%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://%{name}.sourceforge.io
Source0:       https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Do not strip executables
Patch0:        drumkv1-nostrip.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires:      hicolor-icon-theme

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
%doc README
%license LICENSE
%{_datadir}/applications/%{namespace}.%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_bindir}/%{name}_jack
%{_datadir}/mime/packages/%{namespace}.%{name}.xml
%{_mandir}/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_metainfodir}/%{namespace}.%{name}.metainfo.xml
%{_datadir}/%{name}

%files -n lv2-%{name}
%doc README
%license LICENSE
%{_libdir}/lv2/%{name}.lv2/

%changelog
%autochangelog
