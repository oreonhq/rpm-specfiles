%global source0_hash 08b27b0ab79b13d1e0b4399b9f12edd3e44dccf07df4e1a5bed2ab2ef7ddd867
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
Release:        1%{?dist}
%if ! 0%{?beta}
  %global archive_type dist
  %global archive_suffix %{version_code}
%else
  %global archive_type beta
  %global archive_suffix %{version_beta}-%{version_suffix}
%endif
Source0:        https://downloads.freepascal.org/%{name}/beta/%{version_beta}-%{version_suffix}/source/%{name}build-%{version_beta}-%{version_suffix}.tar.gz
%global bootstrap 0
Source10:        fpc.cft
Source11:        fppkg.cfg
Source12:        default.cft
Patch0:         fpc-3.2.0--dwarf-debug.patch
Patch1:         fpc-3.2.0--honor_SOURCE_DATE_EPOCH_in_date.patch
Patch5:         fpc-3.2.2--pas2jni-cthreads.patch
Patch6:         fpc-3.2.2--fix-IDE-data-files-locations.patch
Patch8:         fpc-3.2.2--fallback-to-localhost-when-no-dns-server-specified.patch
Patch9:         fpc-3.2.2--compiletime-check-is-usage.patch
Patch10:        fpc-3.2.4--pas2js-relocation.patch
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
      %endif
    %endif
  %endif
%endif
%global units_native units-%{native_arch}-linux
Requires:       binutils
Requires:       %{name}-%{units_native}%{?_isa} = %{version}-%{release}
%if ! 0%{?bootstrap}
%endif
%ifarch x86_64
%global cross_i386 1
%endif
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
# oreon:deps
BuildRequires:  binutils-aarch64-linux-gnu
BuildRequires:  binutils-arm-linux-gnu
BuildRequires:  binutils-powerpc64le-linux-gnu
BuildRequires:  fpc
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
# /oreon:deps
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

mkdir -p fpc_src
cp -a fpcsrc/rtl fpc_src
cp -a fpcsrc/packages fpc_src
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
pushd fpcsrc
make compiler_cycle FPC=${STARTPP} OPT='%{fpcopt} %{native_opts}'
make rtl_clean
make rtl%{smart}      FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}'
make packages%{smart} FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}'
make utils_all        FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}' DATA2INC=${DATA2INC}
popd
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
pushd fpcsrc
install_compiler '%{native_arch}' '%{native_ppc}'
make rtl_distinstall      ${INSTALLOPTS}
make packages_distinstall ${INSTALLOPTS}
make utils_distinstall    ${INSTALLOPTS}
popd
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
pushd install
make -C doc ${INSTALLOPTS}
make -C man ${INSTALLOPTS} INSTALL_MANDIR=%{buildroot}%{_mandir}
popd
make -C fpcdocs pdfinstall ${INSTALLOPTS}
mv %{buildroot}%{_defaultdocdir}/%{name}-%{version_code}/* %{buildroot}%{_defaultdocdir}/%{name}
rmdir %{buildroot}%{_defaultdocdir}/%{name}-%{version_code}
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE10} \
	-d "libdir=%{_libdir}" \
	-d "sharedir=%{_datadir}" \
	-o %{buildroot}%{_sysconfdir}/fpc.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -1 -d "basepath=%{_libdir}/%{name}/\$fpcversion" -o %{buildroot}%{_libdir}/%{name}/%{version_code}/ide/text/fp.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -2 -o %{buildroot}%{_libdir}/%{name}/%{version_code}/ide/text/fp.ini
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE11} -d CompilerConfigDir=%{_sysconfdir}/fppkg -d arch=%{_arch} -o %{buildroot}%{_sysconfdir}/fppkg.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE12} -d fpcbin=%{_bindir}/fpc -d GlobalPrefix=%{_exec_prefix} -d lib=%{_lib} -o %{buildroot}%{_sysconfdir}/fppkg/default_%{_arch}
cp -a fpcsrc/compiler/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING
cp -a fpcsrc/rtl/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING.rtl
cp -a fpcsrc/rtl/COPYING.FPC %{buildroot}%{_defaultdocdir}/%{name}/COPYING.FPC
mkdir -p %{buildroot}%{_datadir}/fpcsrc
cp -a fpc_src/* %{buildroot}%{_datadir}/fpcsrc/
rm -rf %{buildroot}/usr/lib/%{name}/lexyacc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n fpc-units-%{native_arch}-linux -f %{oreon_filedir}/fpc-units-%{native_arch}-linux.list
%files -n fpc-cross-arm -f %{oreon_filedir}/fpc-cross-arm.list
%files -n fpc-units-arm-linux -f %{oreon_filedir}/fpc-units-arm-linux.list
%files -n fpc-cross-aarch64 -f %{oreon_filedir}/fpc-cross-aarch64.list
%files -n fpc-units-aarch64-linux -f %{oreon_filedir}/fpc-units-aarch64-linux.list
%files -n fpc-cross-powerpc64 -f %{oreon_filedir}/fpc-cross-powerpc64.list
%files -n fpc-units-powerpc64-linux -f %{oreon_filedir}/fpc-units-powerpc64-linux.list
%files -n fpc-ide -f %{oreon_filedir}/fpc-ide.list
%files -n fpc-doc -f %{oreon_filedir}/fpc-doc.list
%files -n fpc-src -f %{oreon_filedir}/fpc-src.list

%changelog

%autochangelog
