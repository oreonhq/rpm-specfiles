%global source1_hash 1cbe58067e624bd62feb88f9263e773f88f36ca30021e96765e4265547da379a
%global source0_hash 1090f680958a73dc1f443a1eb919bd2ad77b3caff38e92e9737dec100c647bc9
%global __requires_exclude pkg-config
%global libmajor 15
%global libminor 0
%global _docdir_fmt %{name}
Name:           pacman
Version:        7.1.0
Release:        1%{?dist}
Source0:        https://gitlab.archlinux.org/pacman/pacman/-/archive/v%{version}/pacman-v%{version}.tar.gz
Source1:        https://www.archlinux.org/mirrorlist/all
URL:            https://gitlab.archlinux.org/pacman/pacman
License:        GPL-2.0-or-later
Summary:        Package manager for the Arch distribution
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       bsdtar
Recommends:     arch-install-scripts
%global __requires_exclude_from ^%{_bindir}/makepkg-template$
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  bsdtar
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gpgme-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
Pacman is the package manager used by the Arch distribution. It can
be used to install Arch into a container or to recover an Arch
installation from a Fedora system (see arch-install-scripts package
for instructions).

Pacman is a frontend for the ALPM (Arch Linux Package Management)
library Pacman does not strive to "do everything." It will add, remove
and upgrade packages in the system, and it will allow you to query the
package database for installed packages, files and owners. It also
attempts to handle dependencies automatically and can download
packages from a remote server. Arch packages are simple archives, with
.pkg.tar.gz extension for binary packages and .src.tar.gz for source
packages.

%package -n libalpm
Summary: Arch Linux Package Management library
%description -n libalpm
This library is the backend behind Pacman — the package manager used
by the Arch distribution. It uses simple compressed files as a package
format, and maintains a text-based package database.

%package -n libalpm-devel
Summary: Development headers for libalpm
Requires: libalpm%{_isa} = %{version}-%{release}
%description -n libalpm-devel
This package contains the public headers necessary to use libalpm.

%package filesystem
Summary: Pacman filesystem layout
License: LicenseRef-Fedora-Public-Domain
BuildArch: noarch
%description filesystem
This package provides some directories used by pacman and related
packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pacman-v%{version}

# Enable some servers by default. rackspace.com is in the "worldwide" section,
# and "kernel.org" seems to be a good default too.
sed -r 's+^#(Server = https://(mirrors.kernel.org|mirror.rackspace.com)/)+\1+' <%{SOURCE1} >mirrorlist

%build

CONFIGURE_OPTS=(
        -Ddoxygen=enabled
)
%meson "${CONFIGURE_OPTS[@]}"
%meson_build
%install
%meson_install
%find_lang pacman
%find_lang pacman-scripts
%find_lang libalpm
cat pacman-scripts.lang >>pacman.lang
install -Dm0644 mirrorlist %{buildroot}%{_sysconfdir}/pacman.d/mirrorlist
cat >>%{buildroot}%{_sysconfdir}/pacman.conf <<EOF
[core]
SigLevel = Required DatabaseOptional
Include = %{_sysconfdir}/pacman.d/mirrorlist
[extra]
SigLevel = Required DatabaseOptional
Include = %{_sysconfdir}/pacman.d/mirrorlist
EOF
%oreon_autofiles libalpm usr/*/lib*.so.*
%oreon_autofiles libalpm-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libalpm -f %{oreon_filedir}/libalpm.list
%files -n libalpm-devel -f %{oreon_filedir}/libalpm-devel.list
%files -n pacman-filesystem -f %{oreon_filedir}/pacman-filesystem.list

%changelog

%autochangelog
