%global source0_hash e0a028ab4d6d5cf5033e293a4205071245911827be052e21a723ed6bd694efb1
%global srcname alsa-ucm-conf-asahi
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}
Name:           alsa-ucm-asahi
Version:        8%{?commit:^%{date}git%{shortcommit}}
Release:        1%{?dist}
Summary:        ALSA Use Case Manager configuration (and topologies) for Apple silicon devices
License:        BSD-3-Clause
URL:            https://github.com/AsahiLinux/alsa-ucm-conf-asahi
%if %{defined commit}
Source0:        https://github.com/AsahiLinux/%{srcname}/archive/v8/%{srcname}-8.tar.gz
%else
Source0:        https://github.com/AsahiLinux/%{srcname}/archive/v8/%{srcname}-8.tar.gz
%endif
BuildArch:      noarch
Requires:       alsa-ucm >= 1.2.7.2
# oreon:deps

# /oreon:deps
%description
The ALSA Use Case Manager configuration (and topologies) for Apple silicon devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{defined commit}
%autosetup -n %{srcname}-%{commit}
%else
%autosetup -n %{srcname}-%{version}
%endif

%install
install -dm 755 %{buildroot}%{_datadir}/alsa/ucm2/conf.d/
cp -a ucm2/conf.d/aop_audio/ %{buildroot}%{_datadir}/alsa/ucm2/conf.d/
cp -a ucm2/conf.d/macaudio/ %{buildroot}%{_datadir}/alsa/ucm2/conf.d/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
