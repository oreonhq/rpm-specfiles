%global source0_hash af81861d2dc4698c49e3d965348c240f711a6d9dba4b0d1e15bd299ec2480d88

%global pypi_name smbprotocol

Name:           python-%{pypi_name}
Version:        1.15.0
Release:        4%{?dist}
Summary:        Interact with a server using the SMB 2/3 Protocol

License:        MIT
URL:            https://github.com/jborean93/smbprotocol
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
SMB is a network file sharing protocol and has numerous iterations
over the years. This library implements the SMBv2 and SMBv3 protocol
based on the MS-SMB2 document.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pyspnego)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
SMB is a network file sharing protocol and has numerous iterations
over the years. This library implements the SMBv2 and SMBv3 protocol
based on the MS-SMB2 document.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%pytest -v tests \
  -k "not reset_connection \
  and not config_domain \
  and not message \
  and not dfs"

%files -n python3-%{pypi_name}  -f %{pyproject_files}
%license LICENSE
%doc README.md
%{python3_sitelib}/smbclient/

%changelog
%autochangelog
