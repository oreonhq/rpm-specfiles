%global source0_hash 7dcc02e8a372098d51a98737e7f662e6edfd75cec7070a11e904141de49d866b

%global srcname pytest-shutil
%global sum A goodie-bag of unix shell and environment tools for py.test

Name:           python-%{srcname}
Version:        1.8.1
Release:        %autorelease
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
This library is a goodie-bag of Unix shell and 
environment management tools for automated tests.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
This library is a goodie-bag of Unix shell and 
environment management tools for automated tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_shutil

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES.md

%changelog
%autochangelog
