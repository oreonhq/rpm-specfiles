%global source0_hash 6a4ad8c85c9efe90d6927d27177b9c3a3de245ab63e7e5c00c3fac3a5b98065f

%global pypi_name peachpy
%global pypi_version 0.2.0
# No tags
%global commit0 349e8f836142b2ed0efeb6bb99b1b715d87202e9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           python-peachpy
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Portable Efficient Assembly Codegen in Higher-level Python

License:        BSD-2-Clause
URL:            https://github.com/Maratyszcza/PeachPy/
Source0:        %{url}/archive/%{commit0}/%{pypi_name}-%{shortcommit0}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
# Do not work with upstream 0.3.14
BuildRequires:  python3dist(opcodes) = 0.3.13

%description
PeachPy is a Python framework for writing high-performance assembly kernels.
PeachPy aims to simplify writing optimized assembly kernels while preserving
all optimization opportunities of traditional assembly.

%package -n     python3-%{pypi_name}
Summary:        Portable Efficient Assembly Codegen in Higher-level Python

%description -n python3-%{pypi_name}
PeachPy is a Python framework for writing high-performance assembly kernels.
PeachPy aims to simplify writing optimized assembly kernels while preserving
all optimization opportunities of traditional assembly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n PeachPy-%{commit0}

# Remove arm test
rm tests/arm/test_arm.py
# Does not work with anything but 0.3.13
sed -i -e 's@Opcodes>=0.3.13@Opcodes==0.3.13@' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst

%changelog
%autochangelog
