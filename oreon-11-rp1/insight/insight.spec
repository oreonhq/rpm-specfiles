%global source0_hash none
%global ver		18.0.50
%global snap		20260306
%global gnulibsnap	20220501
%global enabled_target	aarch64-linux-gnu,powerpc-linux-gnu,riscv64-linux-gnu,s390-linux-gnu,x86_64-redhat-linux-gnu
%global	_python_bytecompile_extra	0
Name:		insight
Version:	%(echo %{ver} | tr - .)%{?snap:.%{snap}}
Release:        1%{?dist}
Summary:        Graphical debugger based on GDB
License:	GPL-3.0-or-later AND LicenseRef-Callaway-GPLv3+-with-exceptions AND GPL-2.0-or-later AND LicenseRef-Callaway-GPLv2+-with-exceptions AND GPL-1.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-GFDL
Url:		https://www.sourceware.org/insight/
Source0:        insight-%{version}.tar.xz
Source1:	insight.1
Requires:	iwidgets
Requires:	xterm
Provides:	bundled(binutils) = %{snap}
Provides:	bundled(gnulib) = %{gnulibsnap}
Provides:	bundled(libiberty) = %{snap}
Provides:	bundled(md5-gcc) = %{snap}
%ifarch %{ix86} x86_64
%global have_libipt	1
%endif
Patch1:		insight-18.0.50-relocate.patch
Patch2:		insight-18.0.50-libtool_tag.patch
Patch3:		insight-18.0.50-cve-2026-4647.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autogen
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libbabeltrace-devel
BuildRequires:  libstdc++
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-podlators
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  tcl8-devel
BuildRequires:  texinfo-tex
BuildRequires:  tk8-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
 Insight is a tight graphical user interface to GDB written in Tcl/Tk.
It provides a comprehensive interface that enables users to harness
most of GDB's power. It's also probably the only up-to-date UI for
the latest GDB version.

#-------------------------------------------------------------------------------
%prep 

#-------------------------------------------------------------------------------

%setup -q -n insight-%{version}

%patch 1 -p1 -b .relocate
%patch 2 -p1 -b .libtool_tag
%patch 3 -p1 -b .cve-2026-4647

#-------------------------------------------------------------------------------
%build

TOPDIR=`pwd`
autogen Makefile.def
autoreconf
for location in gdb/gdbtk/plugins libgui
do	(
		cd $location
		aclocal -I "${TOPDIR}/config"
		automake --add-missing
		autoconf
	)
done
touch gdb/doc/version.subst
. "%{_libdir}/tclConfig.sh"
. "%{_libdir}/tkConfig.sh"
[ '%{_lto_cflags}' != '' ] && %{_fix_broken_configure_for_lto}
CFLAGS="${RPM_OPT_FLAGS} -DDNF_DEBUGINFO_INSTALL"; export CFLAGS
CXXFLAGS="${RPM_OPT_FLAGS} -DDNF_DEBUGINFO_INSTALL"; export CXXFLAGS
LDFLAGS="${LDFLAGS:-%{?build_ldflags}}" ; export LDFLAGS
./configure	--prefix="%{_prefix}"					\
		--libdir="%{_libdir}"					\
		--enable-gdbtk						\
		--disable-binutils					\
		--disable-gdbserver					\
		--disable-elfcpp					\
		--disable-gas						\
		--disable-gold						\
		--disable-gprof						\
		--disable-gprofng					\
		--disable-ld						\
		--disable-rpath						\
		--disable-sim						\
		--disable-zlib						\
		--enable-gdb-build-warnings=,-Wno-unused,-Wno-deprecated-declarations,-Wno-nonnull-compare,-Wno-address,-Wno-stringop-overflow \
		--with-gdb-datadir='%{_datadir}/insight'		\
		--with-jit-reader-dir='%{_libdir}/insight'		\
		--with-separate-debug-dir='/usr/lib/debug'		\
		--with-system-readline					\
		--with-system-zlib					\
		--with-expat						\
		--with-python=%{__python3}				\
		--with-tclinclude="${TCL_SRC_DIR}"			\
		--with-tkinclude="${TK_SRC_DIR}"			\
		--enable-64-bit-bfd					\
		--with-babeltrace					\
		--without-guile						\
		--with-lzma						\
%if 0%{?have_libipt}
		--with-intel-pt						\
%else
		--without-intel-pt					\
%endif
%ifarch sparc sparcv9 sparc64
		--without-mmap						\
%endif
%ifarch %{arm}
		--disable-inprocess-agent				\
%else
		--enable-inprocess-agent				\
%endif
		--with-auto-load-dir='$debugdir:$datadir/auto-load'	\
		--with-auto-load-safe-path='$debugdir:$datadir/auto-load' \
		--enable-targets=%{enabled_target}			\
		%{_target_platform}
make %{?_smp_mflags}
%install
INSTALL="install -p"
make DESTDIR="${RPM_BUILD_ROOT}" INSTALL="${INSTALL}" install
(
	cd	"${RPM_BUILD_ROOT}"
	rm -f .%{_bindir}/gcore
	rm -f .%{_bindir}/gdb-add-index
	rm -f .%{_bindir}/gdb
	rm -f .%{_bindir}/gdbtui
	rm -f .%{_bindir}/gstack
	rm -rf .%{_includedir}
	rm -f .%{_libdir}/*.a
	rm -f .%{_libdir}/*.la
	rm -f .%{_libdir}/*.sh
	rm -f .%{_libdir}/libinproctrace.so
	rm -rf .%{_prefix}/man
	rm -rf .%{_datadir}/man
	rm -rf .%{_datadir}/info
	rm -rf .%{_datadir}/locale
	rm -rf .%{_datadir}/insight/system-gdbinit
	rm -rf .%{_datadir}/insight/guile
)
echo "pkg_mkIndex \"${RPM_BUILD_ROOT}%{_datadir}/insight/gui\"" | tclsh
mkdir -p "${RPM_BUILD_ROOT}%{_datadir}/insight/auto-load"
rpm -ql libstdc++ | grep "^%{_datadir}/gdb/auto-load" | while read T
do	F="${RPM_BUILD_ROOT}%{_datadir}/insight/${T#%{_datadir}/gdb/}"
	if [[ "${F}/" =~ '/__pycache__/' ]]
	then	: # Do not copy cache.
	elif [ -e "${F}" ]
	then	: # Already exists: ignore.
	elif [ -d "${T}" ]
	then	mkdir -p "${F}"
	else	if [ -h "${T}" ]
		then	D=`dirname "${T}"`
			LINK=`realpath --relative-base="${D}" "${T}"`
			if [[ "${LINK}" =~ '^/' ]]
			then	T="${LINK}"
			else	T=`realpath --relative-base="${D}" "${T}"`
			fi
		fi
		ln -s "${T}" "${F}"
	fi
done
${INSTALL} -m 755 -d "${RPM_BUILD_ROOT}%{_mandir}/man1"
${INSTALL} -m 644 -p "%{SOURCE1}" "${RPM_BUILD_ROOT}%{_mandir}/man1/"
${INSTALL} -m 755 -d "${RPM_BUILD_ROOT}%{_datadir}/applications"
desktop-file-install							\
	--dir		"${RPM_BUILD_ROOT}%{_datadir}/applications"	\
	gdb/gdbtk/insight.desktop
${INSTALL} -m 755 -d "${RPM_BUILD_ROOT}%{_datadir}/pixmaps"
${INSTALL} -m 644 gdb/gdbtk/insight_icon.svg				\
	"${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.svg"
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/insight/python/gdb
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
