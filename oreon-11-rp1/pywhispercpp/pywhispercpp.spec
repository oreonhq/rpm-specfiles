%global source1_hash bcee25589bb8052d9e155369f6759a05729a2022d2a8085c1aa4345108523077
%global source0_hash 5df897e5dd9d9f16804fc937bd85b9f5880a0b29a55f8843585e0e03d76195e5
%global pypi_name pywhispercpp
%global whispercpp_version 1.8.2
Name:           %{pypi_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Python bindings for whisper.cpp with a simple Pythonic API
ExcludeArch: %{ix86}
License:        MIT
URL:            https://github.com/absadiki/pywhispercpp
Source0:        https://files.pythonhosted.org/packages/source/p/pywhispercpp/pywhispercpp-%{version}.tar.gz
Source1:        https://github.com/ggml-org/whisper.cpp/archive/refs/tags/v%{whispercpp_version}.tar.gz
Provides: bundled(whisper.cpp) = %{whispercpp_version}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cmake) >= 3.18
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-pywhispercpp = %{version}-%{release}
# /oreon:deps
%description
pywhispercpp provides Python bindings for whisper.cpp with a simple
Pythonic API on top of it.

%package -n python3-%{pypi_name}
Summary:        Python bindings for whisper.cpp with a simple Pythonic API
Requires:       python3-qt5
Provides:       pywhispercpp = %{version}-%{release}
%description -n python3-%{pypi_name}
pywhispercpp provides Python bindings for whisper.cpp with a simple
Pythonic API on top of it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# pybind11 is replaced with system available pybind11-devel
rm -rf pybind11
sed -i 's|add_subdirectory(pybind11)|find_package(pybind11 REQUIRED)|g' CMakeLists.txt

# Remove the whisper.cpp copy bundled in pywhispercpp sources and replace it with a 
# separately versioned whisper.cpp tarball
rm -rf whisper.cpp
tar -xzf %{SOURCE1}
mv whisper.cpp-%{whispercpp_version} whisper.cpp

# Remove shebang
find pywhispercpp -name "*.py" -exec sed -i '/^#!/d' {} \;
# Remove repairwheel from build dependencies as it is not available in fedora
sed -i 's/"repairwheel",//g' pyproject.toml

%build

export CMAKE_ARGS=" -DGGML_NATIVE=ON "
export NO_REPAIR=1
%pyproject_wheel
%install
%pyproject_install
chrpath --replace '$ORIGIN' %{buildroot}%{python3_sitearch}/_pywhispercpp*.so
chrpath --replace '$ORIGIN' %{buildroot}%{python3_sitearch}/libggml-cpu.so
chrpath --replace '$ORIGIN' %{buildroot}%{python3_sitearch}/libggml.so
chrpath --replace '$ORIGIN' %{buildroot}%{python3_sitearch}/libwhisper.so.1
rm -rf %{buildroot}%{python3_sitearch}/libwhisper.so
rm -rf %{buildroot}%{python3_sitearch}/libwhisper.so.%{whispercpp_version}
rm -rf %{buildroot}%{_bindir}/pwcpp-assistant
rm -rf %{buildroot}%{_bindir}/pwcpp-recording
rm -rf %{buildroot}%{_bindir}/pwcpp-livestream
%oreon_autofiles main usr/lib/python3*/site-packages/pywhispercpp* usr/lib64/python3*/site-packages/pywhispercpp* usr/bin/*

%check

%pyproject_check_import -e "pywhispercpp.examples*"
%pytest -v tests/test_c_api.py
%files
%files -n python3-pywhispercpp -f %{oreon_filedir}/python3-pywhispercpp.list

%changelog

%autochangelog
