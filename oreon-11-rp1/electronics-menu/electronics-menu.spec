%global source0_hash b2ca878cebbafc0eda7ef1b88aff9ac83a8e1b92781b30610dd58a5b8b35b320

%{?!_icondir:%define _icondir   %{_datadir}/icons}

Name:       electronics-menu
Version:    1.0
Release:    38%{?dist}
Summary:    Electronics Menu for the Desktop
Summary(fr): Menu « Électronique » pour le bureau

# SPDX confirmed
License:    GPL-2.0-only

URL:        http://geda.seul.org/
Source0:    http://geda.seul.org/dist/%{name}-%{version}.tar.gz
# Created by Chitlesh
Source1:    electronics-menu-1.0-submenu.tar.bz2

Patch0:     electronics-menu-1.0-submenus.patch
Patch1:     electronics-menu-1.0-makefile.patch
Patch2:     electronics-menu-1.0-typo.patch
Patch3:     electronics-menu-1.0-submenus-fr.patch
Patch4:     electronics-menu-1.0-submenus-qucs.patch

BuildRequires: make

BuildArchitectures: noarch

%description
The programs from the category Electronics are normally located
in the Edutainment directory.
This Package adds a Electronics menu to the xdg menu structure.

%{name} is listed among Fedora Electronic Lab (FEL) packages.

%description -l fr
Les programmes de la catégorie Électronique sont normalement situés
dans la catégorie Éducation.
Ce paquetage ajoute le menu Électronique à la structure de menus xdg.

%{name} fait partie des paquetages de Fedora Electronic Lab (FEL).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1

%patch -P0 -p0 -b .submenus
%patch -P1 -p0 -b .submenus
%patch -P2 -p0 -b .typo
%patch -P3 -p0 -b .french
%patch -P4 -p0 -b .qucs

# allowing timestamps
sed -i 's|install|install -p|g' Makefile

# Fedora Specific Vendor
sed -i 's|<Filename>fedora-|<Filename>|' electronics.menu

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README
%{_icondir}/hicolor/??x??/categories/applications-electronics*.png
%{_icondir}/hicolor/scalable/categories/applications-electronics*.svg
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/electronics.menu
%{_datadir}/desktop-directories/*.directory

%changelog
%autochangelog
