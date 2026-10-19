%global source0_hash f60d44830ee7108ba8d58f48ee9f732de44dd917e44eb40410c62fab6846e000
%global date 20250328
%global commit 440518bb7b0015a235f2e209b3fb454b2cf13ea2
%global shortcommit %{sub %{commit} 1 7}
%global extras_data_commit 1d5bdc744743daa3cf15a96489b1e6a7785767e2
%global extras_data_shortcommit %{sub %{extras_data_commit} 1 7}
%global extras_data_url https://github.com/jdavidberger/libsurvive-extras-data
Name:           libsurvive
Version:        1.01^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Open Source Lighthouse Tracking System
URL:            https://github.com/collabora/libsurvive
License:        MIT AND (MIT AND BSD-2-Clause) AND Minpack AND LicenseRef-Fedora-UltraPermissive AND HIDAPI AND ((MIT OR X11) OR BSD-3-Clause OR GPL-1.0-or-later) AND (MIT AND (MIT OR X11) OR BSD-3-Clause) AND (MIT AND (MIT OR X11)) AND Zlib
Source0:        https://github.com/collabora/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-440518b.tar.gz
Source1:        %{extras_data_url}/archive/%{extras_data_commit}/%{name}-extras-data-%{extras_data_commit}.tar.gz#/%{name}-extras-data-%{extras_data_shortcommit}.tar.gz
Patch:          %{name}-no-external-project.patch
Patch:          %{name}-eigen3.patch
ExcludeArch:    %{ix86}
Provides:       bundled(CNFG3D)
Provides:       bundled(CNFG)
Provides:       bundled(crc32)
Provides:       bundled(hidapi)
Provides:       bundled(jsmn)
Provides:       bundled(linmath)
Provides:       bundled(mpfit) = 1.24
Provides:       bundled(zlib)
Requires:       systemd-udev
# oreon:deps
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  gattlib-devel
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  libX11-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb1-devel
BuildRequires:  openblas-devel
BuildRequires:  opencv-devel
BuildRequires:  python3-devel
BuildRequires:  sciplot-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Libsurvive is a set of tools and libraries that enable 6 dof tracking on
Lighthouse and Vive based systems that is completely Open Source and can run on
any device. It currently supports both SteamVR 1.0 and SteamVR 2.0 generation
of devices and should support any tracked object commercially available.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

# Drop bundled libraries for non-Linux platforms
rm redist/*.m redist/dirent.windows.h

# Extract test artifacts in the right places
mkdir -p %{_vpath_builddir}/src/test_cases/libsurvive-extras-data/
tar -xf %{SOURCE1} --strip-components 1 -C %{_vpath_builddir}/src/test_cases/%{name}-extras-data/

%build

%cmake \
  -DLIB_INSTALL_DIR="%{_lib}/" \
  -DENABLE_TESTS=ON \
  -DUSE_OPENBLAS=ON \
  -DUSE_OPENCV=ON
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_prefix}/lib/*.a
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} useful_files/81-vive.rules
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libsurvive-devel -f %{oreon_filedir}/libsurvive-devel.list

%changelog

%autochangelog
