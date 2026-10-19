%global source0_hash 4adb7dec926428f74263d5796673cf142e4720b6e768f5468a8d0933f98c9597
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           gnome-screenshot
Version:        41.0
Release:        13%{?dist}
Summary:        A screenshot utility for GNOME
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-screenshot
Source0:        https://download.gnome.org/sources/%{name}/41/%{name}-%{version}.tar.xz
Patch0:         57.patch
# oreon:deps
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
# /oreon:deps
%description
gnome-screenshot lets you take pictures of your screen.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n gnome-screenshot-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Screenshot.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 41.0-13
- Prepare for Oreon 11 (RP1)
