%global source0_hash 67515fefb9829d054beae40f3e840309be60cda7d68753cafdd526727758f67a

Summary: VideoCD (pre-)mastering and ripping tool
Name:    vcdimager
Version: 2.0.1
Release: 24%{?dist}
License: GPL-2.0-or-later
URL:     http://www.gnu.org/software/vcdimager/
Source:  https://ftp.gnu.org/pub/gnu/vcdimager/vcdimager-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libcdio-devel >= 0.72
BuildRequires: libxml2-devel >= 2.3.8
BuildRequires: pkgconfig >= 0.9
BuildRequires: popt-devel
BuildRequires: zlib-devel

Requires:        %{name}-libs%{?_isa} = %{version}-%{release}

%description
VCDImager allows you to create VideoCD BIN/CUE CD images from MPEG
files. These can be burned with cdrdao or any other program capable of
burning BIN/CUE files.

Also included is VCDRip which does the reverse operation, that is to
rip MPEG streams from images or burned VideoCDs and to show
information about a VideoCD.

%package libs
Summary: Libraries for %{name}

%description libs
The %{name}-libs package contains shared libraries for %{name}.

%package devel
Summary:  Header files and library for VCDImager
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: libcdio-devel

%description devel
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files.

This package contains the header files and a library to develop
applications that will use VCDImager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static --disable-dependency-tracking
%make_build V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

# Sometimes this file gets created... but we don't want it!
rm -f %{buildroot}%{_infodir}/dir

%ldconfig_scriptlets libs

%files
%doc AUTHORS BUGS ChangeLog* FAQ NEWS README THANKS TODO
%doc frontends/xml/videocd.dtd
%license COPYING
%{_bindir}/cdxa2mpeg
%{_bindir}/vcd-info
%{_bindir}/vcdimager
%{_bindir}/vcdxbuild
%{_bindir}/vcdxgen
%{_bindir}/vcdxminfo
%{_bindir}/vcdxrip
%{_infodir}/vcdxrip.info*
%{_infodir}/vcdimager.info*
%{_infodir}/vcd-info.info*
%{_mandir}/man1/cdxa2mpeg.1*
%{_mandir}/man1/vcd-info.1*
%{_mandir}/man1/vcdimager.1*
%{_mandir}/man1/vcdxbuild.1*
%{_mandir}/man1/vcdxgen.1*
%{_mandir}/man1/vcdxminfo.1*
%{_mandir}/man1/vcdxrip.1*

%files libs
%{_libdir}/libvcdinfo.so.0*

%files devel
%doc HACKING
%{_includedir}/libvcd/
%{_libdir}/libvcdinfo.so
%{_libdir}/pkgconfig/libvcdinfo.pc

%changelog
%autochangelog
