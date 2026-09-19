%global source0_hash d373e2f2d4ab444e33238c9765251eafa1903b10fd69da5359ae25096b3a85af

Name:		libhid
Version:	0.2.17
Release:	53%{?dist}
Summary:	User space USB HID access library
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://libhid.alioth.debian.org
# The source for this package was pulled from upstream's Subversion.  Use the
# following commands to generate the tarball:
#  svn co svn://svn.debian.org/libhid/trunk libhid-0.2.17
#  tar -czvf libhid-0.2.17.tar.gz libhid-0.2.17
Source0:	%{name}-%{version}.tar.gz

# Use db2x_docbook2man instead xsltproc to generate man pages
Patch0:		libhid-0.2.17-fix_manpage.patch
# Stop the configure script to mess the flags
Patch1:		libhid-0.2.17-fix_compiler_flags.patch
# Fix FTBFS rhbz#716191
Patch2:		libhid-0.2.17-buildfix.patch
# Fix Python installation on x86_64
Patch3:		libhid-0.2.17-fix_python.patch
BuildRequires:	libusb-compat-0.1-devel, libtool, pkgconfig, docbook2X, docbook-style-xsl
BuildRequires:	make

%description
libhid provides a generic and flexible way to access and interact with USB
HID devices, much like libusb does for plain USB devices. It is based on
libusb, thus it requires no HID support in the kernel and provides means to
take control over a device even if the kernel governs it.

%package devel
Summary: Development files for libhid
Requires: %{name} = %{version}-%{release}
Requires: libusb-compat-0.1-devel

%description devel
This package provides the development files for libhid.
You need this if you want to develop an application with libhid

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fix_manpage
%patch -P3 -p1 -b .fix_python
# Allow build against swig-3.0
sed -i 's|AC_PROG_SWIG(1.3)|AC_PROG_SWIG(3.0)|' configure.ac
autoreconf -i
%patch -P1 -p1 -b .fix_compiler_flags
%patch -P2 -p1

%build
# Fix swig and disable doxygen for now
%configure --disable-static --disable-werror --without-doxygen --disable-swig
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} LDFLAGS="$LDFLAGS -lusb"

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
# Excluded INSTALL and COPYING as they are symlinks to nothing
%license README.licence
%{_libdir}/*.so.*
%{_bindir}/libhid-detach-device
%{_mandir}/man1/*

%files devel
%doc AUTHORS README ChangeLog
%{_libdir}/pkgconfig/libhid.pc
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
