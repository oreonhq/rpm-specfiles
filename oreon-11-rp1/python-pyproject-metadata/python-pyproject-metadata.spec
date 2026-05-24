%bcond doc 0
%if 0%{?oreon} || 0%{?rhel} || 0%{?fedora}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           python-pyproject-metadata
Version:        0.11.0
Release:        2%{?dist}
Summary:        PEP 621 metadata parsing

License:        MIT
URL:            https://github.com/FFY00/python-pyproject-metadata
Source0:        https://github.com/FFY00/python-pyproject-metadata/archive/%{version}/pyproject-metadata-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%if %{with tests}
BuildRequires:  python3-pytest
%endif
%if %{with doc}
BuildRequires:  python3-docs
%endif

%global _desc %{expand:Dataclass for PEP 621 metadata with support for core metadata generation.

This project does not implement the parsing of pyproject.toml containing PEP
621 metadata.  Instead, given a Python data structure representing PEP 621
metadata (already parsed), it will validate this input and generate a PEP
643-compliant metadata file (e.g. PKG-INFO).}

%description
%_desc

%package     -n python3-pyproject-metadata
Summary:        PEP 621 metadata parsing
%py_provides    python3-pyproject_metadata
Provides:       python3dist(pyproject-metadata) = %{version}

%description -n python3-pyproject-metadata
%_desc

%if %{with doc}
%package        doc
Summary:        Documentation for python3-pyproject-metadata

%description    doc
Documentation for python3-pyproject-metadata.
%endif

%prep
%autosetup -n pyproject-metadata-%{version} -p1
sed -i /pytest-cov/d pyproject.toml
%if %{with doc}
sed -e 's|\("https://docs\.python\.org/3/", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -i docs/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with doc}
export PYTHONPATH=$PWD
mkdir html
sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}
%endif

%install
%pyproject_install
%pyproject_save_files -l pyproject_metadata

%check
%if %{with tests}
%pytest -v
%endif

%files -n python3-pyproject-metadata -f %{pyproject_files}
%doc docs/changelog.md README.md

%if %{with doc}
%files doc
%doc html
%endif

%changelog
* Sun May 24 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.0-2
- classic spec, tests off by default on oreon

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.0-1
- Prepare for Oreon 11 (RP1)
