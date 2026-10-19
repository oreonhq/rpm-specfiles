%global source0_hash 592272df3cf01e85e7db300c449df5061092574d099da275d19e97ef0510f8a6
%global origname mesa
%global _lto_cflags %nil
Name:           %{origname}-compat
Summary:        Mesa graphics libraries - legacy compatibility libraries
%global ver 25.0.7
Version:        %{lua:ver = string.gsub(rpm.expand("%{ver}"), "-", "~"); print(ver)}
Release:        1%{?dist}
License:        MIT AND BSD-3-Clause AND SGI-B-2.0
URL:            http://www.mesa3d.org
Source0:        https://archive.mesa3d.org/mesa-25.0.7.tar.xz
Source1:        Mesa-MLAA-License-Clarification-Email.txt
Patch01:        0001-c11-threads-fix-build-on-fedora-44.patch
Patch02:        cd129dbf8af2d16b1243f2ce287ff69c6a5dc557.patch
%if 0%{?with_hardware}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libdrm-devel
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-pycparser
BuildRequires:  python3-pyyaml
# /oreon:deps
%description
%{summary}.

%package libxatracker
Summary:        Mesa XA state tracker
Provides:       libxatracker%{?_isa}
Provides:       mesa-libxatracker%{?_isa}
Obsoletes:      mesa-libxatracker < 25.3
%description libxatracker
%{summary}.

%package libxatracker-devel
Summary:        Mesa XA state tracker development package
Requires: %{name}-libxatracker%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-libxatracker-devel < 25.3
%description libxatracker-devel
%{summary}.

%package libOSMesa
Summary:        Mesa offscreen rendering libraries
Provides:       libOSMesa
Provides:       libOSMesa%{?_isa}
Provides:       deprecated()
%description libOSMesa
%{summary}.

%package libOSMesa-devel
Summary:        Mesa offscreen rendering development package
Requires:       %{name}-libOSMesa%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       deprecated()
%description libOSMesa-devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{origname}-%{ver} -p1
cp %{SOURCE1} docs/

%build

%meson \
  -Dplatforms= \
  -Dosmesa=true \
  -Dgallium-drivers=llvmpipe,svga \
  -Dgallium-vdpau=disabled \
  -Dgallium-va=disabled \
  -Dgallium-xa=enabled \
  -Dgallium-nine=false \
  -Dgallium-opencl=disabled \
  -Dgallium-rusticl=false \
  -Dvulkan-drivers= \
  -Dshared-glapi=enabled \
  -Dgles1=disabled \
  -Dgles2=disabled \
  -Dopengl=true \
  -Dgbm=disabled \
  -Dglvnd=disabled \
  -Dglx=disabled \
  -Degl=disabled \
  -Dllvm=enabled \
  -Dshared-llvm=enabled \
  -Dvalgrind=disabled \
  -Dbuild-tests=false \
  -Dmesa-clc=auto \
  -Dmicrosoft-clc=disabled \
  -Dxlib-lease=disabled \
  -Dandroid-libbacktrace=disabled \
  -Dlibunwind=disabled \
  -Dlmsensors=disabled \
%ifarch %{ix86}
  -Dglx-read-only-text=true \
%endif
  %{nil}
%meson_build
%install
%meson_install
rm -rf %{buildroot}%{_datadir}/drirc.d
rm -rf %{buildroot}%{_includedir}/GL/gl*.h
rm -rf %{buildroot}%{_includedir}/KHR
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mesa-compat-libxatracker -f %{oreon_filedir}/mesa-compat-libxatracker.list
%files -n mesa-compat-libxatracker-devel -f %{oreon_filedir}/mesa-compat-libxatracker-devel.list
%files -n mesa-compat-libOSMesa -f %{oreon_filedir}/mesa-compat-libOSMesa.list
%files -n mesa-compat-libOSMesa-devel -f %{oreon_filedir}/mesa-compat-libOSMesa-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{lua:ver=string.gsub(rpm.expand("%{ver}"),"-","~");print(ver)}-1
- Prepare for Oreon 11 (RP1)
