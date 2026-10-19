%global source0_hash 1700a82730e473cde9e41e5c91879b44b1d25da831abce8d05a7f86c2c9b0fd0
Name:		globus-proxy-utils
%global _name %(tr - _ <<< %{name})
Version:	7.4
Release:        2%{?dist}
Summary:        Grid Community Toolkit - Globus GSI Proxy Utility Programs
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
# oreon:deps
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gsi-callback-devel
BuildRequires:  globus-gsi-cert-utils-devel
BuildRequires:  globus-gsi-credential-devel
BuildRequires:  globus-gsi-openssl-error-devel
BuildRequires:  globus-gsi-proxy-core-devel
BuildRequires:  globus-gsi-sysconfig-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  globus-openssl-module-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus GSI Proxy Utility Programs

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

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
