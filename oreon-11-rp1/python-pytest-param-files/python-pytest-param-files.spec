%global source0_hash ab02608d63f7baf14483682ee6213c9330401f2a14d7a63489b872f6830a9848

Name:           python-pytest-param-files
Version:        0.6.0
Release:        8%{?dist}
Summary:        Create pytest parametrize decorators from external files

# SPDX
License:        MIT
URL:            https://pypi.org/project/pytest_param_files/
Source:         %{pypi_source pytest_param_files}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A package to generate parametrized pytests from external files.
Create a text file with the dot format, then use the `param_file` pytest marker
to create a parametrized test.}

%description %_description

%package -n     python3-pytest-param-files
Summary:        %{summary}

%description -n python3-pytest-param-files %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest_param_files-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_param_files

%check
%pytest

%files -n python3-pytest-param-files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
