%global source0_hash 4401d4e231d842c2de8242395a74a395ca468cd96f5f610d822df33594898a70
Summary:        Utilities for manipulating .desktop files
Name: desktop-file-utils
Version: 0.28
Release:        1%{?dist}
URL: https://www.freedesktop.org/software/desktop-file-utils
Source0:        https://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
Source1: desktop-entry-mode-init.el
Patch0: 0001-validate-Add-Phosh-to-list-of-valid-OnlyShowIn-envir.patch
License: GPL-2.0-or-later
Requires: emacs-filesystem
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  meson
# /oreon:deps
%description
.desktop files are used to describe an application for inclusion in
GNOME or KDE menus.  This package contains desktop-file-validate which
checks whether a .desktop file complies with the specification at
http://www.freedesktop.org/standards/, and desktop-file-install
which installs a desktop file to the standard directory, optionally
fixing it up in the process.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/desktop-file-utils
mv $RPM_BUILD_ROOT%{_emacs_sitelispdir}/*.el* $RPM_BUILD_ROOT%{_emacs_sitelispdir}/desktop-file-utils
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/desktop-entry-mode-init.el
touch $RPM_BUILD_ROOT%{_emacs_sitestartdir}/desktop-entry-mode-init.elc
%transfiletriggerin -- %{_datadir}/applications
update-desktop-database &> /dev/null || :
%transfiletriggerpostun -- %{_datadir}/applications
update-desktop-database &> /dev/null || :
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.28-1
- Prepare for Oreon 11 (RP1)
