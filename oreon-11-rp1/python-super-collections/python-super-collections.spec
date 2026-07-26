%global source0_hash 60f6b6641964fd726a90d3c3281b91503d8b53c6f5f89f50bc8875c4d5f5baf1

Name:           python-super-collections
Version:        0.5.3
Release:        %autorelease
Summary:        Python SuperDictionaries (with attributes) and SuperLists

License:        MIT
URL:            https://github.com/fralau/super-collections
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/super-collections-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides a Python library to instantly convert JSON and YAML files
into objects with attributes.}

%description %_description

%package -n     python3-super-collections
Summary:        %{summary}

%description -n python3-super-collections %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n super-collections-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l super_collections

%check
%pytest -v

%files -n python3-super-collections -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
