%global source0_hash 666fa9b0ecbc88287a7656a4323375f6bcc52a87dfe60d6cb14e4fe7950e7989
%global date 20240930
%global commit 8cc40f73e62adbb8351a0180aa779cdd546170cb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global forgeurl https://github.com/thp/psmoveapi
%global common_description %{expand:
The PS Move API is an open source library to access the Sony Move Motion
Controller via Bluetooth and USB directly from your PC without the need for a
PS3. Tracking in 3D space is possible using a PS Eye or any other suitable
camera source.}
Name:           psmoveapi
Version:        4.0.12^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Library for 6DoF tracking of the PS Move Motion Controller
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://thp.io/2010/psmove
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          %{forgeurl}/pull/499.patch
Patch:          psmoveapi-fedora-changes.patch
Patch:          psmoveapi-no-libusb-compat.patch
Provides:       bundled(sixad) = 1.6.0
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       systemd-udev
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  hidapi-devel
BuildRequires:  libusb1-devel
BuildRequires:  libv4l-devel
BuildRequires:  opencv-devel
BuildRequires:  python3-sphinx
BuildRequires:  sed
BuildRequires:  systemd-devel
# /oreon:deps
%description    %{common_description}

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconf-pkg-config
%description    devel %{common_description}

This package contains development headers and libraries for %{name}.

%package        doc
Summary:        Additional documentation for %{name}
BuildArch:      noarch
%description    doc %{common_description}

This package contains additional documentation for %{name}.

%package        examples
Summary:        Sample and test programs for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    examples %{common_description}

This package contains a number of example and test programs for %{name}.

%package        libs
Summary:        Shared libraries for %{name}
%description    libs %{common_description}

This package contains shared libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

# Strip bundled libraries
rm -r external

# Remove unused OSX sources
rm src/daemon/*.mm

%build

%cmake -DPSMOVE_USE_SIXPAIR=OFF
%cmake_build
sphinx-build-3 docs html
rm -rf html/{.buildinfo,.doctrees}
%install
%cmake_install
for f in example example_new_api multiple test_navcon; do
  chrpath -d "%{_vpath_builddir}/${f}"
  install -Dpm0755 "%{_vpath_builddir}/${f}" "%{buildroot}%{_bindir}/%{name}-${f}"
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n psmoveapi-devel -f %{oreon_filedir}/psmoveapi-devel.list
%files -n psmoveapi-doc -f %{oreon_filedir}/psmoveapi-doc.list
%files -n psmoveapi-examples -f %{oreon_filedir}/psmoveapi-examples.list
%files -n psmoveapi-libs -f %{oreon_filedir}/psmoveapi-libs.list

%changelog

%autochangelog
