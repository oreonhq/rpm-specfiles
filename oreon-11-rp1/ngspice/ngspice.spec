%global source0_hash ba8345f4c3774714c10f33d7da850d361cec7d14b3a295d0dc9fd96f7423812d

# Features in Fedora/Free Electronic Lab
#	What else does this build do aside compiling ngspice ?
#	- Ensures interoperability with xcircuit via Tcl
#	- Ensures interoperability with mot-adms
#	- Provides tclspice capabilities
# Chitlesh Goorah

%global	userelease	1
%global	usegitbare	0

%if 0%{?usegitbare} < 1
# force
%global	userelease	1
%endif

%global	majorver	45
%global	minorver	2
%global	docver	45
%undefine	prever
%global	prerpmver	%(echo "%{?prever}" | sed -e 's|-||g')

%global	baserelease	3

%if 0%{?usegitbare} >= 1
# pre-master-45
%global	gitcommit	1d0beb5e266420b1dd756913356a295ddb60fdce
%global	gitdate	20250830
%global	shortcommit	%(c=%{gitcommit}; echo ${c:0:7})

%global	tarballdate	20250831
%global	tarballtime	2034
%endif

%if	0%{?userelease} >= 1
%global	fedoraver		%{majorver}%{?minorver:.%minorver}
%endif
%if	0%{?usegitbare} >= 1
%global	fedoraver		%{majorver}%{?minorver:.%minorver}^%{gitdate}git%{shortcommit}
%endif

%global	use_gcc_strict_sanitize	0

%global	flagrel	%{nil}
%if		0%{?use_gcc_strict_sanitize} >= 1
%global	flagrel	%{flagrel}.san
%endif

%bcond_with	adms

%undefine       _changelog_trimtime

Name:			ngspice
Version:		%{fedoraver}
Release:		%{baserelease}%{?dist}%{flagrel}
Summary:		A mixed level/signal circuit simulator

# ngspice-42-manual.pdf	CC-BY-SA-4.0 AND BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:		LicenseRef-Callaway-BSD
URL:			http://ngspice.sourceforge.net

%if 0%{?userelease} >= 1
Source0:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{majorver}%{?minorver:.%minorver}/ngspice-%{majorver}%{?minorver:.%minorver}.tar.gz
%endif
%if 0%{?usegitbare} >= 1
Source0:       	ngspice-%{tarballdate}T%{tarballtime}.tar.gz
%endif
Source1:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{majorver}/ngspice-%{docver}-manual.pdf
%if %{with adms}
Source2:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{majorver}/ngspice-adms-va.7z
%endif
Source10:		create-ngspice-git-bare-tarball.sh

# Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or
# not (bug 1047056, debian bug 737279)
Patch0:		ngspice-37-blt-linkage-workaround.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gcc-c++
%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif
BuildRequires:	p7zip

BuildRequires:	readline-devel
BuildRequires:	libXext-devel
BuildRequires:	libpng-devel
BuildRequires:	libICE-devel
BuildRequires:	libXaw-devel
BuildRequires:	libGL-devel
BuildRequires:	libXt-devel
# From ngspice 32
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libXft-devel
BuildRequires:	libXrender-devel

BuildRequires:	fftw3-devel

BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex

BuildRequires:	ImageMagick
BuildRequires:	mot-adms

BuildRequires:	xorg-x11-server-Xvfb
BuildRequires:	git

Requires:	%{name}-codemodel%{?_isa} = %{version}-%{release}
Obsoletes:	ngspice-doc < 20-4.cvs20100619
Provides:	ngspice-doc = %{version}-%{release}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Ngspice is a general-purpose circuit simulator program.
It implements three classes of analysis:
- Nonlinear DC analyses
- Nonlinear Transient analyses
- Linear AC analyses

Ngspice implements the usual circuits elements, like resistors, capacitors,
inductors (single or mutual), transmission lines and a growing number of
semiconductor devices like diodes, bipolar transistors, mosfets (both bulk
and SOI), mesfets, jfet and HFET. Ngspice implements the EKV model but it
cannot be distributed with the package since its license does not allow to
redistribute EKV source code.

Ngspice integrates Xspice, a mixed-mode simulator built upon spice3c1 (and
then some tweak is necessary merge it with spice3f5). Xspice provides a
codemodel interface and an event-driven simulation algorithm. Users can
develop their own models for devices using the codemodel interface.

It can be used for VLSI simulations as well.

%package -n	tclspice
Summary:	Tcl/Tk interface for ngspice
BuildRequires:	pkgconfig(tk) <= 8.999
BuildRequires:	blt-devel

%description -n	tclspice
TclSpice is an improved version of Berkeley Spice designed to be used with
the Tcl/Tk scripting language. The project is based upon the NG-Spice source
code base with many improvements.

%package	codemodel
Summary:	ngspice codemodel and some script files

%description	codemodel
This package contains ngspice codemodel and some script files.

%package	-n libngspice
Summary:	Shared library version of ngspice
Requires:	%{name}-codemodel%{?_isa} = %{version}-%{release}

%description	-n libngspice
This package contains shared library version of ngspice.

%package	-n libngspice-devel
Summary:	Development files for libngspice
Requires:	libngspice%{?isa} = %{version}-%{release}

%description	-n libngspice-devel
This package contains libraries and header files for
developing applications that use libngspice.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?userelease} >= 1
%setup -q -n %{name}-%{majorver}%{?minorver:.%minorver}
git init
git config user.name "%{name} maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"
git add .
git commit -m "base" -q -a
%endif

%if 0%{?usegitbare} >= 1
%setup -q -c -n %{name}-%{majorver}%{?minorver:.%minorver}-%{gitdate}git%{shortcommit} -T -a 0
git clone ./%{name}.git/
cd %{name}
git config user.name "%{name} maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"

git checkout -b %{name}-%{majorver}-fedora %{gitcommit}
%endif

%if %{with adms}
pushd src/spicelib/devices/adms
%if 0%{?userelease} >= 1
7za x %{SOURCE2}
%endif
%if 0%{?usegitbare} >= 1
# Check if some adms va files exist
for f in \
	bsimbulk/admsva/bsimbulk.va \
	bsimcmg/admsva/bsimcmg.va \
	ekv/admsva/ekv.va \
	%{nil}
do
	test -f $f || exit 1
done
%endif

popd
%endif

%patch -P0 -p2 -b .link
git commit -m "Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or not" -a

# make sure the examples are UTF-8...
for nonUTF8 in \
	examples/tclspice/tcl-testbench4/selectfromlist.tcl \
	examples/tclspice/tcl-testbench1/testCapa.cir \
	examples/tclspice/tcl-testbench1/capa.cir \
	ChangeLog \
	%{nil}
do
	iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
	%{__mv} -f $nonUTF8.conv $nonUTF8
done
git commit -m "Change files to UTF8" -a

# rpmlint warnings
find examples/ -type f -name ".cvsignore" -exec rm -rf {} ';'
find src/ -type f -name "*.c" -exec chmod -x {} ';'
find src/ -type f -name "*.h" -exec chmod -x {} ';'
find src/ -type f -name "*.l" -exec chmod -x {} ';'
find src/ -type f -name "*.y" -exec chmod -x {} ';'
git commit -m "Fix permission" -a || :

# Move spinit directory to arch-dependent
sed -i configure.ac -e '\@AC_DEFINE_UNQUOTED.*NGSPICEDATADIR@s|echo .dprefix/share/ngspice|echo %{_libdir}/ngspice|'
sed -i configure.ac -e '\@AC_DEFINE_UNQUOTED.*NGSPICELIBDIR@s|echo .dprefix/share/ngspice|echo %{_libdir}/ngspice|'
sed -i src/misc/ivars.c -e 's|\(["/]\)share/ngspice|\1%_lib/ngspice|'
sed -i src/misc/ivars.c -e 's|\(["/]\)lib/ngspice|\1%_lib/ngspice|'
grep -rl "(pkgdatadir)/" . | xargs sed -i -e 's|(pkgdatadir)/|(pkglibdir)/|'
git commit -m "move spinit directory to arch-dependent" -a

# Fix Tclspice's examples
sed -i \
	's|load "../../../src/.libs/libspice.so"|lappend auto_path "%{_libdir}/tclspice"\npackage require spice|' \
	examples/tclspice/*/*.{tcl,sh}
sed -i \
	's|load ../../../src/.libs/libspice.so|lappend auto_path "%{_libdir}/tclspice"\npackage require spice|' \
	examples/tclspice/*/*.{tcl,sh}
sed -i \
	's|spice::codemodel [\./][\./]*src/xspice/icm/spice2poly/|spice::codemodel %{_libdir}/tclspice/ngspice/|' \
	examples/tclspice/tcl-testbench*/tcl-testbench*.sh
git commit -m "Fix Tclspice's examples" -a

# Fixed minor CVS build
sed -i \
	"s|AM_CPPFLAGS =|AM_CPPFLAGS = -I\$(top_srcdir)/src/maths/ni |" \
	src/spicelib/analysis/Makefile.am
git commit -m "Fix include path" -a

export ACLOCAL_FLAGS=-Im4
./autogen.sh \
%if %{with adms}
	--adms \
%endif
	%{nil}
git commit -m "Execute autogen" -a || :

chmod +x configure

%build
%set_build_flags
%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"

export ASAN_OPTIONS=detect_leaks=0
%endif

%if 0%{?usegitbare} >= 1
cd %{name}
%endif

# ---- Tclspice ----------------------------------------------------------------
# Adding BLT support
export CFLAGS="%{optflags} -I$(pkg-config --variable=includedir tcl)/blt"

# Make builddir for tclspice
%{__mkdir} -p tclspice
%{__cp} -Rl `ls . | grep -v tclspice` tclspice

# Configure tclspice
cd tclspice
sed -i configure* \
	-e 's|\#define NGSPICEDATADIR "\`echo %{_libdir}/ngspice\`"|\#define NGSPICEDATADIR "\`echo %{_libdir}/tclspice/ngspice\`"|'
sed -i src/misc/ivars.c -e 's|/%_libdir/ngspice|/%_lib/tclspice/ngspice|'

# direct access to Tcl_Interp->result deprecated in tcl8.6,
# remaining usage cannot be replaced by Tcl_SetResult
export CPPFLAGS=-DUSE_INTERP_RESULT

# comment by Mamoru TASAKA (20170330)
# Looking at the actually source code, --enable-newpred does not seem to
# make sense, and it seems to cause calculation error (bug 844100, bug 1429130)
#
# (20190120) Remove some obsolete or dangerous configure option
# by the request from the upstream
%configure \
	--disable-silent-rules \
%if %{with adms}
	--enable-adms \
%endif
	--enable-xspice \
	--enable-klu \
	--enable-osdi \
	--enable-maintainer-mode \
	--enable-dependency-tracking \
	--enable-cider \
%if 0
	--enable-newpred \
%endif
	--enable-openmp \
	--enable-predictor \
	--enable-shared \
	--with-readline=yes \
	--with-tcl=$(pkg-config --variable=libdir tcl) \
	--libdir=%{_libdir}/tclspice \
	%{nil}

%make_build -k
# Once install to the temp dir
rm -rf $(pwd)/../INST-TCLSPICE
%{__make} INSTALL="install -p" install DESTDIR=$(pwd)/../INST-TCLSPICE
cd ..
# ------------------------------------------------------------------------------

for opt in SHARED NOSHARED
do
	SHARED_OPT=""
	if test x$opt == xSHARED
	then
		SHARED_OPT="$SHARED_OPT --with-ngshared"
		# bug 1927628
		SHARED_OPT="$SHARED_OPT --with-readline=no"
	else
		SHARED_OPT="$SHARED_OPT --without-ngshared"
		SHARED_OPT="$SHARED_OPT --with-readline=yes"
	fi
%configure \
	--disable-silent-rules \
	${SHARED_OPT} \
%if %{with adms}
	--enable-adms \
%endif
	--enable-xspice \
	--enable-osdi \
	--enable-klu \
	--enable-maintainer-mode \
	--enable-dependency-tracking \
	--enable-cider \
%if 0
	# bug 844100, bug 1429130
	--enable-newpred \
%endif
	--enable-openmp \
	--enable-predictor \
	--enable-shared \
	--libdir=%{_libdir} \
	%{nil}

%{__make} clean
%make_build -k
# Once install to the temp dir
rm -rf $(pwd)/INST-NGSPICE-${opt}
%{__make} INSTALL="install -p" install DESTDIR=$(pwd)/INST-NGSPICE-${opt}
find $(pwd)/INST-NGSPICE-${opt} -type f | sort

done

%install
%if 0%{?usegitbare} >= 1
cp -p %{name}/COPYING .
cd %{name}
%endif

# ---- Tclspice ----------------------------------------------------------------

# Clean up unneeded / duplicate files also installed from ngspice
pushd INST-TCLSPICE
rm -rf ./%{_libdir}/ngspice/include/
# see bug 1311869
rm -f ./%{_libdir}/tclspice/ngspice/scripts/spinit
# binary differ
# for --short-circuit
if [ -f .%{_bindir}/cmpp ] ; then
  mv .%{_bindir}/cmpp{,-tclspice}
fi
popd

# Install
# ref: https://sourceforge.net/p/ngspice/support-requests/34/
# For codemodel files, install non-shared version
# so, first, install ngshared version, then non-shared version
for opt in SHARED NOSHARED
do
	cp -a INST-NGSPICE-${opt}/* %{buildroot}
done
cp -a INST-TCLSPICE/* %{buildroot}

%{__rm} -rf \
	%{buildroot}%{_libdir}/tclspice/libspice.la \
	%{buildroot}%{_libdir}/tclspice/libspicelite.la \
	%{buildroot}%{_libdir}/libngspice.la \
	%{buildroot}%{_includedir}/config.h \
	%{nil}
# ------------------------------------------------------------------------------

# ADMS support
# It seems that the below is not needed, compiled into binary already
# (mtasaka, 20160628)
%if 0
cp -pr ./src/spicelib/devices/adms/ %{buildroot}%{_libdir}/%{name}
%endif

# Ensuring that all docs are under %%{_pkgdocdir}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr examples/ %{buildroot}%{_pkgdocdir}
install -cpm 0644 %{SOURCE1} %{buildroot}%{_pkgdocdir}/%{name}-%{majorver}.pdf

cp -a \
	Stuarts_Poly_Notes \
	FAQ \
	DEVICES \
	ANALYSES \
	%{buildroot}%{_pkgdocdir}
cp -a \
	AUTHORS \
	README* \
	BUGS \
	ChangeLog \
	NEWS \
	%{buildroot}%{_pkgdocdir}

# pull as debuginfo
chmod +x %{buildroot}%{_libdir}/ngspice/*.cm
chmod +x %{buildroot}%{_libdir}/tclspice/ngspice/*.cm

%check
export ASAN_OPTIONS=detect_leaks=0

%if 0%{?usegitbare} >= 1
cd %{name}
%endif

pushd tests

# See https://sourceforge.net/p/ngspice/bugs/544/
rm -rf USERPROFILE
mkdir USERPROFILE
echo "set ngbehavior=mc" > USERPROFILE/spice.rc
export USERPROFILE=$(pwd)/USERPROFILE

xvfb-run \
	-s "-screen 0 640x480x24" \
	make check

popd

%files
%{_bindir}/*
%{_libdir}/%{name}/ivlng.*
%{_mandir}/man1/*
%doc	%{_pkgdocdir}
%license COPYING

%files	-n tclspice
%doc	%{_pkgdocdir}/examples/tclspice
%dir	%{_libdir}/tclspice/
%dir	%{_libdir}/tclspice/%{name}
%{_libdir}/tclspice/libspice*.so*
%{_libdir}/tclspice/%{name}/*.cm
%{_libdir}/tclspice/%{name}/*.tcl
%{_libdir}/tclspice/%{name}/ivlng.*
%{_libdir}/tclspice/%{name}/scripts/

%files	codemodel
%dir	%{_libdir}/%{name}/
%{_libdir}/%{name}/*.cm
%{_libdir}/%{name}/scripts/

%files	-n libngspice
%{_libdir}/libngspice.so.0*

%files	-n libngspice-devel
%{_libdir}/pkgconfig/ngspice.pc
%{_libdir}/libngspice.so
%{_includedir}/ngspice/

%changelog
%autochangelog
