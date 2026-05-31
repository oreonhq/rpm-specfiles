%global source0_hash e735d24135629dfa70001b50e2b7e812300a20f312a0587b7cc03016c278815b

Name:           libXNVCtrl
Version:        580.82.09
Release:        %autorelease
Summary:        Library providing the NV-CONTROL API
License:        GPL-2.0-or-later
URL:            https://download.nvidia.com/XFree86/nvidia-settings
Source:        https://download.nvidia.com/XFree86/nvidia-settings/nvidia-settings-580.82.09.tar.bz2
Patch:          libxnvctrl_so_0.patch

BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

# Obsoletes older package provided in the NVIDIA CUDA repository
Obsoletes: nvidia-%{name} < 3:%{version}-100
Provides: nvidia-%{name} = 3:%{version}-100

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
# Obsoletes older package provided in the NVIDIA CUDA repository
Obsoletes: nvidia-%{name}-devel < 3:%{version}-100
Provides: nvidia-%{name}-devel = 3:%{version}-100

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n nvidia-settings-%{version}


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


%files
%license COPYING
%{_libdir}/%{name}.so.0*

%files devel
%doc doc/NV-CONTROL-API.txt doc/FRAMELOCK.txt
%{_includedir}/NVCtrl/
%{_libdir}/%{name}.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 580.82.09-1
- Prepare for Oreon 11 (RP1)
