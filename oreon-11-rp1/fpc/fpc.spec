%global source0_hash none

# Workaround LTO related issue when stripping the target files
# See related issue for cross-gcc: #1863378
%global __brp_strip_lto %{nil}

Name:           fpc
Summary:        Free Pascal Compiler
License:        GPL-2.0-or-later AND LGPL-2.1-or-later WITH Independent-modules-exception
URL:            http://www.freepascal.org/

%global version_code 3.2.3

%global beta 1
%global version_beta 3.2.4
%global version_suffix rc1

%if ! 0%{?beta}
Version:        %{version_code}
%else
Version:        %{version_beta}~%{version_suffix}
%endif
Release:        3%{?dist}

%if ! 0%{?beta}
  %global archive_type dist
  %global archive_suffix %{version_code}
%else
  %global archive_type beta
  %global archive_suffix %{version_beta}-%{version_suffix}
%endif
Source0:        https://downloads.freepascal.org/fpc/%{archive_type}/%{archive_suffix}/source/fpcbuild-%{archive_suffix}.tar.gz

# Bootstrap the compiler for a new architecture. Set this to 0 after we've bootstrapped.
%global bootstrap 0

# This is only needed when we're bootstrapping.
# But it's not in an 'if defined' block, since the file has to be included in the srpm
# Thus you should enable this line when we're bootstrapping for any target
#
# Last used for aaarch64 and ppc64le bootstrap.
# For the aarch64 bootstrap, a compiler has been used that has been cross-compiled on a x86_64 system using:
#   make all CPU_TARGET=aarch64 OS_TARGET=linux BINUTILSPREFIX=aarch64-linux-gnu-
# For the ppc64 boostrap, a compiler has been used that has been cross-compiled on a x86_64 system using:
#   make all CPU_TARGET=powerpc64 OS_TARGET=linux BINUTILSPREFIX=powerpc64le-linux-gnu- CROSSOPT="-Cb- -Caelfv2"
#
# in the main directory of fpc-r44016. The compilers were then copied using:
#   cp compiler/ppca64    ~/fpc-3.2.0-bin/ppca64-3.2.0-bootstrap
#   cp compiler/ppcppc64  ~/fpc-3.2.0-bin/ppcppc64-3.2.0-bootstrap
# The zip file was then created using:
#   zip -9 fpc-3.2.0-bin.zip -r fpc-3.2.0-bin/
#
# Source100:	https://suve.fedorapeople.org/fpc-3.2.0-bin--patch0.zip

# Configuration templates:
Source10:        fpc.cft
Source11:        fppkg.cfg
Source12:        default.cft

# On Fedora we do not want stabs debug-information. (even on 32 bit platforms)
# https://bugzilla.redhat.com/show_bug.cgi?id=1475223 
Patch0:         fpc-3.2.0--dwarf-debug.patch

# Allow for reproducible builds
# https://bugzilla.redhat.com/show_bug.cgi?id=1778875
Patch1:         fpc-3.2.0--honor_SOURCE_DATE_EPOCH_in_date.patch

# The "pas2jni" util program shipped with FPC uses threads,
# but is compiled without thread support and fails to actually do anything useful when run.
# Submitted upstream: https://gitlab.com/freepascal.org/fpc/source/-/merge_requests/185
Patch5:         fpc-3.2.2--pas2jni-cthreads.patch

# By default, the textmode IDE installs some data files (templates, ASCII art)
# in the same directory as the executable (i.e. /usr/bin). This patch moves
# the data files inside the main FPC install directory (LIBDIR/fpc/VERSION/ide).
Patch6:         fpc-3.2.2--fix-IDE-data-files-locations.patch

# "man 5 resolv.conf" states that, should the file be missing or empty,
# then C stdlib functions dealing with name resolution should fall back
# to querying the DNS server running on the local machine.
#
# FPC, by default, does not link to libc, providing its own standard library;
# said code does not contain this fallback logic.
#
# Backport of upstream commit:
# https://gitlab.com/freepascal.org/fpc/source/-/commit/1cd1415df746ecaf9603bb0afb8660d3af3ea1f1
Patch8:         fpc-3.2.2--fallback-to-localhost-when-no-dns-server-specified.patch

# The compiler produces incorrect "unit unused" hints
# if symbols from a unit are used only for compile-time checks.
#
# Backport of upstream commits:
# https://gitlab.com/freepascal.org/fpc/source/-/commit/22ec4a20332f8208273604b46e727e481f6502eb.patch
# https://gitlab.com/freepascal.org/fpc/source/-/commit/397293f09f7a3e116119ab629687c64aae507539.patch
Patch9:         fpc-3.2.2--compiletime-check-is-usage.patch

# When building pas2js on i386 and ppc64le, fpc generates an executable with text relocations.
# Since binutils-2.45.50-15.fc44, this is rejected by default
# and requires passing some linker flags to explicitly allow it.
#
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2428281
Patch10:        fpc-3.2.4--pas2js-relocation.patch

# FPC uses its own architecture names that do not align with the ones used by Fedora.
%global arm_ppc ppcarm
%global arm_ppcross ppcrossarm
%global arm_arch arm
%global arm_opts -dFPC_ARMHF

%global aarch64_ppc ppca64
%global aarch64_ppcross ppcrossa64
%global aarch64_arch aarch64
%global aarch64_opts %{nil}

%global ppc64le_ppc ppcppc64
%global ppc64le_ppcross ppcrossppc64
%global ppc64le_arch powerpc64
%global ppc64le_opts -Cb- -Caelfv2

%global i386_ppc ppc386
%global i386_ppcross ppcross386
%global i386_arch i386
%global i386_opts %{nil}

%global x86_64_ppc ppcx64
%global x86_64_ppcross ppcrossx64
%global x86_64_arch x86_64
%global x86_64_opts %{nil}

ExclusiveArch: aarch64 %{ix86} x86_64 ppc64le

%ifarch aarch64
  %global native_ppc %{aarch64_ppc}
  %global native_arch %{aarch64_arch}
  %global native_opts %{aarch64_opts}
%else
  %ifarch %{ix86}
    %global native_ppc %{i386_ppc}
    %global native_arch %{i386_arch}
    %global native_opts %{i386_opts}
  %else
    %ifarch ppc64 ppc64le
      %global native_ppc %{ppc64le_ppc}
      %global native_arch %{ppc64le_arch}
      %global native_opts %{ppc64le_opts}
    %else
      %ifarch x86_64
        %global native_ppc %{x86_64_ppc}
        %global native_arch %{x86_64_arch}
        %global native_opts %{x86_64_opts}
      %else
        # Unsupported host arch. Not using %%{error} here because
        # SRPM rebuilds do not care about ExclusiveArch.
      %endif
    %endif
  %endif
%endif

# Helper macro to reduce amount of typing
%global units_native units-%{native_arch}-linux

Requires:       binutils
Requires:       %{name}-%{units_native}%{?_isa} = %{version}-%{release}

%if ! 0%{?bootstrap}
BuildRequires:  fpc
%endif

# Not strictly needed, apart from finding out the path to libgcc
BuildRequires:  gcc

BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(imakeidx.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(tex)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(utf8x.def)
BuildRequires:  texlive-collection-fontsrecommended

# Cross-compiling for i386 is currently supported only on x86_64,
# as it requires support for 80-bit floating point numbers,
# and there's no softfloat80 implementation in the compiler.
%ifarch x86_64
%global cross_i386 1
%endif

# Cross-compiling for x86_64 is currently supported only on i686.
# Same 80-bit float issue as above.
%ifarch %{ix86}
%global cross_x86_64 1
%endif

%ifnarch %{arm}
%global cross_arm 1
%endif

%ifnarch aarch64
%global cross_aarch64 1
%endif

%ifnarch ppc64le
%global cross_ppc64le 1
%endif

%ifarch %{ix86}
%global cross_win32 1
%else
%global cross_win32 0%{?cross_i386}
%endif

%ifarch x86_64
%global cross_win64 1
%else
%global cross_win64 0%{?cross_x86_64}
%endif

%description
Free Pascal is a free 32/64bit Pascal Compiler. It comes with a run-time
library and is fully compatible with Turbo Pascal 7.0 and nearly Delphi
compatible. Some extensions are added to the language, like function
overloading and generics. Shared libraries can be linked. This package
contains the command-line compiler and utilities.

# -- Native units

%package %{units_native}
Summary: Free Pascal Compiler - units for %{native_arch}-linux
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{units_native}
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (%{native_arch} processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).

# -- Cross-compilers

%if 0%{?cross_arm}
%package cross-arm
Summary: Free Pascal Compiler - arm cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-arm-linux%{?_isa} = %{version}-%{release}

Requires: binutils-arm-linux-gnu
BuildRequires: binutils-arm-linux-gnu

%description cross-arm
This package provides a cross-compiler for building Free Pascal applications
for the arm processor architecture.

%package units-arm-linux
Summary: Free Pascal Compiler - units for arm-linux
Requires: %{name}-cross-arm%{?_isa} = %{version}-%{release}

%description units-arm-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (arm processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_aarch64}
%package cross-aarch64
Summary: Free Pascal Compiler - aarch64 cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-aarch64-linux%{?_isa} = %{version}-%{release}

Requires: binutils-aarch64-linux-gnu
BuildRequires: binutils-aarch64-linux-gnu

%description cross-aarch64
This package provides a cross-compiler for building Free Pascal applications
for the aarch64 processor architecture.

%package units-aarch64-linux
Summary: Free Pascal Compiler - units for aarch64-linux
Requires: %{name}-cross-aarch64%{?_isa} = %{version}-%{release}

%description units-aarch64-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (aarch64 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_i386}
%package cross-i386
Summary: Free Pascal Compiler - i386 cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-i386-linux%{?_isa} = %{version}-%{release}

Requires: binutils-x86_64-linux-gnu
BuildRequires: binutils-x86_64-linux-gnu

%description cross-i386
This package provides a cross-compiler for building Free Pascal applications
for the i386 processor architecture.

%package units-i386-linux
Summary: Free Pascal Compiler - units for i386-linux
Requires: %{name}-cross-i386%{?_isa} = %{version}-%{release}

%description units-i386-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (i386 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_ppc64le}
%package cross-powerpc64
Summary: Free Pascal Compiler - powerpc64 cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-powerpc64-linux%{?_isa} = %{version}-%{release}

Requires: binutils-powerpc64le-linux-gnu
BuildRequires: binutils-powerpc64le-linux-gnu

%description cross-powerpc64
This package provides a cross-compiler for building Free Pascal applications
for the powerpc64 processor architecture.

%package units-powerpc64-linux
Summary: Free Pascal Compiler - units for powerpc64-linux
Requires: %{name}-cross-powerpc64%{?_isa} = %{version}-%{release}

%description units-powerpc64-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (powerpc64 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_x86_64}
%package cross-x86_64
Summary: Free Pascal Compiler - x86_64 cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-x86_64-linux%{?_isa} = %{version}-%{release}

Requires: binutils-x86_64-linux-gnu
BuildRequires: binutils-x86_64-linux-gnu

%description cross-x86_64
This package provides a cross-compiler for building Free Pascal applications
for the x86_64 processor architecture.

%package units-x86_64-linux
Summary: Free Pascal Compiler - units for x86_64-linux
Requires: %{name}-cross-x86_64%{?_isa} = %{version}-%{release}

%description units-x86_64-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (x86_64 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

# -- MS Windows units

%if 0%{?cross_win32}
%package units-i386-win32
Summary: Free Pascal Compiler - units for i386-win32
%ifarch %{ix86}
Requires: %{name}%{?_isa} = %{version}-%{release}
%else
Requires: %{name}-cross-i386%{?_isa} = %{version}-%{release}
%endif

%description units-i386-win32
This package provides pre-compiled unit files for developing Free Pascal
applications for MS Windows (i386 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_win64}
%package units-x86_64-win64
Summary: Free Pascal Compiler - units for x86_64-win64
%ifarch x86_64
Requires: %{name}%{?_isa} = %{version}-%{release}
%else
Requires: %{name}-cross-x86_64%{?_isa} = %{version}-%{release}
%endif

%description units-x86_64-win64
This package provides pre-compiled unit files for developing Free Pascal
applications for MS Windows (x86_64 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

# -- Other sub-packages

%package ide
Summary: Free Pascal Compiler - terminal-based IDE
Requires: %{name}-%{units_native}%{?_isa} = %{version}-%{release}
Requires: gpm
Requires: ncurses

%description ide
The fpc-ide package provides "fp", the official terminal-based IDE
for the Free Pascal Compiler.

%package doc
Summary: Free Pascal Compiler - documentation and examples

%description doc
The fpc-doc package contains the documentation (in pdf format) and examples
of Free Pascal.

%package src
Summary:   Free Pascal Compiler - sources
BuildArch: noarch

%description src
The fpc-src package contains the sources of Free Pascal, for documentation or
automatical-code generation purposes.

%global smart _smart
%global fpmakeopt %{?_smp_build_ncpus:--threads=%{_smp_build_ncpus}}
%global fpcopt -gl -gw -k--build-id

%prep
%autosetup -p1 -n fpcbuild-%{archive_suffix}

%if 0%{?bootstrap}
unzip %{SOURCE100}
%endif

%build
# The source-files:
mkdir -p fpc_src
cp -a fpcsrc/rtl fpc_src
cp -a fpcsrc/packages fpc_src

# Remove some unused units
rm -rf fpc_src/packages/amunits/    # Amiga (Motorola 64k CPU)
rm -rf fpc_src/packages/arosunits/  # AROS
rm -rf fpc_src/packages/morphunits/ # MorphOS
rm -rf fpc_src/packages/os2units/   # OS/2
rm -rf fpc_src/packages/os4units/   # Amiga OS4
rm -rf fpc_src/packages/palmunits/  # PalmOS
rm -rf fpc_src/packages/tosunits/   # Atari TOS/GEM
rm -rf fpc_src/packages/winceunits/ # MS Windows CE

%if 0%{?bootstrap}
STARTPP=$(pwd)/fpc-%{version_code}-bin/%{native_ppc}-%{version_code}-bootstrap
%else
STARTPP=%{native_ppc}
%endif

function build_fpcross() {
	TARGET_ARCH="$1"
	TARGET_OPTS="$2"
	TARGET_BINUTILS="$3"

	make compiler_cycle \
		FPC=${NEWPP} OPT='%{fpcopt}' FPMAKEOPT='%{fpmakeopt}' NoNativeBinaries=1 \
		CROSSOPT="${TARGET_OPTS}" CPU_TARGET="${TARGET_ARCH}" BINUTILSPREFIX="${TARGET_BINUTILS}"
}

function build_units() {
	TARGET_ARCH="$1"
	TARGET_OPTS="$2"
	TARGET_BINUTILS="$3"
	TARGET_PPCROSS="$4"
	TARGET_SYSTEM="$5"

	# No -j here as it has no effect. Parallel compilation is controlled via FPMAKEOPT
	if [[ "${TARGET_ARCH}" == "%{native_arch}" ]]; then
		make rtl%{smart} \
			FPC=${NEWPP} OPT="%{fpcopt} ${TARGET_OPTS}" FPMAKEOPT='%{fpmakeopt}' OS_TARGET="${TARGET_SYSTEM}"
		make packages%{smart} \
			FPC=${NEWPP} OPT="%{fpcopt} ${TARGET_OPTS}" FPMAKEOPT='%{fpmakeopt} --NoIDE=1' OS_TARGET="${TARGET_SYSTEM}"
	else
		TARGET_PPCROSS="$(pwd)/compiler/${TARGET_PPCROSS}"
		make rtl%{smart} \
			FPC="${TARGET_PPCROSS}" OPT='%{fpcopt}' FPMAKEOPT='%{fpmakeopt}' \
			CROSSOPT="${TARGET_OPTS}" CPU_TARGET="${TARGET_ARCH}" OS_TARGET="${TARGET_SYSTEM}" BINUTILSPREFIX="${TARGET_BINUTILS}"
		make packages%{smart} \
			FPC="${TARGET_PPCROSS}" OPT='%{fpcopt}' FPMAKEOPT='%{fpmakeopt} --NoIDE=1' \
			CROSSOPT="${TARGET_OPTS}" CPU_TARGET="${TARGET_ARCH}" OS_TARGET="${TARGET_SYSTEM}" BINUTILSPREFIX="${TARGET_BINUTILS}"
	fi
}

NEWPP=$(pwd)/fpcsrc/compiler/%{native_ppc}
DATA2INC=$(pwd)/fpcsrc/utils/data2inc

# -- Native compiler & units

pushd fpcsrc
make compiler_cycle FPC=${STARTPP} OPT='%{fpcopt} %{native_opts}'

# Clean the run-time library files to force a rebuild with the new compiler
make rtl_clean

make rtl%{smart}      FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}'
make packages%{smart} FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}'
make utils_all        FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}' DATA2INC=${DATA2INC}
popd

# -- Cross-compilers

# ! DIRTY HACK !
# Building units for non-Linux OSes in the same directory as the native ones
# seems to mess up the build process somehow, causing rpmbuild to reject
# the resulting packages due to missing build-ids.
#
# Create a copy of the fpcsrc directory (containing compiler sources,
# but also the native compiler we've just built) and perform all work
# related to cross-compilation inside this copy.
cp -a fpcsrc fpcsrc-cross
pushd fpcsrc-cross

%if 0%{?cross_arm}
	build_fpcross '%{arm_arch}' '%{arm_opts}' 'arm-linux-gnu-'
	build_units   '%{arm_arch}' '%{arm_opts}' 'arm-linux-gnu-' '%{arm_ppcross}' linux
%endif
%if 0%{?cross_aarch64}
	build_fpcross '%{aarch64_arch}' '%{aarch64_opts}' 'aarch64-linux-gnu-'
	build_units   '%{aarch64_arch}' '%{aarch64_opts}' 'aarch64-linux-gnu-' '%{aarch64_ppcross}' linux
%endif
%if 0%{?cross_i386}
	build_fpcross '%{i386_arch}' '%{i386_opts}' 'x86_64-linux-gnu-'
	build_units   '%{i386_arch}' '%{i386_opts}' 'x86_64-linux-gnu-' '%{i386_ppcross}' linux
%endif
%if 0%{?cross_ppc64le}
	build_fpcross '%{ppc64le_arch}' '%{ppc64le_opts}' 'powerpc64le-linux-gnu-'
	build_units   '%{ppc64le_arch}' '%{ppc64le_opts}' 'powerpc64le-linux-gnu-' '%{ppc64le_ppcross}' linux
%endif
%if 0%{?cross_x86_64}
	build_fpcross '%{x86_64_arch}' '%{x86_64_opts}' 'x86_64-linux-gnu-'
	build_units   '%{x86_64_arch}' '%{x86_64_opts}' 'x86_64-linux-gnu-' '%{x86_64_ppcross}' linux
%endif

%if 0%{?cross_win32}
	build_units '%{i386_arch}' '%{i386_opts}' 'x86_64-linux-gnu-' '%{i386_ppcross}' win32
%endif
%if 0%{?cross_win64}
	build_units '%{x86_64_arch}' '%{x86_64_opts}' 'x86_64-linux-gnu-' '%{x86_64_ppcross}' win64
%endif

popd

# -- Documentation

# Output is redirected to /dev/null as building the PDFs produces a gargantuan
# number of warnings, bloating persistent logs and making local development
# tedious due exceeding terminal scrollback buffers.
#
# FIXME: -j1 as there is a race - seen on "missing" `rtl.xct'.
make -j1 -C fpcdocs pdf FPC=${NEWPP} >/dev/null 2>/dev/null

%install
NEWPP="$(pwd)/fpcsrc/compiler/%{native_ppc}"
NEWFPCMAKE="$(pwd)/fpcsrc/utils/fpcm/bin/%{native_arch}-linux/fpcmake"
INSTALLOPTS="-j1 FPC=${NEWPP} FPCMAKE=${NEWFPCMAKE} \
                INSTALL_PREFIX=%{buildroot}%{_prefix} \
                INSTALL_LIBDIR=%{buildroot}%{_libdir} \
                INSTALL_BASEDIR=%{buildroot}%{_libdir}/%{name}/%{version_code} \
                CODPATH=%{buildroot}%{_libdir}/%{name}/lexyacc \
                INSTALL_DOCDIR=%{buildroot}%{_defaultdocdir}/%{name} \
                INSTALL_BINDIR=%{buildroot}%{_bindir}
                INSTALL_EXAMPLEDIR=%{buildroot}%{_defaultdocdir}/%{name}/examples"

function install_compiler() {
	TARGET_ARCH="$1"
	TARGET_COMPILER="$2"

	if [[ "${TARGET_ARCH}" == "%{native_arch}" ]]; then
		make compiler_distinstall ${INSTALLOPTS}
	else
		make compiler_distinstall CROSSINSTALL=1 CPU_TARGET="${TARGET_ARCH}" ${INSTALLOPTS}
	fi

	ln -srf "%{buildroot}/%{_libdir}/%{name}/%{version_code}/${TARGET_COMPILER}" "%{buildroot}%{_bindir}/${TARGET_COMPILER}"
}

function install_units() {
	TARGET_ARCH="$1"
	TARGET_SYSTEM="$2"

	if [[ "${TARGET_ARCH}" == "%{native_arch}" ]]; then
		make rtl_distinstall      OS_TARGET="${TARGET_SYSTEM}" ${INSTALLOPTS}
		make packages_distinstall OS_TARGET="${TARGET_SYSTEM}" ${INSTALLOPTS} FPMAKEOPT='--NoIDE=1'
	else
		make rtl_distinstall      CROSSINSTALL=1 CPU_TARGET="${TARGET_ARCH}" OS_TARGET="${TARGET_SYSTEM}" ${INSTALLOPTS}
		make packages_distinstall CROSSINSTALL=1 CPU_TARGET="${TARGET_ARCH}" OS_TARGET="${TARGET_SYSTEM}" ${INSTALLOPTS} FPMAKEOPT='--NoIDE=1'
	fi
}

# -- Native compiler

pushd fpcsrc
install_compiler '%{native_arch}' '%{native_ppc}'
make rtl_distinstall      ${INSTALLOPTS}
make packages_distinstall ${INSTALLOPTS}
make utils_distinstall    ${INSTALLOPTS}
popd

# -- Cross-compilers

pushd fpcsrc-cross

%if 0%{?cross_arm}
	install_compiler '%{arm_arch}' '%{arm_ppcross}'
	install_units    '%{arm_arch}' linux
%endif
%if 0%{?cross_aarch64}
	install_compiler '%{aarch64_arch}' '%{aarch64_ppcross}'
	install_units    '%{aarch64_arch}' linux
%endif
%if 0%{?cross_i386}
	install_compiler '%{i386_arch}' '%{i386_ppcross}'
	install_units    '%{i386_arch}' linux
%endif
%if 0%{?cross_ppc64le}
	install_compiler '%{ppc64le_arch}' '%{ppc64le_ppcross}'
	install_units    '%{ppc64le_arch}' linux
%endif
%if 0%{?cross_x86_64}
	install_compiler '%{x86_64_arch}' '%{x86_64_ppcross}'
	install_units    '%{x86_64_arch}' linux
%endif

%if 0%{?cross_win32}
	install_units '%{i386_arch}' win32
%endif
%if 0%{?cross_win64}
	install_units '%{x86_64_arch}' win64
%endif

popd

# -- Other

pushd install
make -C doc ${INSTALLOPTS}
make -C man ${INSTALLOPTS} INSTALL_MANDIR=%{buildroot}%{_mandir}
popd

make -C fpcdocs pdfinstall ${INSTALLOPTS}

# Remove the version-number from the documentation-directory
mv %{buildroot}%{_defaultdocdir}/%{name}-%{version_code}/* %{buildroot}%{_defaultdocdir}/%{name}
rmdir %{buildroot}%{_defaultdocdir}/%{name}-%{version_code}

# Create a version independent compiler-configuration file with build-id
# enabled by default. For this purpose some non-default templates are used.
# So the samplecfg script could not be used and fpcmkcfg is called directly.
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE10} \
	-d "libdir=%{_libdir}" \
	-d "sharedir=%{_datadir}" \
	-o %{buildroot}%{_sysconfdir}/fpc.cfg
# Create the IDE configuration files
%{buildroot}%{_bindir}/fpcmkcfg -p -1 -d "basepath=%{_libdir}/%{name}/\$fpcversion" -o %{buildroot}%{_libdir}/%{name}/%{version_code}/ide/text/fp.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -2 -o %{buildroot}%{_libdir}/%{name}/%{version_code}/ide/text/fp.ini
# Create the fppkg configuration files
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE11} -d CompilerConfigDir=%{_sysconfdir}/fppkg -d arch=%{_arch} -o %{buildroot}%{_sysconfdir}/fppkg.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE12} -d fpcbin=%{_bindir}/fpc -d GlobalPrefix=%{_exec_prefix} -d lib=%{_lib} -o %{buildroot}%{_sysconfdir}/fppkg/default_%{_arch}

# Include the COPYING-information for the compiler/rtl/fcl in the documentation
cp -a fpcsrc/compiler/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING
cp -a fpcsrc/rtl/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING.rtl
cp -a fpcsrc/rtl/COPYING.FPC %{buildroot}%{_defaultdocdir}/%{name}/COPYING.FPC

# The source-files:
mkdir -p %{buildroot}%{_datadir}/fpcsrc
cp -a fpc_src/* %{buildroot}%{_datadir}/fpcsrc/

# Workaround:
# newer rpm versions do not allow garbage
# delete lexyacc (The hardcoded library path is necessary because 'make
# install' places this file hardcoded at usr/lib)
rm -rf %{buildroot}/usr/lib/%{name}/lexyacc

%files
%{_bindir}/*
%exclude %{_bindir}/ppcross*
%{_libdir}/%{name}
%{_libdir}/libpas2jslib.so*
%exclude %{_libdir}/%{name}/%{version_code}/ppcross*
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/fppkg.cfg
%config(noreplace) %{_sysconfdir}/fppkg/default_%{_arch}
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/NEWS
%doc %{_defaultdocdir}/%{name}/README
%doc %{_defaultdocdir}/%{name}/faq*
%license %{_defaultdocdir}/%{name}/COPYING*
%{_mandir}/*/*
# Exclude units
%exclude %{_libdir}/%{name}/%{version_code}/fpmkinst/
%exclude %{_libdir}/%{name}/%{version_code}/units/
# Exclude IDE-specific files
%exclude %{_bindir}/fp
%exclude %{_bindir}/fp.rsj
%exclude %{_libdir}/%{name}/%{version_code}/fpmkinst/%{native_arch}-linux/ide.fpm
%exclude %{_libdir}/%{name}/%{version_code}/ide
%exclude %{_mandir}/man1/fp.1*

# -- Native units

%files %{units_native}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/fpmkinst/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/fpmkinst/%{native_arch}-linux/
%{_libdir}/%{name}/%{version_code}/units/%{native_arch}-linux/
# Don't forget about the IDE
%exclude %{_libdir}/%{name}/%{version_code}/fpmkinst/%{native_arch}-linux/ide.fpm

# -- Cross-compilers

%if 0%{?cross_arm}
%files cross-arm
%{_bindir}/%{arm_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{arm_ppcross}

%files units-arm-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{arm_arch}-linux/
%endif

%if 0%{?cross_aarch64}
%files cross-aarch64
%{_bindir}/%{aarch64_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{aarch64_ppcross}

%files units-aarch64-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{aarch64_arch}-linux/
%endif

%if 0%{?cross_i386}
%files cross-i386
%{_bindir}/%{i386_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{i386_ppcross}

%files units-i386-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{i386_arch}-linux/
%endif

%if 0%{?cross_ppc64le}
%files cross-powerpc64
%{_bindir}/%{ppc64le_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{ppc64le_ppcross}

%files units-powerpc64-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{ppc64le_arch}-linux/
%endif

%if 0%{?cross_x86_64}
%files cross-x86_64
%{_bindir}/%{x86_64_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{x86_64_ppcross}

%files units-x86_64-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{x86_64_arch}-linux/
%endif

# -- MS Windows units

%if 0%{?cross_win32}
%files units-i386-win32
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{i386_arch}-win32/
%endif

%if 0%{?cross_win64}
%files units-x86_64-win64
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{x86_64_arch}-win64/
%endif

# -- Others

%files ide
%{_bindir}/fp
%{_bindir}/fp.rsj
%{_libdir}/%{name}/%{version_code}/fpmkinst/%{native_arch}-linux/ide.fpm
%{_libdir}/%{name}/%{version_code}/ide
%{_mandir}/man1/fp.1*

%files doc
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/*.pdf
%doc %{_defaultdocdir}/%{name}/*/*

%files src
%{_datadir}/fpcsrc

%changelog
%autochangelog
