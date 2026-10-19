%global source0_hash e3a73728cf30f1e542aed3aa4f18a342e09349b97fe01dfaef86e1603e53af3c
%global __provides_exclude_from ^%{_libdir}/gnome-connections/
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/gnome-connections/ -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           gnome-connections
Version:        51.0
Release:        1%{?dist}
Summary:        A remote desktop client for the GNOME desktop environment
License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://gitlab.gnome.org/gnome/connections/-/wikis/home
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
Obsoletes:      connections < 40.0-2
Provides:       connections = %{version}-%{release}
Provides: bundled(gtk-frdp)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(freerdp3)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-vnc-2.0)
BuildRequires:  pkgconfig(gvncpulse-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(winpr3)
BuildRequires:  vala
BuildRequires:  yelp-tools
# /oreon:deps
%description
Connections is a remote desktop client for the GNOME desktop environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n gnome-connections-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang gnome-connections --with-gnome
rm -rf %{buildroot}%{_includedir}/gnome-connections/
rm -rf %{buildroot}%{_libdir}/gnome-connections/girepository-1.0/
rm -rf %{buildroot}%{_libdir}/gnome-connections/pkgconfig/
rm -rf %{buildroot}%{_datadir}/gnome-connections/gir-1.0/
rm -rf %{buildroot}%{_datadir}/gnome-connections/vapi/
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Connections.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Connections.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
