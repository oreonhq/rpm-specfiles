%global source0_hash 42ffedcd8c9b6363694300c6ffec1ada77f9620176465719acb27b13a4d6f2de
%global so_version 1
Name:       onnx
Version:    1.21.0
Release:        1%{?dist}
Summary:        Open standard for machine learning interoperability
License:    Apache-2.0
URL:        https://github.com/onnx/onnx
Source0:        https://github.com/onnx/onnx/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:     0001-Build-shared-libraries.patch
Patch:     0002-Fix-install-location.patch
Patch:     0003-Fix-nanobind-arguments.patch
Patch:     0004-Let-pyproject_wheel-use-binaries-from-cmake_build.patch
Patch:     0005-Python-binary-should-link-to-system-onnx.patch
Patch:     0006-Remove-python-parameterized-dependency.patch
Patch:     0007-Add-fixes-for-use-with-onnxruntime.patch
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(protobuf) >= 4.25.1
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-onnx = %{version}-%{release}
# /oreon:deps
%description

%package libs
Summary:    Libraries for %{name}
%description libs

%package devel
Summary:    Development files for %{name}
Requires:   %{name}-libs = %{version}-%{release}
%description devel

%package -n python3-onnx
Summary:        Development files for onnx
Requires:   %{name}-libs = %{version}-%{release}
%description -n python3-onnx

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir onnx-%{version}
%oreon_prep
%build

export VPATH_BUILDDIR=%{_vpath_builddir}
%cmake \
    -DONNX_USE_LITE_PROTO=OFF \
    -DONNX_USE_PROTOBUF_SHARED_LIBS=OFF \
    -DONNX_BUILD_PYTHON=ON \
    -DPython_EXECUTABLE=python3.14 \
    -DPY_EXT_SUFFIX=%{python3_ext_suffix} \
    -DPY_SITEARCH=%{python3_sitearch} \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DONNX_DISABLE_STATIC_REGISTRATION=OFF
%cmake_build
%pyproject_wheel
%install
%cmake_install
find "%{buildroot}/%{_includedir}" -type d -empty -delete
find "%{buildroot}/%{python3_sitearch}" -type d -empty -delete
install -p "./onnx/"*.proto -t "%{buildroot}/%{_includedir}/onnx/"
%pyproject_install
%oreon_autofiles python3-onnx usr/lib/python3*/site-packages/onnx* usr/lib64/python3*/site-packages/onnx* usr/bin/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/onnx* usr/lib64/python3*/site-packages/onnx* usr/bin/*

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
%files
%files -n onnx-libs -f %{oreon_filedir}/onnx-libs.list
%files -n onnx-devel -f %{oreon_filedir}/onnx-devel.list
%files -n python3-onnx -f %{oreon_filedir}/python3-onnx.list

%changelog

%autochangelog
