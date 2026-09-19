%global source0_hash 5537529bddc7fa07e773d5cd9baca593e3f5d93474edd1914f68e89506042b33

%global srcname astroquery

Name:           python-%{srcname}
Version:        0.4.11
Release:        %autorelease
Summary:        Python module to access astronomical online data resources

License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

# This package is imported but is not listed as a dep
BuildRequires:  %{py3_dist pillow}
Requires:  %{py3_dist pillow}

%description
Astroquery is an astropy affiliated package that contains a collection of tools
to access online Astronomical data.

%package -n python3-%{srcname}
Summary:  %{summary}

%description -n python3-%{srcname}
Astroquery is an astropy affiliated package that contains a collection of tools
to access online Astronomical data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
# test deps not in Fedora (pytest-dependency)
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files astroquery

%check
%pyproject_check_import -e '*.test*' -e '*.conftest' -e '*.dace'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
