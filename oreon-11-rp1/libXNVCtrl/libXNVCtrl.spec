%global source0_hash 728aa2bd3c99f52ea079945f31568617c4ee06de79f5e07651a6fbe2a211ee7f
Name:           libXNVCtrl
Version:        580.178.04
Release:        1%{?dist}
Summary:        Library providing the NV-CONTROL API
License:        GPL-2.0-or-later
URL:            https://download.nvidia.com/XFree86/nvidia-settings
Source0:        https://download.nvidia.com/XFree86/nvidia-settings/nvidia-settings-580.178.04.tar.bz2
Patch:          libxnvctrl_so_0.patch
Obsoletes: nvidia-%{name} < 3:%{version}-100
Provides: nvidia-%{name} = 3:%{version}-100
# oreon:deps
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
# /oreon:deps
%description
This packages contains the libXNVCtrl library from the nvidia-settings
application. This library provides the NV-CONTROL API for communicating with
the proprietary NVIDIA xorg driver. This package does not contain the
nvidia-settings tool itself as that is included with the proprietary drivers
themselves.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel%{?_isa}
Obsoletes: nvidia-%{name}-devel < 3:%{version}-100
Provides: nvidia-%{name}-devel = 3:%{version}-100
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir nvidia-settings-%{version}
%oreon_prep
%build

%make_build \
   CC="%{__cc}" \
   NV_VERBOSE=1 \
   DO_STRIP=0 \
   STRIP_CMD=/bin/true \
   -C src/%{name} \
   libXNVCtrl.so
%install
pushd src/%{name}
install -m 0755 -d %{buildroot}%{_libdir}/
cp -Prp libXNVCtrl.so* %{buildroot}%{_libdir}/
install -m 0755 -d %{buildroot}%{_includedir}/NVCtrl/
install -p -m 0644 *.h %{buildroot}%{_includedir}/NVCtrl/
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXNVCtrl-devel -f %{oreon_filedir}/libXNVCtrl-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 580.82.09-1
- Prepare for Oreon 11 (RP1)
