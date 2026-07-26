%global source0_hash 407ec0bd3f65fccc3ac8e02f7ba3bb31c95ceca10ebdcfe66120bf56db28e59b

%global srcname conda-package-streaming
%global pkgname conda_package_streaming

# We have a circular dep on conda for tests
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        0.11.0
Release:        9%{?dist}
Summary:        Extract metadata from remote conda packages without downloading whole file

License:        BSD-3-Clause
URL:            https://github.com/conda/conda-package-streaming
Source0:        https://github.com/conda/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global common_description %{expand:Download conda metadata from packages without transferring entire file. Get
metadata from local .tar.bz2 packages without reading entire files.

Uses enhanced pip lazy_wheel to fetch a file out of .conda with no more than
3 range requests, but usually 2.

Uses tar = tarfile.open(fileobj=...) to stream remote .tar.bz2. Closes the
HTTP request once desired files have been seen.}

%description
%{common_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
%if %{without bootstrap}
# Need conda executable for tests
BuildRequires:  conda
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# do not run coverage in pytest, drop unneeded and unpackaged boto3-stubs dev dep
sed -i -e '/cov/d' -e '/boto3-stubs/d' pyproject.toml requirements.txt
%if %{with bootstrap}
sed -i -e '/"conda"/d' -e '/conda-package-handling/d' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pkgname}

%check
%if %{without bootstrap}
# To set CONDA_EXE
. /etc/profile.d/conda.sh
export CONDA_EXE
# The deselected tests require a populated conda package cache which we can't really provide
%pytest -v tests \
  --deselect=tests/test_transmute.py::test_transmute \
  --deselect=tests/test_transmute.py::test_transmute_backwards \
  --deselect=tests/test_url.py::test_lazy_wheel
%else
# Minimal non-conda required test
%pytest -v tests/test_degraded.py
%endif

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
