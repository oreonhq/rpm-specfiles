%global source0_hash 8a8fe36190a219930e1154089aab88c4e40b15c5f00c2c66025de96a4d8a44cd

Summary: A terminal program for displaying Unicode on the console
Name: bogl
Version: 0.1.18
Release: 58%{?dist}
URL: http://packages.debian.org/unstable/source/bogl
Source0: http://update2.intellique.com/repository/archive/pool/main/b/bogl/bogl_0.1.18-1.5.tar.gz
Source1: 14x14cjk.bdf.gz
Patch0: bogl-0.1.18-1.1.sigchld.patch
Patch1: bogl-0.1.18-1.2.reduce-font.patch
Patch2: bogl-0.1.18-1.2.gzip-fonts.patch
Patch3: bogl-0.1.18-1.2.term.patch
Patch4: bogl-0.1.18-1.5.rh.patch
Patch5: bogl-0.1.9-2.6fbdev.patch
Patch6: bogl-0.1.18-noexecstack.patch
Patch7: bogl-0.1.18-format-security.patch
Patch8: bogl-0.1.18-fix-multiple-definition.patch
Patch9: bogl-0.1.18-gcc15-fixes.patch
Epoch: 0
License: GPL-2.0-or-later
BuildRequires: gcc
BuildRequires: gd-devel
BuildRequires: libpng-devel
BuildRequires: ncurses
BuildRequires: make

%description
BOGL stands for Ben's Own Graphics Library.  It is a small graphics
library for Linux kernel frame buffers.  It supports only very simple
graphics.

%package devel
Summary: Development files required to build BOGL applications
Requires: bogl = %{epoch}:%{version}-%{release}

%description devel
The bogl-devel package contains the static libraries and header files
for writing BOGL applications.

%package bterm
Summary: A Unicode capable terminal program for the Linux frame buffer
# Only for /usr/share/terminfo/b
Requires: ncurses-base

%description bterm
The bterm application is a terminal emulator that displays to a Linux
frame buffer.  It is able to display Unicode text on the console.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n bogl-0.1.18
%patch -P0 -p1 -b .sigchld
%patch -P1 -p1 -b .reduce-font
%patch -P2 -p1 -b .gzip-fonts
%patch -P3 -p1 -b .term
%patch -P4 -p1 -b .rh
%patch -P5 -p1 -b .26fbdev
%patch -P6 -p1 -b .noexecstack
%patch -P7 -p1 -b .format-security
%patch -P8 -p1 -b .fix-multiple-definition
%patch -P9 -p1 -b .gcc15-fixes

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"
gunzip -c %{SOURCE1} > font.bdf
./bdftobogl -b font.bdf > font.bgf

%install
rm -rf $RPM_BUILD_ROOT
make CFLAGS="$RPM_OPT_FLAGS" DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir} install
mkdir -p $RPM_BUILD_ROOT/usr/share/bogl/
cp font.bgf $RPM_BUILD_ROOT/usr/share/bogl/
gzip -9 $RPM_BUILD_ROOT/usr/share/bogl/font.bgf
# remove /usr/share/terminfo/b/bterm - shipped in ncurses-base
rm $RPM_BUILD_ROOT/%{_datadir}/terminfo/b/bterm

%ldconfig_scriptlets

%files
%doc ChangeLog README debian/copyright
%{_libdir}/*.so.*

%files devel
%{_bindir}/bdftobogl
%{_bindir}/mergebdf
%{_bindir}/pngtobogl
%{_bindir}/reduce-font
%exclude %{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/bogl

%files bterm
%doc README.BOGL-bterm debian/copyright
%{_bindir}/bterm
/usr/share/bogl

%changelog
%autochangelog
