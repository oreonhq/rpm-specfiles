%global source0_hash 0ef2d71173b8bc3af705d1626f52007173bda5719b7270a4d80740779439f23a
%global _hardened_build 1
Name:		globus-gass-server-ez
%global _name %(tr - _ <<< %{name})
Version:	6.2.20251212
Release:        1%{?dist}
Summary:        Grid Community Toolkit - Globus Gass Server_ez
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
# oreon:deps
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gass-transfer-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  make
# /oreon:deps
%package progs
Summary:	Grid Community Toolkit - Globus Gass Server_ez Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}
%package devel
Summary:	Grid Community Toolkit - Globus Gass Server_ez Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus Gass Server_ez

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Globus Gass Server_ez Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus Gass Server_ez Development Files

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n globus-gass-server-ez-progs -f %{oreon_filedir}/globus-gass-server-ez-progs.list
%files -n globus-gass-server-ez-devel -f %{oreon_filedir}/globus-gass-server-ez-devel.list

%changelog

%autochangelog
