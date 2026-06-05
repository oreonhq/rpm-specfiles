%global source0_hash 62352c7795e231dfce044beb96156065a05a05c974e5de9e023d688d8ff675d7

%undefine __cmake_in_source_build

Summary:    Library to make writing a VNC server easy
Name:       libvncserver
Version:    0.9.15
Release:    6%{?dist}

# NOTE: --with-filetransfer => GPLv2
License:    GPL-2.0-or-later
URL:        http://libvnc.github.io/
Source0:        https://github.com/LibVNC/libvncserver/archive/LibVNCServer-%{version}.tar.gz#/libvncserver-0.9.15.tar.gz

## TLS security type enablement patches
# https://github.com/LibVNC/libvncserver/pull/234
Patch10: 0001-libvncserver-Add-API-to-add-custom-I-O-entry-points.patch
Patch11: 0002-libvncserver-Add-channel-security-handlers.patch
Patch13: 0003-Install-examples_in_datadir.patch
Patch14: 0004-libvncclient-fix-memory-leak-in-CompressClipData.patch

## downstream patches
Patch102: libvncserver-LibVNCServer-0.9.13-system-crypto-policy.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
#BuildRequires:  pkgconfig(lzo2)
BuildRequires:  gettext-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  lzo-devel
BuildRequires:  lzo-minilzo
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
# Additional deps for --with-x11vnc, see https://bugzilla.redhat.com/show_bug.cgi?id=864947
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(xi)

# For %%check
BuildRequires:  xorg-x11-xauth
BuildRequires:  zlib-devel

# For Examples
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  gtk2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

%description
LibVNCServer makes writing a VNC server (or more correctly, a program exporting
a frame-buffer via the Remote Frame Buffer protocol) easy.

It hides the programmer from the tedious task of managing clients and
compression schemata.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
# libvncserver-config deps
Requires:   coreutils
# /usr/include/rfb/rfbproto.h:#include <zlib.h>
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


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS* README* CONTRIBUTING.md HISTORY.md SECURITY.md
%{_libdir}/libvncclient.so.1
%{_libdir}/libvncclient.so.%{version}
%{_libdir}/libvncserver.so.1
%{_libdir}/libvncserver.so.%{version}

%files devel
%{_includedir}/rfb/
%{_libdir}/libvncclient.so
%{_libdir}/libvncserver.so
%{_libdir}/pkgconfig/libvncclient.pc
%{_libdir}/pkgconfig/libvncserver.pc
%{_libdir}/cmake/LibVNCServer/*.cmake

%files examples
%{_datadir}/libvncserver


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.15-6
- Import
