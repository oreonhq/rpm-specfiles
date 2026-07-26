%global source0_hash 9d89c42b8927ec67512313fa126fc32d672fb65b6cc721d354057a29afc6245d

Name:		globus-gass-cache-program
%global _name %(tr - _ <<< %{name})
Version:	7.0
Release:	19%{?dist}
Summary:	Grid Community Toolkit - Tools to manipulate local and remote GASS caches

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gass-cache-devel >= 8
BuildRequires:	globus-gass-copy-devel >= 8
BuildRequires:	globus-gass-transfer-devel >= 7
BuildRequires:	globus-gass-server-ez-devel >= 4
BuildRequires:	globus-gram-client-devel >= 12
BuildRequires:	perl-generators

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Tools to manipulate local and remote GASS caches

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

%files
%{_bindir}/globus-gass-cache
%{_bindir}/globus-gass-cache-destroy
%{_bindir}/globus-gass-cache-util
%dir %{_datadir}/globus
%{_datadir}/globus/globus-gass-cache-util.pl
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%changelog
%autochangelog
