%global source0_hash b47485bbf1118976f347dcfe539a2116725f6c202d438c4ef109d282340464d5
Name:		globus-common
%global _name %(tr - _ <<< %{name})
Version:	18.15
Release:        2%{?dist}
Summary:        Grid Community Toolkit - Common Library
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
Obsoletes:	globus-usage < 6
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%package progs
Summary:	Grid Community Toolkit - Common Library Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}
%package devel
Summary:	Grid Community Toolkit - Common Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libtool-ltdl-devel
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

export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"
export GLOBUS_VERSION=6.2
export SH=/bin/sh
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib} \
	   --with-backward-compatibility-hack
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE
rm %{buildroot}%{_datadir}/globus-user-env.csh
rm %{buildroot}%{_datadir}/globus-user-env.sh
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check NO_EXTERNAL_NET=1
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n globus-common-progs -f %{oreon_filedir}/globus-common-progs.list
%files -n globus-common-devel -f %{oreon_filedir}/globus-common-devel.list
%files -n globus-common-doc -f %{oreon_filedir}/globus-common-doc.list

%changelog

%autochangelog
