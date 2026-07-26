%global source0_hash 97a9b95d38f6dc69c61e4d33c3af5835937b5be5659cd5e4345cc54c3d106c36

%global srcname puzpy

Name:           python-%{srcname}
# PyPI tarball does not contain test files
Version:        0.5.0
Release:        %autorelease
Summary:        Python crossword puzzle library

License:        MIT
URL:            https://github.com/alexdej/puzpy
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Disable irrelevant tests that pull in unpackaged deps
Patch:          puzpy-drop-unneeded-deps.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Implementation of .puz crossword puzzle file parser based on the .puz file
format documentation.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n %{srcname}-%{version}
%autopatch -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -v

%files -n python3-%{srcname}
%license %{python3_sitelib}/puzpy-%{version}.dist-info/licenses/LICENSE
%doc CHANGELOG.md README.md
%pycached %{python3_sitelib}/puz.py
%{python3_sitelib}/%{srcname}-%{version}.dist-info

%changelog
%autochangelog
