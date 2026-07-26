%global source0_hash ffa2f0d6834642fe996d356e728da887201533bb540974ae7ac975e66ecc0e3a

%global pypi_name unicodedata2
%global pypi_version %{version}

Name:           python-%{pypi_name}
Version:        17.0.0
Release:        2%{?dist}
Summary:        Unicodedata backport updated to the latest Unicode version

License:        Apache-2.0
URL:            http://github.com/fonttools/unicodedata2
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)
BuildRequires:  python3dist(pytest-xdist)

%description
This module provides access to the Unicode Character Database (UCD)
which defines character properties for all Unicode characters. The
data contained in this database is compiled from the UCD version 13.0.0.

The versions of this package match Unicode versions, so unicodedata2==13.0.0
is data from Unicode 13.0.0.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module provides access to the Unicode Character Database (UCD) 
which defines character properties for all Unicode characters. The 
data contained in this database is compiled from the UCD version 13.0.0.

The versions of this package match Unicode versions, so unicodedata2==13.0.0 
is data from Unicode 13.0.0.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
