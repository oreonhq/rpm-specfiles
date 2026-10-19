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
Release:        6%{?dist}
Summary:        Static cluster configuration database
License: GPL-2.0-only
URL: https://github.com/chaos/genders
Source0:        https://github.com/chaos/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%if ! %{JAVA}
Obsoletes: genders-java < %{version}-%{release}
Obsoletes: genders-javadoc < %{version}-%{release}
Obsoletes: genders-java-devel < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
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
%description compat
Genders API that is compatible with earlier releases of genders.

%package perl
Summary: Perl libraries
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Config)
%description perl
Genders API bindings for perl.

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

%build

export CPPFLAGS='-I../../../src/libgenders'
%configure \
    --with-perl-extensions \
    --with-perl-vendor-arch \
    --without-java-extensions \
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
%ldconfig_scriptlets -n libgenders
%ldconfig_scriptlets -n libgendersplusplus
%oreon_autofiles libgenders usr/*/lib*.so.*
%oreon_autofiles libgenders-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libgendersplusplus usr/*/lib*.so.*
%oreon_autofiles libgendersplusplus-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n genders-compat -f %{oreon_filedir}/genders-compat.list
%files -n genders-perl -f %{oreon_filedir}/genders-perl.list
%files -n libgenders -f %{oreon_filedir}/libgenders.list
%files -n libgenders-devel -f %{oreon_filedir}/libgenders-devel.list
%files -n libgendersplusplus -f %{oreon_filedir}/libgendersplusplus.list
%files -n libgendersplusplus-devel -f %{oreon_filedir}/libgendersplusplus-devel.list

%changelog

%autochangelog
