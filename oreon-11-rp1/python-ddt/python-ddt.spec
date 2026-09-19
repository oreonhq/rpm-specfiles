%global source0_hash d215d6b083963013c4a19b1e4dcd6a96e80e43ab77519597a6acfcf2e9a3e04b

%bcond tests    1

Name:           python-ddt
Version:        1.7.2
Release:        %autorelease
Summary:        Python library to multiply test cases
License:        MIT
URL:            https://github.com/datadriventests/ddt
Source:         %{pypi_source ddt}
BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
BuildRequires:  python3-six
BuildRequires:  python3-aiounittest
%endif

%global common_description %{expand:
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.}

%description %{common_description}

%package -n python3-ddt
Summary:        %{summary}

%description -n python3-ddt %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ddt-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ddt

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-ddt -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
