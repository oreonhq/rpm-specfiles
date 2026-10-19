%global source0_hash 39cbd4f0efdfddc9755d88217e47f8f2d7108fa767f9d58a2ba26a16d8f7c910
Name:           libshout
Version:        2.4.6
Release:        1%{?dist}
Summary:        Icecast source streaming library
License:        LGPL-2.0-or-later
URL:            https://www.icecast.org/
Source0:        https://downloads.us.xiph.org/releases/libshout/libshout-%{version}.tar.gz
Patch0:         libshout-2.4.3-Allow-disabling-ckport-database-installation.patch
Patch1:         libshout-2.4.3-Default-OpenSSL-cipher-list-is-PROFILE-SYSTEM.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  sed
# /oreon:deps
%description
libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%package        devel
Summary:        Header files for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The libshout-devel package contains the header files needed for developing
applications that send data to an icecast server.  Install libshout-devel if
you want to develop applications using libshout.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1
%patch -P1 -p1
autoreconf -fi

%build

%configure \
  --disable-ckport \
  --enable-examples \
  --enable-pkgconfig \
  --disable-silent-rules \
  --enable-shared \
  --enable-speex \
  --disable-static \
  --enable-theora \
  --enable-thread
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete
rm -rf $RPM_BUILD_ROOT%{_docdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libshout-devel -f %{oreon_filedir}/libshout-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.6-10
- Prepare for Oreon 11 (RP1)
