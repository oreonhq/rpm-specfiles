%global source0_hash c5269bab4dae8060699235f680e14c0e88804e092b540e6d0aac4b5665d0a5cd
%bcond_with tests
%global forgeurl https://gitlab.com/%{name}/%{name}
%global tag v%{version}
ExcludeArch: %{ix86}
%undefine __cmake_in_source_build
%global uuid    org.%{name}.%{name}
Name:           corectrl
Version:        1.5.2
%forgemeta
Release:        1%{?dist}
Summary:        Profile based system control utility
License:        GPL-3.0-or-later AND BSL-1.0 AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
URL:            %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{tag}/%{name}-%{tag}.tar.bz2
Source1:        README.fedora.md
%if %{with tests}
%endif
Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       polkit%{?_isa}
Recommends:     mesa-demos%{?_isa}
Recommends:     util-linux%{?_isa}
Recommends:     vulkan-tools%{?_isa}
Provides:       bundled(units)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Catch2)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(QuaZip-Qt6)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(pugixml)
BuildRequires:  cmake(spdlog)
BuildRequires:  cmake(trompeloeil)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libdrm-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
CoreCtrl is a Free and Open Source GNU/Linux application that allows you to
control with ease your computer hardware using application profiles. It aims to
be flexible, comfortable and accessible to regular users.

- For setup instructions run:

  $ xdg-open %{_docdir}/%{name}/README.fedora.md

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# Unbundle 3rdparty
pushd 3rdparty
rm -rf \
    easyloggingpp \
    fmt \
    pugixml \
    %{nil}
popd
# lib soversion fix
echo "set_property(TARGET corectrl_lib PROPERTY SOVERSION 0)" >> src/CMakeLists.txt

%build

%cmake \
    -G Ninja \
    %if %{with tests}
    -DBUILD_TESTING=ON \
    %else
    -DBUILD_TESTING=OFF \
    %endif
    %{nil}
%cmake_build
%install
%cmake_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/README.fedora.md
find README.md -type f -perm /111 -exec chmod 644 {} \;
find %{buildroot}/%{_datadir}/. -type f -executable -exec chmod -x "{}" \;
rm %{buildroot}/%{_libdir}/libcorectrl.so
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
