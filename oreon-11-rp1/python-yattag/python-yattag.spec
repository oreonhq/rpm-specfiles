%global source0_hash 961ad8ae04333cbacd3b40d8b998fbb51daa1f1ed6001addabe44242981844b4

%global pypi_name yattag

Name:           python-%{pypi_name}
Version:        1.16.1
Release:        %autorelease
Summary:        Generate HTML or XML in a pythonic way

License:        LGPL-2.1-only
URL:            https://www.yattag.org/
Source0:        https://github.com/leforestier/yattag/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Generate HTML or XML in a pythonic way.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
Generate HTML or XML in a pythonic way.

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
%pytest -v test/*.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license license/COPYING

%changelog
%autochangelog
