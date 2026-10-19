%global source0_hash ecb4091ddc5069e580e2294f91ffb2e53b60470eb4a3a1193fee1c5805ced234
%global extdir		caffeine@patapon.info
%global gschemadir	%{_datadir}/glib-2.0/schemas
Name:		gnome-shell-extension-caffeine
Version:	60
Release:        1%{?dist}
Summary:        Disable the screen saver and auto suspend in gnome shell
License:	GPL-2.0-only
URL:		https://github.com/eonpatapon/gnome-shell-extension-caffeine
%if 0%{?shortcommit:1}
Source0:        https://github.com/eonpatapon/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
%else
%endif
BuildArch:	noarch
Requires:	gnome-shell-extension-common
# oreon:deps
BuildRequires:  /usr/bin/glib-compile-schemas
BuildRequires:  gettext
# /oreon:deps
%description
This extension allows the user to easily disable the screen saver and auto
suspend in gnome shell via an icon in the top bar. By default, this function
is also enabled if a full screen application is running, and can be configured
to disable gnome shell's night light as well.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{?commit:-n %{name}-%{commit}}

%build

./update-locale.sh
glib-compile-schemas --strict --targetdir=%{extdir}/schemas/ %{extdir}/schemas
%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -ar %{extdir} %{buildroot}%{_datadir}/gnome-shell/extensions/%{extdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
