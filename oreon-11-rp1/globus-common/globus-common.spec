%global source0_hash b47485bbf1118976f347dcfe539a2116725f6c202d438c4ef109d282340464d5

Name:		globus-common
%global _name %(tr - _ <<< %{name})
Version:	18.15
Release:	2%{?dist}
Summary:	Grid Community Toolkit - Common Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libtool-ltdl-devel
BuildRequires:	doxygen
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter

#		Obsolete dropped packages from GCT
Obsoletes:	globus-usage < 6

%package progs
Summary:	Grid Community Toolkit - Common Library Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package devel
Summary:	Grid Community Toolkit - Common Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libtool-ltdl-devel
#		Obsolete dropped packages from GCT
Obsoletes:	globus-usage-devel < 6

%package doc
Summary:	Grid Community Toolkit - Common Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Common Library

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Common Library Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Common Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Common Library Documentation Files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

export GLOBUS_VERSION=6.2
export SH=/bin/sh
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib} \
	   --with-backward-compatibility-hack

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

# Remove environment scripts
rm %{buildroot}%{_datadir}/globus-user-env.csh
rm %{buildroot}%{_datadir}/globus-user-env.sh

%check
%make_build check NO_EXTERNAL_NET=1

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_common.so.*
%{_libdir}/libglobus_memory_debug.so.*
# This is a loadable module (plugin)
%{_libdir}/libglobus_thread_pthread.so
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/Core
%{perl_vendorlib}/Globus/Core/Config.pm
%{perl_vendorlib}/Globus/Core/Paths.pm
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_bindir}/globus-domainname
%{_bindir}/globus-hostname
%{_bindir}/globus-sh-exec
%{_bindir}/globus-version
%{_sbindir}/globus-libc-hostname
%{_sbindir}/globus-redia
%dir %{_datadir}/globus
%{_datadir}/globus/config.guess
%{_datadir}/globus/globus-args-parser-header
%{_datadir}/globus/globus-script-initializer*
%{_datadir}/globus/globus-sh-tools.sh
%{_datadir}/globus/globus-sh-tools-vars.sh
%doc %{_mandir}/man1/globus-domainname.1*
%doc %{_mandir}/man1/globus-hostname.1*
%doc %{_mandir}/man1/globus-sh-exec.1*
%doc %{_mandir}/man1/globus-version.1*

%files devel
%dir %{_includedir}/globus
%{_includedir}/globus/*
%{_libdir}/libglobus_common.so
%{_libdir}/libglobus_memory_debug.so
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/globus-makefile-header

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
