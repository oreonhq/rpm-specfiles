%global source0_hash ebb38f303f8a3f794db816196315bcddad880be0dc75094e3334bc271db2ed39

%global pypi_name opensearch-py

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        %autorelease
Summary:        Python low-level client for OpenSearch

License:        Apache-2.0
URL:            https://github.com/opensearch-project/%{pypi_name}
Source0:        %{pypi_source opensearch_py}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
opensearch-py is a community-driven, open source OpenSearch client
licensed under the Apache v2.0 License. 
For more information, see opensearch.org.}

%description %_description

%pyproject_extras_subpkg -n python3-opensearch-py async kerberos

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n opensearch_py-%{version}

# Fedora patches certifi anyway to use system certs
sed -i 's/"certifi>=.*"/"certifi"/' setup.py

%generate_buildrequires
%pyproject_buildrequires -x async -x kerberos

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files opensearchpy

%check
%pyproject_check_import -e opensearchpy.helpers.test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
