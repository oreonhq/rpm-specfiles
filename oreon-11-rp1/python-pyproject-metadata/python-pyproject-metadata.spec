%global source0_hash 780315afa93ff19a76df85f0a7db2a2984763ef7728f81383513974f4061366a

%bcond doc 0

Name:           python-pyproject-metadata
Version:        0.12.1
Release:        1%{?dist}
Summary:        PEP 621 metadata parsing
License:        MIT
URL:            https://github.com/FFY00/python-pyproject-metadata
Source0:        https://github.com/FFY00/python-pyproject-metadata/archive/%{version}/pyproject-metadata-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Dataclass for PEP 621 metadata with support for core metadata generation.

This project does not implement the parsing of pyproject.toml containing PEP
621 metadata. Instead, given a Python data structure representing PEP 621
metadata (already parsed), it will validate this input and generate a PEP
643-compliant metadata file (e.g. PKG-INFO).}

%description %_description

%package -n     python3-pyproject-metadata
Summary:        %{summary}

%description -n python3-pyproject-metadata %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n pyproject-metadata-%{version}
sed -i /pytest-cov/d pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyproject_metadata

%check
%pyproject_check_import
%pytest -v

%files -n python3-pyproject-metadata -f %{pyproject_files}
%doc docs/changelog.md README.md

%changelog
%autochangelog
