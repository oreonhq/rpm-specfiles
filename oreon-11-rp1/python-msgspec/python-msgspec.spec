%global source0_hash 33961077a37830c54fa3108bd226a9d7a09b91ff82ef7b976a371039b54b6bc7

%global debug_package %{nil}
%global pypi_name msgspec

Name:           python-%{pypi_name}
Summary:        Fast serialization and validation library
Version:        0.19.0
Source:         https://github.com/jcrist/%{pypi_name}/archive/refs/tags/%{version}/msgspec-%{version}.tar.gz
Release:        %autorelease

License:        BSD-3-Clause
URL:            https://jcristharif.com/msgspec/

# Python 3.14: Fix annotations support
Patch:          https://github.com/jcrist/msgspec/pull/852.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(wheel)
# Adding the pytest dependency manually, as the `tests` extras group also
# includes mypy, pyright, pre-commit and other unpackaged dependencies
BuildRequires:  python3dist(pytest)
BuildRequires:  gcc
ExcludeArch: s390x i686

%generate_buildrequires
%pyproject_buildrequires

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%global _description %{expand:
A fast serialization and validation library, with builtin support for
JSON, MessagePack, YAML, and TOML.}

%description %_description
%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
# Relax all getrefcount tests to allow lower numbers
# Proposed as https://github.com/jcrist/msgspec/pull/854 but does not apply cleanly
sed -Ei 's/sys\.getrefcount\(([^\)]+)\) == ([0-9]+)/sys.getrefcount(\1) <= \2/' tests/test_*.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
# tests/test_raw.py::test_raw_copy_doesnt_leak calls Python from subprocess and is confused by msgspec in $PWD
export PYTHONSAFEPATH=1
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
