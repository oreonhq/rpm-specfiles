%global source0_hash 2360c2019dd88c03e8cdfc4ed5a1f2476be7ff585186753c9911fcf81b376350
%global extdir      %{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
%global gschemadir  %{_datadir}/glib-2.0/schemas
%global giturl https://github.com/micheleg/dash-to-dock
Name:           gnome-shell-extension-dash-to-dock
Version:        109
Release:        1%{?dist}
Summary:        Dock for the Gnome Shell by micxgx@gmail.com
License:        GPL-2.0-or-later
URL:            https://micheleg.github.io/dash-to-dock
%if 0%{?commit:1}
Source0:        %{giturl}/archive/extensions.gnome.org-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
%endif
Source1:        stylesheet.css
BuildArch:      noarch
%if 0%{?fedora} || 0%{?oreon}
%endif
Requires:       gnome-shell-extension-common
# oreon:deps
BuildRequires:  /usr/bin/glib-compile-schemas
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  sassc
# /oreon:deps
%description
This extension enhances the dash moving it out of the overview and
transforming it in a dock for an easier launching of applications
and a faster switching between windows and desktops without having
to leave the desktop view.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if 0%{?commit:1}
%autosetup -n dash-to-dock-%{commit} -p 1
%else
%autosetup -n dash-to-dock-extensions.gnome.org-v%{version} -p 1
%endif

%build

%make_build
%install
%make_install
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}
%find_lang %{name} --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
