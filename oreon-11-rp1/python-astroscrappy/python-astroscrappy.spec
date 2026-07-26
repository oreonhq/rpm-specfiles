%global source0_hash b868079d3e9a2a83f02e2a22a4074fdf2bf115ce3d3038575e6170235c3bf2ca

%global srcname astroscrappy 
%global common_desc Astro-SCRAPPY is designed to detect cosmic rays in images (numpy arrays).

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        Cosmic Ray Annihilation

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source}

BuildRequires:  gcc
ExcludeArch: %{ix86}

%description
%{common_desc}.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{srcname}
%{common_desc}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Remove upper bound version restriction for Cython
sed -i '/Cython>=3/s/, *<3[^"]*//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files astroscrappy

%check
%ifnarch s390x
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}/%{python3_sitearch}
%pytest astroscrappy
popd
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license licenses/LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
