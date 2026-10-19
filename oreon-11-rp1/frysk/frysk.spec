%global source0_hash d85d419b2346c2b9011499052a893d814d6ef042a92d1b69cfb38ccd72d616b2
Summary:        Execution analysis and debugging tool-suite
Name:		frysk
Version:	0.4
Release:        1%{?dist}
%define enable_gnome %{fedora}0 < 170
%define enable_devel %{fedora}0 < 170
License:	GPL-2.0-only WITH 389-exception AND GPL-2.0-or-later WITH Classpath-exception-2.0 AND MIT
URL:		http://sourceware.org/frysk
Source0:        ftp://sourceware.org/pub/frysk/%{name}-%{version}.tar.bz2
Patch0:		frysk-0.4-head.patch
Patch1:		frysk-0.4-bash-dollar-star.patch
Patch2:		frysk-0.4-strayelsif.patch
Patch3:		frysk-0.4-fdebugrpm.patch
Patch4:		frysk-0.4-mktlwidgetdir.patch
Patch5:		frysk-0.4-gcc-warnings.patch
Patch6:		frysk-0.4-funitexitman.patch
Patch7:		frysk-0.4-mvtesttomain.patch
Patch8:		frysk-0.4-taskstoputil.patch
Patch9:		frysk-0.4-publictestbedsymtab.patch
Patch10:	frysk-0.4-noelfmem.patch
Patch11:	frysk-0.4-gccjint.patch
Patch12:	frysk-0.4-taskstoperr.patch
Patch13:	frysk-0.4-lostfork.patch
Patch14:	frysk-0.4-nooptimize.patch
Patch15:	frysk-0.4-skipdecl.patch
Patch16:	frysk-0.4-flushstat.patch
Patch17:	frysk-0.4-ftrace.patch
Patch18:	frysk-0.4-usererrno.patch
Patch19:	frysk-0.4-configure-enable-gnome.patch
Patch20:	frysk-0.4-bin-antlr.patch
Patch21:	frysk-0.4-nopkglibdir.patch
Patch22:	frysk-0.4-no-jdom.patch
Patch23:	frysk-0.4-missing-javah-cni-built.patch
Patch24:	frysk-0.4-jni.patch
Patch25:	frysk-0.4-awk-gensub.patch
Patch26:	frysk-0.4-pic-asm.patch
Patch27:	frysk-0.4-per-thread-java-id.patch
Patch28:	frysk-0.4-unwind-global-id.patch
Patch29:	frysk-0.4-use-installed-antlr.patch
Patch30:	frysk-0.4-use-installed-junit.patch
Patch31:	frysk-0.4-jni-issameobject.patch
Patch32:	frysk-0.4-switch-ecj-to-javac.patch
Patch33:	frysk-0.4-use-installed-jline.patch
Patch34:	frysk-0.4-libunwind-fstack.patch
Patch35:	frysk-0.4-clone-cursor.patch
Patch36:	frysk-0.4-fedpkg-lint-licence.patch
Patch37:	frysk-0.4-fedpkg-lint-solib.patch
Patch38:	frysk-0.4-gelf-newphdr.patch
Patch39:	frysk-0.4-jnixx-signed-unsigned.patch
Patch40:	frysk-0.4-check-p-not-status.patch
Patch41:	frysk-0.4-python3.patch
Patch42:	frysk-0.4-jline1-to-jline.patch
Patch43:	frysk-0.4-disable-arch32-tests.patch
Patch44:	frysk-0.4-steptester-indentation.patch
Patch45:	frysk-0.4-gcc-fcommon.patch
Patch46:	frysk-0.4-javac.patch
Patch47:	frysk-0.4-jnixx-union-as-reserved-word.patch
Patch48:	frysk-0.4-jnixx-dont-emit-nested-classes.patch
Patch49:	frysk-0.4-49-elf-newehdr-null.patch
Patch50:	frysk-0.4-50-autoconf-2-70-fixes.patch
Patch51:	frysk-0.4-51-debugedit-path.patch
Patch52:	frysk-0.4-52-libunwind-tests.patch
Patch53:	frysk-0.4-53-no-new-integer.patch
Patch54:	frysk-0.4-54-c-warnings.patch
Patch100:	frysk-0.4-aclocaljavac.patch
Patch101:	frysk-0.4-cxx-scope.patch
Patch1003:	frysk-0.4-nogtkwerror.patch
Patch666:	frysk-0.4-sodwfl.patch
Requires: junit
Requires: antlr-tool
Requires: jline2
%if %{enable_gnome}
%endif
ExclusiveArch: x86_64 ppc64
%ifarch %{ix86}
%define _target_cpu %{_host_cpu}
%endif
# oreon:deps
BuildRequires:  antlr-tool
BuildRequires:  audit-libs-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  debugedit
BuildRequires:  elfutils-devel
BuildRequires:  gcc-c++
BuildRequires:  java-25-devel
BuildRequires:  jline2
BuildRequires:  junit
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  sharutils
BuildRequires:  transfig
BuildRequires:  xmlto
# /oreon:deps
%description
Frysk is an execution-analysis technology implemented using native
Java and C++.  It is aimed at providing developers and sysadmins with
the ability to both examine and analyze running multi-host,
multi-process, multi-threaded systems.  Frysk allows the monitoring of
running processes and threads, of locking primitives and will also
expose deadlocks, gather data and debug any given process in the
system.

%if %{enable_devel}
%package devel
Summary:	The development part of Frysk
Requires:	%{name} = %{version}-%{release}
%endif
%if %{enable_gnome}
Requires:	python2-dogtail >= 0.5.2
Requires:	metacity
Requires:	python2
%endif
%if %{enable_devel}
%description devel
Frysk is an execution-analysis technology implemented using native
Java and C++.  It is aimed at providing developers and sysadmins with
the ability to both examine and analyze running multi-host,
multi-process, multi-threaded systems.  Frysk allows the monitoring of
running processes and threads, of locking primitives and will also
expose deadlocks, gather data and debug any given process in the
system.

This package contains the development components of Frysk.
%endif

%if %{enable_gnome}
%package gnome
Summary:	The GNOME front-end of Frysk
Requires:	%{name} = %{version}-%{release}
Requires:	libgconf-java
Requires:	libglade-java >= 2.12.5
Requires:	libvte-java >= 0.12.0
%description gnome
Frysk is an execution-analysis technology implemented using native
Java and C++.  It is aimed at providing developers and sysadmins with
the ability to both examine and analyze running multi-host,
multi-process, multi-threaded systems.  Frysk allows the monitoring of
running processes and threads, of locking primitives and will also
expose deadlocks, gather data and debug any given process in the
system.

This package contains the GNOME front end for Frysk.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
pwd

%patch -P0 -p1 -z .head

%patch -P1 -p1 -z .bash-dollar-star
%patch -P2 -p1 -z .strayelsif
%patch -P3 -p1 -z .fdebugrpm
%patch -P4 -p1 -z .mktlwidgetdir
%patch -P5 -p1 -z .gcc-warnings
%patch -P6 -p1 -z .funitexitman
mv frysk-core/frysk/pkglibdir/FunitSimpleInterfaceTest.java frysk-core/frysk/pkglibdir/FunitSimpleInterfaceMain.java
%patch -P7 -p1 -z .mvtesttomain -F 1
mv frysk-core/frysk/util/ProcStopUtil.java frysk-core/frysk/util/TaskStopUtil.java
%patch -P8 -p1 -z .taskstoputil -F 3
%patch -P9 -p1 -z .publictestbedsymtab
%patch -P10 -p1 -z .noelfmem
%patch -P11 -p1 -z .gccjint
%patch -P12 -p1 -z .taskstoperr
%patch -P13 -p1 -z .lostfork
%patch -P14 -p1 -z .nooptimize
%patch -P15 -p1 -z .skipdecl
%patch -P16 -p1 -z .flushstat
%patch -P17 -p1 -z .ftrace
%patch -P18 -p1 -z .usererrno
%patch -P19 -p1 -z .configure-enable-gnome
%patch -P20 -p1 -z .bin-antlr

%if %{enable_gnome}
# don't apply - leaves default as build gnome
%else
%patch -P101 -p1 -z .configure-enable-gnome
%endif

%if %{enable_devel}
# don't apply - leaves devel package installed
%else
%patch -P21 -p1 -z .nopkglibdir
%endif

%patch -P1003 -p1 -z .nogtkwerror

%patch -P666 -p1 -z .sodwfl
rm -rf frysk-imports/elfutils

%if %{enable_gnome}
# don't apply, leave jdom around
%else
%patch -P22 -p1 -z .no-jdom
rm -rf frysk-core/frysk/dom
rm -rf frysk-core/frysk/rt/LineXXX.java
%endif

%patch -P23 -p1 -z .missing-javah-cni-built
%patch -P24 -p1 -z .jni
%patch -P25 -p1 -z .awk-gensub
%patch -P26 -p1 -z .pic-asm
%patch -P27 -p1 -z .per-thread-java-id
%patch -P28 -p1 -z .unwind-global-id
%patch -P29 -p1 -z .use-installed-antlr
rm -rf frysk-imports/antlr
%patch -P30 -p1 -z .use-installed-junit
rm -rf frysk-imports/junit
%patch -P31 -p1 -z .jni-issameobject
%patch -P32 -p1 -z .switch-ecj-to-javac
%patch -P33 -p1 -z .use-installed-jline
rm -rf frysk-imports/jline
# automake doesn't like old names
mv frysk-imports/libunwind/configure.{in,ac}
%patch -P34 -p1 -z .libunwind-fstack
%patch -P35 -p1 -z .clone-cursor
%patch -P36 -p1 -z .fedpkg-lint-licence
%patch -P37 -p1 -z .fedpkg-lint-solib
%patch -P38 -p1 -z .gelf-newphdr
%patch -P39 -p1 -z .jnixx-signed-unsigned
%patch -P40 -p1 -z .check-p-not-status
%patch -P41 -p1 -z .python3
%patch -P42 -p1 -z .jline1-to-jline
%patch -P43 -p1 -z .disable-arch32-tests
%patch -P44 -p1 -z .steptester-indentation
%patch -P45 -p1 -z .gcc-fcommon
%patch -P46 -p1 -z .javac
%patch -P47 -p1 -z .jnixx-union-as-reserved-word
%patch -P48 -p1 -z .jnixx-dont-emit-nested-classes
%patch -P49 -p1 -z .49-elf-newehdr-null
%patch -P50 -p1 -z .50-autoconf-2-70-fixes
%patch -P51 -p1 -z .51-debugedit-path
%patch -P52 -p1 -z .52-libunwind-tests.patch
%patch -P53 -p1 -z .53-no-new-integer.patch
%patch -P54 -p1 -z .54-c-warnings.patch

echo "%{version}-%{release}" > frysk-common/version.in

# don't try to build assembler test files
rm frysk-core/frysk/pkglibdir/*.S

./bootstrap.sh

%build 

uname -a
gcc --version
pwd
mkdir -p build
cd build
rpm -ql xmlto || :
ls -l /usr/bin/xmlto || :
rm -f configure
echo '#!/bin/sh -x'			>> configure
echo 'exec ../$(basename $0) "$@"'	>> configure
chmod a+x configure
%configure \
	CFLAGS="$RPM_OPT_FLAGS" \
	CXXFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/usr/share/frysk
pwd
cd build
make DESTDIR=$RPM_BUILD_ROOT install %{?_smp_mflags}
find $RPM_BUILD_ROOT
%if %{enable_gnome}
touch -r \
  ../frysk-gui/frysk/gui/FryskGui.java-in \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/dogtail_scripts/frysk_suite.py
for f in test2866.py test2985.py test3380.py; do
  touch -r \
    ../frysk-gui/frysk/gui/test/dogtail_scripts/$f \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/dogtail_scripts/$f
done
%endif
%if %{enable_devel}
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/gen-type-funit-tests
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/ChangeLog
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/test-exe-x86.c.source
%else
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/test-sysroot
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_mandir}/man8
%endif
%if %{enable_gnome}
echo "Hidden=true" >> $RPM_BUILD_ROOT%{_datadir}/applications/frysk.desktop
%endif
%if %{enable_devel}
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/funit-exec-alias
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/funit-*-nodebug
%oreon_autofiles main
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
