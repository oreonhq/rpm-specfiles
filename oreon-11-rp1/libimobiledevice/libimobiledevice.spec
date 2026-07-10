%global source0_hash 23cc0077e221c7d991bd0eb02150a0d49199bcca1ddf059edccee9ffd914939d

%global forgeurl https://github.com/libimobiledevice/libimobiledevice

Name:           libimobiledevice
Version:        1.4.0
Release:        %autorelease
Summary:        Library for connecting to mobile devices

License:        LGPL-2.0-or-later AND MIT AND Zlib
URL:            https://libimobiledevice.org/
Source0:        %{forgeurl}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  glib2-devel
BuildRequires:  openssl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libplist-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libtatsu-devel
BuildRequires:  libusbmuxd-devel
BuildRequires:  libusbx-devel
BuildRequires:  libxml2-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  readline-devel

Provides:       bundled(ed25519)
Provides:       bundled(SRP6a)

Recommends: usbmuxd

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
%autosetup -p1 -n %{name}-%{version}

%build
export PYTHON_VERSION="%{python3_version}"
%configure --disable-static
%make_build

%install
%make_install

%files
%license COPYING.LESSER
%doc AUTHORS README.md
%{_libdir}/libimobiledevice-1.0.so.6*

%files utils
%{_bindir}/afcclient
%{_bindir}/idevice*
%{_mandir}/man1/afcclient.1*
%{_mandir}/man1/idevice*.1*

%files devel
%{_libdir}/pkgconfig/libimobiledevice-1.0.pc
%{_libdir}/libimobiledevice-1.0.so
%{_includedir}/libimobiledevice/

%files -n python3-libimobiledevice
%{python3_sitearch}/imobiledevice.so

%changelog
%autochangelog
