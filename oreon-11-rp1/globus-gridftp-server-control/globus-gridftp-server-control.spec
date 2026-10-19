%global source0_hash 6d06d6305639b1833dfb60fbff60608f260b8f1563220cbf6d2b41aba4afbfd3
Name:		globus-gridftp-server-control
%global _name %(tr - _ <<< %{name})
Version:	9.5
Release:        2%{?dist}
Summary:        Grid Community Toolkit - Globus GridFTP Server Library
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
Requires:	globus-xio-gsi-driver%{?_isa} >= 2
Requires:	globus-xio-pipe-driver%{?_isa} >= 2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gsi-openssl-error-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-error-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  globus-xio-devel
BuildRequires:  globus-xio-gsi-driver-devel
BuildRequires:  globus-xio-pipe-driver-devel
BuildRequires:  make
# /oreon:deps
%package devel
Summary:	Grid Community Toolkit - Globus GridFTP Server Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus GridFTP Server Library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus GridFTP Server Library Development Files

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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n globus-gridftp-server-control-devel -f %{oreon_filedir}/globus-gridftp-server-control-devel.list

%changelog

%autochangelog
