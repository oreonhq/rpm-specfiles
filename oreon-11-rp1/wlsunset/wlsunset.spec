%global source0_hash a86ffb1793fe622802ec25795b69df864715986ecc175f7734e739c9e264ed72

Name:           wlsunset
Version:        0.4.0
Release:        4%{?dist}
Summary:        Day/night gamma adjustments for Sway

License:        MIT
URL:            https://sr.ht/~kennylevinsen/%{name}
Source0:        https://git.sr.ht/~kennylevinsen/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.56
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

%description
Day/night gamma adjustments for Sway and other Wayland compositors
supporting wlr-gamma-control-unstable-v1.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
