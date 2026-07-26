%global source0_hash b23fc42ff6f6ef6954e4852c1fb512cdd18dbea03134f91f856a95ccc9461f78

%global pypi_name typing-inspect
%global pypi_srcname typing_inspect

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        12%{?dist}
Summary:        Runtime inspection utilities for typing module

License:        MIT
URL:            https://github.com/ilevkivskyi/%{pypi_srcname}
Source0:        %{pypi_source %pypi_srcname}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(mypy-extensions) >= 0.3.0
BuildRequires:  python3dist(typing-extensions) >= 3.7.4
BuildRequires:  python3dist(pytest)

%description
Typing Inspect The "%{pypi_srcname}" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(mypy-extensions) >= 0.3.0
Requires:       python3dist(typing-extensions) >= 3.7.4
%description -n python3-%{pypi_name}
The "%{pypi_srcname}" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_srcname}

%check
%pytest --deselect=test_typing_inspect.py::GetUtilityTestCase::test_parameters \
  --deselect=test_typing_inspect.py::GetUtilityTestCase::test_typed_dict_mypy_extension

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
