%global source0_hash ecd8cc9687bbb5e1b4dddc155aa1f3ea873d6e9f9e968221378daf04c2e4f763

%global pypi_name aioftp
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.26.2
Release:        5%{?dist}
Summary:        FTP client/server for asyncio

License:        Apache-2.0
URL:            https://github.com/aio-libs/aioftp
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
FTP client/server for asyncio.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%if %{with network}
BuildRequires:  %{py3_dist async-timeout}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist siosocks}
BuildRequires:  %{py3_dist trustme}
%endif

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%if %{with network}
%check
%pytest -v tests
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license license.txt
%doc README.rst

%changelog
%autochangelog
