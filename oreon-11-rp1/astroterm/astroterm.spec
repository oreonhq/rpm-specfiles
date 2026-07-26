%global source0_hash 3dc44b1e90be8fbe5bcc7656032560f51275f985c7e3f783c9028e1838ec7bed

Name:           astroterm
Version:        1.0.6
Release:        4%{?dist}
Summary:        A planetarium for your terminal

License:        MIT
URL:            https://github.com/da-luce/astroterm
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://tdc-www.harvard.edu/catalogs/ybsc5.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  argtable-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  /usr/bin/xxd

%description
astroterm is a terminal-based star map.
It displays the real-time positions of stars, planets,
constellations, and more, all within your terminal—no telescope required!
Configure sky views by date, time, and location with precise ASCII-rendered
visuals.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
gunzip -dc %{SOURCE1} > data/ybsc5

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/astroterm

%changelog
%autochangelog
