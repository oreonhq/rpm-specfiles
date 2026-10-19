%global source2_hash 4b1aa7498f622711688ce6f6ee5b8c84dc60563b6b38c546ed16ec1695c02295
%global source1_hash b279b55fee925c05c069a48efa6ae55d4163b0ec946757a43adf4b35cee86bcf
%global source0_hash 7a1c4056af114ef7ed61f3665a614ce7085a442d5712a85a5bbebf84b217d29c
%bcond_without httpclient
%bcond_without oro
%bcond_without vfs
%bcond_without sftp
%global jarname ivy
Name:           apache-%{jarname}
Version:        2.6.0
Release:        1%{?dist}
Summary:        Java-based dependency manager
License:        Apache-2.0
URL:            https://ant.apache.org/ivy
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://archive.apache.org/dist/ant/%{jarname}/%{version}/%{name}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/ant/%{jarname}/%{version}/%{name}-%{version}-src.tar.gz.asc
Source2:        https://archive.apache.org/dist/ant/KEYS
Source3:         00-global-settings.patch
%if %{with httpclient}
%endif
%if %{with oro}
%endif
%if %{with vfs}
%endif
%if %{with sftp}
%endif
Provides:       ivy = %{version}-%{release}
# oreon:deps
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  gnupg2
BuildRequires:  ivy-local
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.connector-factory)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.jsch)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-vfs2)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk18on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk18on)
BuildRequires:  mvn(oro:oro)
# /oreon:deps
%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.

%{?javadoc_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
# Upstream tarball uses CRLF so %%autosetup patch step cannot match hunks
dos2unix src/java/org/apache/ivy/util/FileUtil.java
dos2unix src/java/org/apache/ivy/ant/IvyAntSettings.java
patch -p1 -l < %{SOURCE3}
# Don't hardcode sysconfdir path
sed -i 's:/etc/ivy/:%{_sysconfdir}/ivy/:' src/java/org/apache/ivy/ant/IvyAntSettings.java
# remove BOM
%pom_remove_dep :jsch.agentproxy
# remove test deps
%pom_remove_dep junit:junit
%pom_remove_dep org.hamcrest:hamcrest-core
%pom_remove_dep org.hamcrest:hamcrest-library
%pom_remove_dep org.apache.ant:ant-testutil
%pom_remove_dep org.apache.ant:ant-junit
%pom_remove_dep org.apache.ant:ant-junit4
%pom_remove_dep ant-contrib:ant-contrib
%pom_remove_dep xmlunit:xmlunit
# change jdk15on to jdk18on
%pom_change_dep :bcpg-jdk15on :bcpg-jdk18on
%pom_change_dep :bcprov-jdk15on :bcprov-jdk18on
# optional dep: httpclient
%if %{without httpclient}
# remove all httpclient related dep(s)
%pom_remove_dep :httpclient
# remove file(s) related to httpclient
rm src/java/org/apache/ivy/util/url/HttpClientHandler.java
%endif
# optional dep: oro
%if %{without oro}
# remove all oro related dep(s)
%pom_remove_dep :oro
# remove file(s) related to oro
rm src/java/org/apache/ivy/plugins/matcher/GlobPatternMatcher.java
%endif
# optional dep: vfs
%if %{without vfs}
# remove all vfs related dep(s)
%pom_remove_dep :commons-vfs2
# remove file(s) related to vfs
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsRepository.java
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsResource.java
rm src/java/org/apache/ivy/plugins/repository/vfs/ivy_vfs.xml
rm src/java/org/apache/ivy/plugins/resolver/VfsResolver.java
%endif
# optional dep: sftp
%if %{without sftp}
# remove all sftp related dep(s)
%pom_remove_dep :jsch
%pom_remove_dep :jsch.agentproxy
%pom_remove_dep :jsch.agentproxy.connector-factory
%pom_remove_dep :jsch.agentproxy.jsch
# remove file(s) related to sftp
rm src/java/org/apache/ivy/plugins/repository/sftp/SFTPRepository.java
rm src/java/org/apache/ivy/plugins/repository/sftp/SFTPResource.java
rm src/java/org/apache/ivy/plugins/repository/ssh/AbstractSshBasedRepository.java
rm src/java/org/apache/ivy/plugins/repository/ssh/RemoteScpException.java
rm src/java/org/apache/ivy/plugins/repository/ssh/Scp.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshCache.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshRepository.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshResource.java
rm src/java/org/apache/ivy/plugins/resolver/AbstractSshBasedResolver.java
rm src/java/org/apache/ivy/plugins/resolver/SFTPResolver.java
rm src/java/org/apache/ivy/plugins/resolver/SshResolver.java
%endif
# compatibility
%mvn_file : %{name}/ivy ivy
# remove prebuilt documentation
rm -rf asciidoc
# publish artifacts through xmvn
%pom_xpath_set ivy:publish/@resolver xmvn build.xml

%build

mkdir -p ~/.ant
cp /etc/ant.conf ~/.ant
sed -i '$a JAVA_HOME=/usr/lib/jvm/java-21-openjdk' ~/.ant/ant.conf
ant -Divy.mode=local \
    -f build-release.xml \
    release-version jar javadoc publish-local
%install
%mvn_install -J build/reports/api
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "apache-ivy/ivy" > %{buildroot}%{_sysconfdir}/ant.d/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
