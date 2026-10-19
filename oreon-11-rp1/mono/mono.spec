%global source0_hash 3024c97c0bc8cbcd611c401d5f994528704108ceb31f31b28dea4783004d0820
%bcond_with bootstrap
%ifarch s390x
%undefine _hardened_build
%endif
%if 0%{?el6}
%global mono_arches %{ix86} x86_64 sparc sparcv9 ia64 %{arm} alpha s390x ppc ppc64 ppc64le
%global _monodir %{_prefix}/lib/mono
%global _monogacdir %{_monodir}/gac
%endif
%if 0%{?el7}
%global _monodir %{_prefix}/lib/mono
%global _monogacdir %{_monodir}/gac
%endif
Name:           mono
Version:        6.14.1
Release:        1%{?dist}
Summary:        Cross-platform, Open Source, .NET development framework
License:        MIT
URL:            http://www.mono-project.com
Source0:        https://dl.winehq.org/mono/sources/mono/%{name}-%{version}.tar.xz
Source1:        mono.snk
Source2:        mono-find-provides
Source3:        mono-find-requires
Source4:        mono.attr
Patch0:         mono-6.6.0-ignore-reference-assemblies.patch
Patch1:         mono-4.2.1-ppc.patch
Patch2:         mono-5.10.0-find-provides.patch
Patch3:         mono-4.2-fix-winforms-trayicon.patch
Patch4:         mono-6.6.0-aarch64.patch
Patch5:         mono-6.6.0-roslyn-binaries.patch
Patch6:         mono-5.18.0-use-mcs.patch
Patch7:         mono-5.18.0-reference-assemblies-fix.patch
Patch8:         mono-5.18.0-sharpziplib-parent-path-traversal.patch
Patch10:        0001-DocumentationEnumerator.cs-Declare-iface-and-ifaceMe.patch
Patch11:        0001-Replace-new-Csharp-features-with-old-ones.patch
Patch12:        0001-Reenable-mdoc.exe-build.patch
Patch13:	mono-6.6.0-fix-multi-arch-issue.patch
Patch14:        mono-configure-c99.patch
Patch15:        mono-6.12.0-correct-alloc-free-for-zlib.patch
Patch16:        mono-6.14.0-arm64-fix-pointer-int.patch
Patch17:        https://gitlab.winehq.org/mono/mono/-/commit/694cb61761a8ee51d404debbdb019f64d09b61c9.patch
%if %{without bootstrap}
%endif
ExclusiveArch: %mono_arches
%global _use_internal_dependency_generator 0
%global __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | grep -v 4.7.1-api | grep -v 4.5-api| /usr/lib/rpm/redhat/find-provides && printf "%s\\n" "${filelist[@]}" | grep -v 4.7.1-api | grep -v 4.5-api | prefix=%{buildroot}%{_prefix} %{buildroot}%{_bindir}/mono-find-provides; } | sort | uniq'
%global __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/redhat/find-requires && printf "%s\\n" "${filelist[@]}" | prefix=%{buildroot}%{_prefix} %{buildroot}%{_bindir}/mono-find-requires; } | sort | uniq | grep ^...'
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libgdiplus-devel
BuildRequires:  libicu-devel
BuildRequires:  make
BuildRequires:  perl-Getopt-Long
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  valgrind-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package core
Summary:        The Mono CIL runtime, suitable for running .NET code
Requires:       libgdiplus
Provides:       mono(System.Collections.Immutable) = 1.2.0.0
Provides:       mono(System.Diagnostics.StackTrace) = 4.0.2.0
Provides:       mono(System.IO) = 4.0.10.0
Provides:       mono(System.IO.Compression) = 4.1.1.0
Provides:       mono(System.Linq.Expressions) = 4.0.10.0
Provides:       mono(System.Reflection) = 4.0.10.0
Provides:       mono(System.Runtime) = 4.0.20.0
Provides:       mono(System.Runtime.Extensions) = 4.0.10.0
Provides:       mono(System.Runtime.InteropServices) = 4.0.20.0
Provides:       mono(System.Runtime.Loader) = 4.0.0.0
Provides:       mono(System.Text.Encoding.CodePages) = 4.0.2.0
Provides:       mono(System.ValueTuple) = 4.0.1.0
Provides:       mono(System.Collections) = 4.0.0.0
Provides:       mono(System.Diagnostics.Debug) = 4.0.0.0
Provides:       mono(System.Globalization) = 4.0.0.0
Provides:       mono(System.IO) = 4.0.0.0
Provides:       mono(System.Linq) = 4.0.0.0
Provides:       mono(System.Reflection) = 4.0.0.0
Provides:       mono(System.Runtime) = 4.0.0.0
Provides:       mono(System.Runtime.Extensions) = 4.0.0.0
Provides:       mono(System.Runtime.InteropServices) = 4.0.0.0
Provides:       mono(System.Security.Cryptography.Algorithms) = 4.0.0.0
Provides:       mono(System.Text.Encoding) = 4.0.0.0
Provides:       mono(System.Text.Encoding.Extensions) = 4.0.0.0
Provides:       mono(System.Threading) = 4.0.0.0
Provides:       mono(System.Xml.XPath.XDocument) = 4.0.1.0
%description core
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,
I18N, Cairo and Mono.*).

%package winfx
Summary:        Mono implementation of core WinFX APIs
Requires:       mono-core = %{version}-%{release}
%description winfx
Open source implementation of core WinFX APIs

%package mvc
Summary:        Mono implementation of ASP.NET MVC
Requires:       mono-core = %{version}-%{release}
%description mvc
This is the Mono implementation of ASP.NET MVC

%package mvc-devel
Summary:        Development files for  ASP.NET MVC
Requires:       mono-core = %{version}-%{release}
%description mvc-devel
This is the Mono implementation of ASP.NET MVC

%package devel
Summary:        Development tools for Mono
Requires:       mono-core = %{version}-%{release}
Requires:       pkgconfig
Requires:       glib2-devel
%description devel
This package completes the Mono developer toolchain with the mono profiler,
assembler and other various tools.

%package locale-extras
Summary:        Extra locale information for Mono
Requires:       mono-core = %{version}-%{release}
%description locale-extras
This package contains assemblies to support I18N applications for
non-latin alphabets.

%package extras
Summary:        Provides the infrastructure for running and building daemons and services with Mono as well as various stub assemblies
Requires:       mono-core = %{version}-%{release}
%description extras
This package provides the library and application to run services
and daemons with Mono. It also includes stubs for the following
assemblies: Microsoft.Vsa,
System.Configuration.Install, System.Management, System.Messaging.

%package reactive
License:        MIT AND Apache-2.0
Summary:        Reactive Extensions for Mono core libraries
Requires:       mono-core = %{version}-%{release}
%description reactive
Reactive Extensions for Mono, this packages don't depend on
desktop-specific features.

%package reactive-winforms
License:        MIT AND Apache-2.0
Summary:        Reactive Extensions for Mono desktop-specific libraries
Requires:       mono-core = %{version}-%{release}
Requires:       mono-reactive = %{version}-%{release}
%description reactive-winforms
Reactive Extensions for Mono, desktop-specific packages (winforms,
windows threading).

%package reactive-devel
Summary:        Development files for system.web
Requires:       mono-core = %{version}-%{release}
Requires:       mono-reactive = %{version}-%{release} pkgconfig
%description reactive-devel
This package provides the .pc file for mono-rx

%package winforms
Summary:        Windows Forms implementation for Mono
Requires:       mono-core = %{version}-%{release}
%description winforms
This package provides a fully managed implementation of
System.Windows.Forms, the default graphical toolkit for .NET
applications.

%package wcf
Summary:        Mono implementation of Windows Communication Foundation
Requires:       mono-core = %{version}-%{release}
%description wcf
This package provides an implementation of WCF, the Windows Communication
Foundation.

%package web
Summary:        ASP.NET, Remoting, and Web Services for Mono
Requires:       mono-core = %{version}-%{release}
%description web
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.

%package web-devel
Summary:        Development files for system.web
Requires:       mono-core = %{version}-%{release}
Requires:       mono-web = %{version}-%{release} pkgconfig
%description web-devel
This package provides the .pc file for mono-web

%package data
Summary:        Database connectivity for Mono
Requires:       mono-core = %{version}-%{release}
%description data
This package provides a Mono assembly to facilitate data access
and manipulation with databases, LDAP compatible directory servers
and/or XML data exchange. Beyond the ADO.NET, Novell.LDAP and
System.DirectoryServices assemblies, it also includes a command
line sql application as well as the Microsoft SQL Server and ODBC
data providers.

%package data-sqlite
Summary:        sqlite database connectivity for Mono
Requires:       mono-core = %{version}-%{release}
Requires:       sqlite-libs%{?_isa}
%description data-sqlite
This package contains the ADO.NET Data provider for the sqlite
database.

%package data-oracle
Summary:        Oracle database connectivity for Mono
Requires:       mono-core = %{version}-%{release}
%description data-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%package -n ibm-data-db2
Summary:        IBM DB2 database connectivity for Mono
Requires:       mono-core = %{version}-%{release}
%description -n ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.

%package -n monodoc
Summary:        The mono documentation system
Requires:       mono-core = %{version}-%{release}
%description -n monodoc
monodoc is the documentation package for the mono .NET environment

%package -n monodoc-devel
Summary:        .pc file for monodoc
Requires:       monodoc = %{version}-%{release} pkgconfig
Requires:       mono-core = %{version}-%{release}
%description -n monodoc-devel
Development file for monodoc

%package complete
Summary:        Install everything built from the mono source tree
Requires:       ibm-data-db2 = %{version}
Requires:       mono-core = %{version}
Requires:       mono-data = %{version}
Requires:       mono-data-oracle = %{version}
Requires:       mono-data-sqlite = %{version}
Requires:       mono-devel = %{version}
Requires:       mono-extras = %{version}
Requires:       mono-locale-extras = %{version}
Requires:       mono-mvc = %{version}
Requires:       mono-reactive = %{version}
Requires:       mono-wcf = %{version}
Requires:       mono-web = %{version}
Requires:       mono-winforms = %{version}
Requires:       mono-winfx = %{version}
Requires:       monodoc = %{version}
%description -n mono-complete
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Install everything built from the mono source tree.  Note that this does
not install anything from outside the mono source (XSP, mono-basic, etc.).

%global gac_dll(dll)  %{_monogacdir}/%{1} \
  %{_monodir}/4.5/%{1}.dll \
  %{nil}
%global mono_bin(bin) %{_bindir}/%{1} \
  %{_monodir}/4.5/%{1}.exe \
  %{_monodir}/4.5/%{1}.exe.* \
  %{nil}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%patch -P 0 -p1
%ifarch ppc ppc64 ppc64le s390x
%patch -P 1 -p1
%endif
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
pushd external/api-doc-tools
%patch -P 10 -p1
%patch -P 11 -p1
popd
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1

# don't build mono-helix-client which requires the helix-binaries to build
sed -i 's|mono-helix-client||g' mcs/tools/Makefile

# use v4.7.1 instead of v4.7
sed -i 's|BOOTSTRAP_BIN_PROFILE = v4.7|BOOTSTRAP_BIN_PROFILE = v4.7.1|g' mcs/build/profiles/build.make

# Remove hardcoded lib directory for libMonoPosixHelper.so from the config
sed -i 's|$mono_libdir/||g' data/config.in

%if %{with bootstrap}
# for bootstrap, keep some binaries
find . -name "*.dll" -not -path "./mcs/class/lib/monolite-linux/*" -not -path "./external/binary-reference-assemblies/v4.7.1/*" -print -delete
find . -name "*.exe" -not -path "./mcs/class/lib/monolite-linux/*" -print -delete
%else
# Remove all prebuilt binaries
rm -rf mcs/class/lib/monolite-linux/*
find . -name "*.dll" -print -delete
find . -name "*.exe" -print -delete
# use the binaries from the currently installed mono
cd external/binary-reference-assemblies && mv v4.7.1 v4.7.1.tobuild && ln -s %{_monodir}/4.7.1-api v4.7.1 && cd -
%endif

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%ifarch ppc64le
%define _lto_cflags %{nil}
%endif
%ifarch s390x
RPM_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed -e 's/-O2 /-O1 /g')
%endif
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-rpath \
           --with-csc=mcs \
           --disable-system-aot \
           --with-moonlight=no
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH=`pwd`/mono/native/.libs
make %{?_smp_mflags}
cd external/binary-reference-assemblies && if [ -d v4.7.1.tobuild ]; then rm -f v4.7.1 && mv v4.7.1.tobuild v4.7.1; fi && cd -
find ./external/binary-reference-assemblies/v4.7.1/ -name \*.dll -print -delete
BUILD_PATH=`pwd` && cd ./external/binary-reference-assemblies/ && MONO_PATH=$BUILD_PATH/mcs/class/lib/net_4_x-linux/ V=1 CSC="$BUILD_PATH/runtime/mono-wrapper $BUILD_PATH/mcs/class/lib/net_4_x-linux/mcs.exe" make -C v4.7.1
%install
export LD_LIBRARY_PATH=`pwd`/mono/native/.libs
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/pki/mono
install -p -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/mono/
mkdir -p %{buildroot}%{_monodir}/4.7.1-api
cp external/binary-reference-assemblies/v4.7.1/*.dll %{buildroot}%{_monodir}/4.7.1-api
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_monodir}/*/Mono.Security.Win32*
rm %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_datadir}/libgc-mono
rm -f %{buildroot}%{_bindir}/cilc
rm -f %{buildroot}%{_mandir}/man1/cilc.1*
rm -f %{buildroot}%{_mandir}/man1/mdb2ppdb.1*
rm -f %{buildroot}%{_monodir}/*/browsercaps-updater.*
rm -f %{buildroot}%{_monodir}/*/culevel.*
rm -f %{buildroot}%{_monodir}/2.0/cilc.exe*
rm -f %{buildroot}%{_monodir}/*/mscorlib.dll.so
rm -f %{buildroot}%{_monodir}/*/mcs.exe.so
rm -f %{buildroot}%{_monodir}/*/gmcs.exe.so
rm -f %{buildroot}%{_monodir}/4.0/dmcs.exe.so
rm -rf %{buildroot}%{_bindir}/mono-configuration-crypto
rm -rf %{buildroot}%{_mandir}/man?/mono-configuration-crypto*
rm -rf %{buildroot}%{_monodir}/4.5/*.so
rm -f %{buildroot}%{_bindir}/nunit-console
rm -f %{buildroot}%{_bindir}/nunit-console2
rm -f %{buildroot}%{_bindir}/nunit-console4
rm -f %{buildroot}%{_monodir}/4.5/nunit*
rm -Rf %{buildroot}%{_monodir}/gac/nunit*
rm -f %{buildroot}%{_libdir}/pkgconfig/mono-nunit.pc
rm -f %{buildroot}%{_bindir}/dmcs
rm -f %{buildroot}%{_bindir}/csc
rm -f %{buildroot}%{_bindir}/csc-dim
rm -f %{buildroot}%{_bindir}/csi
rm -f %{buildroot}%{_bindir}/vbc
rm -f %{buildroot}%{_bindir}/prj2make
rm -f %{buildroot}%{_mandir}/man1/prj2make*
mkdir -p %{buildroot}%{_datadir}/gdb/auto-load%{_bindir}
%{__mv} -f %{buildroot}%{_bindir}/mono-gdb.py \
           %{buildroot}%{_datadir}/gdb/auto-load%{_bindir}/
rm -f %{buildroot}%{_libdir}/pkgconfig/cecil.pc
rm -rf %{buildroot}%{_monodir}/msbuild
rm -rf %{buildroot}/usr/lib/debug%{_libdir}/libmono-btls-shared.so-*.debug
rm -rf %{buildroot}/usr/lib/debug%{_libdir}/libmono-native.so*.debug
rm -rf %{buildroot}/usr/lib/debug%{_bindir}/mono-hang-watchdog-*.debug
cd %{buildroot}%{_monodir} && ln -s 4.7.1-api 4.5-api && cd -
cd %{buildroot}%{_monodir} && ln -s 4.7.1-api 4.0-api && cd -
%if 0%{?el7}%{?el8} == 0
mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m755 %{SOURCE2} %{SOURCE3} %{buildroot}%{_rpmconfigdir}
install -p -m644 %{SOURCE4} %{buildroot}%{_fileattrsdir}
%endif
rm %{buildroot}%{_bindir}/mono-find-requires
rm %{buildroot}%{_bindir}/mono-find-provides
%find_lang mcs
%oreon_autofiles ibm-data-db2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles monodoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles monodoc-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post core

%{?ldconfig}
%{_bindir}/cert-sync --quiet /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
%ldconfig_postun
%files -f %{oreon_filedir}/main.list
%files -n mono-core -f %{oreon_filedir}/mono-core.list
%files -n mono-winfx -f %{oreon_filedir}/mono-winfx.list
%files -n mono-mvc -f %{oreon_filedir}/mono-mvc.list
%files -n mono-mvc-devel -f %{oreon_filedir}/mono-mvc-devel.list
%files -n mono-devel -f %{oreon_filedir}/mono-devel.list
%files -n mono-locale-extras -f %{oreon_filedir}/mono-locale-extras.list
%files -n mono-extras -f %{oreon_filedir}/mono-extras.list
%files -n mono-reactive -f %{oreon_filedir}/mono-reactive.list
%files -n mono-reactive-winforms -f %{oreon_filedir}/mono-reactive-winforms.list
%files -n mono-reactive-devel -f %{oreon_filedir}/mono-reactive-devel.list
%files -n mono-winforms -f %{oreon_filedir}/mono-winforms.list
%files -n mono-wcf -f %{oreon_filedir}/mono-wcf.list
%files -n mono-web -f %{oreon_filedir}/mono-web.list
%files -n mono-web-devel -f %{oreon_filedir}/mono-web-devel.list
%files -n mono-data -f %{oreon_filedir}/mono-data.list
%files -n mono-data-sqlite -f %{oreon_filedir}/mono-data-sqlite.list
%files -n mono-data-oracle -f %{oreon_filedir}/mono-data-oracle.list
%files -n ibm-data-db2 -f %{oreon_filedir}/ibm-data-db2.list
%files -n monodoc -f %{oreon_filedir}/monodoc.list
%files -n monodoc-devel -f %{oreon_filedir}/monodoc-devel.list
%files -n mono-complete -f %{oreon_filedir}/mono-complete.list

%changelog

%autochangelog

