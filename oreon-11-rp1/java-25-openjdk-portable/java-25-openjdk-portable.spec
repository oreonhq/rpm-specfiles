%define debug_package %{nil}
%global source0_hash a6c53f39d45c7a1ac01754ecbb4f867a8c42012178e65896d082dbf385c7dd95
%global _general_options -O2 %{?_lto_cflags} -fexceptions -g -grecord-gcc-switches -pipe
%global build_type_safety_c 0
%undefine _distro_extra_cflags
%undefine _distro_extra_cxxflags
%undefine _distro_extra_fflags
%undefine _distro_extra_ldflags
%undefine _hardened_build
%undefine _annotated_build
%global set_build_flags \
  CFLAGS="%{optflags} -fno-lifetime-dse -fno-lto" ; export CFLAGS ; \
  CXXFLAGS="%{build_cxxflags} -fno-lifetime-dse -fno-lto" ; export CXXFLAGS ; \
  FFLAGS="%{build_fflags}" ; export FFLAGS ; \
  FCFLAGS="%{build_fflags}" ; export FCFLAGS ; \
  VALAFLAGS="%{build_valaflags}" ; export VALAFLAGS ; \
  LDFLAGS="%{build_ldflags}" ; export LDFLAGS ; \
  LT_SYS_LIBRARY_PATH="%{_libdir}:" ; export LT_SYS_LIBRARY_PATH ; \
  CC="%{__cc}" ; export CC ; \
  CXX="%{__cxx}" ; export CXX
%bcond_without fastdebug
%bcond_without slowdebug
%bcond_without release
%bcond_without staticlibs
%bcond_with artifacts
%bcond_with fresh_libjvm
%bcond_with system_libs
%if %{with staticlibs}
%define __brp_strip_static_archive %{nil}
%global include_staticlibs 1
%else
%global include_staticlibs 0
%endif
%if %{with system_libs}
%global system_libs 1
%global link_type system
%global freetype_lib %{nil}
%else
%global system_libs 0
%global link_type bundled
%global freetype_lib |libfreetype[.]so.*
%endif
%global _find_debuginfo_opts -g
%define _lto_cflags %{nil}
%global debug_suffix_unquoted -slowdebug
%global fastdebug_suffix_unquoted -fastdebug
%global main_suffix_unquoted -main
%global staticlibs_suffix_unquoted -staticlibs
%global debug_suffix "%{debug_suffix_unquoted}"
%global fastdebug_suffix "%{fastdebug_suffix_unquoted}"
%global normal_suffix ""
%global main_suffix "%{main_suffix_unquoted}"
%global staticlibs_suffix "%{staticlibs_suffix_unquoted}"
%global debug_warning This package is unoptimised with full debugging. Install only as needed and remove ASAP.
%global fastdebug_warning This package is optimised with full debugging. Install only as needed and remove ASAP.
%global debug_on unoptimised with full debugging on
%global fastdebug_on optimised with full debugging on
%global for_fastdebug for packages with debugging on and optimisation
%global for_debug for packages with debugging on and no optimisation
%if %{with release}
%global include_normal_build 1
%else
%global include_normal_build 0
%endif
%global normal_build %{nil}
%define is_release_build() %( if [ "%{?1}" == "%{debug_suffix_unquoted}" -o "%{?1}" == "%{fastdebug_suffix_unquoted}" ]; then echo "0" ; else echo "1"; fi )
%global is_system_jdk 0
%global aarch64         aarch64 arm64 armv8
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
%global multilib_arches %{power64} sparc64 x86_64
%global debug_arches    %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} s390x
%global fastdebug_arches x86_64 ppc64le aarch64
%global jit_arches      %{arm} %{aarch64} %{ix86} %{power64} s390x sparcv9 sparc64 x86_64 riscv64
%global zero_arches ppc s390
%global bootstrap_arches %{jit_arches}
%global systemtap_arches %{jit_arches}
%global aot_arches      x86_64 %{aarch64}
%global sa_arches       %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} %{arm} riscv64
%global share_arches    %{jit_arches}
%global shenandoah_arches x86_64 %{aarch64} riscv64
%global zgc_arches x86_64 riscv64
%global ssbd_arches x86_64
%global svml_arches x86_64
%if (0%{?rhel} > 0 && 0%{?rhel} < 8) || (0%{?oreon} >= 11)
%global gdb_arches %{arm} %{aarch64} %{ix86} %{power64} sparcv9 sparc64 x86_64 %{zero_arches}
%else
%global gdb_arches %{jit_arches} %{zero_arches}
%endif
%global jdk_test_arch x86_64
%if %{with slowdebug}
%ifarch %{debug_arches}
%global include_debug_build 1
%else
%global include_debug_build 0
%endif
%else
%global include_debug_build 0
%endif
%ifarch %{shenandoah_arches}
%global use_shenandoah_hotspot 1
%else
%global use_shenandoah_hotspot 0
%endif
%if %{with fastdebug}
%ifarch %{fastdebug_arches}
%global include_fastdebug_build 1
%else
%global include_fastdebug_build 0
%endif
%else
%global include_fastdebug_build 0
%endif
%global slowdebug_build %{nil}
%global fastdebug_build %{nil}
%global build_loop %{slowdebug_build} %{fastdebug_build} %{normal_build}
%global staticlibs_loop %{nil}
%if 0%{?flatpak}
%global bootstrap_build false
%else
%ifarch %{bootstrap_arches}
%global bootstrap_build true
%else
%global bootstrap_build false
%endif
%endif
%global static_libs_target %{nil}
%global bootstrap_targets images %{static_libs_target} legacy-jre-image
%global release_targets images docs-zip %{static_libs_target} legacy-jre-image
%global debug_targets images %{static_libs_target} legacy-jre-image
%global hotspot_target hotspot
%if ((0%{?fedora} > 0) || (0%{?rhel} >= 9) || (0%{?epel} >= 9) || (0%{?oreon} >= 11))
%global is_dtstoolchain  system
%global dtsversion       %{nil}
%global dtsname          %{nil}
%global exclusive_arches %{java_arches}
%define dts_brs # Brs for system\
%else
%if ((0%{?epel}) > 0 && (0%{?epel} <= 8))
%global is_dtstoolchain  toolset
%global dtsversion       14
%global dtsname          gcc-toolset-%{dtsversion}
%global exclusive_arches %{java_arches}
%define dts_brs # Brs for toolset\
%else
"Unsupported system: fedora=0%{?fedora} rhel=0%{?rhel} epel=0%{?epel} centos=0%{?centos}"
exit 1
%endif
%endif
%if ((0%{?epel}) > 0 || (0%{?fedora} > 8) || (0%{?oreon} >= 11))
%global use_portable_bootjdk 0
%else
%global use_portable_bootjdk 1
%endif
%global pandoc_available 0
%global ourflags %(echo %optflags | sed -e 's|-Wall|-Wformat -Wno-cpp|' | sed -r -e 's|-O[0-9]*||' | sed -e 's|-flto=auto||' -e 's|-ffat-lto-objects||' -e 's|-flto||')
%global ourcppflags %(echo %ourflags | sed -e 's|-fexceptions||')
%global ourldflags %{__global_ldflags}
%ifarch x86_64
%global archinstall amd64
%global stapinstall x86_64
%endif
%ifarch ppc
%global archinstall ppc
%global stapinstall powerpc
%endif
%ifarch %{ppc64be}
%global archinstall ppc64
%global stapinstall powerpc
%endif
%ifarch %{ppc64le}
%global archinstall ppc64le
%global stapinstall powerpc
%endif
%ifarch %{ix86}
%global archinstall i686
%global stapinstall i386
%endif
%ifarch ia64
%global archinstall ia64
%global stapinstall ia64
%endif
%ifarch s390
%global archinstall s390
%global stapinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%global stapinstall s390
%endif
%ifarch %{arm}
%global archinstall arm
%global stapinstall arm
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%global stapinstall arm64
%endif
%ifarch riscv64
%global archinstall riscv64
%global stapinstall %{_target_cpu}
%endif
%ifarch sparcv9
%global archinstall sparc
%global stapinstall %{_target_cpu}
%endif
%ifarch sparc64
%global archinstall sparcv9
%global stapinstall %{_target_cpu}
%endif
%ifarch noarch
%global archinstall %{nil}
%global stapinstall %{nil}
%endif
%ifarch %{systemtap_arches}
%global with_systemtap 0
%else
%global with_systemtap 0
%endif
%global featurever 25
%global interimver 0
%global updatever 3
%global patchver 0
%global buildjdkver 25
%if 0%{?rhel} && !0%{?epel} || (0%{?oreon} >= 11)
  %global lts_designator \"LTS\"
  %global lts_designator_zip -%{lts_designator}
%else
  %global lts_designator \"\"
  %global lts_designator_zip \"\"
%endif
%global oj_vendor Red Hat, Inc.
%global oj_vendor_url https://www.redhat.com/
%if 0%{?epel}
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL&component=%{component}&version=epel%{epel}
%else
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&component=%{component}&version=%{fedora}
%else
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global oj_vendor_bug_url https://access.redhat.com/support/cases/
%else
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi
%endif
%endif
%endif
%global oj_vendor_version (Red_Hat-%{version}-%{rpmrelease})
%global icedteaver      6.0.0pre00-c848b93a8598
%global fipsver 57722aab802
%global newjavaver %{featurever}.%{interimver}.%{updatever}.%{patchver}
%global javaver         %{featurever}
%global filever %(svn=%{newjavaver}; for i in 1 2 3 4 5 6 ; do svn=${svn%%.0} ; done; echo ${svn})
%global vcstag jdk-%{filever}+%{buildver}%{?tagsuffix:-%{tagsuffix}}
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{vcstag}
%global top_level_dir_name_backup %{top_level_dir_name}-backup
%global buildver        9
%global rpmrelease      1
%if %is_system_jdk
%global combiver $( expr 20 '*' %{patchver} + %{buildver} )
%global priority %( printf '%02d%02d%02d%02d' %{featurever} %{interimver} %{updatever} %{combiver} )
%else
%global priority %( printf '%08d' 1 )
%endif
%global is_ga           1
%global build_type GA
%global ea_designator ""
%global ea_designator_zip %{nil}
%global extraver %{nil}
%global eaprefix %{nil}
%global compatiblename  java-%{featurever}-%{origin}
%global fullversion     %{compatiblename}-%{version}-%{release}
%global jdkimage                jdk
%global static_libs_image       static-libs-graal
%define buildoutputdir() %{expand:build/jdk%{featurever}.build%{?1}}
%define installoutputdir() %{expand:install/jdk%{featurever}.install%{?1}}
%global miscinstalloutputdir install
%global altjavaoutputdir %{miscinstalloutputdir}/altjava.install
%define packageoutputdir() %{expand:packages/jdk%{featurever}.packages%{?1}}
%define uniquejavadocdir()    %{expand:%{fullversion}.%{_arch}%{?1}}
%define uniquesuffix()        %{expand:%{fullversion}.%{_arch}%{?1}}
%global jreimage                jre
%if ((0%{?fedora} > 0) || (0%{?epel} > 0) || (0%{?oreon} >= 11))
%define regexBase %{version}-%{release}
%else
%define regexBase el%{rhel}\\(_[0-9]\\)*
%endif
%define jreportablenameimpl() %(echo %{uniquesuffix ""} | sed "s;%{regexBase};\\0.portable%{1}.jre;g" | sed "s;openjdkportable;el;g")
%define jdkportablenameimpl() %(echo %{uniquesuffix ""} | sed "s;%{regexBase};\\0.portable%{1}.jdk;g" | sed "s;openjdkportable;el;g")
%define jdkportablesourcesnameimpl() %(echo %{uniquesuffix ""} | sed "s;%{regexBase};\\0.portable%{1}.sources;g" | sed "s;openjdkportable;el;g" | sed "s;.%{_arch};.noarch;g")
%define staticlibsportablenameimpl() %(echo %{uniquesuffix ""} | sed "s;%{regexBase};\\0.portable%{1}.static-libs;g" | sed "s;openjdkportable;el;g")
%define jmodsportablenameimpl() %(echo %{uniquesuffix ""} | sed "s;%{regexBase};\\0.portable%{1}.jmods;g" | sed "s;openjdkportable;el;g")
%define jreportablearchive()  %{expand:%{jreportablenameimpl -- %%{1}}.tar.xz}
%define jdkportablearchive()  %{expand:%{jdkportablenameimpl -- %%{1}}.tar.xz}
%define jdkportablesourcesarchive()  %{expand:%{jdkportablesourcesnameimpl -- %%{1}}.tar.xz}
%define staticlibsportablearchive()  %{expand:%{staticlibsportablenameimpl -- %%{1}}.tar.xz}
%define jmodsportablearchive()  %{expand:%{jmodsportablenameimpl -- %%{1}}.tar.xz}
%define jreportablename()     %{expand:%{jreportablenameimpl -- %%{1}}}
%define jdkportablename()     %{expand:%{jdkportablenameimpl -- %%{1}}}
%define jdkportablesourcesname()     %{expand:%{jdkportablesourcesnameimpl -- %%{1}}}
%define staticlibsportablename()     %{expand:%{jdkportablenameimpl -- %%{1}}}
%define docportablename() %(echo %{uniquesuffix ""} | sed "s;%{regexBase};\\0.portable.docs;g" | sed "s;openjdkportable;el;g")
%define docportablearchive()  %{docportablename}.tar.xz
%define miscportablename() %(echo %{uniquesuffix ""} | sed "s;%{regexBase};\\0.portable.misc;g" | sed "s;openjdkportable;el;g")
%define miscportablearchive()  %{miscportablename}.tar.xz
%define jreportablearchiveForFiles()  %(echo %{jreportablearchive -- ""})
%define jdkportablearchiveForFiles()  %(echo %{jdkportablearchive -- ""})
%define jdkportablesourcesarchiveForFiles()  %(echo %{jdkportablesourcesarchive -- ""})
%define staticlibsportablearchiveForFiles()  %(echo %{staticlibsportablearchive -- ""})
%define jmodsportablearchiveForFiles()  %(echo %{jmodsportablearchive -- ""})
%ifarch %{fastdebug_arches}
%global bootdebugpkg fastdebug
%endif
%global bootjdkpkg_name java-%{featurever}-%{origin}
%global bootjdkpkg %{bootjdkpkg_name}-portable-devel%{?bootdebugpkg:-%{bootdebugpkg}} >= %{buildjdkver}
%global bootjdkzip %{_jvmdir}/%{bootjdkpkg_name}-*.portable%{?bootdebugpkg:.%{bootdebugpkg}}.jdk.%{_arch}.tar.xz
%global bootjdk %{_builddir}/%{uniquesuffix -- ""}/%{bootjdkpkg_name}.boot
%if %{with fresh_libjvm} && %{buildjdkver} == %{featurever}
%global build_hotspot_first 1
%else
%global build_hotspot_first 0
%endif
%global _privatelibs libsplashscreen[.]so.*|libawt_xawt[.]so.*|libjli[.]so.*|libattach[.]so.*|libawt[.]so.*|libextnet[.]so.*|libawt_headless[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjimage[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmanagement_agent[.]so.*|libmanagement_ext[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libprefs[.]so.*|librmi[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsystemconf[.]so.*|libzip[.]so.*%{freetype_lib}
%global _publiclibs libjawt[.]so.*|libjava[.]so.*|libjvm[.]so.*|libverify[.]so.*|libjsig[.]so.*
%if %is_system_jdk
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
%global __provides_exclude_from ^.*/%{uniquesuffix -- %{debug_suffix_unquoted}}/.*$
%global __requires_exclude_from ^.*/%{uniquesuffix -- %{debug_suffix_unquoted}}/.*$
%global __provides_exclude_from ^.*/%{uniquesuffix -- %{fastdebug_suffix_unquoted}}/.*$
%global __requires_exclude_from ^.*/%{uniquesuffix -- %{fastdebug_suffix_unquoted}}/.*$
%else
%global __provides_exclude ^(%{_privatelibs}|%{_publiclibs})$
%global __requires_exclude ^(%{_privatelibs}|%{_publiclibs})$
%endif
%ifarch %{zero_arches}
%global vm_variant zero
%else
%global vm_variant server
%endif
%global etcjavasubdir     %{_sysconfdir}/java/java-%{javaver}-%{origin}
%define etcjavadir()      %{expand:%{etcjavasubdir}/%{uniquesuffix -- %{?1}}}
%define sdkdir()        %{expand:%{uniquesuffix -- %{?1}}}
%define jrelnk()        %{expand:jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}%{?1}}
%define sdkbindir()     %{expand:%{_jvmdir}/%{sdkdir -- %{?1}}/bin}
%define jrebindir()     %{expand:%{_jvmdir}/%{sdkdir -- %{?1}}/bin}
%global alt_java_name     alt-java
%global generated_sources_name     generated_sources
%global rpm_state_dir %{_localstatedir}/lib/rpm-state/
%if 0%{?flatpak}
%global alternatives_requires /usr/sbin/alternatives
%else
%global alternatives_requires %{_sbindir}/alternatives
%endif
%define java_rpo() %{expand:
}
%define java_devel_rpo() %{expand:
}
%define java_static_libs_rpo() %{expand:
}
%define java_docs_rpo() %{expand:
}
%define java_misc_rpo() %{expand:
}
%global __jar_repack 0
%define component %(echo %{name} | sed "s;-portable%{?pkgos:-%{pkgos}};;g")
%if "%{?exclusive_arches}" == "%{nil}"
ExcludeArch: %{ix86}
%else
ExclusiveArch:  %{exclusive_arches}
%endif
Name:    java-25-%{origin}-portable%{?pkgos:-%{pkgos}}
Version: %{newjavaver}.%{buildver}
Release:        1%{?dist}
Epoch:   1
Summary:        OpenJDK 25 Runtime Environment portable edition
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30) || (0%{?oreon} >= 11)
Group:   Development/Languages
%endif
License:  Apache-1.1 AND Apache-2.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-BSD-with-advertising AND GPL-1.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-GPLv2-with-exceptions AND IJG AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND MPL-2.0 AND LicenseRef-Callaway-Public-Domain AND W3C AND Zlib AND ISC AND FTL AND LicenseRef-RSA
URL:      http://openjdk.java.net/
Source0:        https://%{origin}-sources.osci.io/%{origin}%{featurever}/%{origin}-%{filever}+%{buildver}.tar.xz
Source10: NEWS
Source11: alt-java.c
Source12: remove-intree-libraries.sh
Source13: TestCryptoLevel.java
Source14: TestECDSA.java
Source15: TestSecurityProperties.java
Source16: CheckVendor.java
Source18: TestTranslations.java
Patch1001: fips-%{featurever}u-%{fipsver}.patch
Patch2001: jdk8375294-handle-EOPNOTSUPP-in-copying.patch
%{dts_brs}
%ifarch %{zero_arches}
%endif
Provides: bundled(freetype) = 2.14.2
Provides: bundled(giflib) = 6.1.2
Provides: bundled(harfbuzz) = 12.3.2
Provides: bundled(lcms2) = 2.17.0
Provides: bundled(libjpeg) = 6b
Provides: bundled(libpng) = 1.6.57
Provides: bundled(zlib) = 1.3.2
%{java_rpo %{nil}}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  ca-certificates
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  elfutils-devel
BuildRequires:  file
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  java-25-openjdk-portable-devel
BuildRequires:  javapackages-filesystem
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libstdc++-static
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  nss-devel
BuildRequires:  pkgconfig
BuildRequires:  tar
BuildRequires:  unzip
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  zip
# /oreon:deps
%description
The %{origin_nice} %{featurever} runtime environment - portable edition.

%package sources
Summary: %{origin_nice} %{featurever} full patched sources of portable JDK
%description sources
The %{origin_nice} %{featurever} full patched sources of portable JDK to build, attach to debuggers or for debuginfo

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Using the echo macro breaks rpmdev-bumpspec, as it parses the first line of stdout :-(
echo "Preparing %{oj_vendor_version}"
echo "System is RHEL=%{?rhel}%{!?rhel:0}, CentOS=%{?centos}%{!?centos:0}, EPEL=%{?epel}%{!?epel:0}, Fedora=%{?fedora}%{!?fedora:0}"
echo "Build JDK version is %{buildjdkver}, bootstrap JDK package is %{bootjdkpkg}"

%if 0%{?_build_cpu:1}
  echo "CPU: %{_target_cpu}, arch install directory: %{archinstall}, SystemTap install directory: %{_build_cpu}"
%else
  %{error:Unrecognised architecture %{_target_cpu}}
%endif

if [ %{include_normal_build} -eq 0 -o  %{include_normal_build} -eq 1 ] ; then
  echo "include_normal_build is %{include_normal_build}"
else
  echo "include_normal_build is %{include_normal_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 11
fi
if [ %{include_debug_build} -eq 0 -o  %{include_debug_build} -eq 1 ] ; then
  echo "include_debug_build is %{include_debug_build}"
else
  echo "include_debug_build is %{include_debug_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 12
fi
if [ %{include_fastdebug_build} -eq 0 -o  %{include_fastdebug_build} -eq 1 ] ; then
  echo "include_fastdebug_build is %{include_fastdebug_build}"
else
  echo "include_fastdebug_build is %{include_fastdebug_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 13
fi
if [ %{include_debug_build} -eq 0 -a  %{include_normal_build} -eq 0 -a  %{include_fastdebug_build} -eq 0 ] ; then
  echo "You have disabled all builds (normal,fastdebug,slowdebug). That is a no go."
  exit 14
fi

%if %{with fresh_libjvm} && ! %{build_hotspot_first}
%{warn: The build of a fresh libjvm has been disabled due to a JDK version mismatch}
%{warn: Build JDK version is %{buildjdkver}, feature JDK version is %{featurever}}
%endif

export XZ_OPT="-T0"
%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 8 ] ; then
 echo "priority must be 8 digits in total, violated"
 exit 14
fi

# OpenJDK patches

# Patch the JDK
# This syntax is deprecated:
#    %%patchN [...]
# and should be replaced with:
#    %%patch -PN [...]
# For example:
#    %%patch1001 -p1
# becomes:
#    %%patch -P1001 -p1
# The replacement format suggested by recent (circa Fedora 38) RPM
# deprecation messages:
#    %%patch N [...]
# is not backward-compatible with prior (circa RHEL-8) versions of
# rpmbuild.
pushd %{top_level_dir_name}
# Add crypto policy and FIPS support
%patch -P1001 -p1
# Add EOPNOTSUPP patch
%patch -P2001 -p1
popd # openjdk

echo "Generating %{alt_java_name} man page"
altjavamanpage=%{top_level_dir_name}/src/java.base/share/man/%{alt_java_name}.md
altjavatext="Hardened java binary recommended for launching untrusted code from the Web e.g. javaws"
sed -r -e 's|([^/.])java([^./])|\1alt-java\2|g' %{top_level_dir_name}/src/java.base/share/man/java.md | \
    sed -e 's|JAVA(|ALT-JAVA(|' | \
    sed -e "s|java - launch a Java application|alt-java - ${altjavatext}|" >> ${altjavamanpage}

# The OpenJDK version file includes the current
# upstream version information. For some reason,
# configure does not automatically use the
# default pre-version supplied there (despite
# what the file claims), so we pass it manually
# to configure
VERSION_FILE=$(pwd)/%{top_level_dir_name}/make/conf/version-numbers.conf
if [ -f ${VERSION_FILE} ] ; then
    UPSTREAM_EA_DESIGNATOR=$(grep '^DEFAULT_PROMOTED_VERSION_PRE' ${VERSION_FILE} | cut -d '=' -f 2)
else
    echo "Could not find OpenJDK version file.";
    exit 16
fi
if [ "x${UPSTREAM_EA_DESIGNATOR}" != "x%{ea_designator}" ] ; then
    echo "WARNING: Designator mismatch";
    echo "Spec file is configured for a %{build_type} build with designator '%{ea_designator}'"
    echo "Upstream version-pre setting is '${UPSTREAM_EA_DESIGNATOR}'";
    exit 17
fi

# Systemtap is processed in rpms on fedoras and epels

# Prepare desktop files
# Portables do not have desktop integration

# Extract devkit
%if "%{is_dtstoolchain}" ==  "devkit"
  devkittarball=%{_datadir}/%{dtsname}/sdk-%{_target_cpu}-%{_target_os}-gnu*.tar.gz
  echo "Extracting devkit ${devkittarball}";
  mkdir devkit;
  tar -C devkit --strip-components=1 -xzf ${devkittarball}
  DEVKIT_ROOT=$(pwd)/devkit
  source ${DEVKIT_ROOT}/devkit.info
  echo "Installed ${DEVKIT_NAME} devkit"
%else
%if 0%{?centos} > 0
  echo "No devkit for CentOS %{?centos}"
%else
  echo "No devkit for %{_target_cpu} on RHEL %{?rhel}";
%endif
%endif

  # Extract build JDK
  pushd %{_jvmdir}
  sha256sum --check %{bootjdkzip}.sha256sum
  popd
  tar -xJf %{bootjdkzip}
  mv java-%{featurever}-openjdk-%{buildjdkver}* %{bootjdk}
  # Print release information
  echo "Installed boot JDK:"
  cat %{bootjdk}/release

%build

export NUM_PROC=%(/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :)
export NUM_PROC=${NUM_PROC:-1}
%if 0%{?_smp_ncpus_max}
[ ${NUM_PROC} -gt %{?_smp_ncpus_max} ] && export NUM_PROC=%{?_smp_ncpus_max}
%endif
mem_mb=$(awk '/MemAvailable:/ {print int($2/1024)}' /proc/meminfo 2>/dev/null || echo 65536)
job_cap=$((mem_mb / 4096))
[ ${job_cap} -lt 1 ] && job_cap=1
[ ${job_cap} -gt 8 ] && job_cap=8
[ ${NUM_PROC} -gt ${job_cap} ] && export NUM_PROC=${job_cap}
echo "Using NUM_PROC=${NUM_PROC} (mem_mb=${mem_mb})"
unset MAKEFLAGS
export XZ_OPT="-T${NUM_PROC}"
%ifarch s390x sparc64 alpha %{power64} %{aarch64} riscv64
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif
EXTRA_CFLAGS="%ourcppflags"
EXTRA_CPP_FLAGS="%ourcppflags"
%ifarch %{power64} ppc
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
%ifarch %{ix86}
EXTRA_CFLAGS="$(echo ${EXTRA_CFLAGS} | sed -e 's|-mstackrealign|-mincoming-stack-boundary=2 -mpreferred-stack-boundary=4|')"
EXTRA_CPP_FLAGS="$(echo ${EXTRA_CPP_FLAGS} | sed -e 's|-mstackrealign|-mincoming-stack-boundary=2 -mpreferred-stack-boundary=4|')"
%endif
%if "%{is_dtstoolchain}" ==  "devkit"
EXTRA_CFLAGS="$(echo ${EXTRA_CFLAGS} | sed -e 's|-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1||')"
EXTRA_CPP_FLAGS="$(echo ${EXTRA_CPP_FLAGS} | sed -e 's|-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1||')"
EXTRA_CFLAGS="${EXTRA_CFLAGS} -gdwarf-4"
EXTRA_CPP_FLAGS="${EXTRA_CPP_FLAGS} -gdwarf-4"
%endif
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-lto"
EXTRA_CPP_FLAGS="$EXTRA_CPP_FLAGS -fno-lto"
export EXTRA_CFLAGS EXTRA_CPP_FLAGS
VERSION_FILE="$(pwd)"/"%{top_level_dir_name}"/make/conf/version-numbers.conf
OPENJDK_UPSTREAM_TAG_EPOCH="$(stat --format=%Y "${VERSION_FILE}")"
function buildjdk() {
    local outputdir=${1}
    local buildjdk=${2}
    local maketargets="${3}"
    local debuglevel=${4}
    local link_opt=${5}
    local debug_symbols=${6}
    local devkit=${7}
    local top_dir_abs_src_path=$(pwd)/%{top_level_dir_name}
    local top_dir_abs_build_path=$(pwd)/${outputdir}
    if [ "x%{link_type}" = "xbundled" ] ; then
        libc_link_opt="static";
    else
        libc_link_opt="dynamic";
    fi
    echo "Using output directory: ${outputdir}";
    echo "Checking build JDK ${buildjdk} is operational..."
    ${buildjdk}/bin/java -version
    echo "Using make targets: ${maketargets}"
    echo "Using debuglevel: ${debuglevel}"
    echo "Using link_opt: ${link_opt}"
    echo "Using debug_symbols: ${debug_symbols}"
    echo "Building %{newjavaver}-%{buildver}, pre=%{ea_designator}, opt=%{lts_designator}"
%if "%{is_dtstoolchain}" ==  "devkit"
    LIBPATH="${devkit}/lib:${devkit}/lib64"
    echo "Setting library path to ${LIBPATH}"
%else
%if "%{is_dtstoolchain}" ==  "toolset"
    toolset=/opt/rh/%{dtsname}/root/
    LIBPATH="${toolset}/lib:${toolset}/lib64"
    echo "Setting library path to ${LIBPATH}"
%else
    LIBPATH=${LD_LIBRARY_PATH}
    echo "Keeping library path as ${LIBPATH}"
%endif
%endif
    mkdir -p ${outputdir}
    pushd ${outputdir}
    LD_LIBRARY_PATH=${LIBPATH} \
    %{?dts_command} bash ${top_dir_abs_src_path}/configure \
%ifarch %{zero_arches}
    --with-jvm-variants=zero \
%endif
%if "%{is_dtstoolchain}" ==  "devkit"
    --with-devkit=${devkit} \
%endif
%if "%{is_dtstoolchain}" ==  "toolset"
    --with-extra-path="/opt/rh/%{dtsname}/root/bin:/opt/rh/%{dtsname}/root/usr/bin" \
    --with-toolchain-path="/opt/rh/%{dtsname}/root/bin:/opt/rh/%{dtsname}/root/usr/bin" \
%endif
    --with-version-build=%{buildver} \
    --with-version-pre="%{ea_designator}" \
    --with-version-opt="%{lts_designator}" \
    --with-vendor-version-string="%{oj_vendor_version}" \
    --with-vendor-name="%{oj_vendor}" \
    --with-vendor-url="%{oj_vendor_url}" \
    --with-vendor-bug-url="%{oj_vendor_bug_url}" \
    --with-vendor-vm-bug-url="%{oj_vendor_bug_url}" \
    --with-boot-jdk=${buildjdk} \
    --with-boot-jdk-jvmargs="-Xmx4g -XX:+UseParallelGC -XX:CICompilerCount=2 -XX:ParallelGCThreads=2" \
    --with-debug-level=${debuglevel} \
    --with-native-debug-symbols="${debug_symbols}" \
    --disable-absolute-paths-in-output \
    --enable-unlimited-crypto \
    --enable-linkable-runtime \
    --enable-keep-packaged-modules \
    --with-zlib=%{link_type} \
    --with-freetype=%{link_type} \
    --with-libjpeg=${link_opt} \
    --with-giflib=${link_opt} \
    --with-libpng=${link_opt} \
    --with-lcms=${link_opt} \
    --with-harfbuzz=${link_opt} \
    --with-stdc++lib=${libc_link_opt} \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC" \
    --with-source-date="version" \
    --disable-javac-server \
%ifarch %{zgc_arches}
    --with-jvm-features=zgc \
%endif
    --disable-warnings-as-errors  \
    || ( pwd; cat $(find | grep config.log) && false )
    cat spec.gmk
    LD_LIBRARY_PATH=${LIBPATH} \
    %{?dts_command} make LOG=info JOBS=${NUM_PROC} \
      WARNINGS_ARE_ERRORS="-Wno-error" \
      CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" $maketargets ||\
        ( pwd; find ${top_dir_abs_src_path} ${top_dir_abs_build_path} -name \"hs_err_pid*.log\" | xargs cat && false )
    popd
}
function installjdk() {
    local outputdir=${1}
    local installdir=${2}
    local jdkimagepath=${installdir}/images/%{jdkimage}
    local jreimagepath=${installdir}/images/%{jreimage}
    echo "Installing build from ${outputdir} to ${installdir}..."
    mkdir -p ${installdir}
    echo "Installing images..."
    mv ${outputdir}/images ${installdir}
    if [ -d ${outputdir}/bundles ] ; then
        echo "Installing bundles...";
        mv ${outputdir}/bundles ${installdir} ;
    fi
%if !%{with artifacts}
    echo "Removing output directory...";
    rm -rf ${outputdir}
%endif
    for imagepath in ${jdkimagepath} ${jreimagepath}; do
        if [ -d ${imagepath} ] ; then
            find ${imagepath} -iname '*.jar' -exec chmod ugo+r {} \;
            find ${imagepath} -iname '*.so' -exec chmod +x {} \;
            find ${imagepath}/bin/ -exec chmod +x {} \;
            install -m 644 %{SOURCE10} ${imagepath}
            cat ${imagepath}/release
        fi
    done
}
function genchecksum() {
    local checkedfile=${1}
    checkdir=$(dirname ${1})
    checkfile=$(basename ${1})
    echo "Generating checksum for ${checkfile} in ${checkdir}..."
    pushd ${checkdir}
    sha256sum ${checkfile} > ${checkfile}.sha256sum
    sha256sum --check ${checkfile}.sha256sum
    popd
}
function packFullPatchedSources() {
  srcpackagesdir=`pwd`
  createtar ${srcpackagesdir}/%{jdkportablesourcesarchive -- ""} --transform "s|^|%{jdkportablesourcesname -- ""}/|" %{top_level_dir_name}
  genchecksum ${srcpackagesdir}/%{jdkportablesourcesarchive -- ""}
}
function findgeneratedsources() {
  local targetDir=${1}
  local targetDirParent=$(dirname ${targetDir})
  local builtJdk=${2}
  local builtJdkName=$(basename ${builtJdk})
  local sources=${3}
  local sourcesName=$(basename ${sources})
  local sourcesParent=$(dirname ${sources})
  local target=${sourcesParent}/${targetDirParent}/%{generated_sources_name}
  local suffixes="cpp\|hpp\|h\|hh\|rl"
  suffixes=".*\.\($suffixes\)$"
  mkdir -p $target
  pushd ${builtJdk}
    mkdir -p ${target}/${builtJdkName}
    cp --parents $(find . | grep -e "$suffixes" -e "NONE$") ${target}/${builtJdkName}
  popd
  pushd ${sources}
    mkdir -p ${target}/${sourcesName}
    cp --parents $(find make | grep -e ".$suffixes" -e "NONE$") ${target}/${sourcesName}
  popd
}
function createtar() {
  tar -cJf  "$@"
}
function packagejdk() {
    local imagesdir=$(pwd)/${1}/images
    local docdir=$(pwd)/${1}/images/docs
    local bundledir=$(pwd)/${1}/bundles
    local packagesdir=$(pwd)/${2}
    local srcdir=$(pwd)/%{top_level_dir_name}
    local tapsetdir=$(pwd)/tapset
    local altjavadir=$(pwd)/${3}
    local gensources=$(pwd)/%{miscinstalloutputdir}/%{generated_sources_name}
    echo "Packaging build from ${imagesdir} to ${packagesdir}..."
    mkdir -p ${packagesdir}
    pushd ${imagesdir}
    if [ "x$suffix" = "x" ] ; then
        nameSuffix=""
    else
        nameSuffix=`echo "$suffix"| sed s/-/./`
    fi
    jdkname=%{jdkportablename -- "$nameSuffix"}
    jdkarchive=${packagesdir}/%{jdkportablearchive -- "$nameSuffix"}
    jmodsarchive=${packagesdir}/%{jmodsportablearchive -- "$nameSuffix"}
    jrename=%{jreportablename -- "$nameSuffix"}
    jrearchive=${packagesdir}/%{jreportablearchive -- "$nameSuffix"}
    staticname=%{staticlibsportablename -- "$nameSuffix"}
    staticarchive=${packagesdir}/%{staticlibsportablearchive -- "$nameSuffix"}
    debugarchive=${packagesdir}/%{jdkportablearchive -- "${nameSuffix}.debuginfo"}
    if [ "x$suffix" = "x" ] ; then
      docname=%{docportablename}
      docarchive=${packagesdir}/%{docportablearchive}
      built_doc_archive=jdk-%{filever}%{ea_designator_zip}+%{buildver}%{lts_designator_zip}-docs.zip
    fi
    miscname=%{miscportablename}
    miscarchive=${packagesdir}/%{miscportablearchive}
    mv %{jdkimage} ${jdkname}
    mv %{jreimage} ${jrename}
    if [ "x$suffix" = "x" ] ; then
        createtar ${debugarchive} $(find ${jdkname} -name \*.debuginfo)
        genchecksum ${debugarchive}
        mkdir ${docname}
        mv ${docdir} ${docname}
        mv ${bundledir}/${built_doc_archive} ${docname}
        createtar ${docarchive} ${docname}
        genchecksum ${docarchive}
        mkdir ${miscname}
        for s in 16 24 32 48 ; do
            cp -av ${srcdir}/src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png ${miscname}
        done
        cp -av ${altjavadir}/%{alt_java_name} ${miscname}
        cp -avr ${gensources} ${miscname}
        createtar ${miscarchive} ${miscname}
        genchecksum ${miscarchive}
    fi
    createtar ${jmodsarchive} --exclude='**.debuginfo' ${jdkname}/jmods
    genchecksum ${jmodsarchive}
    rm -rv ${jdkname}/jmods
    createtar ${jdkarchive} --exclude='**.debuginfo' ${jdkname}
    genchecksum ${jdkarchive}
    createtar ${jrearchive}  --exclude='**.debuginfo' ${jrename}
    genchecksum ${jrearchive}
    mv ${jdkname} %{jdkimage}
    mv ${jrename} %{jreimage}
    popd #images
}
packFullPatchedSources
%if "%{is_dtstoolchain}" ==  "devkit"
  DEVKIT_ROOT=$(pwd)/devkit
  source ${DEVKIT_ROOT}/devkit.info
  GCC="${DEVKIT_TOOLCHAIN_PATH}/gcc --sysroot=${DEVKIT_SYSROOT}"
  LIBPATH="${DEVKIT_ROOT}/lib:${DEVKIT_ROOT}/lib64"
%else
%if "%{is_dtstoolchain}" ==  "toolset"
    toolset=/opt/rh/%{dtsname}/root/
    GCC="${toolset}/usr/bin/gcc"
    LIBPATH="${toolset}/lib:${toolset}/lib64"
%else
  GCC=$(which gcc)
%endif
%endif
echo "Building %{SOURCE11}"
mkdir %{miscinstalloutputdir}
mkdir %{altjavaoutputdir}
LD_LIBRARY_PATH="${LIBPATH}" ${GCC} ${EXTRA_CFLAGS} -o %{altjavaoutputdir}/%{alt_java_name} %{SOURCE11}
echo "Building %{newjavaver}-%{buildver}, pre=%{ea_designator}, opt=%{lts_designator}"
  systemjdk=%{bootjdk}
for suffix in %{build_loop} ; do
  if [ "x$suffix" = "x" ] ; then
      debugbuild=release
  else
      debugbuild=`echo $suffix  | sed "s/-//g"`
  fi
  if [ "x$suffix" = "x" ] ; then
    debug_symbols=external
  else
    debug_symbols=internal
  fi
  builddir=%{buildoutputdir -- ${suffix}}
  bootbuilddir=boot${builddir}
  installdir=%{installoutputdir -- ${suffix}}
  bootinstalldir=boot${installdir}
  packagesdir=%{packageoutputdir -- ${suffix}}
  link_opt="%{link_type}"
  if echo $debugbuild | grep -q "debug" ; then
      maketargets="%{debug_targets}"
      run_bootstrap=false
  else
      maketargets="%{release_targets}"
      run_bootstrap=%{bootstrap_build}
  fi
  if ${run_bootstrap} ; then
      buildjdk ${bootbuilddir} ${systemjdk} "%{bootstrap_targets}" ${debugbuild} ${link_opt} ${debug_symbols} ${DEVKIT_ROOT}
      installjdk ${bootbuilddir} ${bootinstalldir}
      buildjdk ${builddir} $(pwd)/${bootinstalldir}/images/%{jdkimage} "${maketargets}" ${debugbuild} ${link_opt} ${debug_symbols} ${DEVKIT_ROOT}
      findgeneratedsources ${installdir} ${builddir} $(pwd)/%{top_level_dir_name}
      installjdk ${builddir} ${installdir}
      %{!?with_artifacts:rm -rf ${bootinstalldir}}
  else
      buildjdk ${builddir} ${systemjdk} "${maketargets}" ${debugbuild} ${link_opt} ${debug_symbols} ${DEVKIT_ROOT}
      findgeneratedsources ${installdir} ${builddir} $(pwd)/%{top_level_dir_name}
      installjdk ${builddir} ${installdir}
  fi
  packagejdk ${installdir} ${packagesdir} %{altjavaoutputdir}
done # end of release / debug cycle loop
%check

for suffix in %{build_loop} ; do
top_dir_abs_main_build_path=$(pwd)/%{installoutputdir -- ${suffix}}
export JAVA_HOME=${top_dir_abs_main_build_path}/images/%{jdkimage}
%if "%{is_dtstoolchain}" ==  "devkit"
  DEVKIT_ROOT=$(pwd)/devkit
  source ${DEVKIT_ROOT}/devkit.info
  NM="${DEVKIT_TOOLCHAIN_PATH}/nm"
%else
  NM=$(which nm)
%endif
READELF=$(which eu-readelf)
GDB=$(which gdb)
%ifarch %{jdk_test_arch}
  $JAVA_HOME/bin/javac -d . %{SOURCE13}
  $JAVA_HOME/bin/java --add-opens java.base/javax.crypto=ALL-UNNAMED TestCryptoLevel
  $JAVA_HOME/bin/javac -d . %{SOURCE14}
  $JAVA_HOME/bin/java $(echo $(basename %{SOURCE14})|sed "s|\.java||")
  $JAVA_HOME/bin/javac -d . %{SOURCE15}
  export PROG=$(echo $(basename %{SOURCE15})|sed "s|\.java||")
  export SEC_DEBUG="-Djava.security.debug=properties"
  $JAVA_HOME/bin/java ${SEC_DEBUG} ${PROG} false
  $JAVA_HOME/bin/java ${SEC_DEBUG} -Djava.security.disableSystemPropertiesFile=false ${PROG} false
  $JAVA_HOME/bin/javac -d . %{SOURCE16}
  $JAVA_HOME/bin/java $(echo $(basename %{SOURCE16})|sed "s|\.java||") "%{oj_vendor}" "%{oj_vendor_url}" "%{oj_vendor_bug_url}" "%{oj_vendor_version}"
%if ! 0%{?flatpak}
  $JAVA_HOME/bin/javac -d . %{SOURCE18}
  $JAVA_HOME/bin/java $(echo $(basename %{SOURCE18})|sed "s|\.java||") JRE || echo "Fedora is often ahead in timezones, ignoring"
  $JAVA_HOME/bin/java -Djava.locale.providers=CLDR $(echo $(basename %{SOURCE18})|sed "s|\.java||") CLDR || echo "Fedora is often ahead in timezones, ignoring"
%endif
  jtreg_test=$(pwd)/%{top_level_dir_name}/test/jdk/sun/security/lib/CheckBlockedCerts.java
  jtreg_dir=$(dirname ${jtreg_test})
  $JAVA_HOME/bin/java --add-exports java.base/sun.security.util=ALL-UNNAMED -Dtest.src=${jtreg_dir} ${jtreg_test}
  unzip -l $JAVA_HOME/lib/src.zip | grep 'sun.misc.Unsafe'
  $JAVA_HOME/bin/javap -c -l java.lang.Object | grep "Compiled from"
  $JAVA_HOME/bin/javap -c -l java.lang.Object | grep LineNumberTable
  $JAVA_HOME/bin/javap -c -l java.lang.Object | grep LocalVariableTable
  $JAVA_HOME/bin/javap -c -l java.nio.ByteBuffer | grep "Compiled from"
  $JAVA_HOME/bin/javap -c -l java.nio.ByteBuffer | grep LineNumberTable
  $JAVA_HOME/bin/javap -c -l java.nio.ByteBuffer | grep LocalVariableTable
%else
  $JAVA_HOME/bin/java -version
%endif
if ! ${NM} $JAVA_HOME/bin/java | grep set_speculation ; then true ; else false; fi
%ifarch %{ssbd_arches}
${NM} %{altjavaoutputdir}/%{alt_java_name} | grep prctl
%else
if ! ${NM} %{altjavaoutputdir}/%{alt_java_name} | grep prctl ; then true ; else false; fi
%endif
if [ "x$suffix" = "x" ] ; then
  so_suffix="debuginfo"
else
  so_suffix="so"
fi
find "$JAVA_HOME" -iname "*.$so_suffix" -print0 | while read -d $'\0' lib
do
  if [ -f "$lib" ] ; then
    echo "Testing $lib for debug symbols"
    ${READELF} -S "$lib" | grep "] .debug_"
    test $(${READELF} -S "$lib" | grep -E "\]\ .debug_(info|abbrev)" | wc --lines) == 2
    old_IFS="$IFS"
    IFS=$'\n'
    for line in $(${READELF} -s "$lib" | grep "00000000      0 FILE    LOCAL  DEFAULT")
    do
      echo "$line" | grep -E "ABS ((.*/)?[-_a-zA-Z0-9]+\.(c|cc|cpp|cxx|o|S|oS))?$"
    done
    IFS="$old_IFS"
    if [ "`basename $lib`" = "libjvm.so" ]; then
      ${READELF} -s "$lib" | \
        grep -E "00000000      0 FILE    LOCAL  DEFAULT      ABS javaCalls.(cpp|o)$"
    fi
    ${READELF} -S "$lib" | grep 'gnu'
    if ${READELF} -S "$lib" | grep '] .gnu_debuglink' | grep PROGBITS; then
      echo "bad .gnu_debuglink section."
      ${READELF} -x .gnu_debuglink "$lib"
      false
    fi
  fi
done
${GDB} -q "$JAVA_HOME/bin/java" <<EOF | tee gdb.out
handle SIGSEGV pass nostop noprint
handle SIGILL pass nostop noprint
set breakpoint pending on
break javaCalls.cpp:58
commands 1
backtrace
quit
end
run -version
EOF
%ifarch %{gdb_arches}
grep 'JavaCallWrapper::JavaCallWrapper' gdb.out
%endif
done
%install
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}
 mv %{jdkportablesourcesarchive -- ""} $RPM_BUILD_ROOT%{_jvmdir}/
 mv %{jdkportablesourcesarchive -- ""}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
for suffix in %{build_loop} ; do
    packagesdir=%{packageoutputdir -- ${suffix}}
    if [ "x$suffix" == "x" ] ; then
        nameSuffix=""
    else
        nameSuffix=`echo "$suffix"| sed s/-/./`
    fi
    jdkarchive=${packagesdir}/%{jdkportablearchive -- "$nameSuffix"}
    jmodsarchive=${packagesdir}/%{jmodsportablearchive -- "$nameSuffix"}
    jrearchive=${packagesdir}/%{jreportablearchive -- "$nameSuffix"}
    staticarchive=${packagesdir}/%{staticlibsportablearchive -- "$nameSuffix"}
    debugarchive=${packagesdir}/%{jdkportablearchive -- "${nameSuffix}.debuginfo"}
    mv ${jdkarchive} $RPM_BUILD_ROOT%{_jvmdir}/
    mv ${jdkarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
    mv ${jmodsarchive} $RPM_BUILD_ROOT%{_jvmdir}/
    mv ${jmodsarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
    mv ${jrearchive} $RPM_BUILD_ROOT%{_jvmdir}/
    mv ${jrearchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
    if [ "x$suffix" = "x" ] ; then
        mv ${debugarchive} $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${debugarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
    fi
done
    if [ "x$suffix" = "x" ] ; then
        docarchive=${packagesdir}/%{docportablearchive}
        miscarchive=${packagesdir}/%{miscportablearchive}
        mv ${docarchive} $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${docarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${miscarchive} $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${miscarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
   fi
for file in `ls $RPM_BUILD_ROOT%{_jvmdir}/*.sha256sum` ; do
    ls -l $file ;
    cat $file ;
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n java-25-openjdk-portable-sources -f %{oreon_filedir}/java-25-openjdk-portable-sources.list

%changelog

%autochangelog
