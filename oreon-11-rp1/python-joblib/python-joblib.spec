%global source0_hash 8561a3269e6801106863fd0d6d84bb737be9e7631e33aaed3fb9ce5953688da3

%bcond check 0

%global srcname joblib

Name:  python-%{srcname}
Version: 1.5.3
Release: %autorelease
Summary: Lightweight pipelining: using Python functions as pipeline jobs

License: BSD-3-Clause
URL: https://joblib.readthedocs.io
Source0: %{pypi_source}

Patch: joblib-unbundle-cloudpickle.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Joblib is a set of tools to provide lightweight pipelining in Python.
In particular, joblib offers:
 * transparent disk-caching of the output values and lazy
   re-evaluation (memorize pattern)
 * easy simple parallel computing
 * logging and tracing of the execution}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

# Testing
%if %{with check}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist lz4}
BuildRequires:  %{py3_dist psutil} 
BuildRequires:  %{py3_dist threadpoolctl}
%endif

Recommends: %{py3_dist numpy}
Recommends: %{py3_dist lz4}
Recommends: %{py3_dist psutil} 
Provides: bundled(python3dist(loky)) = 3.5.6

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
rm -rf joblib/externals/cloudpickle/ 

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files joblib

%if %{with check}
%check
%pytest \
 --deselect "joblib/test/test_memory.py::test_parallel_call_cached_function_defined_in_jupyter" \
 --deselect "joblib/test/test_numpy_pickle.py::test_joblib_pickle_across_python_versions" \
 --deselect "joblib/test/test_numpy_pickle.py::test_joblib_pickle_across_python_versions_with_mmap" \
  joblib
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
