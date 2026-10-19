%global source0_hash 0b18f471956f60adc4cabed25fd8563237f81f2d5107e0cd0b4058110f2be100
Name:           python-jsonref
Version:        1.1.0
Release:        14%{?dist}
Summary:        Python library for automatic dereferencing of JSON Reference objects
License:        MIT
URL:            https://github.com/gazpachoking/jsonref
Source0:        https://github.com/gazpachoking/jsonref/archive/v%{version}/jsonref-%{version}.tar.gz
Patch:          0001-Migrate-to-pdm-backend.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pdm-pep517) >= 1.0.0
Requires:       python3-jsonref = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jsonref
Summary:        Python library for automatic dereferencing of JSON Reference objects
%description -n python3-jsonref

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jsonref-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jsonref usr/lib/python3*/site-packages/jsonref* usr/lib64/python3*/site-packages/jsonref* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jsonref* usr/lib64/python3*/site-packages/jsonref* usr/bin/*

%check

%pytest -v tests.py
%files
%files -n python3-jsonref -f %{oreon_filedir}/python3-jsonref.list

%changelog

%autochangelog
