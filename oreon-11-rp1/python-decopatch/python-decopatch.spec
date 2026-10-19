%global source0_hash 957f49c93f4150182c23f8fb51d13bb3213e0f17a79e09c8cca7057598b55720
Name:           python-decopatch
Version:        1.4.10
Release:        1%{?dist}
Summary:        Helper to write python decorators
License:        BSD-3-Clause
URL:            https://pypi.org/project/decopatch
Source0:        https://files.pythonhosted.org/packages/source/d/decopatch/decopatch-%{version}.tar.gz
Patch:          0001-Adjust-for-whitespace-changes-with-python-3.12.patch
Patch:          decopatch-1.4.10-no-pytest-runner.patch
BuildArch:	noarch
%bcond tests 1
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 39.2
Requires:       python3-decopatch = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-decopatch
Summary:        Helper to write python decorators
%description -n python3-decopatch

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n decopatch-%{version}
cat >pyproject.toml <<EOF
[build-system]
requires = ["setuptools_scm"%{?with_tests:, "pypandoc", "pytest", "pytest-cases"}]
build-backend = "setuptools.build_meta"
EOF

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-decopatch usr/lib/python3*/site-packages/decopatch* usr/lib64/python3*/site-packages/decopatch* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/decopatch* usr/lib64/python3*/site-packages/decopatch* usr/bin/*

%check

%if %{with tests}
TEST_ARGS=(
  --deselect=tests/test_doc.py::test_doc_add_tag_function
)
PYTHONPATH=build/lib %python3 -m pytest -v "${TEST_ARGS[@]}"
%else
%pyproject_check_import
%endif
%files
%files -n python3-decopatch -f %{oreon_filedir}/python3-decopatch.list

%changelog

%autochangelog
