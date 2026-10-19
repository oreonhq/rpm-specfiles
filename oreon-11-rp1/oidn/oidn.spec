%global source0_hash e71fd043a70f1cc80e301d1b90df6c1f536098c4dd94baa612742f6db3369c36
%bcond 	        hip 1
%bcond          ninja 1
Name:           oidn
Version:        2.5.1
Release:        1%{?dist}
Summary:        Library of denoising filters for images rendered with ray tracing
License:        Apache-2.0
URL:            https://openimagedenoise.github.io/
Source0:        https://github.com/OpenImageDenoise/%{name}/releases/download/v%{version}/%{name}-%{version}.src.tar.gz
%if %{with hip}
%global toolchain clang
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong//' -e 's/-fcf-protection//' -e 's/-mtls-dialect=gnu2//' )
%endif
ExclusiveArch:  x86_64
%if %{with hip}
%endif
%if %{with hip}
%else
%endif
Recommends:     ispc-gpu
%if %{with ninja}
%endif
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  help2man
BuildRequires:  hipcc
BuildRequires:  ispc
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(OpenImageIO)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime
# /oreon:deps
%description
Intel Open Image Denoise is an open source library of high-performance, 
high-quality denoising filters for images rendered with ray tracing.

%package        libs
Summary:        Libraries for %{name}
%description    libs
The %{name}-libs package contains shared library for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        docs
Summary:        Documentation for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildArch:      noarch
%description docs
The %{name}-docs package contains documentation for %{name}.

%prep

%autosetup -n %{name}-%{version}%{?prerelease:-%{prerelease}}

%build

%cmake \
%if %{with ninja}
    -G Ninja \
%endif
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
%if %{with hip}
    -DOIDN_DEVICE_HIP=ON \
    -DOIDN_DEVICE_HIP_COMPILER=%{_bindir}/hipcc \
    -DROCM_PATH=%{_libdir}
%endif
%cmake_build
%install
%cmake_install
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done
chrpath --delete %{buildroot}%{_bindir}/%{name}{Denoise,Test,Benchmark}
chrpath --delete %{buildroot}%{_libdir}/libOpenImageDenoise{,_core,_device_cpu}.so.*
%if %{with hip}
chrpath --delete %{buildroot}%{_libdir}/libOpenImageDenoise_device_hip.so.*
%endif
rm -rf %{buildroot}%{_docdir}/OpenImageDenoise
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n oidn-libs -f %{oreon_filedir}/oidn-libs.list
%files -n oidn-devel -f %{oreon_filedir}/oidn-devel.list
%files -n oidn-docs -f %{oreon_filedir}/oidn-docs.list

%changelog

%autochangelog
