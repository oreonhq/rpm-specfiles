%global source0_hash b8417e214dfabaf1cadd0e162961e0341b0f1b864d2f865f2b101d7dce0c9eb1
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}
Name:           asahi-audio
Version:        3.4%{?commit:^%{date}git%{shortcommit}}
Release:        1%{?dist}
Summary:        PipeWire DSP profiles for Apple Silicon machines
License:        MIT
URL:            https://github.com/AsahiLinux/asahi-audio
%if %{defined commit}
Source0:        https://github.com/AsahiLinux/%{name}/archive/v3.4/%{name}-3.4.tar.gz
%else
Source0:        https://github.com/AsahiLinux/%{name}/archive/v3.4/%{name}-3.4.tar.gz
%endif
BuildArch:      noarch
Requires:       pipewire >= 1.0
Requires:       wireplumber >= 0.5.1-2
Requires:       pipewire-module-filter-chain-lv2
Requires:       lsp-plugins-lv2 >= 1.2.13-2
Requires:       lv2-bankstown >= 1.1.0
Requires:       lv2-triforce >= 0.2.0
Recommends:     speakersafetyd
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
PipeWire and WirePlumber DSP profiles and configurations to
drive the speaker arrays in Apple Silicon laptops and desktops.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{?commit:-n %{name}-%{commit}}

%build

%make_build
%install
%make_install PREFIX=%{_prefix} DATA_DIR=%{_datadir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
