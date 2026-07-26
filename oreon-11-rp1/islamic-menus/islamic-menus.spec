%global source0_hash 92ad5c597a88f5c2349c047f1b882b65eb0026ddd098fe166cdae3c336f334f4

%global owner ojuba-org
%global commit 276a1aa30d3740539c4a8a3340245711fe9f7284

Name:			islamic-menus
Version:		1.0.6
Release:		27%{?dist}
Summary:		Islamic menus for desktops conforming with XDG standards
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:		GPL-3.0-or-later
URL:			https://github.com/ojuba-org/islamic-menus
Source0:		https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:		noarch
Requires:		redhat-menus hicolor-icon-theme
BuildRequires:	intltool
BuildRequires: make

%description
Categorize islamic apps in a menu for the GNOME, KDE and other
XDG-conforming desktops.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_sysconfdir}/xdg/menus/applications-gnome-merged/islamic.menu

%files
%doc COPYING
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/islamic.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/hicolor/scalable/categories/*.svg

%changelog
%autochangelog
