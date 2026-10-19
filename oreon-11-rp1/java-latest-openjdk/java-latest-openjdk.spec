%global source0_hash none
%global source31_hash dee152c42d1c0be89c94d6dd59de82b27301209a65d1a4f90e69c2b2637e2fbb
%if 0%{?oreon} >= 11
%undefine _distro_extra_cflags
%undefine _distro_extra_cxxflags
%undefine _distro_extra_fflags
%undefine _distro_extra_ldflags
%endif
%bcond_without fastdebug
%bcond_without slowdebug
%bcond_without release
%bcond_without staticlibs
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
%define debug_package %{nil}
%define __brp_strip %{nil}
%define add_determinism_options --handler=-jar
%global freetype_lib |libfreetype[.]so.*
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
%global systemtap_arches %{jit_arches}
%global aot_arches      x86_64 %{aarch64}
%global sa_arches       %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} %{arm} riscv64
%global share_arches    %{jit_arches}
%global shenandoah_arches x86_64 %{aarch64} riscv64
%global zgc_arches x86_64 riscv64
%global ssbd_arches x86_64
%global svml_arches x86_64
%global simdsort_arches x86_64
%global sleef_arches aarch64 riscv64
%if (0%{?rhel} > 0 && 0%{?rhel} < 8) || (0%{?oreon} >= 11)
%global gdb_arches %{arm} %{aarch64} %{ix86} %{power64} sparcv9 sparc64 x86_64 %{zero_arches}
%else
%global gdb_arches %{jit_arches} %{zero_arches}
%endif
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
%ifarch %{zero_arches}
%global vm_variant zero
%else
%global vm_variant server
%endif
%global debugedit %( if [ -f "%{_rpmconfigdir}/debugedit"  ]; then echo "%{_rpmconfigdir}/debugedit" ; else echo "/usr/bin/debugedit"; fi )
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)
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
%global with_systemtap 1
%else
%global with_systemtap 0
%endif
%global featurever 26
%global interimver 0
%global updatever 1
%global patchver 0
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
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL&component=%{name}&version=epel%{epel}
%else
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&component=%{name}&version=%{fedora}
%else
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global oj_vendor_bug_url https://access.redhat.com/support/cases/
%else
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi
%endif
%endif
%endif
%global oj_vendor_version (Red_Hat-%{version}-%{release})
%global icedteaver      6.0.0pre00-c848b93a8598
%global fipsver 57722aab802
%global nssadapter_version 0.1.1
%global nssadapter_name nssadapter-%{nssadapter_version}
%global crypto_policy_active true
%global newjavaver %{featurever}.%{interimver}.%{updatever}.%{patchver}
%global javaver         %{featurever}
%global filever %(svn=%{newjavaver}; for i in 1 2 3 4 5 6 ; do svn=${svn%%.0} ; done; echo ${svn})
%global vcstag jdk-%{filever}+%{buildver}%{?tagsuffix:-%{tagsuffix}}
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{vcstag}-
%global top_level_dir_name_backup %{top_level_dir_name}-backup
%global buildver        8
%global rpmrelease      2
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
%global compatiblename  %{name}
%global portable_compatiblename java-%{featurever}-%{origin}
%define fullversion()     %{expand:%{compatiblename}%{?1}-%{version}-%{release}}
%define installoutputdir() %{expand:jdk%{featurever}.install-nsscp%{?1}}
%global static_libs_root        lib/static
%global static_libs_arch_dir    %{static_libs_root}/linux-%{archinstall}
%global static_libs_install_dir %{static_libs_arch_dir}/glibc
%define uniquejavadocdir() %{expand:%{compatiblename}%{?1}}
%define uniquesuffix() %{expand:%{compatiblename}%{?1}}
%global _privatelibs libsplashscreen[.]so.*|libawt_xawt[.]so.*|libjli[.]so.*|libattach[.]so.*|libawt[.]so.*|libextnet[.]so.*|libawt_headless[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjimage[.]so.*|libjsound[.]so.*|libjsvml[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmanagement_agent[.]so.*|libmanagement_ext[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libprefs[.]so.*|librmi[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsimdsort[.]so.*|libsleef[.]so.*|libsyslookup[.]so.*|libzip[.]so.*%{freetype_lib}
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
%global etcjavasubdir     %{_sysconfdir}/java/java-%{javaver}-%{origin}
%define etcjavadir()      %{expand:%{etcjavasubdir}/%{uniquesuffix -- %{?1}}}
%define sdkdir()        %{expand:%{uniquesuffix -- %{?1}}}
%define sdkbindir()     %{expand:%{_jvmdir}/%{sdkdir -- %{?1}}/bin}
%define jrebindir()     %{expand:%{_jvmdir}/%{sdkdir -- %{?1}}/bin}
%global alt_java_name     alt-java
%global generated_sources_name     generated_sources
%global rpm_state_dir %{_localstatedir}/lib/rpm-state/
%global repack_file repack.info
%if 0%{?flatpak}
%global alternatives_requires /usr/sbin/alternatives
%global javazidir /usr/share/javazi-1.8
%global portablejvmdir /usr/lib/jvm
%else
%global alternatives_requires %{_sbindir}/alternatives
%global javazidir %{_datadir}/javazi-1.8
%global portablejvmdir %{_jvmdir}
%endif
%global family %{name}.%{_arch}
%global family_noarch  %{name}
%if 0%{?java_arches:1}
ExclusiveArch:  %{java_arches}
%else
ExcludeArch: %{ix86}
%endif
%global update_desktop_icons /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%define post_script() %{expand:
update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
}
%define priority_for() %{expand:%[%{?1:1}%{!?1:0} ? %{priority} - 1 : %{priority}]}
%global man_comp .gz
%define alternatives_java_install() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
alternatives --install %{_bindir}/java java %{jrebindir -- %{?1}}/java %{priority_for -- %{?1}} \\
  --slave %{_jvmdir}/jre jre %{_jvmdir}/%{sdkdir -- %{?1}} \\
  --slave %{_bindir}/%{alt_java_name} %{alt_java_name} %{jrebindir -- %{?1}}/%{alt_java_name} \\
  --slave %{_bindir}/keytool keytool %{jrebindir -- %{?1}}/keytool \\
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir -- %{?1}}/rmiregistry \\
  --slave %{_mandir}/man1/java.1%{man_comp} java.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/java.1 \\
  --slave %{_mandir}/man1/%{alt_java_name}.1%{man_comp} %{alt_java_name}.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/%{alt_java_name}.1 \\
  --slave %{_mandir}/man1/keytool.1%{man_comp} keytool.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/keytool.1 \\
  --slave %{_mandir}/man1/rmiregistry.1%{man_comp} rmiregistry.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/rmiregistry.1
alternatives --install %{_jvmdir}/jre-%{origin} jre_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}} %{priority_for -- %{?1}}
alternatives --install %{_jvmdir}/jre-%{javaver} jre_%{javaver} %{_jvmdir}/%{sdkdir -- %{?1}} %{priority_for -- %{?1}}
alternatives --install %{_jvmdir}/jre-%{javaver}-%{origin} jre_%{javaver}_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}} %{priority_for -- %{?1}}
}
%define post_headless() %{expand:
%{alternatives_java_install -- %{?1}}
update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
}
%define postun_script() %{expand:
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{update_desktop_icons}
fi
}
%define preun_headless() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
if [ $1 -eq 0 ]
then
  alternatives --remove java %{jrebindir -- %{?1}}/java
  alternatives --remove jre_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}}
  alternatives --remove jre_%{javaver} %{_jvmdir}/%{sdkdir -- %{?1}}
  alternatives --remove jre_%{javaver}_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}}
fi
}
%define posttrans_script() %{expand:
%{update_desktop_icons}
}
%define alternatives_javac_install() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
alternatives --install %{_bindir}/javac javac %{sdkbindir -- %{?1}}/javac %{priority_for -- %{?1}} \\
  --slave %{_jvmdir}/java java_sdk %{_jvmdir}/%{sdkdir -- %{?1}} \\
  --slave %{_bindir}/jlink jlink %{sdkbindir -- %{?1}}/jlink \\
  --slave %{_bindir}/jmod jmod %{sdkbindir -- %{?1}}/jmod \\
%ifarch %{sa_arches}
%ifnarch %{zero_arches}
  --slave %{_bindir}/jhsdb jhsdb %{sdkbindir -- %{?1}}/jhsdb \\
%endif
%endif
  --slave %{_bindir}/jar jar %{sdkbindir -- %{?1}}/jar \\
  --slave %{_bindir}/jarsigner jarsigner %{sdkbindir -- %{?1}}/jarsigner \\
  --slave %{_bindir}/javadoc javadoc %{sdkbindir -- %{?1}}/javadoc \\
  --slave %{_bindir}/javap javap %{sdkbindir -- %{?1}}/javap \\
  --slave %{_bindir}/jcmd jcmd %{sdkbindir -- %{?1}}/jcmd \\
  --slave %{_bindir}/jconsole jconsole %{sdkbindir -- %{?1}}/jconsole \\
  --slave %{_bindir}/jdb jdb %{sdkbindir -- %{?1}}/jdb \\
  --slave %{_bindir}/jdeps jdeps %{sdkbindir -- %{?1}}/jdeps \\
  --slave %{_bindir}/jdeprscan jdeprscan %{sdkbindir -- %{?1}}/jdeprscan \\
  --slave %{_bindir}/jfr jfr %{sdkbindir -- %{?1}}/jfr \\
  --slave %{_bindir}/jimage jimage %{sdkbindir -- %{?1}}/jimage \\
  --slave %{_bindir}/jinfo jinfo %{sdkbindir -- %{?1}}/jinfo \\
  --slave %{_bindir}/jmap jmap %{sdkbindir -- %{?1}}/jmap \\
  --slave %{_bindir}/jnativescan jnativescan %{sdkbindir -- %{?1}}/jmap \\
  --slave %{_bindir}/jps jps %{sdkbindir -- %{?1}}/jps \\
  --slave %{_bindir}/jpackage jpackage %{sdkbindir -- %{?1}}/jpackage \\
  --slave %{_bindir}/jshell jshell %{sdkbindir -- %{?1}}/jshell \\
  --slave %{_bindir}/jstack jstack %{sdkbindir -- %{?1}}/jstack \\
  --slave %{_bindir}/jstat jstat %{sdkbindir -- %{?1}}/jstat \\
  --slave %{_bindir}/jstatd jstatd %{sdkbindir -- %{?1}}/jstatd \\
  --slave %{_bindir}/jwebserver jwebserver %{sdkbindir -- %{?1}}/jwebserver \\
  --slave %{_bindir}/serialver serialver %{sdkbindir -- %{?1}}/serialver \\
  --slave %{_mandir}/man1/jar.1%{man_comp} jar.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jar.1 \\
  --slave %{_mandir}/man1/jarsigner.1%{man_comp} jarsigner.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jarsigner.1 \\
  --slave %{_mandir}/man1/javac.1%{man_comp} javac.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/javac.1 \\
  --slave %{_mandir}/man1/javadoc.1%{man_comp} javadoc.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/javadoc.1 \\
  --slave %{_mandir}/man1/javap.1%{man_comp} javap.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/javap.1 \\
  --slave %{_mandir}/man1/jcmd.1%{man_comp} jcmd.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jcmd.1 \\
  --slave %{_mandir}/man1/jconsole.1%{man_comp} jconsole.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jconsole.1 \\
  --slave %{_mandir}/man1/jdb.1%{man_comp} jdb.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jdb.1 \\
  --slave %{_mandir}/man1/jdeps.1%{man_comp} jdeps.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jdeps.1 \\
  --slave %{_mandir}/man1/jinfo.1%{man_comp} jinfo.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jinfo.1 \\
  --slave %{_mandir}/man1/jmap.1%{man_comp} jmap.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jmap.1 \\
  --slave %{_mandir}/man1/jnativescan.1%{man_comp} jnativescan.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jnativescan.1 \\
  --slave %{_mandir}/man1/jps.1%{man_comp} jps.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jps.1 \\
  --slave %{_mandir}/man1/jpackage.1%{man_comp} jpackage.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jpackage.1 \\
  --slave %{_mandir}/man1/jstack.1%{man_comp} jstack.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jstack.1 \\
  --slave %{_mandir}/man1/jstat.1%{man_comp} jstat.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jstat.1 \\
  --slave %{_mandir}/man1/jwebserver.1%{man_comp} jwebserver.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jwebserver.1 \\
  --slave %{_mandir}/man1/jstatd.1%{man_comp} jstatd.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jstatd.1 \\
  --slave %{_mandir}/man1/serialver.1%{man_comp} serialver.1%{man_comp} %{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/serialver.1
alternatives --install %{_jvmdir}/java-%{origin} java_sdk_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}} %{priority_for -- %{?1}}
alternatives --install %{_jvmdir}/java-%{javaver} java_sdk_%{javaver} %{_jvmdir}/%{sdkdir -- %{?1}} %{priority_for -- %{?1}}
}
%define post_devel() %{expand:
%{alternatives_javac_install -- %{?1}}
update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
}
%define preun_devel() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
if [ $1 -eq 0 ]
then
  alternatives --remove javac %{sdkbindir -- %{?1}}/javac
  alternatives --remove java_sdk_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}}
  alternatives --remove java_sdk_%{javaver} %{_jvmdir}/%{sdkdir -- %{?1}}
fi
}
%define postun_devel() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{update_desktop_icons}
fi
}
%define posttrans_devel() %{expand:
%{update_desktop_icons}
}
%define alternatives_javadoc_install() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
alternatives --install %{_javadocdir}/java-%{origin} javadocdir_%{origin} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api %{priority_for -- %{?1}}
alternatives --install %{_javadocdir}/java-%{javaver} javadocdir_%{javaver} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api %{priority_for -- %{?1}}
alternatives --install %{_javadocdir}/java javadocdir %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api %{priority_for -- %{?1}}
}
%define preun_javadoc() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
if [ $1 -eq 0 ]
then
  alternatives --remove javadocdir %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api
  alternatives --remove javadocdir_%{origin} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api
  alternatives --remove javadocdir_%{javaver} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api
fi
}
%define alternatives_javadoczip_install() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
alternatives --install %{_javadocdir}/java-%{origin}.zip javadoczip_%{origin} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip %{priority_for -- %{?1}}
alternatives --install %{_javadocdir}/java-%{javaver}.zip javadoczip_%{javaver} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip %{priority_for -- %{?1}}
alternatives --install %{_javadocdir}/java-zip javadoczip %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip %{priority_for -- %{?1}}
}
%define preun_javadoc_zip() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
if [ $1 -eq 0 ]
then
  alternatives --remove javadoczip %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip
  alternatives --remove javadoczip_%{origin} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip
  alternatives --remove javadoczip_%{javaver} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip
fi
}
%define files_jre() %{expand:
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-%{origin}.png
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsplashscreen.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libawt_xawt.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjawt.so
}
%define files_jre_headless() %{expand:
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/lib/
%doc %{_defaultdocdir}/%{uniquejavadocdir --   %{?1}}/%{fullversion -- %{nil}}.specfile
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%doc %{_jvmdir}/%{sdkdir -- %{?1}}/NEWS	
%doc %{_defaultdocdir}/%{uniquejavadocdir -- %{?1}}/NEWS
%dir %{_defaultdocdir}/%{uniquejavadocdir -- %{?1}}
%dir %{_sysconfdir}/.java/.systemPrefs
%dir %{_sysconfdir}/.java
%dir %{_jvmdir}/%{sdkdir -- %{?1}}
%{_jvmdir}/%{sdkdir -- %{?1}}/release
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/bin
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/java
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/%{alt_java_name}
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/keytool
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/rmiregistry
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/lib
%ifarch %{jit_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/classlist
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jexec
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jspawnhelper
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jrt-fs.jar
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/modules
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/psfont.properties.ja
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/psfontj2d.properties
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/tzdb.dat
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/tzdb.dat.upstream
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjli.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jvm.cfg
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libattach.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libawt.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libextnet.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjsig.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libawt_headless.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libdt_socket.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libfontmanager.so
%if ! %{system_libs}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libfreetype.so
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libinstrument.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libj2gss.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libj2pcsc.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libj2pkcs11.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjaas.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjava.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjavajpeg.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjdwp.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjimage.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjsound.so
%ifarch %{svml_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjsvml.so
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/liblcms.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libmanagement.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libmanagement_agent.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libmanagement_ext.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libmlib_image.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libnet.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libnio.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libprefs.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/librmi.so
%ifarch %{sa_arches}
%ifnarch %{zero_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsaproc.so
%endif
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsctp.so
%ifarch %{simdsort_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsimdsort.so
%endif
%ifarch %{sleef_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsleef.so
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsyslookup.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libverify.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libzip.so
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr/default.jfc
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr/profile.jfc
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/java.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/%{alt_java_name}.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/keytool.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/rmiregistry.1
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}/*.so
%ifarch %{share_arches}
%attr(444, root, root) %{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}/classes.jsa
%attr(444, root, root) %{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}/classes_coh.jsa
%ifnarch %{ix86} %{arm32}
%attr(444, root, root) %{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}/classes_nocoops.jsa
%attr(444, root, root) %{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}/classes_nocoops_coh.jsa
%endif
%endif
%dir %{etcjavasubdir}
%dir %{etcjavadir -- %{?1}}
%dir %{etcjavadir -- %{?1}}/lib
%dir %{etcjavadir -- %{?1}}/lib/security
%{etcjavadir -- %{?1}}/lib/security/cacerts
%{etcjavadir -- %{?1}}/lib/security/cacerts.upstream
%dir %{etcjavadir -- %{?1}}/conf
%dir %{etcjavadir -- %{?1}}/conf/management
%dir %{etcjavadir -- %{?1}}/conf/security
%dir %{etcjavadir -- %{?1}}/conf/security/policy
%dir %{etcjavadir -- %{?1}}/conf/security/policy/limited
%dir %{etcjavadir -- %{?1}}/conf/security/policy/unlimited
%config(noreplace) %{etcjavadir -- %{?1}}/lib/security/blocked.certs
%config(noreplace) %{etcjavadir -- %{?1}}/lib/security/public_suffix_list.dat
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/limited/exempt_local.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/limited/default_local.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/limited/default_US_export.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/unlimited/default_local.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/unlimited/default_US_export.policy
 %{etcjavadir -- %{?1}}/conf/security/policy/README.txt
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/java.security
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/java.security.upstream
%dir %{etcjavadir -- %{?1}}/conf/security/redhat
%dir %{etcjavadir -- %{?1}}/conf/security/redhat/false
%dir %{etcjavadir -- %{?1}}/conf/security/redhat/true
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/redhat/SunPKCS11-FIPS.cfg
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/redhat/crypto-policies.properties
%config %{etcjavadir -- %{?1}}/conf/security/redhat/false/crypto-policies.properties
%config %{etcjavadir -- %{?1}}/conf/security/redhat/true/crypto-policies.properties
%config %{etcjavadir -- %{?1}}/conf/security/redhat/false/fips.properties
%config %{etcjavadir -- %{?1}}/conf/security/redhat/true/fips.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/management/jmxremote.access
%config  %{etcjavadir -- %{?1}}/conf/management/jmxremote.password.template
%config(noreplace) %{etcjavadir -- %{?1}}/conf/management/management.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/jaxp.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/jaxp-strict.properties.template
%config(noreplace) %{etcjavadir -- %{?1}}/conf/logging.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/net.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/sound.properties
%{_jvmdir}/%{sdkdir -- %{?1}}/conf
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/security
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_bindir}/java
%ghost %{_jvmdir}/jre
%ghost %{_bindir}/%{alt_java_name}
%ghost %{_bindir}/keytool
%ghost %{_bindir}/rmiregistry
%ghost %{_jvmdir}/jre-%{origin}
%ghost %{_jvmdir}/jre-%{javaver}
%ghost %{_jvmdir}/jre-%{javaver}-%{origin}
%endif
%endif
%ghost %{_jvmdir}/%{sdkdir -- %{?1}}/conf.rpmmoved
%ghost %{_jvmdir}/%{sdkdir -- %{?1}}/lib/security.rpmmoved
}
%define files_devel() %{expand:
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/bin
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jar
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jarsigner
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javac
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javadoc
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javap
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jcmd
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jconsole
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdb
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdeps
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdeprscan
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jfr
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jimage
%ifarch %{sa_arches}
%ifnarch %{zero_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jhsdb
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jhsdb.1
%endif
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jinfo
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jlink
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jmap
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jmod
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jnativescan
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jps
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jpackage
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jshell
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstack
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstat
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstatd
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jwebserver
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/serialver
%{_jvmdir}/%{sdkdir -- %{?1}}/include
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/ct.sym
%{_datadir}/applications/*jconsole%{?1}.desktop
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jar.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jarsigner.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/javac.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/javadoc.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/javap.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jconsole.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jcmd.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jdb.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jdeprscan.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jdeps.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jfr.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jinfo.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jlink.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jmap.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jmod.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jnativescan.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jps.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jpackage.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jshell.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jstack.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jstat.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jstatd.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/jwebserver.1
%{_jvmdir}/%{sdkdir -- %{?1}}/man/man1/serialver.1
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_bindir}/javac
%ghost %{_jvmdir}/java
%ghost %{_jvmdir}/%{alt_java_name}
%ghost %{_bindir}/jlink
%ghost %{_bindir}/jmod
%ghost %{_bindir}/jhsdb
%ghost %{_bindir}/jar
%ghost %{_bindir}/jarsigner
%ghost %{_bindir}/javadoc
%ghost %{_bindir}/javap
%ghost %{_bindir}/jconsole
%ghost %{_bindir}/jcmd
%ghost %{_bindir}/jdb
%ghost %{_bindir}/jdeps
%ghost %{_bindir}/jdeprscan
%ghost %{_bindir}/jfr
%ghost %{_bindir}/jimage
%ghost %{_bindir}/jinfo
%ghost %{_bindir}/jmap
%ghost %{_bindir}/jps
%ghost %{_bindir}/jpackage
%ghost %{_bindir}/jshell
%ghost %{_bindir}/jstack
%ghost %{_bindir}/jstat
%ghost %{_bindir}/jstatd
%ghost %{_bindir}/jwebserver
%ghost %{_bindir}/serialver
%ghost %{_jvmdir}/java-%{origin}
%ghost %{_jvmdir}/java-%{javaver}
%endif
%endif
}
%define files_jmods() %{expand:
%{_jvmdir}/%{sdkdir -- %{?1}}/jmods
}
%define files_demo() %{expand:
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%{_jvmdir}/%{sdkdir -- %{?1}}/demo
}
%define files_src() %{expand:
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/src.zip
%{_jvmdir}/%{sdkdir -- %{?1}}/full_sources
%{_jvmdir}/%{sdkdir -- %{?1}}/%{generated_sources_name}
}
%define files_static_libs() %{expand:
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/%{static_libs_root}
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/%{static_libs_arch_dir}
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/%{static_libs_install_dir}
%{_jvmdir}/%{sdkdir -- %{?1}}/%{static_libs_install_dir}/lib*.a
}
%define files_javadoc() %{expand:
%doc %{_javadocdir}/%{uniquejavadocdir -- %{?1}}
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%dir %{_jvmdir}/%{sdkdir -- %{?1}}
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_javadocdir}/java
%ghost %{_javadocdir}/java-%{origin}
%ghost %{_javadocdir}/java-%{javaver}
%endif
%endif
}
%define files_javadoc_zip() %{expand:
%doc %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%dir %{_jvmdir}/%{sdkdir -- %{?1}}
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_javadocdir}/java-zip
%ghost %{_javadocdir}/java-%{origin}.zip
%ghost %{_javadocdir}/java-%{javaver}.zip
%endif
%endif
}
%define files_crypto_adapter() %{expand:
%dir %{_libdir}/%{sdkdir -- %{?1}}
%{_libdir}/%{sdkdir -- %{?1}}/libnssadapter.so
}
%define java_rpo() %{expand:
Requires: fontconfig%{?_isa}
Requires: xorg-x11-fonts-Type1
Requires: libXcomposite%{?_isa}
Requires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
%if 0%{?rhel} >= 8 || 0%{?fedora} > 0 || (0%{?oreon} >= 11)
Recommends: gtk3%{?_isa}
%endif
Provides: java-%{javaver}-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java%{?1} = %{epoch}:%{version}-%{release}
Provides: jre%{?1} = %{epoch}:%{version}-%{release}
%endif
}
%define java_headless_rpo() %{expand:
Requires: ca-certificates
Requires: javapackages-filesystem
Requires: tzdata-java >= 2024a
Requires: lksctp-tools%{?_isa}
Requires: cups-libs
Requires: crypto-policies
Requires: nss
Requires(post):   %{alternatives_requires}
Requires(postun): %{alternatives_requires}
%if 0%{?rhel} >= 8 || 0%{?fedora} > 0 || (0%{?oreon} >= 11)
Suggests: lksctp-tools%{?_isa}, pcsc-lite-libs%{?_isa}
%endif
Requires: %{name}-crypto-adapter%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-%{origin}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-%{origin}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: java-headless%{?1} = %{epoch}:%{version}-%{release}
%endif
}
%define java_devel_rpo() %{expand:
Requires:         %{name}%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
Requires(post):   %{alternatives_requires}
Requires(postun): %{alternatives_requires}
Provides: java-sdk-%{javaver}-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-sdk-%{javaver}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-devel%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-devel%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-devel-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-sdk-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-devel%{?1} = %{epoch}:%{version}-%{release}
Provides: java-sdk%{?1} = %{epoch}:%{version}-%{release}
%endif
}
%define java_static_libs_rpo() %{expand:
Requires:         %{name}-devel%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
}
%define java_jmods_rpo() %{expand:
Requires:         %{name}-devel%{?1} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-jmods%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-jmods%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-jmods%{?1} = %{epoch}:%{version}-%{release}
%endif
}
%define java_demo_rpo() %{expand:
Requires: %{name}%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-demo%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-demo%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-demo%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-demo%{?1} = %{epoch}:%{version}-%{release}
%endif
}
%define java_javadoc_rpo() %{expand:
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
Requires(post):   %{alternatives_requires}
Requires(postun): %{alternatives_requires}
Provides: java-%{javaver}-javadoc%{?1}%{?2} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc%{?1}%{?2} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-javadoc%{?1}%{?2} = %{epoch}:%{version}-%{release}
%endif
}
%define java_src_rpo() %{expand:
Requires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-src%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-src%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-src%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-src%{?1} = %{epoch}:%{version}-%{release}
%endif
}
%global __jar_repack 0
%global portable_name %{name}-portable
%global portable_version %{version}-1
Name:    java-latest-%{origin}
Version: %{newjavaver}.%{buildver}
Release:        1%{?dist}
Epoch:   1
Summary:        OpenJDK 26 Runtime Environment
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30) || (0%{?oreon} >= 11)
Group:   Development/Languages
%endif
License:  Apache-1.1 AND Apache-2.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-BSD-with-advertising AND GPL-1.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-GPLv2-with-exceptions AND IJG AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND MPL-2.0 AND LicenseRef-Callaway-Public-Domain AND W3C AND Zlib AND ISC AND FTL AND LicenseRef-RSA
URL:      http://openjdk.java.net/
Source19: hotspot.stp.in
Source20: hotspot_gc.stp.in
Source21: hotspot_jni.stp.in
Source22: jstack.stp.in
Source9: jconsole.desktop.in
Source13: TestCryptoLevel.java
Source14: TestECDSA.java
Source15: TestSecurityProperties.java
Source16: CheckVendor.java
Source18: TestTranslations.java
Source31: https://github.com/rh-openjdk/nss-native-fips-key-import-export-adapter/releases/download/%{nssadapter_version}/%{nssadapter_name}.tar.xz
Source32: create-redhat-properties-files.bash
Provides: bundled(freetype) = 2.13.3
Provides: bundled(giflib) = 5.2.2
Provides: bundled(harfbuzz) = 10.4.0
Provides: bundled(lcms2) = 2.17.0
Provides: bundled(libjpeg) = 6b
Provides: bundled(libpng) = 1.6.51
Provides: bundled(zlib) = 1.3.1
%ifarch %{sleef_arches}
Provides: bundled(sleef) = 3.6.1
%endif
%{java_rpo %{nil}}
# oreon:deps
BuildRequires:  /usr/bin/gcc
BuildRequires:  /usr/bin/objcopy
BuildRequires:  /usr/bin/readelf
BuildRequires:  crypto-policies
BuildRequires:  desktop-file-utils
BuildRequires:  elfutils-devel
BuildRequires:  gcc
BuildRequires:  gdb
BuildRequires:  java-latest-openjdk-portable-docs
BuildRequires:  java-latest-openjdk-portable-misc
BuildRequires:  java-latest-openjdk-portable-sources
BuildRequires:  javapackages-filesystem
BuildRequires:  make
BuildRequires:  nss-devel
BuildRequires:  nss-softokn-devel
BuildRequires:  pkgconfig
BuildRequires:  tzdata-java
BuildRequires:  unzip
BuildRequires:  zip
# /oreon:deps
%description
The %{origin_nice} %{featurever} runtime environment.

# crypto-adapter

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source31_hash}" = "none" || { f="%{SOURCE31}"; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source31_hash}" || { echo "oreon: Source31 hash mismatch" >&2; exit 1; }; }
echo "Preparing %{oj_vendor_version}"

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

export XZ_OPT="-T0"
# do not add -a 0; will break build dirs
%setup -q -c -n %{uniquesuffix ""} -T
# Prepare libnssadapter.so source code
tar -xJf %{SOURCE31}
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 8 ] ; then
 echo "priority must be 8 digits in total, violated"
 exit 14
fi

tar -xf %{portablejvmdir}/%{portable_compatiblename}*%{version}*portable.sources.noarch.tar.xz
tar -xf %{portablejvmdir}/%{portable_compatiblename}*%{version}*portable*.misc.%{_arch}.tar.xz
tar -xf %{portablejvmdir}/%{portable_compatiblename}*%{version}*portable*.docs.%{_arch}.tar.xz

# print out info abot binaries used for repack. The version-less fallbacks are for development only, where can be cheated environment
echo "Those RPMs are just repacking portable tarballs extracted from portable RPMs" > %{repack_file}
echo "Usually this exact portable RPM can not be obtained via dnf install, but you can download it." >> %{repack_file}
echo "The exact info is at bottom." >> %{repack_file}
echo "All java- names and versions:" >> %{repack_file}
ls -l %{portablejvmdir} >> %{repack_file}
rpm -qa | grep "java-" >> %{repack_file}
echo "Used %{portable_compatiblename}.*portable:" >> %{repack_file}
ls -l %{portablejvmdir} | grep "%{portable_compatiblename}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Used %{name}.*portable:" >> %{repack_file}
rpm -qa | grep "%{name}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Used %{version}.*portable:" >> %{repack_file}
ls -l %{portablejvmdir} | grep "%{version}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Used portable.*%{version}:" >> %{repack_file}
rpm -qa | grep "portable.*%{version}" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Where this is %{fullversion %{nil}}" >> %{repack_file}
portableNvr=`rpm -qa | grep %{name}-portable-misc-%{version} | sed "s/-misc-/-/" | sed "s/.%{_arch}.*//"`
if [ "x${portableNvr}" == x ] ; then
  portableNvr=`rpm -qa | grep %{name}-portable-misc- | sed "s/-misc-/-/" | sed "s/.%{_arch}.*//"`" #incorrect!"
fi
echo "Which repacked ${portableNvr}" >> %{repack_file}
echo "You can download the repacked portables from:" >> %{repack_file}
echo "`date`" >> %{repack_file}

# Extract systemtap tapsets

# Prepare desktop files
# The _X_ syntax indicates variables that are replaced by make upstream
# The @X@ syntax indicates variables that are replaced by configure upstream
for suffix in %{build_loop} ; do
for file in %{SOURCE9}; do
    FILE=`basename $file | sed -e s:\.in$::g`
    EXT="${FILE##*.}"
    NAME="${FILE%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed    -e  "s:_SDKBINDIR_:%{sdkbindir -- $suffix}:g" $file > $OUTPUT_FILE
    sed -i -e  "s:@target_cpu@:%{_arch}:g" $OUTPUT_FILE
    sed -i -e  "s:@OPENJDK_VER@:%{version}-%{release}.%{_arch}$suffix:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VER@:%{javaver}:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VENDOR@:%{origin}:g" $OUTPUT_FILE
done
done

%build

src_image=`ls -d %{portable_compatiblename}*%{version}*portable.sources.noarch`
misc_image=`ls -d %{portable_compatiblename}*%{version}*portable.misc.%{_arch}`
cp -rf $misc_image/%{generated_sources_name}/%{vcstag}/ $src_image # it would be nice to remove them once debugsources are generated:(
ln -s $src_image/%{vcstag} %{vcstag}
mkdir build
pushd build
  cp -r ../$misc_image/%{generated_sources_name}/jdk%{featurever}.build* .
popd
doc_image=`ls -d %{portable_compatiblename}*%{version}*portable.docs.%{_arch}`
for suffix in %{build_loop} ; do
  mkdir %{installoutputdir -- ${suffix}}
  if [ "x$suffix" = "x" ] ; then
      make -C %{nssadapter_name} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"
  elif [ "x$suffix" = "x%{fastdebug_suffix_unquoted}" ] ; then
      make -C %{nssadapter_name} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"
  else # slowdebug
      make -C %{nssadapter_name} CFLAGS="%{build_cflags} -O0 -Wp,-U_FORTIFY_SOURCE -Wno-error" LDFLAGS="%{build_ldflags}"
  fi
  installdir=%{installoutputdir -- ${suffix}}
  mkdir ${installdir}/lib
  install -m 755 %{nssadapter_name}/bin/libnssadapter.so ${installdir}/lib
  make -C %{nssadapter_name} clean
done # end of release / debug cycle loop
%install
function customisejdkProperties() {
    local imagepath=${1}
    local suffix=${2}
    local secpath=${imagepath}/conf/security
    if [ -d ${imagepath} ] ; then
        cp -v "${secpath}"/java.security{,.upstream}
        bash -ex %{SOURCE32} ${secpath} %{_libdir}/%{sdkdir -- ${suffix}}/libnssadapter.so
    fi
}
function customisejdkTzdata() {
    local imagepath=${1}
    local suffix=${2}
    if [ -d ${imagepath} ] ; then
        mv ${imagepath}/lib/tzdb.dat{,.upstream}
        ln -s %{javazidir}/tzdb.dat ${imagepath}/lib/tzdb.dat
    fi
}
function installjdk() {
    local imagepath=${1}
    local suffix=${2}
    if [ -d ${imagepath} ] ; then
        find ${imagepath} -iname '*.jar' -exec chmod ugo+r {} \;
        find ${imagepath} -iname '*.so' -exec chmod +x {} \;
        find ${imagepath}/bin/ -exec chmod +x {} \;
        customisejdkTzdata ${imagepath} ${suffix}
        customisejdkProperties ${imagepath} ${suffix}
        mv ${imagepath}/lib/security/cacerts{,.upstream}
        ln -sv /etc/pki/java/cacerts ${imagepath}/lib/security
    fi
}
function debugcheckjdk() {
    local imagepath=${1}
    local debug_suffix=${2}
    if [ -d ${imagepath} ] ; then
        find "${imagepath}" -iname "*.$debug_suffix" -print0 | while read -d $'\0' lib
        do
            if [ -f "$lib" ] ; then
                echo "Testing $lib for debug symbols"
                eu-readelf -S "$lib" | grep "] .debug_"
                test $(eu-readelf -S "$lib" | grep -E "\]\ .debug_(info|abbrev)" | wc --lines) == 2
                old_IFS="$IFS"
                IFS=$'\n'
                for line in $(eu-readelf -s "$lib" | grep "00000000      0 FILE    LOCAL  DEFAULT")
                do
                    echo "$line" | grep -E "ABS ((.*/)?[-_a-zA-Z0-9]+\.(c|cc|cpp|cxx|o|S|oS))?$"
                done
                IFS="$old_IFS"
                if [ "`basename $lib`" = "libjvm.so" ]; then
                    eu-readelf -s "$lib" | \
                        grep -E "00000000      0 FILE    LOCAL  DEFAULT      ABS javaCalls.(cpp|o)$"
                fi
                eu-readelf -S "$lib" | grep 'gnu'
                if eu-readelf -S "$lib" | grep "\] .gnu_debuglink" | grep PROGBITS; then
                   echo "bad .gnu_debuglink section."
                   eu-readelf -x .gnu_debuglink "$lib"
                   false
                fi
            fi
        done
gdb -q "${imagepath}/bin/java" <<EOF | tee gdb.out
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
    fi
}
for suffix in %{build_loop} ; do
  if [ "x$suffix" = "x" ] ; then
      debugbuild=""
  else
      debugbuild=`echo $suffix  | sed "s/-/./g"`
  fi
  for jdkjre in jdk ; do
    buildoutputdir=`ls -d %{portable_compatiblename}*portable${debugbuild}.${jdkjre}*`
    top_dir_abs_main_build_path=$(pwd)/${buildoutputdir}
    installjdk  ${top_dir_abs_main_build_path} ${suffix}
    clashinglibs=""
%ifarch %{svml_arches}
    clashinglibs="$clashinglibs lib/libjsvml.so"
%endif
    for lib in $clashinglibs ; do
      libjsvmlgcchackdir=`mktemp -d`
      pushd $libjsvmlgcchackdir
        libjsvml=${top_dir_abs_main_build_path}/$lib
        ls -l $libjsvml
        echo "#include <stdio.h>" > a.c
        echo "int main(void) {  printf(\"$libjsvml\"); }" >> a.c
        gcc a.c -o exe
        readelf -n  exe | grep "Build ID"
        readelf -n  $libjsvml | grep "Build ID"
        objcopy --dump-section .note.gnu.build-id=id exe
        objcopy --update-section  .note.gnu.build-id=id $libjsvml
        readelf -n $libjsvml | grep -i "Build ID"
      popd
      rm -rf $libjsvmlgcchackdir
    done
    if [ $jdkjre == jdk ] ; then
      if [ "x$suffix" = "x" ] ; then
        debugsuffix="debuginfo"
      else
        debugsuffix="so"
      fi
      debugcheckjdk ${top_dir_abs_main_build_path} $debugsuffix
    fi
    cat ${top_dir_abs_main_build_path}/release
  done
done # end of release / debug cycle loop
STRIP_KEEP_SYMTAB=libjvm*
for suffix in %{build_loop} ; do
  if [ "x$suffix" = "x" ] ; then
      debugbuild=""
  else
      debugbuild=`echo $suffix  | sed "s/-/./g"`
  fi
  buildoutputdir=`ls -d %{portable_compatiblename}*portable${debugbuild}.jdk*`
  top_dir_abs_main_build_path=$(pwd)/${buildoutputdir}
  jdk_image=${top_dir_abs_main_build_path}
  src_image=`echo ${top_dir_abs_main_build_path} | sed "s/portable.*.%{_arch}/portable.sources.noarch/"`
  misc_image=`echo ${top_dir_abs_main_build_path} | sed "s/portable.*.%{_arch}/portable.misc.%{_arch}/"`
  docs_image=`echo ${top_dir_abs_main_build_path} | sed "s/portable.*.%{_arch}/portable.docs.%{_arch}/"`
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
     ${src_image}/%{vcstag}/src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png \
     $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-%{origin}.png
done
cp -a ${jdk_image} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}
cp -a ${src_image} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/full_sources
cp -a ${misc_image}/%{generated_sources_name} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}
cp -a ${misc_image}/alt-java $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/bin
install -d -m 755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{uniquejavadocdir -- $suffix}
cp %{repack_file} $RPM_BUILD_ROOT%{_defaultdocdir}/%{uniquejavadocdir --  $suffix}/%{fullversion -- %{nil}}.specfile
pushd ${jdk_image}
popd
  install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{sdkdir -- ${suffix}}
%if 0%{?fedora} || 0%{?rhel} >= 11 || (0%{?oreon} >= 11)
  mv $RPM_BUILD_ROOT/../%{name}/%{installoutputdir -- $suffix}/lib/libnssadapter.so          $RPM_BUILD_ROOT%{_libdir}/%{sdkdir -- ${suffix}}
%else
  mv $RPM_BUILD_ROOT/../../BUILD/%{name}/%{installoutputdir -- $suffix}/lib/libnssadapter.so $RPM_BUILD_ROOT%{_libdir}/%{sdkdir -- ${suffix}}
%endif
if ! echo $suffix | grep -q "debug" ; then
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}
  built_doc_archive=$(basename $(ls ${docs_image}/jdk*docs.zip))
  cp -a ${docs_image}/${built_doc_archive} \
     $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}.zip
  pushd $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}
    unzip ${docs_image}/${built_doc_archive} 
  popd
fi
commondocdir=${RPM_BUILD_ROOT}%{_defaultdocdir}/%{uniquejavadocdir -- $suffix}
install -d -m 755 ${commondocdir}
cp -a ${top_dir_abs_main_build_path}/NEWS ${commondocdir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix -- $suffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/conf/  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/lib/security  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}
  ln -s %{etcjavadir -- $suffix}/conf  ./conf
popd
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/lib
  ln -s %{etcjavadir -- $suffix}/lib/security  ./security
popd
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/ -name "*.so" -exec chmod 755 {} \; ;
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/ -type d -exec chmod 755 {} \; ;
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/legal -type f -exec chmod 644 {} \; ;
done
%{__mkdir} -p $RPM_BUILD_ROOT/usr/src/debug
cp -a ${src_image} $RPM_BUILD_ROOT/usr/src/debug/%{name}-%{version}-%{release}
pushd $RPM_BUILD_ROOT/usr
find src/debug -mindepth 1 -maxdepth 1 | sed 's,^,/usr/,' >> %{_builddir}/%{compatiblename}/debugsourcefiles.list
popd
%{__mkdir} -p $RPM_BUILD_ROOT/usr/lib/debug/%{_jvmdir}/%{sdkdir -- %{normal_suffix}}/lib/server
%{__mkdir} -p $RPM_BUILD_ROOT/usr/lib/debug/%{_jvmdir}/%{sdkdir -- %{normal_suffix}}/bin
pushd $RPM_BUILD_ROOT
for f in $(find .%{_jvmdir}/%{sdkdir -- %{normal_suffix}} -name \*.debuginfo); do
  %{__mv} $f "$RPM_BUILD_ROOT/usr/lib/debug/$(dirname $f)/$(basename $f)"
done
popd
pushd $RPM_BUILD_ROOT/usr/lib/debug%{_jvmdir}
find %{compatiblename} -name \*.debuginfo | sed 's,^,/usr/lib/debug%{_jvmdir}/,' >> %{_builddir}/%{compatiblename}/debugfiles.list
popd
%oreon_autofiles main

%check

for suffix in %{build_loop} ; do
 if [ "x$suffix" = "x" ] ; then
      debugbuild=""
  else
      debugbuild=`echo $suffix  | sed "s/-/./g"`
  fi
  buildoutputdir=`ls -d %{portable_compatiblename}*portable${debugbuild}.jdk*`
  top_dir_abs_main_build_path=$(pwd)/${buildoutputdir}
export JAVA_HOME_INTERNAL=${top_dir_abs_main_build_path}  # have in-tree setup before move of configs to /etc
export JAVA_HOME=${RPM_BUILD_ROOT}%{_jvmdir}/%{sdkdir -- $suffix} # have systems setup with links to /etc
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME_INTERNAL/bin/java --add-opens java.base/javax.crypto=ALL-UNNAMED TestCryptoLevel 
$JAVA_HOME/bin/javac -d . %{SOURCE14}
$JAVA_HOME_INTERNAL/bin/java $(echo $(basename %{SOURCE14})|sed "s|\.java||")
$JAVA_HOME/bin/javac -d . %{SOURCE15}
export PROG=$(echo $(basename %{SOURCE15})|sed "s|\.java||")
export SEC_DEBUG="-Djava.security.debug=properties"
$JAVA_HOME_INTERNAL/bin/java ${SEC_DEBUG} ${PROG} true
$JAVA_HOME_INTERNAL/bin/java ${SEC_DEBUG} -Dredhat.crypto-policies=false ${PROG} false
if ! nm $JAVA_HOME/bin/java | grep set_speculation ; then true ; else false; fi
%ifarch %{ssbd_arches}
nm $JAVA_HOME/bin/%{alt_java_name} | grep prctl
%else
if ! nm $JAVA_HOME/bin/%{alt_java_name} | grep prctl ; then true ; else false; fi
%endif
$JAVA_HOME/bin/javac -d . %{SOURCE16}
$JAVA_HOME/bin/javac -d . %{SOURCE18}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE18})|sed "s|\.java||") JRE || echo "TZDATA no longer can be synced with system, because we repack"
$JAVA_HOME/bin/java -Djava.locale.providers=CLDR $(echo $(basename %{SOURCE18})|sed "s|\.java||") CLDR || echo "TZDATA no longer can be synced with system, because we repack"
$JAVA_HOME/bin/jar -tf $JAVA_HOME/lib/src.zip | grep 'sun.misc.Unsafe'
$JAVA_HOME/bin/javap -l -c java.lang.Object | grep "Compiled from"
$JAVA_HOME/bin/javap -l -c java.lang.Object | grep LineNumberTable
$JAVA_HOME/bin/javap -l -c java.lang.Object | grep LocalVariableTable
$JAVA_HOME/bin/javap -l -c java.nio.ByteBuffer | grep "Compiled from"
$JAVA_HOME/bin/javap -l -c java.nio.ByteBuffer | grep LineNumberTable
$JAVA_HOME/bin/javap -l -c java.nio.ByteBuffer | grep LocalVariableTable
done

%files -f %{oreon_filedir}/main.list
