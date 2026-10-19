%global source0_hash b9e3ec33fafe9a26c855b8b74de2804680e5f840150053c844cbfba717e9b41a
%global basever 2.3.2
%global origrel 1
%global somajor 2
Name:           louvre
Version:        %{basever}%{?origrel:_%{origrel}}
Release:        1%{?dist}
Summary:        C++ library for building Wayland compositors
License:        MIT
URL:            https://cuarzosoftware.github.io/Louvre/
Source0:        https://github.com/CuarzoSoftware/Louvre/archive/v%{basever}-%{origrel}/Louvre-%{basever}-%{origrel}.tar.gz
# oreon:deps
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(SRM)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
Louvre is a high-performance C++ library designed for building
Wayland compositors with a strong emphasis on ease of development.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Example applications using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    examples
The %{name}-examples package contains example applications using
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Louvre-%{basever}%{?origrel:-%{origrel}}

%build

pushd src
%meson
%meson_build
popd
%install
pushd src
%meson_install
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n louvre-devel -f %{oreon_filedir}/louvre-devel.list
%files -n louvre-examples -f %{oreon_filedir}/louvre-examples.list

%changelog

%autochangelog
