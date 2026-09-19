%global source0_hash 0b18f471956f60adc4cabed25fd8563237f81f2d5107e0cd0b4058110f2be100

Name:           python-jsonref
Version:        1.1.0
Release:        14%{?dist}
Summary:        Python library for automatic dereferencing of JSON Reference objects

License:        MIT
URL:            https://github.com/gazpachoking/jsonref
# PyPI tarball doesn't have tests
Source:         %{url}/archive/v%{version}/jsonref-%{version}.tar.gz
# https://github.com/gazpachoking/jsonref/commit/f18f30772df086bebdcc9b1b76a35558b4a0a897
Patch:          0001-Migrate-to-pdm-backend.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
jsonref is a library for automatic dereferencing of JSON Reference objects for
Python (supporting Python 3.7+).  This library lets you use a data structure
with JSON reference objects, as if the references had been replaced with the
referent data.}

%description %_description

%package -n     python3-jsonref
Summary:        %{summary}

%description -n python3-jsonref %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n jsonref-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jsonref proxytypes

%check
%pytest -v tests.py

%files -n python3-jsonref -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
