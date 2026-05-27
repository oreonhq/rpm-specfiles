%global source0_hash 898ceff3007b11aaec5b13844ac673b99ee186b2706b9b2ab41ba6be8c29ad06

Name:           wayland-utils
Version:        1.3.0
Release:        5%{?dist}
Summary:        Wayland utilities

License:        MIT
URL:            https://wayland.freedesktop.org/
# freedesktop.org/releases .tar.xz for this version returns 404 use git tag archive
Source0:        https://gitlab.freedesktop.org/wayland/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client) >= 1.20
BuildRequires:  pkgconfig(wayland-protocols) >= 1.44
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109

%description
wayland-utils contains wayland-info, a standalone version of weston-info,
a utility for displaying information about the Wayland protocols supported
by the Wayland compositor.
wayland-info also provides additional information for a subset of Wayland
protocols it knows about, namely Linux DMABUF, presentation time, tablet and
XDG output protocols.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wayland-info
%{_mandir}/man1/wayland-info.1*

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-5
- Source0 GitLab archive freedesktop releases URL 404 for 1.3.0

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-4
- bump release (retry failed build)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-3
- Prepare for Oreon 11 (RP1)
