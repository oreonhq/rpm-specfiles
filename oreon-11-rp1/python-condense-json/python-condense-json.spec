%global source0_hash 25fe8d434fdafd849e8d98f21a3e18f96ae2d6dbc2c17565f29e4843d039d2bc

Summary:        Python function for condensing JSON using replacement strings
Name:           python-condense-json
Version:        0.1.3
Release:        %autorelease
License:        Apache-2.0
URL:            https://pypi.python.org/project/condense-json/
Source:         %{pypi_source condense_json}
Patch:          python-condense-json-0.1.3-toml.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%global _description \
Python function for condensing JSON using replacement strings

%description %{_description}

%package     -n python3-condense-json
Summary:        %{summary}
%description -n python3-condense-json %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n condense_json-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l condense_json

%check
%pytest

%files -n python3-condense-json -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
