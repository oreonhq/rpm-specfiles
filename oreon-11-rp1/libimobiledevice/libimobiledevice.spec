%global source0_hash abd343e0f5a5fea43ed36e3fc54b803d0ef0a53ffd28304bae20111e93ee39e4

%global forgeurl https://github.com/libimobiledevice/libimobiledevice
%global commit ed9703db1ee6d54e3801b618cee9524563d709e1
%global date 20240916
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           libimobiledevice
Version:        1.3.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Library for connecting to mobile devices

License:        LGPL-2.0-or-later
URL:            https://libimobiledevice.org/
Source:        https://github.com/libimobiledevice/libimobiledevice/archive/refs/tags/ed9703db1ee6d54e3801b618cee9524563d709e1.tar.gz#/libimobiledevice-ed9703db1ee6d54e3801b618cee9524563d709e1.tar.gz
# Use SHA256 signature, instead of SHA1 for pairing
Patch:        https://github.com/libimobiledevice/libimobiledevice/pull/1616.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
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
BuildRequires:  readline-devel

# Applications using libimobiledevice might use sockets provided by usbmuxd to
# work
Recommends: usbmuxd

%description
libimobiledevice is a library for connecting to mobile devices including phones
and music players

%package        devel
Summary:        Development package for libimobiledevice
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with libimobiledevice.

%package        utils
Summary:        Utilities for libimobiledevice
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
Utilities for use with libimobiledevice.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{commit}

%if %{defined commit}
echo %{version} > .tarball-version
%endif

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --without-cython
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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0^%{date}git%{shortcommit}-1
- Prepare for Oreon 11 (RP1)
