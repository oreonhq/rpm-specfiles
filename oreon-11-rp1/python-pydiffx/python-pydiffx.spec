%global source0_hash 0986dbb0a87cbf79e244e2f1c0e2b696d8e86b3861ea2955757a61d38e139228

Name:           python-pydiffx
Version:        1.1
Release:        15%{?dist}
Summary:        Python implementation of the DiffX specification
License:        MIT
URL:            https://diffx.org/pydiffx/
Source:         %{pypi_source pydiffx}

BuildArch:      noarch

BuildRequires:  python3-devel

# https://github.com/beanbaginc/diffx/pull/2
Patch:          add_requirements.patch
# https://github.com/beanbaginc/diffx/issues/4
Patch:          pydiffx-1.1-Fix-Python-3.12-compatibility.patch

%global _description %{expand:
DiffX is a proposed specification for a structured version of Unified
Diffsthat contains metadata, standardized parsing, multi-commit diffs, and
binary diffs, in a format compatible with existing diff parsers.

This module is a reference implementation designed to make it easy to read
and write DiffX files in any Python application.}

%description %_description

%package -n python3-pydiffx
Summary:        %{summary}

%description -n python3-pydiffx %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pydiffx-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pydiffx

%check
%pytest

%files -n python3-pydiffx -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
