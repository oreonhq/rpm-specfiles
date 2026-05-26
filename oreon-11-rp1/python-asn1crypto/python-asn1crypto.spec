# Created by pyp2rpm-3.2.2
%global pypi_name asn1crypto

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        17%{?dist}
Summary:        Fast Python ASN.1 parser and serializer

License:        MIT
URL:            https://github.com/wbond/asn1crypto
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 13ae38502be632115abf8a24cbe5f4da52e3b5231990aff31123c805306ccb9c
%global source0_file asn1crypto-1.5.1.tar.gz
# oreon url source checksums end
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%generate_buildrequires
%pyproject_buildrequires

%description
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/asn1crypto-1.5.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "13ae38502be632115abf8a24cbe5f4da52e3b5231990aff31123c805306ccb9c" || { echo "oreon: Source0 SHA256 mismatch for asn1crypto-1.5.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.1-17
- Prepare for Oreon 11 (RP1)
