%global source0_hash e0da0cc9e2bb5f205712f0a19407ae1391e8d2ef6197fd599e4be848a3d8ee76
%global jspspec 3.1
%global major_version 10
%global minor_version 1
%global micro_version 60
%global packdname apache-tomcat-%{version}-src
%global servletspec 6.0
%global elspec 5.0
%global tcuid 53
%global native_version 2.0.14
%global basedir %{_var}/lib/%{name}
%global appdir %{basedir}/webapps
%global homedir %{_datadir}/%{name}
%global bindir %{homedir}/bin
%global confdir %{_sysconfdir}/%{name}
%global libdir %{_javadir}/%{name}
%global logdir %{_var}/log/%{name}
%global cachedir %{_var}/cache/%{name}
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work
Name:          tomcat
Epoch:         1
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:        1%{?dist}
Summary:        Apache Servlet/JSP Engine, RI for Servlet 6.0/JSP 3.1 API
License:       Apache-2.0
URL:           http://tomcat.apache.org/
Source0:        http://www.apache.org/dist/%{name}/%{name}-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:       %{name}-%{major_version}.%{minor_version}.conf
Source2:       %{name}-%{major_version}.%{minor_version}.sysconfig
Source3:       %{name}-%{major_version}.%{minor_version}.wrapper
Source4:       %{name}-%{major_version}.%{minor_version}.logrotate
Source5:       %{name}-%{major_version}.%{minor_version}-digest.script
Source6:       %{name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source7:       %{name}-%{major_version}.%{minor_version}.service
Source8:       %{name}-functions
Source9:       %{name}-preamble
Source10:      %{name}-server
Source11:      %{name}-named.service
Source12:      module-start-up-parameters.conf
Patch0:        %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        %{name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
Patch2:        %{name}-build.patch
Patch3:        %{name}-%{major_version}.%{minor_version}-catalina-policy.patch
Patch4:        %{name}-%{major_version}.%{minor_version}-bnd-annotation.patch
Patch5:        %{name}-%{major_version}.%{minor_version}-JDTCompiler.patch
Patch6:        rhbz-1857043.patch
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch
Requires:      (java-25-headless or java-25)
Requires:      javapackages-tools
Requires:      %{name}-lib = %{epoch}:%{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
Recommends:    tomcat-native >= %{native_version}
%endif
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:         %{name}-log4j = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  aqute-bnd
BuildRequires:  aqute-bndlib
BuildRequires:  ecj
BuildRequires:  findutils
BuildRequires:  java-25-devel
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  systemd
BuildRequires:  tomcat-jakartaee-migration
# /oreon:deps
%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
%description docs-webapp
The docs web application for Apache Tomcat.

%package jsp-%{jspspec}-api
Summary: Apache Tomcat JavaServer Pages v%{jspspec} API Implementation Classes
Provides: jsp = %{jspspec}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-jsp-2.3-api < 1:9.1
Provides:  %{name}-jsp-2.3-api = %{?epoch:%{epoch}:}%{version}-%{release}
%description jsp-%{jspspec}-api
Apache Tomcat JSP API Implementation Classes.

%package lib
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: ecj >= 4.20
Recommends: tomcat-jakartaee-migration
Requires(preun): coreutils
%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Summary: Apache Tomcat Java Servlet v%{servletspec} API Implementation Classes
Provides: servlet = %{servletspec}
Obsoletes: %{name}-servlet-4.0-api < 1:9.1
Provides:  %{name}-servlet-4.0-api = %{?epoch:%{epoch}:}%{version}-%{release}
%description servlet-%{servletspec}-api
Apache Tomcat Servlet API Implementation Classes.

%package el-%{elspec}-api
Summary: Apache Tomcat Expression Language v%{elspec} API Implementation Classes
Provides: el_api = %{elspec}
Obsoletes: %{name}-el-3.0-api < 1:9.1
Provides:  %{name}-el-3.0-api = %{?epoch:%{epoch}:}%{version}-%{release}
%description el-%{elspec}-api
Apache Tomcat EL API Implementation Classes.

%package webapps
Summary: The ROOT web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
%description webapps
The ROOT web application for Apache Tomcat.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{packdname}
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch 0 -p0
%patch 1 -p0
%patch 2 -p0
%patch 3 -p0
%patch 4 -p0
%patch 5 -p0
%patch 6 -p0

# Remove webservices naming resources as it's generally unused
%{__rm} -rf java/org/apache/naming/factory/webservices

# Configure maven files
%mvn_package ":tomcat-el-api" tomcat-el-api
%mvn_alias "org.apache.tomcat:tomcat-el-api" "jakarta.servlet:jakarta.servlet-api"
%mvn_package ":tomcat-jsp-api" tomcat-jsp-api
%mvn_alias "org.apache.tomcat:tomcat-jsp-api" "jakarta.servlet:jakarta.servlet.jsp"
%mvn_package ":tomcat-servlet-api" tomcat-servlet-api

# Create a sysusers.d config file
cat >tomcat.sysusers.conf <<EOF
u tomcat %{tcuid} 'Apache Tomcat' %{homedir} -
EOF

%build

touch HACK
%{ant} -Dbase.path="." \
  -Dbuild.compiler="modern" \
  -Dcommons-daemon.jar="HACK" \
  -Dcommons-daemon.native.src.tgz="HACK" \
  -Djdt.jar="$(build-classpath ecj/ecj)" \
  -Dtomcat-native.tar.gz="HACK" \
  -Dtomcat-native.home="." \
  -Dcommons-daemon.native.win.mgr.exe="HACK" \
  -Dnsis.exe="HACK" \
  -Djaxrpc-lib.jar="HACK" \
  -Dwsdl4j-lib.jar="HACK" \
  -Dbnd.jar="$(build-classpath aqute-bnd/biz.aQute.bnd)" \
  -Dbnd-annotation.jar="$(build-classpath aqute-bnd/biz.aQute.bnd.annotation)" \
  -Dversion="%{version}" \
  -Dversion.build="%{micro_version}" \
  -Dmigration-lib.jar="$(build-classpath tomcat-jakartaee-migration/jakartaee-migration.jar)" \
  deploy
%{__rm} output/build/bin/commons-daemon.jar output/build/lib/ecj.jar output/build/lib/jakartaee-migration.jar
%{__rm} -rf output/build/webapps/examples
%install
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sbindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{appdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{bindir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/conf.d
/bin/echo "Place your custom *.conf files here. Shell expansion is supported." > ${RPM_BUILD_ROOT}%{confdir}/conf.d/README
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{logdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{_localstatedir}/lib/tomcats
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{homedir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{tempdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{workdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_unitdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}
pushd output/build
    %{__cp} -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} -a conf/*.{policy,properties,xml,xsd} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE2} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
%{__install} -m 0755 %{SOURCE3} \
    ${RPM_BUILD_ROOT}%{_sbindir}/%{name}
%{__install} -m 0644 %{SOURCE7} \
    ${RPM_BUILD_ROOT}%{_unitdir}/%{name}.service
%{__sed} -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE4} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}.disabled
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE5} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{name}-digest
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{name}-tool-wrapper
%{__install} -m 0644 %{SOURCE8} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}/functions
%{__install} -m 0755 %{SOURCE9} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}/preamble
%{__install} -m 0755 %{SOURCE10} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}/server
%{__install} -m 0644 %{SOURCE11} \
    ${RPM_BUILD_ROOT}%{_unitdir}/%{name}@.service
%{__install} -m 0644 %{SOURCE12} ${RPM_BUILD_ROOT}%{confdir}/conf.d/
sed -i \
   "s,el-api.jar,%{name}-el-%{elspec}-api.jar,;
    s,servlet-api.jar,%{name}-servlet-%{servletspec}-api.jar,;
    s,jsp-api.jar,%{name}-jsp-%{jspspec}-api.jar,;" \
    ${RPM_BUILD_ROOT}%{bindir}/catalina-tasks.xml
pushd ${RPM_BUILD_ROOT}%{_javadir}
   %{__mv} %{name}/jsp-api.jar %{name}-jsp-%{jspspec}-api.jar
   %{__ln_s} %{name}-jsp-%{jspspec}-api.jar %{name}-jsp-api.jar
   %{__mv} %{name}/servlet-api.jar %{name}-servlet-%{servletspec}-api.jar
   %{__ln_s} %{name}-servlet-%{servletspec}-api.jar %{name}-servlet-api.jar
   %{__mv} %{name}/el-api.jar %{name}-el-%{elspec}-api.jar
   %{__ln_s} %{name}-el-%{elspec}-api.jar %{name}-el-api.jar
popd
pushd output/build
    %{_bindir}/build-jar-repository lib ecj 2>&1
    %{_bindir}/build-jar-repository lib tomcat-jakartaee-migration 2>&1
popd
pushd ${RPM_BUILD_ROOT}%{libdir}
    %{__ln_s} ../../java/%{name}-jsp-%{jspspec}-api.jar .
    %{__ln_s} ../../java/%{name}-servlet-%{servletspec}-api.jar .
    %{__ln_s} ../../java/%{name}-el-%{elspec}-api.jar .
    %{__ln_s} $(build-classpath ecj/ecj) jasper-jdt.jar
    %{__ln_s} $(build-classpath tomcat-jakartaee-migration/jakartaee-migration) jakartaee-migration.jar
    cp ../../%{name}/bin/tomcat-juli.jar .
popd
pushd ${RPM_BUILD_ROOT}%{homedir}
    %{__ln_s} %{appdir} webapps
    %{__ln_s} %{confdir} conf
    %{__ln_s} %{libdir} lib
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{tempdir} temp
    %{__ln_s} %{workdir} work
popd
pushd res/maven
    for pom in *.pom; do
        sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $pom
    done
popd
%mvn_artifact res/maven/tomcat-el-api.pom output/build/lib/el-api.jar
%mvn_artifact res/maven/tomcat-jsp-api.pom output/build/lib/jsp-api.jar
%mvn_artifact res/maven/tomcat-servlet-api.pom output/build/lib/servlet-api.jar
%mvn_file org.apache.tomcat:tomcat-annotations-api tomcat/annotations-api
%mvn_artifact res/maven/tomcat-annotations-api.pom ${RPM_BUILD_ROOT}%{libdir}/annotations-api.jar
%mvn_artifact res/maven/tomcat-api.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-api.jar
%mvn_file org.apache.tomcat:tomcat-catalina-ant tomcat/catalina-ant
%mvn_artifact res/maven/tomcat-catalina-ant.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-ant.jar
%mvn_file org.apache.tomcat:tomcat-catalina-ha tomcat/catalina-ha
%mvn_artifact res/maven/tomcat-catalina-ha.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-ha.jar
%mvn_file org.apache.tomcat:tomcat-catalina tomcat/catalina
%mvn_artifact res/maven/tomcat-catalina.pom ${RPM_BUILD_ROOT}%{libdir}/catalina.jar
%mvn_artifact res/maven/tomcat-coyote.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-coyote.jar
%mvn_artifact res/maven/tomcat-dbcp.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-dbcp.jar
%mvn_artifact res/maven/tomcat-i18n-cs.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-cs.jar
%mvn_artifact res/maven/tomcat-i18n-de.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-de.jar
%mvn_artifact res/maven/tomcat-i18n-es.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-es.jar
%mvn_artifact res/maven/tomcat-i18n-fr.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-fr.jar
%mvn_artifact res/maven/tomcat-i18n-ja.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-ja.jar
%mvn_artifact res/maven/tomcat-i18n-ko.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-ko.jar
%mvn_artifact res/maven/tomcat-i18n-pt-BR.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-pt-BR.jar
%mvn_artifact res/maven/tomcat-i18n-ru.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-ru.jar
%mvn_artifact res/maven/tomcat-i18n-zh-CN.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-zh-CN.jar
%mvn_file org.apache.tomcat:tomcat-jasper-el tomcat/jasper-el
%mvn_artifact res/maven/tomcat-jasper-el.pom ${RPM_BUILD_ROOT}%{libdir}/jasper-el.jar
%mvn_file org.apache.tomcat:tomcat-jasper tomcat/jasper
%mvn_artifact res/maven/tomcat-jasper.pom ${RPM_BUILD_ROOT}%{libdir}/jasper.jar
%mvn_file org.apache.tomcat:tomcat-jaspic-api tomcat/jaspic-api
%mvn_artifact res/maven/tomcat-jaspic-api.pom ${RPM_BUILD_ROOT}%{libdir}/jaspic-api.jar
%mvn_artifact res/maven/tomcat-jdbc.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-jdbc.jar
%mvn_artifact res/maven/tomcat-jni.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-jni.jar
%mvn_artifact res/maven/tomcat-juli.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-juli.jar
%mvn_file org.apache.tomcat:tomcat-ssi tomcat/catalina-ssi
%mvn_artifact res/maven/tomcat-ssi.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-ssi.jar
%mvn_file org.apache.tomcat:tomcat-storeconfig tomcat/catalina-storeconfig
%mvn_artifact res/maven/tomcat-storeconfig.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-storeconfig.jar
%mvn_file org.apache.tomcat:tomcat-tribes tomcat/catalina-tribes
%mvn_artifact res/maven/tomcat-tribes.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-tribes.jar
%mvn_artifact res/maven/tomcat-util-scan.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-util-scan.jar
%mvn_artifact res/maven/tomcat-util.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-util.jar
%mvn_file org.apache.tomcat:tomcat-websocket-api tomcat/websocket-api
%mvn_artifact res/maven/tomcat-websocket-api.pom ${RPM_BUILD_ROOT}%{libdir}/websocket-api.jar
%mvn_artifact res/maven/tomcat-websocket.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-websocket.jar
%mvn_artifact res/maven/tomcat-websocket-client-api.pom ${RPM_BUILD_ROOT}%{libdir}/websocket-client-api.jar
%mvn_artifact res/maven/tomcat.pom
%mvn_install
install -m0644 -D tomcat.sysusers.conf %{buildroot}%{_sysusersdir}/tomcat.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.service
%preun

%{__rm} -rf %{workdir}/* %{tempdir}/*
%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n tomcat-admin-webapps -f %{oreon_filedir}/tomcat-admin-webapps.list
%files -n tomcat-docs-webapp -f %{oreon_filedir}/tomcat-docs-webapp.list
%files -n tomcat-jsp-3.1-api -f %{oreon_filedir}/tomcat-jsp-3.1-api.list
%files -n tomcat-lib -f %{oreon_filedir}/tomcat-lib.list
%files -n tomcat-servlet-6.0-api -f %{oreon_filedir}/tomcat-servlet-6.0-api.list
%files -n tomcat-el-5.0-api -f %{oreon_filedir}/tomcat-el-5.0-api.list
%files -n tomcat-webapps -f %{oreon_filedir}/tomcat-webapps.list

%changelog

%autochangelog
