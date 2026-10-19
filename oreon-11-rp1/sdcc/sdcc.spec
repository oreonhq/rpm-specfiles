%global source0_hash 5fd6a93e5997ce01756868fe35e441095cfb637894a80c262514a634094973b6
Name:           sdcc
Version:        4.6.0
Release:        1%{?dist}
Summary:        Small Device C Compiler
License:        GPL-2.0-or-later
URL:            http://sdcc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sdcc/sdcc-src-%{version}.tar.bz2
Source1:        README.fedora
Source2:        sdcc-%{version}-lyx-preferences
Source3:        sdcc-%{version}-libierty-acinclude.m4
Source4:	sdcc-%{version}-libcpp-aclocal.m4
Source5:        sdcc-%{version}-libbacktrace.patch
Patch1:         sdcc-%{version}-python3.patch
Patch2:         sdcc-%{version}-pic16-glue.patch
Patch3:		sdcc-%{version}-aslink.patch
Patch4:		sdcc-%{version}-bool.patch
Provides:       bundled(libiberty)
Requires:       emacs-filesystem
Obsoletes:      emacs-sdcc <= 3.6.0
# oreon:deps
BuildRequires:  /usr/bin/python3
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gdb-headless
BuildRequires:  ghostscript
BuildRequires:  gputils
BuildRequires:  inkscape
BuildRequires:  latex2html
BuildRequires:  libtool
BuildRequires:  lyx
BuildRequires:  make
BuildRequires:  tex(ulem.sty)
BuildRequires:  tex-preview
BuildRequires:  texinfo
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-footnotehyper
BuildRequires:  texlive-xetex
BuildRequires:  zlib-devel
# /oreon:deps
%description
SDCC is a C compiler for 8051 class and similar microcontrollers.
The package includes the compiler, assemblers and linkers, a device
simulator and a core library. The processors supported (to a varying
degree) include the 8051, ds390, z80, hc08, and PIC.

%package libc-sources
Summary:        Small Device C Compiler
License:        GPL-2.0-or-later
Requires:       sdcc = %{version}-%{release}
%description libc-sources
SDCC is a C compiler for 8051 class and similar microcontrollers.
This package includes the sources for the C library, and is only necessary
if you want to modify the C library or as reference of how it works.

%prep

%setup -q -n sdcc-%{version}
find . -regex '.*.\.[ch]*$' -executable -a -exec chmod a-x '{}' \;
%patch 1 -p1
%patch 2 -p0
%patch 3 -p1
%patch 4 -p1
# Disable brp-strip-static-archive for now because it errors trying to
# strip foreign binaries.
echo '%{__os_install_post}'
%global __os_install_post %(echo '%{__os_install_post}' | 
        sed -e 's#/usr/lib/rpm.*/brp-strip-static-archive .*##g' |
        sed -e 's#/usr/lib/rpm.*/brp-strip-lto .*##g')

%build

OPTS='PDFOPT="/bin/cp"'
AUTO_VER=`autoconf -V | sed -n "s/.[^0-9]*\(2\.[0-9]*\)$/\1/"p`
TAR_VER=2.69
cd support/cpp
sed -i -e /${TAR_VER}/s/${TAR_VER}/${AUTO_VER}/ config/override.m4 
autoconf
cd ../sdbinutils
sed -i -e /${TAR_VER}/s/${TAR_VER}/${AUTO_VER}/ config/override.m4 
autoconf
cd libiberty
cp %SOURCE3  ./acinclude.m4
sed -i -e '/AC_CONFIG_AUX_DIR/s/$libiberty_topdir/"..\/"/' configure.ac
autoconf
cd ../bfd
sed -i -e /${TAR_VER}/s/${TAR_VER}/${AUTO_VER}/ aclocal.m4
sed -i -e /bfd64.m4/d aclocal.m4
sed -i -e /jobserver.m4/d aclocal.m4
sed -i -e /GNU_MAKE_JOBSERVER/d configure.ac
autoconf
cd ../binutils
sed -i -e /${TAR_VER}/s/${TAR_VER}/${AUTO_VER}/ aclocal.m4
sed -i -e '/jobserver.m4\|pkg.m4/d' aclocal.m4
sed -i -e '/GNU_MAKE_JOBSERVER\|jobserver.m4\|debuginfod.m4\|AC_DEBUGINFOD/d' configure.ac
autoconf
cd ../..
cd cpp/gcc
autoconf
cd ../libcpp
cp %SOURCE4  ./aclocal.m4
autoconf
cd ../libbacktrace
cp %SOURCE4  ./aclocal.m4
patch  -p0 <%SOURCE5
cd ../../..
%configure --enable-doc --disable-non-free  STRIP=: ${OPTS} PYTHON=python3
mkdir -p ~/.lyx
cp %SOURCE2  ~/.lyx/preferences
%{__make} Q= QUIET=
%install
make install DESTDIR=$RPM_BUILD_ROOT Q=
mv $RPM_BUILD_ROOT%{_datadir}/doc installed-docs
install -m 644 %SOURCE1 installed-docs
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/%{name}
mv $RPM_BUILD_ROOT%{_bindir}/*.el $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/%{name}
find $RPM_BUILD_ROOT -type f -name \*.c -exec chmod a-x '{}' \;
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/sdcc
mv $RPM_BUILD_ROOT%{_bindir}/* $RPM_BUILD_ROOT%{_libexecdir}/sdcc
pushd $RPM_BUILD_ROOT%{_bindir}
for x in ../libexec/sdcc/*; do
fname=$(basename $x)
if [ $fname = 'sdcc' ]; then
cc1Path=`find ../libexec -name cc1 | sed -n -e 's/\.\.\(.*\)\/cc1/\/usr\1/p'`
echo "#!/usr/bin/sh
PATH=/usr/libexec/sdcc:$cc1Path:\$PATH
/usr/libexec/%{name}/$fname \"\$@\"" > %{name}-$fname
else
echo "#!/usr/bin/sh
PATH=/usr/libexec/sdcc:\$PATH
/usr/libexec/%{name}/$fname \"\$@\"" > %{name}-$fname
fi
chmod 755 %{name}-$fname
done
popd
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/src/pic16
find . -type f -name '*.a' -exec chmod 664 '{}' \;
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sdcc-libc-sources -f %{oreon_filedir}/sdcc-libc-sources.list

%changelog

%autochangelog
