%global source0_hash 86677b4aef54b32bcdc11bb48d63f0a30ee520c8aa60e1f0f51d6cd671ee4010
Name:		globus-ftp-control
%global _name %(tr - _ <<< %{name})
Version:	9.10
Release:        10%{?dist}
Summary:        Grid Community Toolkit - GridFTP Control Library
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
Requires:	globus-gss-assist%{?_isa} >= 11
Requires:	globus-gssapi-gsi%{?_isa} >= 13
Requires:	globus-io%{?_isa} >= 11
Requires:	globus-xio-gsi-driver%{?_isa} >= 4
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-error-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  globus-io-devel
BuildRequires:  globus-xio-devel
BuildRequires:  globus-xio-gsi-driver-devel
BuildRequires:  make
BuildRequires:  openssl
# /oreon:deps
%package devel
Summary:	Grid Community Toolkit - GridFTP Control Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%package doc
Summary:	Grid Community Toolkit - GridFTP Control Library Documentation Files
BuildArch:	noarch
%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GridFTP Control Library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GridFTP Control Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GridFTP Control Library Documentation Files

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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

GLOBUS_HOSTNAME=localhost %make_build check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n globus-ftp-control-devel -f %{oreon_filedir}/globus-ftp-control-devel.list
%files -n globus-ftp-control-doc -f %{oreon_filedir}/globus-ftp-control-doc.list

%changelog

%autochangelog
