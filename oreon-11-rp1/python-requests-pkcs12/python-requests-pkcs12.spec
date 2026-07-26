%global source0_hash 623f25d75e20f017f1c241cc10a1fa264dcb27da27e9f7bf8bbd1dd9cb685787

%global pypi_name requests-pkcs12

Name:           python-%{pypi_name}
Version:        1.27
Release:        2%{?dist}
Summary:        Add PKCS12 support to the requests library

License:        ISC
URL:            https://github.com/m-click/requests_pkcs12
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Source1:        test_integration.py
BuildArch:      noarch

%description
This library adds PKCS12 support to the Python requests library. It is
integrated into requests as recommended by its authors: creating a custom
TransportAdapter, which provides a custom SSLContext.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

# For tests
BuildRequires:  python3-requests
BuildRequires:  python3-pytest
BuildRequires:  openssl

%description -n python3-%{pypi_name}
This library adds PKCS12 support to the Python requests library. It is
integrated into requests as recommended by its authors: creating a custom
TransportAdapter, which provides a custom SSLContext.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n requests_pkcs12-%{version}
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l requests_pkcs12

%check
%pyproject_check_import
%{pytest} -v

# embeded test with connection to example.com
# skip it with unavailable network (in koji)
if getent hosts example.com; then
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="%{buildroot}%{_bindir}:$PATH" \
    PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}" \
    %{__python3} -c 'import requests_pkcs12; requests_pkcs12.test()'
fi

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
