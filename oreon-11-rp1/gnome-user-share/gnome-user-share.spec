%global source0_hash a04d483f49b3f769da8ff5e2d3fcbffbeaf3b6c6b71d82d2a2a623bb4b1e0dd4
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnome-user-share
Version:        48.3
Release:        1%{?dist}
Summary:        Gnome user file sharing
License:        GPL-2.0-or-later AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://gitlab.gnome.org/GNOME/gnome-user-share
Source0:        http://download.gnome.org/sources/%{name}/48/%{name}-%{version}.tar.xz
Requires:       httpd
Requires:       mod_dnssd
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  httpd
BuildRequires:  meson
BuildRequires:  mod_dnssd
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
gnome-user-share is a small package that binds together various free
software projects to bring easy to use user-level file sharing to the
masses.

The program is meant to run in the background when the user is logged
in, and when file sharing is enabled a webdav server is started that
shares the $HOME/Public folder. The share is then published to all
computers on the local network using mDNS/rendezvous, so that it shows
up in the Network location in GNOME.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
%install
%meson_install
%find_lang gnome-user-share --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-user-share-webdav.desktop
%post

%systemd_user_post gnome-user-share-webdav.service
%preun

%systemd_user_preun gnome-user-share-webdav.service
%postun

%systemd_user_postun_with_restart gnome-user-share-webdav.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
