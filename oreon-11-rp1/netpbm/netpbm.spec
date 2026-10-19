%global source0_hash 4f7609286f9b0e1b80699e69cb031244a2009357e0ae83acf7d689f9f5012448
Summary:        A library for handling different graphics file formats
Name:            netpbm
Version:         11.16.00
Release:        1%{?dist}
License:         BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-or-later AND GPL-3.0-or-later AND IJG AND MIT AND NTP AND PostgreSQL AND LicenseRef-MIT-CRL-Xim AND LicenseRef-Public-Domain
URL: http://netpbm.sourceforge.net/
Source0:        netpbm-%{version}.tar.xz
Patch1:        netpbm-security-code.patch
Patch2:        netpbm-ppmfadeusage.patch
Patch3:        netpbm-CVE-2017-2587.patch
Patch4:        netpbm-python3.patch
Patch5:        netpbm-time.patch
Patch6:        netpbm-gcc4.patch
Patch7:        netpbm-bmptopnm.patch
Patch8:        netpbm-CAN-2005-2471.patch
Patch9:        netpbm-xwdfix.patch
Patch10:        netpbm-multilib.patch
Patch11:        netpbm-glibc.patch
Patch12:        netpbm-docfix.patch
Patch13:        netpbm-pamtojpeg2k.patch
Patch14:        netpbm-manfix.patch
Patch15:        netpbm-jasper.patch
Patch16:        netpbm-libdir-so.patch
Patch18:        netpbm-shlib-ldflags.patch
%if (0%{?fedora} && 0%{?fedora} < 28) || (0%{?rhel} || 0%{?rhel} <= 7) || (0%{?oreon} >= 11)
%else
%endif
# oreon:deps
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  ghostscript-core
BuildRequires:  jasper-devel
BuildRequires:  jbigkit-devel
BuildRequires:  libX11-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  python3
BuildRequires:  subversion
# /oreon:deps
%description
The netpbm package contains a library of functions which support
programs for handling various graphics file formats, including .pbm
(portable bitmaps), .pgm (portable graymaps), .pnm (portable anymaps),
.ppm (portable pixmaps) and others.

%package devel
Summary:         Development tools for programs which will use the netpbm libraries
Requires:        netpbm = %{version}-%{release}
%description devel
The netpbm-devel package contains the header files and static libraries,
etc., for developing programs which can handle the various graphics file
formats supported by the netpbm libraries.

Install netpbm-devel if you want to develop programs for handling the
graphics file formats supported by the netpbm libraries.  You'll also need
to have the netpbm package installed.

%package progs
Summary:         Tools for manipulating graphics files in netpbm supported formats
Requires:        ghostscript
Requires:        netpbm = %{version}-%{release}
%description progs
The netpbm-progs package contains a group of scripts for manipulating the
graphics files in formats which are supported by the netpbm libraries.  For
example, netpbm-progs includes the rasttopnm script, which will convert a
Sun rasterfile into a portable anymap.  Netpbm-progs contains many other
scripts for converting from one graphics file format to another.

If you need to use these conversion scripts, you should install
netpbm-progs.  You'll also need to install the netpbm package.

%package doc
Summary:         Documentation for tools manipulating graphics files in netpbm supported formats
Requires:        netpbm-progs = %{version}-%{release}
%description doc
The netpbm-doc package contains a documentation in HTML format for utilities
present in netpbm-progs package.

If you need to look into the HTML documentation, you should install
netpbm-doc.  You'll also need to install the netpbm-progs package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
rm -rf converter/other/jpeg2000/libjasper/
rm -rf converter/other/jbig/libjbig/

%build

%set_build_flags
./configure <<EOF
EOF
TOP=`pwd`
make \
	CC="%{__cc}" \
	LDFLAGS="$LDFLAGS -L$TOP/pbm -L$TOP/pgm -L$TOP/pnm -L$TOP/ppm" \
	CFLAGS="$CFLAGS -fPIC -flax-vector-conversions -fno-strict-aliasing" \
	CFLAGS_CONFIG="$CFLAGS" \
	LADD="-lm" \
	JPEGINC_DIR=%{_usr}/include \
	PNGINC_DIR=%{_usr}/include \
	TIFFINC_DIR=%{_usr}/include \
	JPEGLIB_DIR=%{_usr}/%{_lib} \
	JBIGLIB=%{_usr}/%{_lib}/libjbig.so.2.1 \
	PNGLIB_DIR=%{_usr}/%{_lib} \
	TIFFLIB_DIR=%{_usr}/%{_lib} \
	LINUXSVGALIB="NONE" \
	X11LIB=%{_usr}/%{_lib}/libX11.so \
	XML2LIBS="NONE"
cd userguide
rm -f *.manual-pages
rm -f *.manfix
for i in *.html ; do
  ../buildtools/makeman ${i}
done
for i in 1 3 5 ; do
  mkdir -p man/man${i}
  mv *.${i} man/man${i}
done
%install
make package pkgdir=%{buildroot}%{_prefix} LINUXSVGALIB="NONE" XML2LIBS="NONE"
mkdir -p %{buildroot}%{_libdir}
if [ "%{_lib}" != "lib" ]; then
  mv %{buildroot}%{_prefix}/lib/lib* %{buildroot}%{_libdir}
fi
cp -af lib/libnetpbm.a %{buildroot}%{_libdir}/libnetpbm.a
mkdir -p %{buildroot}%{_datadir}
mv userguide/man %{buildroot}%{_mandir}
sed -i 's/\xa0//' %{buildroot}%{_mandir}/man1/pgmminkowski.1
for i in hpcdtoppm \
	 ppmsvgalib vidtoppm picttoppm \
	 directory error extendedopacity \
	 pam pbm pgm pnm ppm index libnetpbm_dir \
	 liberror ppmtotga; do
	rm -f %{buildroot}%{_mandir}/man1/${i}.1
done
rm -f %{buildroot}%{_mandir}/man5/extendedopacity.5
mkdir -p %{buildroot}%{_datadir}/netpbm
mv %{buildroot}%{_prefix}/misc/*.map %{buildroot}%{_datadir}/netpbm/
mv %{buildroot}%{_prefix}/misc/rgb.txt %{buildroot}%{_datadir}/netpbm/
rm -rf %{buildroot}%{_prefix}/README
rm -rf %{buildroot}%{_prefix}/VERSION
rm -rf %{buildroot}%{_prefix}/link
rm -rf %{buildroot}%{_prefix}/misc
rm -rf %{buildroot}%{_prefix}/man
rm -rf %{buildroot}%{_prefix}/pkginfo
rm -rf %{buildroot}%{_prefix}/config_template
rm -rf %{buildroot}%{_prefix}/pkgconfig_template
rm -f %{buildroot}%{_libdir}/lib*.a
pushd %{buildroot}%{_bindir}
rm -f pgmtopbm pnmcomp
ln -s pamcomp pnmcomp
echo -e '#!/bin/sh\npamditherbw $@ | pamtopnm\n' > pgmtopbm
chmod 0755 pgmtopbm
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd test
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export PBM_TESTPREFIX=%{buildroot}%{_bindir}
export PBM_BINPREFIX=%{buildroot}%{_bindir}
./Execute-Tests && exit 0
popd
%files -f %{oreon_filedir}/main.list
%files -n netpbm-devel -f %{oreon_filedir}/netpbm-devel.list
%files -n netpbm-progs -f %{oreon_filedir}/netpbm-progs.list
%files -n netpbm-doc -f %{oreon_filedir}/netpbm-doc.list

%changelog

%autochangelog
