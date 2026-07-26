%global source0_hash 7eec616f608991b754be81848da2d19dfe112b84893cd457474786e82be69a71

Summary:    Java bindings for the libvirt virtualization API
Name:       libvirt-java
Version:    0.4.9
Prefix:     libvirt
Release:    35%{?dist}%{?extra_release}
License:    MIT
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
Source:     http://libvirt.org/sources/java/%{name}-%{version}.tar.gz

# Fix FTBFS issue (bz #914153)
Patch0001: 0001-Fix-build-with-jna-3.5.0.patch
URL:        http://libvirt.org/

Requires:   jna
Requires:   libvirt-client >= 0.9.12
%if 0%{?fedora} >= 21
Requires:   java-25-headless >= 1.5.0
%else
Requires:   java-25 >= 1.5.0
%endif
Requires:   jpackage-utils
BuildRequires:  ant-openjdk25 
BuildRequires:  jna
BuildRequires:  ant-junit
BuildRequires:  java-25-devel >= 1.5.0
BuildRequires:  jpackage-utils

#
# the jpackage-utils should provide a %{java_home} macro
# to select a different Java JVM from the default one use the following
# rpmbuild --define 'java_home /usr/lib/jvm/your_jvm_of_choice'
#

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

%check
ant test

%files
%doc AUTHORS LICENCE NEWS README INSTALL
%{_javadir}/*.jar

%files devel
%doc src/test/java/test.java

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
%autochangelog
