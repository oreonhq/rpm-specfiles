%global source0_hash 9f601c68f6e993451587dd422e352aa5478b7f584947587d38773f329b9b6ab4

# Review:       https://bugzilla.redhat.com/487973

Name:           lxmenu-data
Version:        0.1.7
Release:        2%{?dist}
Summary:        Data files for the LXDE menu

# SPDX confirmed
License:        LGPL-2.0-or-later
URL:            http://lxde.org
Source0:        https://github.com/lxde/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        lxmenu-data-0.1-COPYING
Patch0:         lxmenu-data-0.1.1-menu.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  intltool >= 0.40.0
BuildRequires:  automake
BuildRequires:  gtk-doc
BuildRequires:  libtool
# AM_GLIB_GNU_GETTEXT in glib-gettext.m4
BuildRequires:  pkgconfig(glib-2.0)
Requires:       redhat-menus
BuildArch:      noarch

%description
The lxmenu-data contains files used to build the menu in LXDE according to 
the freedesktop-org menu spec. Currently it's used by LXPanel and LXLauncher.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#%%patch -P0 -p1 -b .orig
sh autogen.sh

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
#FIXME: add changelog when there is one
%doc AUTHORS
%doc README
%doc TODO
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/menus/lxde-applications.menu
%{_datadir}/desktop-directories/lxde-*.directory

%changelog
%autochangelog
