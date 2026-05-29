%global source0_hash 3686e1446dff59245432b0679c760d3bf3f40bfb64d8c8312d71feed7114d0a0

Name:           apache-commons-net
Version:        3.12.0
Release:        %autorelease
Summary:        Internet protocol suite Java library
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-net/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/commons/net/source/commons-net-3.12.0-src.tar.gz
Source1:        https://downloads.apache.org/commons/net/source/commons-net-3.12.0-src.tar.gz.asc
Source2:        https://downloads.apache.org/commons/KEYS

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.junit.vintage:junit-vintage-engine)
# for signature verification
BuildRequires:  gnupg2
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.11.1-11

%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n commons-net-%{version}-src
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%pom_remove_plugin :exec-maven-plugin

# Fails with "Coverage checks have not been met."
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

%pom_remove_dep org.apache.ftpserver:ftpserver-core

# Disable tests that depends on commons-collections4 (not packaged yet)
%pom_remove_dep :commons-collections4
rm src/test/java/org/apache/commons/net/util/SubnetUtilsTest.java

# Disable tests that rely on networking to be available and working.
# Depending on host configuration, on different systems they fail with
# errors such as "Connection timed out", "Address already in use",
# "Temporary failure in name resolution" etc.
rm \
src/test/java/org/apache/commons/net/chargen/CharGenUDPClientTest.java \
src/test/java/org/apache/commons/net/daytime/DaytimeTCPClientTest.java \
src/test/java/org/apache/commons/net/daytime/DaytimeUDPClientTest.java \
src/test/java/org/apache/commons/net/discard/DiscardUDPClientTest.java \
src/test/java/org/apache/commons/net/echo/EchoUDPClientTest.java \
src/test/java/org/apache/commons/net/ftp/AbstractFtpsTest.java \
src/test/java/org/apache/commons/net/ftp/FTPClientTransferModeTest.java \
src/test/java/org/apache/commons/net/ftp/FTPSClientTest.java \
src/test/java/org/apache/commons/net/ftp/NoProtocolSslConfigurationProxy.java \
src/test/java/org/apache/commons/net/tftp/TFTPAckPacketTest.java \
src/test/java/org/apache/commons/net/tftp/TFTPDataPacketTest.java \
src/test/java/org/apache/commons/net/tftp/TFTPErrorPacketTest.java \
src/test/java/org/apache/commons/net/tftp/TFTPReadRequestPacketTest.java \
src/test/java/org/apache/commons/net/tftp/TFTPRequestPacketTest.java \
src/test/java/org/apache/commons/net/tftp/TFTPServerPathTest.java \
src/test/java/org/apache/commons/net/tftp/TFTPTest.java \
src/test/java/org/apache/commons/net/tftp/TFTPWriteRequestPacketTest.java \
src/test/java/org/apache/commons/net/time/TimeTCPClientTest.java \
src/test/java/org/apache/commons/net/time/TimeUDPClientTest.java \

%mvn_file : commons-net %{name}
%mvn_alias : org.apache.commons:commons-net

%build
%mvn_build -j -- -Dcommons.osgi.symbolicName=org.apache.commons.net

%install
%mvn_install

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%changelog
* Wed Apr 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.0-2
- %%autosetup -n commons-net-%%{version}-src for upstream source tarball layout

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.0-1
- Prepare for Oreon 11 (RP1)
