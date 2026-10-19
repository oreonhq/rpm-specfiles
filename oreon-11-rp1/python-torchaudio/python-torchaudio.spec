%global source0_hash e59e7bc53709b41a7c9d3f18f2bdeb8b2aaaffcc498b0b9c0b49b20425f121ac
%global pypi_name torchaudio
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 17a70815259222570feb071034acd7bae2adc019
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240318
%global pypi_version 2.3.0
%else
%global pypi_version 2.9.0
%endif
%global desc %{expand: \
The aim of torchaudio is to apply PyTorch to the audio domain. By supporting
PyTorch, torchaudio follows the same philosophy of providing strong GPU
acceleration, having a focus on trainable features through the autograd
system, and having consistent style (tensor names and dimension names).
Therefore, it is primarily a machine learning library and not a general
signal processing library. The benefits of PyTorch can be seen in torchaudio
through having all the computations be through PyTorch operations which
makes it easy to use and feel like a natural extension. }
%ifarch x86_64
%bcond_with rocm
%endif
%global toolchain gcc
Name:           python-%{pypi_name}
%if %{with gitcommit}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
%else
Version:        %{pypi_version}
%endif
Release:        1%{?dist}
Summary:        Audio signal processing, powered by PyTorch
License:        BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND MIT
URL:            https://github.com/pytorch/audio
%if %{with gitcommit}
Source0:        https://github.com/pytorch/audio/archive/refs/tags/v%{version}.tar.gz#/audio-v%{version}.tar.gz
%else
%endif
ExclusiveArch:  x86_64
%if %{with rocm}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-torchaudio = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        Audio signal processing, powered by PyTorch
%description -n python3-%{pypi_name}
%{desc}

%prep

%if %{with gitcommit}
%autosetup -p1 -n audio-%{commit0}
%else
%autosetup -p1 -n audio-%{version}
%endif

rm -rf third_party/*

%build

export BUILD_SOX=OFF
export USE_FFMPEG=OFF
%if %{with rocm}
export USE_ROCM=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
%pyproject_wheel
%else
%pyproject_wheel
%endif
%install
%if %{with rocm}
export USE_ROCM=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
%pyproject_install
%else
%pyproject_install
%endif
for f in `find %{buildroot} -name '*.py'`; do
    if [ ! -x $f ]; then
        sed -i '1{\@^#!/usr/bin@d}' $f
    fi
done
%oreon_autofiles main usr/lib/python3*/site-packages/torchaudio* usr/lib64/python3*/site-packages/torchaudio* usr/bin/*

%files
%files -n python3-torchaudio -f %{oreon_filedir}/python3-torchaudio.list

%changelog

%autochangelog
