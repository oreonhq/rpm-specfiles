%global source0_hash e632fa5986894c8a74f39ed6a2153bfe445d9550119ebe48273e867f445042bc
Name:		globus-gram-client-tools
%global _name %(tr - _ <<< %{name})
Version:	12.2
Release:        10%{?dist}
Summary:        Grid Community Toolkit - Job Management Tools (globusrun)
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
Requires:	globus-common-progs >= 15
# oreon:deps
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gass-server-ez-devel
BuildRequires:  globus-gass-transfer-devel
BuildRequires:  globus-gram-client-devel
BuildRequires:  globus-gram-protocol-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-rsl-devel
BuildRequires:  make
# /oreon:deps
%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Job Management Tools (globusrun)

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
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
