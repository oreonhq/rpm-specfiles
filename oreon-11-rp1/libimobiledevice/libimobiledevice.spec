%global source0_hash 23cc0077e221c7d991bd0eb02150a0d49199bcca1ddf059edccee9ffd914939d
%global forgeurl https://github.com/libimobiledevice/libimobiledevice
Name:           libimobiledevice
Version:        1.4.0
Release:        1%{?dist}
Summary:        Library for connecting to mobile devices
License:        LGPL-2.0-or-later AND MIT AND Zlib
URL:            https://libimobiledevice.org/
Source0:        %{forgeurl}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Provides:       bundled(ed25519)
Provides:       bundled(SRP6a)
Recommends: usbmuxd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libplist-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libtatsu-devel
BuildRequires:  libusbmuxd-devel
BuildRequires:  libusbx-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
libimobiledevice is a library for connecting to mobile devices including phones
and music players

%package        devel
Summary:        Development package for libimobiledevice
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Files for development with libimobiledevice.

%package  -n    python3-libimobiledevice
Summary:        Python3 bindings for libimobiledevice
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3
%description -n python3-libimobiledevice
%{name}, python3 libraries and bindings.

%package        utils
Summary:        Utilities for libimobiledevice
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    utils
Utilities for use with libimobiledevice.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

export PYTHON_VERSION="%{python3_version}"
%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles python3-libimobiledevice usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libimobiledevice-devel -f %{oreon_filedir}/libimobiledevice-devel.list
%files -n python3-libimobiledevice -f %{oreon_filedir}/python3-libimobiledevice.list
%files -n libimobiledevice-utils -f %{oreon_filedir}/libimobiledevice-utils.list

%changelog

%autochangelog
