%global source0_hash 90288e8900a274a3aee20530eb391645994ae9867220916ba0f5c4677bfe9f4d
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           accerciser
Version:        3.48.0
Release:        1%{?dist}
Summary:        Interactive Python accessibility explorer for the GNOME desktop
License:        LicenseRef-Callaway-BSD
URL:            https://wiki.gnome.org/Apps/Accerciser
Source0:        https://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       libwnck3
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-ipython-console
Requires:       python3-pyatspi
Requires:       python3-xlib
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3
BuildRequires:  python3-devel
# /oreon:deps
%description
Accerciser is an interactive Python accessibility explorer for the GNOME
desktop. It uses AT-SPI to inspect and control widgets, allowing you to check
if an application is providing correct information to assistive technologies
and automated test frameworks. Accerciser has a simple plugin framework which
you can use to create custom views of accessibility information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export PYTHON=%{python3}
%meson
%meson_build
%install
%meson_install
%find_lang accerciser --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/accerciser.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
