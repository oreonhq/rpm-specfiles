%global source0_hash 6bfd3da084c2977fb5cee26c8e94bf55e358da8e86dd2a83c6fa9174f24672a1
%global xfceversion 4.20
Name:           orage
Version:        %{xfceversion}.2
Release:        1%{?dist}
Summary:        A calendar application
License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Requires:       hicolor-icon-theme
Requires:       dbus-common
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfce4ui-2)
# /oreon:deps
%description
Orage is a fast and easy to use graphical time-managing application for the
Xfce Desktop Environment. It uses portable ical format and includes common
calendar features like repeating appointments and multiple alarming
possibilities. Orage does not have group calendar features, but can
only be used for single user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
