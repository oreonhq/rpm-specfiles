%global source0_hash 434ea95081b90f88f8dd6d67d6d9d4a517d55d83da9f04870bb27633511c5d39

Name:           camorama
Version:        0.21.2
Release:        13%{?dist}
Summary:        Gnome webcam viewer
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/alessio/camorama
Source0:        https://linuxtv.org/downloads/camorama/camorama-%{version}.tar.gz
Patch0:		fix_crash_on_device_change.patch
BuildRequires:  gcc desktop-file-utils libappstream-glib
BuildRequires:  gettext-devel libv4l-devel gtk3-devel cairo-devel
BuildRequires:  gdk-pixbuf2-devel gnome-common make
Requires:       hicolor-icon-theme

%description
A simple Gnome webcam viewer, with the ability to apply some video effects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
%configure --prefix /usr
%make_build

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install
%find_lang %{name}

# below is the desktop file and icon stuff.
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md THANKS TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/camorama.desktop
%{_datadir}/icons/hicolor/*x*/devices/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
