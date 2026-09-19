%global source0_hash 8b7199e495dc19b190f8f02ace8782f533266a4bd7c7d3cf6f4cf09b2de13e71

Name:           pamixer
Version:        1.6
Release:        %autorelease
Summary:        PulseAudio command line mixer

License:        GPL-3.0-or-later
URL:            https://github.com/cdemoulins/pamixer
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(cxxopts)
BuildRequires:  pkgconfig(libpulse)
# require *-static for header-only library
BuildRequires:  cxxopts-static

%description
Pamixer is like amixer but for PulseAudio. It can control the volume
levels of the sinks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.rst
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
