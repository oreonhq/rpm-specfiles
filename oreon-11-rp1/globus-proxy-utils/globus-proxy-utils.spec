%global source0_hash 1700a82730e473cde9e41e5c91879b44b1d25da831abce8d05a7f86c2c9b0fd0

Name:		globus-proxy-utils
%global _name %(tr - _ <<< %{name})
Version:	7.4
Release:	2%{?dist}
Summary:	Grid Community Toolkit - Globus GSI Proxy Utility Programs

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-openssl-module-devel >= 3
BuildRequires:	globus-gsi-openssl-error-devel >= 2
BuildRequires:	globus-gsi-cert-utils-devel >= 8
BuildRequires:	globus-gsi-sysconfig-devel >= 5
BuildRequires:	globus-gsi-credential-devel >= 5
BuildRequires:	globus-gsi-callback-devel >= 4
BuildRequires:	globus-gsi-proxy-core-devel >= 6
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 4
BuildRequires:	openssl-devel
#		Additional requirements for make check
BuildRequires:	openssl
BuildRequires:	perl-interpreter
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)

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
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%check
%make_build check

%files
%{_bindir}/grid-cert-diagnostics
%{_bindir}/grid-proxy-destroy
%{_bindir}/grid-proxy-info
%{_bindir}/grid-proxy-init
%doc %{_mandir}/man1/grid-cert-diagnostics.1*
%doc %{_mandir}/man1/grid-proxy-destroy.1*
%doc %{_mandir}/man1/grid-proxy-info.1*
%doc %{_mandir}/man1/grid-proxy-init.1*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%changelog
%autochangelog
