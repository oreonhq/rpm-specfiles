%global source0_hash 217ea60daa87f51277795d16c153d70436ccaba9ae63938b97a25865352096fa
Summary:        Java bindings for the libvirt virtualization API
Name:       libvirt-java
Version:    0.5.4
Prefix:     libvirt
Release:        1%{?dist}
License:    MIT
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        http://libvirt.org/sources/java/%{name}-%{version}.tar.gz
Patch0001: 0001-Fix-build-with-jna-3.5.0.patch
URL:        http://libvirt.org/
Requires:   jna
Requires:   libvirt-client >= 0.9.12
Requires:   java-25 >= 1.5.0
Requires:   jpackage-utils
# oreon:deps
BuildRequires:  ant-junit
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
BuildRequires:  jna
BuildRequires:  jpackage-utils
# /oreon:deps
%description
Libvirt-java is a base framework allowing to use libvirt, the virtualization
API though the Java programming language.
It requires libvirt-client >= 0.9.12

%package    devel
Summary:    Compressed Java source files for %{name}
Requires:   %{name} = %{version}-%{release}
%description    devel
Libvirt-java is a base framework allowing to use libvirt, the virtualization
API though the Java programming language. This is the development part needed
to build applications with Libvirt-java.

%package    javadoc
Summary:    Java documentation for %{name}
Requires:   jpackage-utils
%description    javadoc
API documentation for %{name}.
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Fix FTBFS issue (bz #914153)
%patch -P0001 -p1

%build

ant build docs
%install
rm -fr %{buildroot}
install -d -m0755 %{buildroot}%{_javadir}
install -d -m0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp target/%{prefix}-%{version}.jar %{buildroot}%{_javadir}/%{prefix}.jar
cp -r target/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{_javadocdir}/%{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

ant test
%files -f %{oreon_filedir}/main.list
%files -n libvirt-java-devel -f %{oreon_filedir}/libvirt-java-devel.list
%files -n libvirt-java-javadoc -f %{oreon_filedir}/libvirt-java-javadoc.list

%changelog

%autochangelog
