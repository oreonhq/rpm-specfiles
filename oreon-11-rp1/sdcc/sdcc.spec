%global source0_hash none

Name:           sdcc
Version:        4.4.0
Release:        5%{?dist}
Summary:        Small Device C Compiler
# Automatically converted from old format: GPLv2+ - review is highly recommended.
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

BuildRequires: make
BuildRequires:  bison, gcc-c++, automake, libtool
BuildRequires:  boost-devel zlib-devel
BuildRequires:  flex
Buildrequires:  gputils
BuildRequires:  lyx inkscape ghostscript
BuildRequires:  latex2html
BuildRequires:  tex(ulem.sty) tex-preview
BuildRequires:  texinfo texlive-xetex texlive-footnotehyper texlive-epstopdf
# Work around to lyx-common missing R: /usr/bin/python
BuildRequires:  /usr/bin/python3 gdb-headless
Provides:       bundled(libiberty)
Requires:       emacs-filesystem
Obsoletes:      emacs-sdcc <= 3.6.0

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
# Preset PDFOPT to /bin/cp
OPTS='PDFOPT="/bin/cp"'

# The following is to get configure.ac files to work with current autoconf
AUTO_VER=`autoconf -V | sed -n "s/.[^0-9]*\(2\.[0-9]*\)$/\1/"p`
TAR_VER=2.69
cd support/cpp
sed -i -e /${TAR_VER}/s/${TAR_VER}/${AUTO_VER}/ config/override.m4 
autoconf
cd ../sdbinutils
sed -i -e /${TAR_VER}/s/${TAR_VER}/${AUTO_VER}/ config/override.m4 
autoconf
cd libiberty
# autoupdate does not properly convert configure.ac
#this is a fudge as $libiberty_topdir not now defined when AC_CONFIG_AUX_DIR is used
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
#autoconf
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

# Create launch scripts in _bindir
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

%files
%doc installed-docs/*
%{_bindir}/*
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/emacs/site-lisp/%{name}/*.el
%{_mandir}/*/*
%exclude %{_datadir}/%{name}/lib/src
# Don't include support files as already in binutils-devel
%exclude %{_includedir}/
%exclude %{_libdir}/
%exclude %{_infodir}/

%files libc-sources
%{_datadir}/%{name}/lib/src

%changelog
%autochangelog
