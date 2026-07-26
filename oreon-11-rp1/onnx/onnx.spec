%global source0_hash 8d5e983c36037003615e5a02d36b18fc286541bf52de1a78f6cf9f32005a820e

Name:       onnx
Version:    1.17.0
Release:    12%{?dist}
Summary:    Open standard for machine learning interoperability
License:    Apache-2.0

URL:        https://github.com/onnx/onnx
Source0:    https://github.com/onnx/onnx/archive/v%{version}/%{name}-%{version}.tar.gz
# Build shared libraries and fix install location 
Patch:     0000-Build-shared-libraries-and-fix-install-location.patch
# Use system protobuf and require parameterized
Patch:     0001-Use-system-protobuf-and-require-parameterized.patch
# Let pyproject_wheel use binaries from cmake_build
Patch:     0002-Let-pyproject_wheel-use-binaries-from-cmake_build.patch
# Add fixes for use with onnxruntime
Patch:     0003-Add-fixes-for-use-with-onnxruntime.patch
# Add fixes for use with onnxruntime
Patch:     0004-Remove-python-parameterized-dependency.patch

%if %{undefined fc40} && %{undefined fc41}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

BuildRequires:  cmake >= 3.13
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pybind11
BuildRequires:  python3-pytest
BuildRequires:  protobuf-devel

%global _description %{expand:
%{name} provides an open source format for AI models, both deep learning and
traditional ML. It defines an extensible computation graph model, as well as
definitions of built-in operators and standard data types.}

%description %_description

%package libs
Summary:    Libraries for %{name}

%description libs %_description

%package devel
Summary:    Development files for %{name}
Requires:   %{name}-libs = %{version}-%{release} 

%description devel %_description

%package -n python3-onnx
Summary:    %{summary}
Requires:   %{name}-libs = %{version}-%{release}

%description -n python3-onnx %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n onnx-%{version}

# Use system protobuf
sed -r -i 's/protobuf>=3.20.2/protobuf>=3.14.0/' pyproject.toml

# Drop nbval options from pytest. Plugin is not available in Fedora.
sed -r \
    -e 's/--nbval //' \
    -e 's/--nbval-current-env //' \
    -i pyproject.toml

%generate_buildrequires
%pyproject_buildrequires requirements-reference.txt

%build
%cmake \
    -DONNX_USE_LITE_PROTO=OFF \
    -DONNX_USE_PROTOBUF_SHARED_LIBS=ON \
    -DBUILD_ONNX_PYTHON=ON \
    -DPYTHON_EXECUTABLE=%{python3} \
    -DPY_EXT_SUFFIX=%{python3_ext_suffix} \
    -DPY_SITEARCH=%{python3_sitearch} \
    -DCMAKE_SKIP_RPATH:BOOL=ON
# Generate protobuf header and source files
%cmake_build -- gen_onnx_proto
# Build 
%cmake_build
# Build python libs
%pyproject_wheel

%install
%cmake_install
# Need to remove empty directories
find "%{buildroot}/%{_includedir}" -type d -empty -delete
find "%{buildroot}/%{python3_sitearch}" -type d -empty -delete
# Install *.proto files
install -p "./onnx/"*.proto -t "%{buildroot}/%{_includedir}/onnx/"

%pyproject_install
%pyproject_save_files onnx

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%ifarch riscv64
export PYTEST_ADDOPTS="-k 'not test_float8_e4m3fn_negative_nan and \
not test_float8_e5m2_negative_nan and not test_maxpool_2d_uint8_cpu'"
%endif
%ifarch s390x
export PYTEST_ADDOPTS="-k 'not test_make_tensor_raw'"
%endif

%pytest

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libonnx.so.%{version}
%{_libdir}/libonnx_proto.so.%{version}

%files devel
%{_libdir}/libonnx.so
%{_libdir}/libonnx_proto.so
%{_libdir}/cmake/ONNX
%{_includedir}/%{name}/

%files -n python3-onnx -f %{pyproject_files}
%{_bindir}/backend-test-tools
%{_bindir}/check-model
%{_bindir}/check-node

%changelog
%autochangelog
