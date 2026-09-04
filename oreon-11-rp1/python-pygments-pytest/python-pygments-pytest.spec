%global source0_hash 5a0fa6d2fbca121f02240facd1caa05ad50193152766692e5057b98c926f772b

%bcond_with tests

Name:           python-pygments-pytest
Version:        2.4.0
Release:        %autorelease
Summary:        A pygments lexer for pytest output
License:        MIT
URL:            https://github.com/asottile/pygments-pytest
Source0:        https://github.com/asottile/pygments-pytest/archive/v%{version}/pygments-pytest-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
This library provides a pygments lexer called pytest.
This library also provides a sphinx extension.

%package -n     python3-pygments-pytest
Summary:        %{summary}

%description -n python3-pygments-pytest
This library provides a pygments lexer called pytest.
This library also provides a sphinx extension.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n pygments-pytest-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygments_pytest

%if %{with tests}
%check
%pytest -v
%endif

%files -n python3-pygments-pytest -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
