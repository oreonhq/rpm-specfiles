%global source0_hash none

Summary:         A library for handling different graphics file formats
Name:            netpbm
Version:         11.13.00
Release:         2%{?dist}
# See copyright_summary for details
License:         BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-or-later AND GPL-3.0-or-later AND IJG AND MIT AND NTP AND PostgreSQL AND LicenseRef-MIT-CRL-Xim AND LicenseRef-Public-Domain
URL: http://netpbm.sourceforge.net/
# Source0 is prepared by
# svn checkout https://svn.code.sf.net/p/netpbm/code/advanced netpbm-%%{version}
# svn checkout https://svn.code.sf.net/p/netpbm/code/userguide netpbm-%%{version}/userguide
# svn checkout https://svn.code.sf.net/p/netpbm/code/trunk/test netpbm-%%{version}/test
# and removing the .svn directories ( find -name "\.svn" -type d -print0 | xargs -0 rm -rf )
Source0:         netpbm-%{version}.tar.xz
Patch1:          netpbm-security-code.patch
Patch2:          netpbm-ppmfadeusage.patch
Patch3:          netpbm-CVE-2017-2587.patch
Patch4:          netpbm-python3.patch
Patch5:          netpbm-time.patch
Patch6:          netpbm-gcc4.patch
Patch7:          netpbm-bmptopnm.patch
Patch8:          netpbm-CAN-2005-2471.patch
Patch9:          netpbm-xwdfix.patch
Patch10:         netpbm-multilib.patch
Patch11:         netpbm-glibc.patch
Patch12:         netpbm-docfix.patch
Patch13:         netpbm-pamtojpeg2k.patch
Patch14:         netpbm-manfix.patch
Patch15:         netpbm-jasper.patch
Patch16:         netpbm-libdir-so.patch
Patch17:         netpbm-c99.patch
Patch18:         netpbm-shlib-ldflags.patch

BuildRequires:   make
BuildRequires:   subversion
BuildRequires:   libjpeg-devel, libpng-devel, libtiff-devel, flex, gcc, jbigkit-devel
BuildRequires:   libX11-devel, perl-generators, python3, jasper-devel, libxml2-devel
BuildRequires:   perl(Config), perl(Cwd), perl(English), perl(Fcntl), perl(File::Basename)
BuildRequires:   perl(strict)
%if (0%{?fedora} && 0%{?fedora} < 28) || (0%{?rhel} || 0%{?rhel} <= 7) || (0%{?oreon} >= 11)
BuildRequires:   ghostscript-core
%else
BuildRequires:   ghostscript
%endif

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
_tar="netpbm-%{version}.tar.xz"
if test ! -f "$_tar"; then
  rm -rf netpbm-%{version}
  svn export --force https://svn.code.sf.net/p/netpbm/code/advanced netpbm-%{version}
  svn export --force https://svn.code.sf.net/p/netpbm/code/userguide netpbm-%{version}/userguide
  find netpbm-%{version} -name .svn -type d -prune -exec rm -rf {} +
  tar cJf "$_tar" netpbm-%{version}
  rm -rf netpbm-%{version}
fi
test "%{source0_hash}" = "none" || { f="$_tar"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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

# prepare man files
cd userguide
# BZ 948531
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

# Ugly hack to have libs in correct dir on 64bit archs.
mkdir -p %{buildroot}%{_libdir}
if [ "%{_lib}" != "lib" ]; then
  mv %{buildroot}%{_prefix}/lib/lib* %{buildroot}%{_libdir}
fi

cp -af lib/libnetpbm.a %{buildroot}%{_libdir}/libnetpbm.a

mkdir -p %{buildroot}%{_datadir}
mv userguide/man %{buildroot}%{_mandir}

# Get rid of the useless non-ascii character in pgmminkowski.1
sed -i 's/\xa0//' %{buildroot}%{_mandir}/man1/pgmminkowski.1

# Don't ship man pages for non-existent binaries and bogus ones
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

# Don't ship the static library
rm -f %{buildroot}%{_libdir}/lib*.a

# remove/symlink/substitute obsolete utilities
pushd %{buildroot}%{_bindir}
rm -f pgmtopbm pnmcomp
ln -s pamcomp pnmcomp
echo -e '#!/bin/sh\npamditherbw $@ | pamtopnm\n' > pgmtopbm
chmod 0755 pgmtopbm
popd

%ldconfig_scriptlets

%check
pushd test
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export PBM_TESTPREFIX=%{buildroot}%{_bindir}
export PBM_BINPREFIX=%{buildroot}%{_bindir}
./Execute-Tests && exit 0
popd

%files
%doc doc/copyright_summary doc/COPYRIGHT.PATENT doc/HISTORY README
%license doc/GPL_LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%dir %{_includedir}/netpbm
%{_includedir}/netpbm/*.h
%{_mandir}/man3/*
%{_libdir}/lib*.so

%files progs
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/netpbm/

%files doc
%doc userguide/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11.13.00-2
- Import
