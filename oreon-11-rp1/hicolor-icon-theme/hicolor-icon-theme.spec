%global source0_hash db0e50a80aa3bf64bb45cbca5cf9f75efd9348cf2ac690b907435238c3cf81d7
Name: hicolor-icon-theme
Version: 0.18
Release:        1%{?dist}
Summary:        Basic requirement for icon themes
License: GPL-2.0-or-later
URL: https://www.freedesktop.org/wiki/Software/icon-theme/
Source0:        https://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.xz
BuildArch: noarch
# oreon:deps
BuildRequires:  meson
# /oreon:deps
%description
Contains the basic directories and files needed for icon theme support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# for some reason this file is executable in the tarball
chmod 0644 COPYING

%build

%meson
%meson_build
%install
%meson_install
rm $RPM_BUILD_ROOT%{_datadir}/pkgconfig/default-icon-theme.pc
touch $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
%transfiletriggerin -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :
%transfiletriggerpostun -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.18-1
- Prepare for Oreon 11 (RP1)
