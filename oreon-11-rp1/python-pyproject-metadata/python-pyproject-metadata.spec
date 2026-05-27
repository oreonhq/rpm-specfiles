%global source0_hash e15d2f1bab8b3cf18161773b96f34f0199ef483034c577da2731c3a3290cfe76

# Building the documentation requires the furo Sphinx theme.  But building furo
# requires sphinx_theme_builder, which requires this package.  Avoid a
# dependency loop with this conditional.
%bcond doc 0

Name:           python-pyproject-metadata
Version:        0.11.0
Release:        %autorelease
Summary:        PEP 621 metadata parsing

License:        MIT
URL:            https://github.com/FFY00/python-pyproject-metadata
VCS:            git:%{url}.git
Source:        https://github.com/FFY00/python-pyproject-metadata/archive/0.11.0/pyproject-metadata-0.11.0.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -l pyproject_metadata

BuildRequires:  %{py3_dist pytest}
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

%description -n python3-pyproject-metadata
%_desc

%if %{with doc}
%package        doc
Summary:        Documentation for python3-pyproject-metadata

%description    doc
Documentation for python3-pyproject-metadata.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n pyproject-metadata-%{version}
# No need to BuildRequire pytest-cov to run pytest
sed -i /pytest-cov/d pyproject.toml

%if %{with doc}
# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3/", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -i docs/conf.py
%endif

%build -a
%if %{with doc}
# Build the documentation
export PYTHONPATH=$PWD
mkdir html
sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}
%endif

%check
%pytest -v

%files -n python3-pyproject-metadata -f %{pyproject_files}
%doc docs/changelog.md README.md

%if %{with doc}
%files doc
%doc html
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.0-1
- Import
