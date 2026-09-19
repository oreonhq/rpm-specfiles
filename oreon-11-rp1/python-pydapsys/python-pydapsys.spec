%global source0_hash e4cd8588c76b6ed6c065bca9574c8e8552f631a5b14ef028815c87341a3446c7

%global pypi_name pydapsys

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        %{autorelease}
Summary:        Read recordings made with DAPSYS

%global forgeurl https://github.com/Digital-C-Fiber/PyDapsys
%forgemeta

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource
# Include CITATION.cff
Patch:          %{forgeurl}/commit/7e6ccd6feb8fb5198cf7810d8344ec44ab2f8f85.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
PyDapsys is a package to read neurography recordings made with DAPSYS
(Data Acquisition Processor System). It is based on a
reverse-engineered specification of the binary data format used by the
latest DAPSYS version.

Optionally, the library provides functionality to store loaded data
into Neo datastructures, from where they can be exported into various
other formats.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%pyproject_extras_subpkg -n python3-%{pypi_name} neo

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Drop upper bound on numpy. Allow building with NumPy 2.x.
sed -r -i 's/^numpy.*/numpy = ">=1.21"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x neo

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}

%check
# Project does not provide unit tests
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CITATION.cff
%license LICENSE

%changelog
%autochangelog
