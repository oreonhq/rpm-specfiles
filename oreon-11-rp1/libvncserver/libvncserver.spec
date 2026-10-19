%global source0_hash 62352c7795e231dfce044beb96156065a05a05c974e5de9e023d688d8ff675d7
%undefine __cmake_in_source_build
Summary:        Library to make writing a VNC server easy
Name:       libvncserver
Version:    0.9.15
Release:        1%{?dist}
License:    GPL-2.0-or-later
URL:        http://libvnc.github.io/
Source0:        https://github.com/LibVNC/libvncserver/archive/LibVNCServer-%{version}.tar.gz#/libvncserver-0.9.15.tar.gz
Patch10: 0001-libvncserver-Add-API-to-add-custom-I-O-entry-points.patch
Patch11: 0002-libvncserver-Add-channel-security-handlers.patch
Patch13: 0003-Install-examples_in_datadir.patch
Patch14: 0004-libvncclient-fix-memory-leak-in-CompressClipData.patch
Patch102: libvncserver-LibVNCServer-0.9.13-system-crypto-policy.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  lzo-devel
BuildRequires:  lzo-minilzo
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  xorg-x11-xauth
BuildRequires:  zlib-devel
# /oreon:deps
%description
LibVNCServer makes writing a VNC server (or more correctly, a program exporting
a frame-buffer via the Remote Frame Buffer protocol) easy.

It hides the programmer from the tedious task of managing clients and
compression schemata.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   coreutils
Requires:   zlib-devel
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Examples for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description    examples
This package contains examples making use of %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-LibVNCServer-%{version}

# Nuke bundled minilzo
rm src/common/crypto_openssl.c
rm src/common/d3des.c
rm src/common/d3des.h
rm src/common/minilzo.h
rm src/common/sha1.c
rm src/common/sha.h
rm src/common/sha-private.h

# Fix encoding
for file in ChangeLog ; do
    mv ${file} ${file}.OLD && \
    iconv -f ISO_8859-1 -t UTF8 ${file}.OLD > ${file} && \
    touch --reference ${file}.OLD $file
done

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_CXX_COMPILER=/usr/bin/g++
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libvncserver-devel -f %{oreon_filedir}/libvncserver-devel.list
%files -n libvncserver-examples -f %{oreon_filedir}/libvncserver-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.15-6
- Import
