%global source0_hash 8b7199e495dc19b190f8f02ace8782f533266a4bd7c7d3cf6f4cf09b2de13e71
Name:           pamixer
Version:        1.6
Release:        1%{?dist}
Summary:        PulseAudio command line mixer
License:        GPL-3.0-or-later
URL:            https://github.com/cdemoulins/pamixer
Source0:        https://github.com/cdemoulins/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cxxopts-static
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(cxxopts)
BuildRequires:  pkgconfig(libpulse)
# /oreon:deps
%description
Pamixer is like amixer but for PulseAudio. It can control the volume
levels of the sinks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
