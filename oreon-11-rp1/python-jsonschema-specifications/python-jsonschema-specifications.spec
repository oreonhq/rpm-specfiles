%global source0_hash b540987f239e745613c7a9176f3edb72b832a4ac465cf02712288397832b5e8d
Name:           python-jsonschema-specifications
Version:        2025.9.1
Release:        1%{?dist}
Summary:        The JSON Schema meta-schemas and vocabularies, exposed as a Registry
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema-specifications
Source0:        https://files.pythonhosted.org/packages/source/j/jsonschema_specifications/jsonschema_specifications-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-jsonschema-specifications = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jsonschema-specifications
Summary:        The JSON Schema meta-schemas and vocabularies, exposed as a Registry
# oreon:reqs
Requires:       python3dist(referencing) >= 0.31.0
# /oreon:reqs
%description -n python3-jsonschema-specifications

%prep
%global oreon_srcdir jsonschema_specifications-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jsonschema-specifications usr/lib/python3*/site-packages/jsonschema_specifications* usr/lib64/python3*/site-packages/jsonschema_specifications* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jsonschema_specifications* usr/lib64/python3*/site-packages/jsonschema_specifications* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jsonschema-specifications -f %{oreon_filedir}/python3-jsonschema-specifications.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2024.10.1-7
- Prepare for Oreon 11 (RP1)
