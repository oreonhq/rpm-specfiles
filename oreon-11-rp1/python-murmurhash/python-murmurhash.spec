%global source0_hash 49d3c401a5b221d5b8118c05154a8bae638ccdbfae1292371bbb466da3a86928

%global pypi_name murmurhash

Name:           python-%{pypi_name}
Version:        1.0.10
Release:        13%{?dist}
Summary:        Cython bindings for MurmurHash2

License:        MIT
URL:            https://github.com/explosion/murmurhash
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Cython bindings for MurmurHash2

%package -n     python3-%{pypi_name}
Summary:        Cython bindings for MurmurHash2

%description -n python3-%{pypi_name}
Cython bindings for MurmurHash2

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove random *.h
rm -rf include/msvc9/stdint.h

%generate_buildrequires
%pyproject_buildrequires requirements.txt

%build
%pyproject_wheel

%check
pushd %{buildroot}/%{python3_sitearch}
%pytest -p no:cacheprovider %{pypi_name}/tests
popd

%install
%pyproject_install

# E: zero-length /usr/lib64/python3.12/site-packages/murmurhash/__init__.pxd
rm %{buildroot}%{python3_sitearch}/%{pypi_name}/__init__.pxd

# remove local murmurhash/ headers
rm -rf %{buildroot}%{python3_sitearch}/%{pypi_name}/include

# remove tests
rm -rf %{buildroot}/%{python3_sitearch}%{pypi_name}/tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info

%changelog
%autochangelog
