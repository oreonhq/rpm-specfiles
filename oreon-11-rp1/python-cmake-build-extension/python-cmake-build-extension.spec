%global source0_hash bfb5edbe2d62b3ae82c6d54a5f0bac5a3c8692d70f816386a4a022dfd18c9c3e
%bcond test_example 1
Name:           python-cmake-build-extension
Version:        0.6.1
Release:        1%{?dist}
Summary:        Setuptools extension to build and package CMake projects
License:        MIT AND BSD-3-Clause
URL:            https://github.com/diegoferigo/cmake-build-extension
Source0:        https://files.pythonhosted.org/packages/source/c/cmake_build_extension/cmake_build_extension-%{version}.tar.gz
Patch:          https://github.com/diegoferigo/cmake-build-extension/pull/55.patch
BuildArch:      noarch
%if %{with test_example}
%endif
%global common_description %{expand:
This project aims to simplify the integration of C++ projects based on CMake
with Python packaging tools. CMake provides out-of-the-box support to either
SWIG and pybind11, that are two among the most used projects to create Python
bindings from C++ sources.
If you have any experience with these hybrid projects, you know the challenges
to make packaging right! This project takes inspiration from pre-existing
examples (pybind/cmake_example, among many others) and provides a simple,
flexible, and reusable setuptools extension with the following features:
  • Bridge between CMake projects and Python packaging.
  • Configure and build the CMake project from setup.py.
  • Install the CMake project in the resulting Python package.
  • Allow passing custom CMake options.
  • Allow creating a top-level __init__.py.
  • Expose C++ executables to the Python environment.
  • Provide a context manager to import reliably CPython modules on all major
    OSs.
  • Disable the C++ extension in editable installations (requiring to manually
    call CMake to install the C++ project).}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cmake-build-extension = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-cmake-build-extension
Summary:        Setuptools extension to build and package CMake projects
License:        MIT
Requires:       cmake
Requires:       ninja-build
%description -n python3-cmake-build-extension %{common_description}

%package -n python3-cmake-build-extension-doc
Summary:        Documentation and examples for cmake-build-extension
Requires:       python3-cmake-build-extension = %{version}-%{release}
%description -n python3-cmake-build-extension-doc %{common_description}

%prep

%autosetup -p1
# We use the system cmake and ninja-build packages in lieu of the PyPI “cmake”
# and “ninja” distributions, respectively.
sed -r -i '/^[[:blank:]]*\b(cmake|ninja)\b[[:blank:]]*$/d' setup.cfg

%if %{with test_example}
# Keep the original example/ “clean” so we can install it as documentation;
# make a copy to test-build.
cp -rp example test_example
%endif

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cmake-build-extension usr/lib/python3*/site-packages/cmake_build_extension* usr/lib64/python3*/site-packages/cmake_build_extension* usr/bin/*
%oreon_autofiles python3-cmake-build-extension-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/cmake_build_extension* usr/lib64/python3*/site-packages/cmake_build_extension* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with test_example}
pushd test_example >/dev/null
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
%pyproject_wheel
BLIB="${PWD}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}"
export PYTHONPATH="${PYTHONPATH}:${BLIB}"
export PATH="${PATH}:${BLIB}/mymath_pybind11/bin:${BLIB}/mymath_swig/bin"
%pytest
popd >/dev/null
%endif
%files
%files -n python3-cmake-build-extension -f %{oreon_filedir}/python3-cmake-build-extension.list
%files -n python3-cmake-build-extension-doc -f %{oreon_filedir}/python3-cmake-build-extension-doc.list

%changelog

%autochangelog
