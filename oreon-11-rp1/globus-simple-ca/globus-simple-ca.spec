%global source0_hash b2ef4519295cc42f793db12f41689686f07d8176cb3896e40a126b852bfa002f

Name:		globus-simple-ca
%global _name %(tr - _ <<< %{name})
Version:	5.4
Release:	10%{?dist}
Summary:	Grid Community Toolkit - Simple CA Utility

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	openssl
#		Additional requirements for make check
BuildRequires:	globus-common-progs >= 15
BuildRequires:	perl-interpreter
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)

Requires:	globus-common-progs >= 15
Requires:	globus-gsi-cert-utils-progs
Requires:	openssl

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Simple CA Utility

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

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
%{_bindir}/grid-ca-create
%{_bindir}/grid-ca-package
%{_bindir}/grid-ca-sign
%doc %{_mandir}/man1/grid-ca-create.1*
%doc %{_mandir}/man1/grid-ca-package.1*
%doc %{_mandir}/man1/grid-ca-sign.1*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%changelog
%autochangelog
