%global source0_hash d282fa6481a5b85f71e36e8bad4cfa938cc8eaac4c42ffa27f9203ac634813f4
Name:           libfakekey
Version:        0.3
%global so_version 0
Release:        1%{?dist}
Summary:        Library for converting characters to X key-presses
License:        LGPL-2.0-or-later
URL:            https://git.yoctoproject.org/libfakekey
Source0:        https://sources.voidlinux.org/libfakekey-%{version}/libfakekey-%{version}.tar.gz
Obsoletes:      libfakekey-doc < 0.3-22
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
# /oreon:deps
%description
libfakekey is a simple library for converting UTF-8 characters into 'fake' X
key-presses.

%package        devel
Summary:        Development files for libfakekey
Requires:       libfakekey%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xtst)
%description    devel
The libfakekey-devel package contains libraries and header files for developing
applications that use libfakekey.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
# The tarball generated from the git tag has no configure script, so this is
# mandatory. See autogen.sh (which, however, we do not use because we need to
# use the %%configure macro).
autoreconf --force --install --verbose
%configure --disable-static

%build

%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libfakekey-devel -f %{oreon_filedir}/libfakekey-devel.list

%changelog

%autochangelog

