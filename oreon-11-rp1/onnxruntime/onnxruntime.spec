%global source0_hash 2a90eb9a306c1eeb29213f5b165a55008ac5cb7d27e0935c4458c51a49ef091d
%global __provides_exclude_from ^(%{python3_sitearch}/onnxruntime/.*|%{_libdir}/rocm/lib/.*)$
%bcond migraphx 0
%bcond dnnl 0
%bcond openvino 0
%bcond test 1
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${backend}
%global backends %nil
%global backends %backends cpu
%if %{with migraphx}
%global backends %backends migraphx
%endif
%if %{with dnnl}
%global backends %backends dnnl
%endif
%if %{with openvino}
%global backends %backends openvino
%endif
%global so_version 1
Summary:        A cross-platform inferencing and training accelerator
Name:       onnxruntime
Version:    1.26.0
Release:        1%{?dist}
License:    MIT AND Apache-2.0 AND BSL-1.0 AND BSD-3-Clause
URL:        https://github.com/microsoft/onnxruntime
Source0:        https://github.com/microsoft/onnxruntime/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:      0001-Disable-download-deps.patch
Patch:      0002-System-date-and-mp11.patch
Patch:      0003-System-safeint.patch
Patch:      0004-System-eigen3.patch
Patch:      0005-System-flatbuffers.patch
Patch:      0006-Do-not-set-COMPILE_WARNING_AS_ERROR.patch
Patch:      0007-migraphx-Fix-C-20-deprecated-this-capture.patch
Patch:      0008-System-dnnl.patch
Patch:      0009-dnnl-Clean-unused-vars.patch
Patch:      0010-openVINO-runtime-fix.patch
Patch:      0011-onnx-static-registration-fix.patch
ExcludeArch:    s390x %{arm} %{ix86}
%ifarch x86_64 aarch64 ppc64 ppc64le s390x riscv64
Provides: libonnxruntime_providers_shared.so()(64bit)
Provides: libonnxruntime_providers_shared.so(VERS_1.0)(64bit)
%else
Provides: libonnxruntime_providers_shared.so
Provides: libonnxruntime_providers_shared.so(VERS_1.0)
%endif
%ifnarch ppc64le
%endif
%if %{with migraphx}
%endif
%if %{with dnnl}
%endif
%if %{with openvino}
%endif
# oreon:deps
BuildRequires:  abseil-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  bzip2
BuildRequires:  cmake
BuildRequires:  cpuinfo-devel
BuildRequires:  date-devel
BuildRequires:  eigen3-devel
BuildRequires:  flatbuffers-compiler
BuildRequires:  flatbuffers-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gsl-devel
BuildRequires:  gtest-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  json-devel
BuildRequires:  make
BuildRequires:  onnx-devel
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-static
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  re2-devel
BuildRequires:  safeint-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{name} is a cross-platform inferencing and training accelerator compatible
with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras,
scikit-learn, and more.

%package devel
Summary:    The development part of the %{name} package
Requires:   %{name}%{_isa} = %{version}-%{release}
%description devel
The development part of the %{name} package

%package -n python3-onnxruntime
Summary:        The development part of the onnxruntime package
%description -n python3-onnxruntime
Python bindings for the %{name} package

%if %{with test}
%package test
Summary:    The test binaries of the %{name} package
Requires:   %{name}%{_isa} = %{version}-%{release}
%description test
The test binaries of the %{name} package
%endif

%if %{with migraphx}
%package migraphx
Summary:    %{summary}
Conflicts:  %{name}%{_isa} = %{version}-%{release}
Provides:   %{name}%{_isa} = %{version}-%{release}
RemovePathPostfixes: .migraphx
%description migraphx
The migraphx execution provider for the %{name} library

%package -n python3-onnxruntime-migraphx
Summary:        A cross-platform inferencing and training accelerator
Conflicts:  python3-onnxruntime = %{version}-%{release}
Provides:   python3-onnxruntime = %{version}-%{release}
RemovePathPostfixes: .migraphx:.migraphx.pyc
%description -n python3-onnxruntime-migraphx
The migraphx execution provider for the %{name} python library

%if %{with test}
%package migraphx-test
Summary:    The test binaries of the %{name}-migraphx package
Requires:   %{name}-migraphx%{_isa} = %{version}-%{release}
Conflicts:  %{name}-test%{_isa} = %{version}-%{release}
Provides:   %{name}-test%{_isa} = %{version}-%{release}
RemovePathPostfixes: .migraphx
%description migraphx-test
The test binaries of the %{name}-migraphx package
%endif

%endif

%if %{with dnnl}
%package dnnl
Summary:    %{summary}
Conflicts:  %{name}%{_isa} = %{version}-%{release}
Provides:   %{name}%{_isa} = %{version}-%{release}
RemovePathPostfixes: .dnnl
%description dnnl
The dnnl execution provider for the %{name} library

%package -n python3-onnxruntime-dnnl
Summary:        A cross-platform inferencing and training accelerator
Conflicts:  python3-onnxruntime = %{version}-%{release}
Provides:   python3-onnxruntime = %{version}-%{release}
RemovePathPostfixes: .dnnl:.dnnl.pyc
%description -n python3-onnxruntime-dnnl
The dnnl execution provider for the %{name} python library

%if %{with test}
%package dnnl-test
Summary:    The test binaries of the %{name}-dnnl package
Requires:   %{name}-dnnl%{_isa} = %{version}-%{release}
Conflicts:  %{name}-test%{_isa} = %{version}-%{release}
Provides:   %{name}-test%{_isa} = %{version}-%{release}
RemovePathPostfixes: .dnnl
%description dnnl-test
The test binaries of the %{name}-dnnl package
%endif

%endif

%if %{with openvino}
%package openvino
Summary:    %{summary}
Conflicts:  %{name}%{_isa} = %{version}-%{release}
Provides:   %{name}%{_isa} = %{version}-%{release}
RemovePathPostfixes: .openvino
%description openvino
The openvino execution provider for the %{name} library

%package -n python3-onnxruntime-openvino
Summary:        A cross-platform inferencing and training accelerator
Conflicts:  python3-onnxruntime = %{version}-%{release}
Provides:   python3-onnxruntime = %{version}-%{release}
RemovePathPostfixes: .openvino:.openvino.pyc
%description -n python3-onnxruntime-openvino
The openvino execution provider for the %{name} python library

%if %{with test}
%package openvino-test
Summary:    The test binaries of the %{name}-openvino package
Requires:   %{name}-openvino%{_isa} = %{version}-%{release}
Conflicts:  %{name}-test%{_isa} = %{version}-%{release}
Provides:   %{name}-test%{_isa} = %{version}-%{release}
RemovePathPostfixes: .openvino
%description openvino-test
The test binaries of the %{name}-openvino package
%endif

%endif

%package doc
Summary:    Documentation files for the %{name} package
%description doc
Documentation files for the %{name} package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# Downstream-only: do not pin the version of abseil-cpp; use what we have.
sed -r -i 's/(FIND_PACKAGE_ARGS[[:blank:]]+)[0-9]{8}/\1/' \
    cmake/external/abseil-cpp.cmake
# Remove unnecesary folders
rm -rf onnxruntime/cmake/external/{onnx,libprotobuf-mutator,emsdk}

%build

%{python3} onnxruntime/core/flatbuffers/schema/compile_schema.py --flatc /usr/bin/flatc
%{python3} onnxruntime/lora/adapter_format/compile_schema.py --flatc /usr/bin/flatc
%global cmake_config \\\
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
 -Donnxruntime_BUILD_BENCHMARKS=OFF \\\
 -Donnxruntime_BUILD_SHARED_LIB=ON \\\
 -Donnxruntime_ENABLE_PYTHON=ON \\\
 -DPYTHON_VERSION=%{python3_version} \\\
 -Donnxruntime_DISABLE_ABSEIL=OFF \\\
 -Donnxruntime_ENABLE_DLPACK=OFF \\\
 -Donnxruntime_USE_FULL_PROTOBUF=ON \\\
 -Donnxruntime_USE_PREINSTALLED_EIGEN=ON \\\
 -Deigen_SOURCE_PATH=/usr/include/eigen3 \\\
 -DProtobuf_BUILD_SHARED_LIBS=OFF \\\
 -S cmake
%ifarch ppc64le
%global cmake_config %cmake_config \\\
 -Donnxruntime_ENABLE_CPUINFO=OFF
%else
%global cmake_config %cmake_config \\\
 -Donnxruntime_ENABLE_CPUINFO=ON
%endif
%if %{with test}
%global cmake_tests \\\
 -Donnxruntime_BUILD_UNIT_TESTS=ON
%else
%global cmake_tests \\\
 -Donnxruntime_BUILD_UNIT_TESTS=OFF
%endif
for backend in %backends; do
    cp -R ./onnxruntime ./onnxruntime.bak
    cp ./requirements.txt ./requirements.txt.bak
    if [ "${backend}" == "cpu" ]; then
        %cmake %cmake_config \
            %cmake_tests
    elif [ "${backend}" == "migraphx" ]; then
        %cmake %cmake_config \
            %cmake_tests \
            -Donnxruntime_USE_MIGRAPHX=ON
    elif [ "${backend}" == "dnnl" ]; then
        %cmake %cmake_config \
            %cmake_tests \
            -Donnxruntime_USE_DNNL=ON
    elif [ "${backend}" == "openvino" ]; then
        %cmake %cmake_config \
            %cmake_tests \
            -Donnxruntime_USE_OPENVINO=ON
    fi
    %cmake_build
    cp -R ./%{__cmake_builddir}/onnxruntime/* ./onnxruntime
    cp ./%{__cmake_builddir}/requirements.txt ./requirements.txt
    if [ "${backend}" == "cpu" ]; then
        %pyproject_wheel
    elif [ "${backend}" == "migraphx" ]; then
        %pyproject_wheel -C--global-option=--use_migraphx
    elif [ "${backend}" == "dnnl" ]; then
        cp -p ./%{__cmake_builddir}/libonnxruntime_providers_dnnl.so \
              ./onnxruntime/capi/
        %pyproject_wheel -C--global-option=--use_dnnl
    elif [ "${backend}" == "openvino" ]; then
        %pyproject_wheel -C--global-option=--use_openvino
    fi
    mkdir -p dist_onnxruntime_${backend}
    mv %{_pyproject_wheeldir}/*.whl dist_onnxruntime_${backend}/
    mv ./build dist_onnxruntime_${backend}/
    rm -rf ./onnxruntime
    rm -rf ./requirements.txt
    mv ./onnxruntime.bak ./onnxruntime
    mv ./requirements.txt.bak ./requirements.txt
done
%install
mkdir -p %{_builddir}/buildroot_acumulator
for backend in %backends; do
    %cmake_install
    if [ "${backend}" = "cpu" ]; then
        mkdir -p "%{buildroot}/%{_docdir}/"
        cp --preserve=timestamps -r "./docs/" "%{buildroot}/%{_docdir}/%{name}"
    fi
    cp dist_onnxruntime_${backend}/*.whl %{_pyproject_wheeldir}/
    cp -r dist_onnxruntime_${backend}/build ./build
    %pyproject_install
    %if ! %{with test}
        rm -rf %{buildroot}%{_bindir}
    %endif
    if [ "${backend}" = "cpu" ]; then
        cp %{pyproject_files} %{_builddir}/files_${backend}
    else
        cp %{pyproject_files} %{_builddir}/files_${backend}
        sed -i '/^%dir/! { /\.dist-info/! s/$/.'"${backend}"'/}' %{_builddir}/files_${backend}
        find %{buildroot}%{python3_sitearch}/onnxruntime/ -type f -exec bash -c 'mv "${0}" "${0}.'"${backend}"'"' {} \;
        sed -i 's/.pyc.'"${backend}"'$/.pyc.'"${backend}"'.pyc/' %{_builddir}/files_${backend}
        find %{buildroot}%{python3_sitearch}/onnxruntime/ -type f -iname "*.pyc.${backend}" -exec bash -c 'mv "${0}" "${0}.pyc"' {} \;
        mv  %{buildroot}%{_libdir}/libonnxruntime.so.%{version} \
            %{buildroot}%{_libdir}/libonnxruntime.so.%{version}.${backend}
        mv  %{buildroot}%{_libdir}/libonnxruntime_providers_shared.so \
            %{buildroot}%{_libdir}/libonnxruntime_providers_shared.so.${backend}
        %if %{with test}
            mv  %{buildroot}%{_bindir}/onnx_test_runner \
                %{buildroot}%{_bindir}/onnx_test_runner.${backend}
            mv  %{buildroot}%{_bindir}/onnxruntime_test \
                %{buildroot}%{_bindir}/onnxruntime_test.${backend}
        %endif
    fi
    rm -f %{_pyproject_record}
    cp -a %{buildroot}/* %{_builddir}/buildroot_acumulator/
    rm -rf %{buildroot}/*
    rm -rf %{_pyproject_wheeldir}/*
    rm -rf ./build
done
mkdir -p %{buildroot}
cp -a %{_builddir}/buildroot_acumulator/* %{buildroot}
rm -rf %{_builddir}/buildroot_acumulator
%oreon_autofiles python3-onnxruntime usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with test}
%check

export GTEST_FILTER=" \
    -CContribOpTest.StringNormalizerSensitiveFilterOutNoCase \
    -CContribOpTest.StringNormalizerSensitiveFilterOutLower \
    -CContribOpTest.StringNormalizerSensitiveFilterOutUpper \
    -CContribOpTest.StringNormalizerSensitiveFilterOutUpperWithLocale \
    -CContribOpTest.StringNormalizerInsensitiveFilterOutUpperWithLocale \
    -CContribOpTest.StringNormalizerSensitiveFilterOutUpperEmptyCase \
    -CContribOpTest.StringNormalizerSensitiveFilterOutUpperSameOutput \
    -CRandom.MultinomialGoodCase \
    -CRandom.MultinomialDefaultDType \
    -CSamplingTest.Gpt2Sampling_CPU "
%if %{with test}
for backend in %backends; do
    %ctest
done
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n onnxruntime-devel -f %{oreon_filedir}/onnxruntime-devel.list
%files -n python3-onnxruntime -f %{oreon_filedir}/python3-onnxruntime.list
%files -n onnxruntime-test -f %{oreon_filedir}/onnxruntime-test.list
%files -n onnxruntime-doc -f %{oreon_filedir}/onnxruntime-doc.list

%changelog

%autochangelog
%endif
%endif
%endif
