%global source0_hash 7d80b540673921c317c5541a055dc0c5f9a49c9c3ee255767fd7fe2a61c31093
Name:           camorama
Version:        0.21.2
Release:        13%{?dist}
Summary:        Gnome webcam viewer
License:        GPL-2.0-or-later
URL:            https://github.com/alessio/camorama
Source0:        https://linuxtv.org/downloads/camorama/camorama-%{version}.tar.gz
Patch0:		fix_crash_on_device_change.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libv4l-devel
BuildRequires:  make
# /oreon:deps
%description
A simple Gnome webcam viewer, with the ability to apply some video effects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --prefix /usr
%make_build
%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install
%find_lang %{name}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
