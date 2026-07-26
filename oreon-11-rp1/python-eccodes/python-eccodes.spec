%global source0_hash 08fe1544e6fa597a416bde9a630af4b6e34a021bc3c209f0ece4f7ed5990f992

Name:           python-eccodes
Version:        2.45.0
Release:        1%{?dist}
Summary:        Python interface to the ecCodes GRIB and BUFR decoder/encoder
License:        Apache-2.0

%global sphinx_doc_path build/sphinx/html/

# note: upstream has changed the name on pypi from eccodes-python to eccodes
URL:            https://pypi.org/project/eccodes/
Source0:        https://files.pythonhosted.org/packages/source/e/eccodes/eccodes-%{version}.tar.gz
# see https://github.com/ecmwf/eccodes-python/pull/21
Patch1:         python-eccodes-setup.patch
# see https://github.com/ecmwf/eccodes-python/issues/36
Patch2:         python-eccodes-sphinx-config.patch
# ECMWF introduced a new dependency called findlibs
# to find libeccodes.so easier on non-linux platforms.
# Since this is not useful at all for fedora users 
# I don't plan to package this python lib, so I patched out the use of it.
Patch3:         python-eccodes-disable-findlibs.patch

# note that the fast bindings are arch dependent
BuildRequires:  eccodes-devel
BuildRequires:  python3-devel
# needed to build the fast bindings
BuildRequires:  python3-cffi
# needed for checks/tests
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy
# these next 2 seem not actually used, although they are mentioned as
# test dependencies in the setup.py file:
#BuildRequires:  python3-pytest-cov
#BuildRequires:  python3-pytest-flakes

# needed to build the documentation
BuildRequires:  python3-sphinx

# dont try to build for architectures for which the main
# ecccodes library cannot yet be build

# as explained in bugzilla #1562066
ExcludeArch: i686
# as explained in bugzilla #1562076
# this one should no longer be necessary
# ExcludeArch: s390x
# as explained in bugzilla #1562084
ExcludeArch: armv7hl

%global _description \
Python 3 interface to encode and decode GRIB and BUFR files via the \
ECMWF ecCodes library. It allows reading and writing of GRIB 1 and 2 \
files and BUFR 3 and 4 files.

%description %_description

%package -n python3-eccodes
Summary: %summary

%description -n python3-eccodes %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n eccodes-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l eccodes gribapi

# NOTE:
# this package includes 2 c header files named gribapi/eccodes.h and
# gribapi/grib_api.h in the python module. This is intentional.
# The cffi interface reads them during runtime and extracts some
# constants from them.
# The function grib_get_api_version is called during import of the eccodes
# module and crashes with a runtime error if the files are not there.
# Therefore this next delete has been disabled.
#rm %%{buildroot}%%{python3_sitearch}/gribapi/*.h

# build documentation
# note that the new sphinx-build command only works AFTER installation
# of the module # so it can no longer be executed during the build stage.
PYTHONPATH=%{buildroot}%{python3_sitearch} \
sphinx-build -b html docs %sphinx_doc_path

# remove generated sphinx files that are not part of the actual documentation
rm %sphinx_doc_path/.buildinfo
rm -rf %sphinx_doc_path/.doctrees

%check

%{__python3} -m eccodes selfcheck
%{__python3} -m pytest -v

%files -n python3-eccodes -f %{pyproject_files}
%license  LICENSE
%doc README.rst
%doc %sphinx_doc_path

%changelog
%autochangelog
