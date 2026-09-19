%global source0_hash 5d62ca0d8f1e4dffeb253d6f0633e08ec5134b521f16c9ee5c8ff9aa0b7fb94d

%global majorver 1
%global minorver 28
%global patchver 1

%global commit 27b915d95d625cafe77efc56f8e4a854ffdb3ff5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20231119

%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif

Name:    genders
Version: %{majorver}.%{minorver}.%{patchver}~^%{commitdate}git%{shortcommit}
Release: 6%{?dist}
Summary: Static cluster configuration database
License: GPL-2.0-only

URL: https://github.com/chaos/genders
Source: https://github.com/chaos/genders/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: autoconf
%if ! %{JAVA}
Obsoletes: genders-java < %{version}-%{release}
Obsoletes: genders-javadoc < %{version}-%{release}
Obsoletes: genders-java-devel < %{version}-%{release}
%endif

%description
Genders is a static cluster configuration database used for cluster
configuration management.  It is used by a variety of tools and
scripts for management of large clusters.  The genders database is
typically replicated on every node of the cluster. It describes the
layout and configuration of the cluster so that tools and scripts can
sense the variations of cluster nodes. By abstracting this information
into a plain text file, it becomes possible to change the
configuration of a cluster by modifying only one file.

%package compat
Summary: Compatibility library 
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
%if 0%{?rhel} >= 6 || 0%{?fedora} > 0
BuildArch: noarch
%endif
%description compat
Genders API that is compatible with earlier releases of genders.

%package perl
Summary: Perl libraries
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Config)
%description perl
Genders API bindings for perl.

%if %{JAVA}
%package javadoc
Summary: Java Documentation
BuildRequires: java-devel
%description javadoc
Genders API Documentation for java.

%package java-devel
Summary: Java Development libraries
Requires: %{name}-java%{?_isa} = %{version}-%{release}
%description java-devel
Genders API bindings for java.

%package java
Summary: Java libraries
BuildRequires: java-devel
BuildRequires: make
%description java
%endif
Genders API bindings for java.

%global __provides_exclude_from ^(.%{perl_vendorarch}/*\\.so)$

%package -n libgenders
Summary: Genders libraries
%description -n libgenders
Genders API for C.

%package -n libgenders-devel
Summary: Genders development libraries
Requires: libgenders%{?_isa} = %{version}-%{release}
%description -n libgenders-devel
Genders development headers and libraries for C.

%package -n libgendersplusplus
Summary: Genders libraries for C++
Requires: libgenders%{?_isa} = %{version}-%{release}
%description -n libgendersplusplus
Genders API for C++.

%package -n libgendersplusplus-devel
Summary: Genders development libraries
Requires: libgenders-devel%{?_isa} = %{version}-%{release}
Requires: libgendersplusplus%{?_isa} = %{version}-%{release}
%description -n libgendersplusplus-devel
Genders development headers and libraries for C++.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup  -q -n %{name}-%{commit}

%if 0%{?rhel} <= 6
%global __provides_exclude ^Lib%{name}.so.*$
%endif

%build
%if %{JAVA}
export CPPFLAGS='-I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -I../../../src/libgenders'
%else
export CPPFLAGS='-I../../../src/libgenders'
%endif
%configure \
    --with-perl-extensions \
    --with-perl-vendor-arch \
%if %{JAVA}
    --with-java-extensions \
%else
    --without-java-extensions \
%endif
    --without-python-extensions \
    --with-cplusplus-extensions \
    --with-extension-destdir="%{buildroot}"
%{__make}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} make install
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.a
chmod +w %{buildroot}/%{perl_vendorarch}/auto/Lib%{name}/Lib%{name}.so
rm -f %{buildroot}/%{perl_vendorarch}/auto/Lib%{name}/Lib%{name}.bs
rm -f %{buildroot}/%{perl_vendorarch}/auto/Lib%{name}/.packlist
mkdir -p %{buildroot}/%{_libexecdir}

mkdir -p %{buildroot}/%{_jnidir}
%if 0%{?rhel} == 5
%define _datarootdir %{_prefix}/share
%endif
%if %{JAVA}
mv %{buildroot}/%{_datarootdir}/java/Genders.jar %{buildroot}/%{_jnidir}/
%endif

%ldconfig_scriptlets -n libgenders
%ldconfig_scriptlets -n libgendersplusplus
%if %{JAVA}
%ldconfig_scriptlets -n genders-java
%endif

%files
%doc README NEWS ChangeLog DISCLAIMER DISCLAIMER.UC COPYING TUTORIAL genders.sample
%{_mandir}/man1/*
%{_mandir}/man3/genders.3*
%{_bindir}/*

%files -n libgenders
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libgenders.so.0*
%{_mandir}/man3/libgenders.3*

%files -n libgenders-devel
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_mandir}/man3/genders_*
%{_includedir}/genders.h
%{_libdir}/libgenders.so

%files -n libgendersplusplus
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libgendersplusplus.so.2*

%files -n libgendersplusplus-devel
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libgendersplusplus.so
%{_includedir}/gendersplusplus*

%files perl
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_mandir}/man3/Libgenders*
%{_mandir}/man3/Genders*
%{perl_vendorarch}/*

%if %{JAVA}
%files java-devel
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libGendersjni.so

%files java
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libGendersjni.so.*
%{_jnidir}/Genders.jar

%files javadoc
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_docdir}/%{name}-%{majorver}.%{minorver}.%{patchver}-javadoc
%endif

%files compat
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_mandir}/man3/gendlib*
%{_usr}/lib/genders/*

%changelog
%autochangelog
