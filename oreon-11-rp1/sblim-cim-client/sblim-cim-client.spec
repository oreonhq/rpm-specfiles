%global source1_hash 8c54a9141be4e59a2b40cd86d3ac1cea8ee8a2860bcd93d525b9809d88f2b734
%global source0_hash bd74e75f51f8364037942821047473bca65bff3a90c3759f79e6c3095960901b
%global archive_folder_name cim-client
%global cim_client_jar_file sblimCIMClient
%global slp_name sblim-slp-client
%global slp_client_jar_file sblimSLPClient
Summary:        Java CIM Client library
Name:           sblim-cim-client
Version:        1.3.9.3
Release:        1%{?dist}
License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}-src.zip
Source1:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-samples-%{version}-src.zip
Patch0:         sblim-cim-client-1.3.9.3-fix-for-java-11-openjdk.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-25-headless >= 1.4
Requires:       jpackage-utils
Requires:       xerces-j2 >= 2.7.1
Requires:       tog-pegasus >= 2:2.5.1
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  dos2unix
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  xerces-j2
# /oreon:deps
%description
The purpose of this package is to provide a CIM Client Class Library for Java
applications. It complies to the DMTF standard CIM Operations over HTTP and
intends to be compatible with JCP JSR48 once it becomes available. To learn
more about DMTF visit http://www.dmtf.org.
More info about the Java Community Process and JSR48 can be found at
http://www.jcp.org and http://www.jcp.org/en/jsr/detail?id=48.

%package javadoc
Summary:        Javadoc for %{name}
%description javadoc
Javadoc for sblim-cim-client.

%package manual
Summary:        Manual and sample code for %{name}
Requires:       sblim-cim-client = %{version}-%{release}
%description manual
Manual and sample code for sblim-cim-client.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archive_folder_name}
rm version.txt
%setup -q -T -D -b 1 -n %{archive_folder_name}
%autopatch -p1

%build

export ANT_OPTS="-Xmx256m"
ant \
        -Dbuild.compiler=modern \
        -DManifest.version=%{version} \
        build-release
%install
dos2unix COPYING README ChangeLog NEWS
pushd samples
  dos2unix README.samples
  pushd org/sblim/slp/example
    dos2unix *
  popd
  pushd org/sblim/wbem/cimclient/sample
    dos2unix *
  popd
popd
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -pm 644 samples/README.samples $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr  samples/org $RPM_BUILD_ROOT%{_datadir}/%{name}
dos2unix cim.defaults slp.conf
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/java
install -pm 644 cim.defaults $RPM_BUILD_ROOT%{_sysconfdir}/java/%{name}.properties
install -pm 644 slp.conf $RPM_BUILD_ROOT%{_sysconfdir}/java/%{slp_name}.properties
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{archive_folder_name}/%{cim_client_jar_file}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
(
  cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}.jar %{cim_client_jar_file}.jar;
)
install -pm 644 %{archive_folder_name}/%{slp_client_jar_file}.jar $RPM_BUILD_ROOT%{_javadir}/%{slp_name}.jar
(
  cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{slp_name}.jar %{slp_client_jar_file}.jar;
)
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr %{archive_folder_name}/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sblim-cim-client-javadoc -f %{oreon_filedir}/sblim-cim-client-javadoc.list
%files -n sblim-cim-client-manual -f %{oreon_filedir}/sblim-cim-client-manual.list

%changelog

%autochangelog
