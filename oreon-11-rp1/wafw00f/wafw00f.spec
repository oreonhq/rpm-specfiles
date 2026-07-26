%global source0_hash e4a784b5c6f0632d129146e0a6a769495044e6faa7ab8b498d1f6d5b14744479

Name:           wafw00f
Version:        2.3.2
Release:        2%{?dist}
Summary:        Tool to identifies and fingerprints Web Application Firewall (WAF)

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sandrogauci/wafw00f
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
WAFW00F identifies and fingerprints Web Application Firewall (WAF) products.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
sed -i -e '/^#!\//, 1d' {wafw00f/*.py,wafw00f/*/*.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files
%doc CREDITS.txt README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.dist-info/
%{python3_sitelib}/%{name}/

%changelog
%autochangelog
