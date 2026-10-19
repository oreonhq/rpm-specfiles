%global source0_hash ce7d6457409925cf5beca2ee8502ac764d0331e257758ffbf986a9103e1e84d2
%global uname         jigawatts
%global uversion      6c78499af1a1d536368267e5ab5449232b05f878
%global dversion      %(echo %{uversion} | sed s/-/_/)
%global aarch64       aarch64 arm64 armv8
%global shortcommit %(c=%{uversion}; echo ${c:0:7})
%global commitdate 20210827
Name:    %{uname}
Version: 0.2
Release:        1%{?dist}
Summary:        Java CRIU helper
License: LicenseRef-Callaway-GPLv2-with-exceptions
URL:     https://github.com/chflood/%{uname}
Source0:        https://github.com/chflood/jigawatts/archive/6c78499af1a1d536368267e5ab5449232b05f878.tar.gz#/jigawatts-0.2.tar.gz
Patch0:  output_loc.patch
Requires:   java-25-headless
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x
# oreon:deps
BuildRequires:  criu-devel
BuildRequires:  exec-maven-plugin
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  java-25-devel
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-local-openjdk25
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-provider-junit5
BuildRequires:  mvn(org.apache.commons:commons-lang3)
# /oreon:deps
%description
CRIU is a Linux utility that allows the checkpointing and restoring
of processes.You can read more about CRIU at criu.org. CRIU for
Java is a package which makes it more convenient to use CRIU from
Java.

%package javadoc
Summary: Javadoc for %{name}
%description javadoc
Javadoc for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{uname}-%{uversion}
%patch -P0 -p1
%pom_add_dep org.apache.commons:commons-lang3:3.12.0:test
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='exec-maven-plugin']/pom:executions/pom:execution/pom:configuration/pom:arguments" '<argument>-g</argument>'
# Work-around for RHBZ#1977671, /usr/lib64 missing on default java.library.path on aarch64
%ifarch %{aarch64}
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" '<forkCount>1</forkCount>
        <environmentVariables>
            <LD_LIBRARY_PATH>/usr/lib64:${project.build.directory}</LD_LIBRARY_PATH>
        </environmentVariables>'
%else
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" '<forkCount>1</forkCount>
        <environmentVariables>
            <LD_LIBRARY_PATH>${project.build.directory}</LD_LIBRARY_PATH>
        </environmentVariables>'
%endif

%build

%mvn_build --xmvn-javadoc -f
%install
%mvn_install
mkdir -p %{buildroot}/%{_libdir}
cp ./target/libJigawatts.so %{buildroot}/%{_libdir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jigawatts-javadoc -f %{oreon_filedir}/jigawatts-javadoc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2-0.18.
- Prepare for Oreon 11 (RP1)
