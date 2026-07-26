%global source0_hash none

%global commit0 d94c9fa77c11afe7d04670d92b3930c417e19f4b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20180610

Name:           bcd
Version:        1.1
Release:        21.%{?date0}git%{?shortcommit0}%{?dist}
Summary:        Bayesian Collaborative Denoiser for Monte-Carlo Rendering
# BSD: main program
# AGPLv3+: src/io/exr
# Automatically converted from old format: BSD and AGPLv3+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND AGPL-3.0-or-later
URL:            https://github.com/superboubek/bcd
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# Many patches are tight to upstream accepting building shared
# and removing bundled dependencies
# https://github.com/superboubek/bcd/issues/12
# don't use bundled deps
Patch0:         bcd-nodeps.patch
# Missing includes
# https://github.com/superboubek/bcd/pull/11
Patch1:         bcd-gcc.patch
# Use system eigen3
# Set std=c++14 for eigen3-5.0.0
Patch2:         bcd-eigen3.patch
# Turn into a shared library forging SONAME (no ABI stability expected)
Patch3:         bcd-links.patch
# Remove cuda arch - not supported in current nvcc
Patch4:         bcd-cuda.patch
# Use system json
Patch5:         bcd-json.patch
# TODO
# BCD calls exit
#https://github.com/superboubek/bcd/issues/13

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++

# As of OpenEXR 3 upstream has significantly reorganized the libraries
# including splitting out imath as a standalone library (which this project may
# or may not need). Please see
# https://github.com/AcademySoftwareFoundation/Imath/blob/master/docs/PortingGuide2-3.md
# for porting details and encourage upstream to support it. For now a 2.x
# compat package is provided.
%if 0%{?fedora} > 33
BuildRequires:  cmake(OpenEXR) < 3
%else
BuildRequires:  OpenEXR-devel
%endif
BuildRequires:  eigen3-devel
BuildRequires:  json-devel
BuildRequires:  zlib-devel

%description
BCD allows to denoise images rendered with Monte Carlo path tracing and
provided in the form of their samples statistics (average, distribution
and covariance of per-pixel color samples). BCD can run in CPU (e.g.,
renderfarm) or GPU (e.g., desktop) mode. It can be integrated as a library
to any Monte Carlo renderer, using the provided sample accumulator to
interface the Monte Carlo simulation with the BCD internals, and comes
with a graphics user interface for designing interactively the denoising
parameters, which can be saved in JSON format and later reused in batch.

BCD has been designed for easy integration and low invasiveness in the
host renderer, in a high spp context (production rendering). There are
at least three ways to integrate BCD in a rendering pipeline, by either:

* Dumping all samples in a raw file, using the raw2bcd tool to generate
the rendering statistics from this file and then running the BCD using
the CLI tool.

* Exporting the mandatory statistics from the rendering loop in EXR
format and running the BCD CLI tool to obtain a denoised image.

* Directly integrating the BCD library into the renderer, using the
sample accumulator to post samples to BCD during the path tracing and
denoising the accumulated values after rendering using the library.

%package        cli
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    cli
The %{name}-cli package contains libraries and header files for
developing applications that use %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
# TODO: Please submit an issue to upstream (rhbz#2380473)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
export CXXFLAGS="%{optflags} $(pkgconf --cflags eigen3 OpenEXR) $(pkgconf --cflags --keep-system-cflags nlohmann_json)/nlohmann"
export LDFLAGS="%{build_ldflags} $(pkgconf --libs eigen3 OpenEXR)"
%cmake \
  -DBCD_BUILD_GUI=OFF \
  %{?_with_cuda: \
   -DCUDA_TOOLKIT_ROOT_DIR=%{_cuda_prefix} \
   -DCUDA_USE_STATIC_CUDA_RUNTIME=OFF \
  } \
  %{!?_with_cuda:-DBCD_USE_CUDA=OFF}

%cmake_build

%install
%cmake_install

%if "%{_lib}" == "lib64"
mv %{buildroot}%{_prefix}/lib \
  %{buildroot}%{_libdir}
%endif

mkdir -p %{buildroot}%{_includedir}
cp -pr include/* %{buildroot}%{_includedir}

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so.0*

%files cli
%{_bindir}/bcd-cli
%{_bindir}/bcd-raw-converter

%files devel
%{_includedir}/bcd
%{_libdir}/*.so

%changelog
%autochangelog
