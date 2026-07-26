%global source0_hash c0b97799a51041d2e9b6fc1e64ca64d4f4da8eec7bde1cce16c822ba30a2409d

Name:		globus-gridmap-verify-myproxy-callout
%global _name %(tr - _ <<< %{name})
Version:	3.2
Release:	18%{?dist}
Summary:	Grid Community Toolkit - Globus gridmap myproxy callout

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gsi-sysconfig-devel >= 5
BuildRequires:	globus-gssapi-gsi-devel >= 9
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	globus-gridmap-callout-error-devel
BuildRequires:	globus-gsi-credential-devel >= 6
BuildRequires:	globus-gsi-cert-utils-devel >= 8
BuildRequires:	globus-gssapi-error-devel >= 4
BuildRequires:	openssl-devel

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus gridmap myproxy callout

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

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%ldconfig_scriptlets

%files
# This is a loadable module (plugin)
%{_libdir}/libglobus_gridmap_verify_myproxy_callout.so
%config(noreplace) %{_sysconfdir}/gridmap_verify_myproxy_callout-gsi_authz.conf
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%changelog
%autochangelog
