%global source0_hash 9d509a9121431c7228c1f6f71736a73af155bdeb60c324ab09c9eb2e83cfc4b6

%bcond check 1
%global srcname tifffile

Name: python-%{srcname}
Version: 2026.2.16
Release: %autorelease
Summary: Read and write TIFF(r) files

License: BSD-3-Clause
URL: https://www.lfd.uci.edu/~gohlke/
Source0: %{pypi_source}

BuildArch: noarch

BuildRequires: python3-devel

%global _description %{expand:
Tifffile is a Python library to:
 * store numpy arrays in TIFF (Tagged Image File Format) files, and
 * read image and metadata from TIFF-like files used in bioimaging.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  %{py3_dist setuptools}
# Testing
%if %{with check}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist fsspec}
%endif

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Remove shebang
%autosetup -n %{srcname}-%{version}
sed -i -e "1d" tifffile/lsm2bin.py 
sed -i 's/\r$//' README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files tifffile

%if %{with check}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"
# 7 tests fail out of 1000 
# these tests require network or additional packages not in Fedora
pytest-%{python3_version} -v tests \
 --deselect=tests/test_tifffile.py::test_issue_infinite_loop \
 --deselect=tests/test_tifffile.py::test_issue_jpeg_ia \
 --deselect=tests/test_tifffile.py::test_func_pformat_xml \
 --deselect=tests/test_tifffile.py::test_filehandle_seekable \
 --deselect=tests/test_tifffile.py::test_read_cfa \
 --deselect=tests/test_tifffile.py::test_read_tiles \
 --deselect=tests/test_tifffile.py::test_write_cfa \
 --deselect=tests/test_tifffile.py::test_write_volume_png
%else
%pyproject_check_import -t
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/lsm2bin
%{_bindir}/tifffile
%{_bindir}/tiff2fsspec
%{_bindir}/tiffcomment

%changelog
%autochangelog
