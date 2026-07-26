%global source0_hash ea3ff4e5b6a4513ae68169f221a1ba6016962268675a4b983dec6f7c7cf863cb

%global srcname result

Name:           python-%{srcname}
Version:        0.17.0
Release:        %autorelease
Summary:        A Rust-like result type for Python

License:        MIT
URL:            https://github.com/rustedpy/result
# pypi wheel does not contain tests
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch:          %{srcname}-no-cov.diff

BuildArch:      noarch
BuildRequires:  python3-devel
# requirements-dev.txt has extras we don't need
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A simple Result type for Python 3 inspired by Rust, fully type annotated.

The idea is that a result value can be either `Ok(value)` or `Err(error)`, with
a way to differentiate between the two. `Ok` and `Err` are both classes
encapsulating an arbitrary value. `Result[T, E]` is a generic type alias for
`typing.Union[Ok[T], Err[E]]`.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest -v
%if 0%{?python3_version_nodots} >= 310
%pytest -v tests/test_pattern_matching.py
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
