%global source0_hash 97d99d041d71e3b1831b6713db74ea24ac6e5bfa18eb481598b81d624cad16d2

%bcond bootstrap 0
%bcond tests %{without bootstrap}

Name:           python-tox-current-env
Version:        0.0.17
Release:        %autorelease
Summary:        Tox plugin to run tests in current Python environment

License:        MIT
URL:            https://github.com/fedora-python/tox-current-env
Source0:        https://files.pythonhosted.org/packages/source/t/tox_current_env/tox_current_env-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:	python3dist(pytest-xdist)
BuildRequires:	python3dist(tox) >= 3.28

%description
The tox-current-env plugin allows to run tests in current Python environment.

%package -n     python%{python3_pkgversion}-tox-current-env
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-tox-current-env}

%description -n python%{python3_pkgversion}-tox-current-env
The tox-current-env plugin allows to run tests in current Python environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n tox_current_env-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tox_current_env

%check
%pyproject_check_import -e '*.hooks?'
%if %{with tests}
%pytest -k "not regular and not noquiet_installed_packages[None]"
%endif

%files -n python%{python3_pkgversion}-tox-current-env -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
