%global source0_hash 5d6ccfb4aae6111d60518d4194c673d7dc1b5b7ac56f89568b12cc2a906b1563
%global commit0 d94c9fa77c11afe7d04670d92b3930c417e19f4b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20180610
Name:           bcd
Version:        1.1
Release:        1%{?dist}
Summary:        Bayesian Collaborative Denoiser for Monte-Carlo Rendering
License:        LicenseRef-Callaway-BSD AND AGPL-3.0-or-later
URL:            https://github.com/superboubek/bcd
Source0:        https://github.com/superboubek/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         bcd-nodeps.patch
Patch1:         bcd-gcc.patch
Patch2:         bcd-eigen3.patch
Patch3:         bcd-links.patch
Patch4:         bcd-cuda.patch
Patch5:         bcd-json.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(OpenEXR)
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles bcd-cli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bcd-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n bcd-cli -f %{oreon_filedir}/bcd-cli.list
%files -n bcd-devel -f %{oreon_filedir}/bcd-devel.list

%changelog

%autochangelog
