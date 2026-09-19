%global source0_hash 4e6aea3f8975fec720f6eb87aad620d5297a8a5a137615e4cf047e95d2b9d308

Name:           wmenu
Version:        0.2.0
Release:        %autorelease
Summary:        Efficient dynamic menu for Wayland

# Main source: MIT
# protocols/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant
License:        MIT
URL:            https://codeberg.org/adnano/wmenu
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
An efficient dynamic menu for Sway and wlroots based Wayland compositors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

%build
%meson \
    -Dwerror=false
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
