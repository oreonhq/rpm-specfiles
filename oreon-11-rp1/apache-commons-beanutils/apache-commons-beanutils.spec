# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 28cace1c5f454f6b17bc7d0175aab79fe85799b4fd56b16bb4683dabd2c84cc7
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond_without bootstrap

Name:           apache-commons-beanutils
Version:        1.11.0
Release:        %autorelease
Summary:        Java utility methods for accessing and modifying the properties of arbitrary JavaBeans
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-beanutils/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://archive.apache.org/dist/commons/beanutils/source/commons-beanutils-%{version}-src.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.9.4-40

%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

%prep
%oreon_verify_sources
%autosetup -p1 -n commons-beanutils-%{version}-src
sed -i 's/\r//' *.txt

%pom_remove_plugin :maven-assembly-plugin

%mvn_alias :{*} :@1-core :@1-bean-collections
%mvn_alias :{*} org.apache.commons:@1 org.apache.commons:@1-core org.apache.commons:@1-bean-collections
%mvn_file : %{name} %{name}-core %{name}-bean-collections
%mvn_file : commons-beanutils commons-beanutils-core commons-beanutils-bean-collections

%build
# Some tests fail in Koji
%mvn_build -j -f -- -Dcommons.packageId=beanutils

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.11.0-3
- bump release (retry failed build)

* Wed Apr 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.11.0-2
- %%autosetup -n commons-beanutils-%%{version}-src for upstream source tarball layout

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.11.0-1
- Prepare for Oreon 11 (RP1)
