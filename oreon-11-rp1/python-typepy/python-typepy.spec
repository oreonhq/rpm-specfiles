%global source0_hash b69fd48b9f50cdb3809906eef36b855b3134ff66c8893a4f8580abddb0b39517

%global pypi_name typepy

Name:           python-%{pypi_name}
Version:        1.3.2
Release:        7%{?dist}
Summary:        Python library for variable type checker/validator/converter at a run time

License:        MIT
URL:            https://github.com/thombashi/typepy 
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

#test requirements
BuildRequires:  python3-tcolorpy
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil
%description
Python library for variable type checker/validator/converter at a run time.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:  python3-mbstrdecoder >= 1.0.0

%description -n python3-%{pypi_name}
Python library for variable type checker/validator/converter at a run time.

%pyproject_extras_subpkg -n python3-%{pypi_name} datetime

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

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files} 
%license LICENSE
%doc README.rst

%changelog
%autochangelog
