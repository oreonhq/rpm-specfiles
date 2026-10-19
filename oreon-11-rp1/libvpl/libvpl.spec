%global source0_hash 4de3e2faf1e8307fb282e4a43f443191810f6a6b0a484fffa7995ba1c814c6ec
%global mfx_major 2
%global mfx_minor 16
Name:           libvpl
Epoch:          1
Version:        2.17.0
Release:        1%{?dist}
Summary:        Intel Video Processing Library
License:        MIT
URL:            https://intel.github.io/libvpl/latest/index.html
Source0:        https://github.com/intel/libvpl/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Recommends:     intel-mediasdk
Recommends:     intel-vpl-gpu-rt
Obsoletes:      oneVPL <= 2023.4.0
Provides:       oneVPL%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

The base package is limited to the dispatcher and samples. To use oneVPL for
video processing you need to install at least one implementation. Current
implementations:

- intel-vpl-gpu-rt for use on Intel Xe graphics and newer
- intel-mediasdk for use on legacy Intel graphics

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      oneVPL-devel <= 2023.4.0
Provides:       oneVPL-devel%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample programs and source code for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      oneVPL-samples <= 2023.4.0
Provides:       oneVPL-samples%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}
%description    samples
This package contains sample programs and applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libvpl-%{version}
%oreon_prep
%build

%cmake \
-DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
-DBUILD_EXAMPLES=ON
%cmake_build
%install
%cmake_install
rm -fr %{buildroot}%{_datadir}/vpl/licensing
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libvpl-devel -f %{oreon_filedir}/libvpl-devel.list
%files -n libvpl-samples -f %{oreon_filedir}/libvpl-samples.list

%changelog

%autochangelog
