%global source0_hash 427c4c20bdeb06022d706ba24cb14838b62cca4456a6072e826d7ffa706a4b1a
%global mingw_build_ucrt64 1
%{?mingw_package_header}
%global debug_package %{nil}
%global __strip /bin/true
%define _lto_cflags %{nil}
Name:           DirectX-Headers
Version:        1.619.4
Release:        1%{?dist}
Summary:        Official Direct3D 12 headers
License:        MIT
URL:            https://github.com/microsoft/DirectX-Headers
Source0:        https://github.com/microsoft/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%{?_with_test:BuildRequires: gtest-devel}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc-c++
# /oreon:deps
%description
Official Direct3D 12 headers

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n mingw32-directx-headers
Summary:        Official DirectX headers available under an open source license
%description -n mingw32-directx-headers
Official DirectX headers available under an open source license

%package -n mingw64-directx-headers
Summary:        Official DirectX headers available under an open source license
%description -n mingw64-directx-headers
Official DirectX headers available under an open source license

%package -n ucrt64-directx-headers
Summary:        Official DirectX headers available under an open source license
%description -n ucrt64-directx-headers
Official DirectX headers available under an open source license

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Change EOL encoding
for i in LICENSE README.md ; do
  sed -i -e 's/\r$//' ${i}
  touch -r SECURITY.md ${i}
done

%build

%meson \
 %{?!_with_test:-Dbuild-test=false}
%meson_build
%mingw_meson
%mingw_ninja
%install
%meson_install
%mingw_ninja_install
%oreon_autofiles DirectX-Headers-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mingw32-directx-headers usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-directx-headers usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-directx-headers usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{?_with_test:
%meson_test
}
%files -f %{oreon_filedir}/main.list
%files -n DirectX-Headers-devel -f %{oreon_filedir}/DirectX-Headers-devel.list
%files -n mingw32-directx-headers -f %{oreon_filedir}/mingw32-directx-headers.list
%files -n mingw64-directx-headers -f %{oreon_filedir}/mingw64-directx-headers.list
%files -n ucrt64-directx-headers -f %{oreon_filedir}/ucrt64-directx-headers.list

%changelog

%autochangelog
