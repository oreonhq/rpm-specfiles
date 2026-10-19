%global source0_hash 573c84f15f5f963a440500f6f43412c928ac2335f6b69dcb58f1a1fe5201024b
%global gtk4_version 4.15.1
%global libadwaita_version 1.6~alpha
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           baobab
Version:        50.0
Release:        1%{?dist}
Summary:        A graphical directory tree analyzer
License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Baobab
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Requires:       gtk4%{?_isa} >= %{libadwaita_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala
# /oreon:deps
%description
Baobab is able to scan either specific directories or the whole filesystem, in
order to give the user a graphical tree representation including each
directory size or percentage in the branch.  It also auto-detects in real-time
any change made to your home folder as far as any mounted/unmounted device.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.gnome.baobab.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.baobab.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
