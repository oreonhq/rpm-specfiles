Name:           wayland-utils
Version:        1.3.0
Release:        3%{?dist}
Summary:        Wayland utilities

License:        MIT
URL:            https://wayland.freedesktop.org/
Source0:        https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-3
- Prepare for Oreon 11 (RP1)
