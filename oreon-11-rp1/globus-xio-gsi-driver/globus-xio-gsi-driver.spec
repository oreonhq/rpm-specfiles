%global source0_hash 9a28f8da77efbd8560bcfacdd514f81f5653d1c612d7fe3c479e52a4c8c1ed76
Name:		globus-xio-gsi-driver
%global _name %(tr - _ <<< %{name})
Version:	6.2.20251212
Release:        1%{?dist}
Summary:        Grid Community Toolkit - Globus XIO GSI Driver
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
Requires:	globus-gss-assist%{?_isa} >= 11
Requires:	globus-gssapi-gsi%{?_isa} >= 13
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-error-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  globus-xio-devel
BuildRequires:  make
BuildRequires:  perl(strict)
BuildRequires:  perl-interpreter
# /oreon:deps
%package devel
Summary:	Grid Community Toolkit - Globus XIO GSI Driver Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%package doc
Summary:	Grid Community Toolkit - Globus XIO GSI Driver Documentation Files
BuildArch:	noarch
%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus XIO GSI Driver

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus XIO GSI Driver Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus XIO GSI Driver Documentation Files

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build

export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n globus-xio-gsi-driver-devel -f %{oreon_filedir}/globus-xio-gsi-driver-devel.list
%files -n globus-xio-gsi-driver-doc -f %{oreon_filedir}/globus-xio-gsi-driver-doc.list

%changelog

%autochangelog
