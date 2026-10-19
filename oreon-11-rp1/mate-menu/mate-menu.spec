%global source0_hash 36aa865b72664b8cc90d9c1c429fd3c44e2c198369aae4eaaa87228a5add075c
%global debug_package %{nil}
%global _name   mate_menu
Name:           mate-menu
Version:        22.04.2
Release:        1%{?dist}
Summary:        Advanced Menu for the MATE Desktop
License:        GPL-2.0-or-later AND LicenseRef-Callaway-MIT
BuildArch:      noarch
Url:            https://github.com/ubuntu-mate/%{name}
Source0:        https://github.com/ubuntu-mate/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         mate-menu_adjust-package-manager.patch
Patch2:         mate-menu_default-applications.patch
Requires:       mate-menus
Requires:       mozo
Requires:       python3-configobj
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       python3-xlib
Requires:       python3-setproctitle
Requires:       python3-unidecode
Requires:       beesu
Requires:       mate-panel
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mate-menu = %{version}-%{release}
# /oreon:deps
%description
An advanced menu for MATE. Supports filtering, favorites,
auto-session, and many other features.
This menu originated in the Linux Mint distribution and has
been ported to other distributions that ship the MATE Desktop
Environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P1 -p1 -b .adjust-package-manager
%patch -P2 -p1 -b .default-applications

# xdg-su isn't available in fedora
sed -i 's/xdg-su/beesu/g' %{_name}/execute.py

%build

%pyproject_wheel
%install
%pyproject_install
%py_byte_compile %{python3} %{buildroot}%{_usr}/lib/%{name}/*.py
rm -rf %{buildroot}%{_datadir}/locale/ber
rm -rf %{buildroot}%{_datadir}/locale/es_419/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/es_419/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/nah/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/zh-Hans/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/zh-Hans/
%find_lang %{name}
%oreon_autofiles main

%files

%changelog

%autochangelog
