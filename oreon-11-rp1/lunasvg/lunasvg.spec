%global source0_hash 1abf1472ee6c4d19797916e8cc3c2e4b628e0d81178ffac60bdb0d457e32c690
Name:           lunasvg
Version:        3.5.0
Release:        1%{?dist}
Summary:        Standalone SVG rendering library in C++
License:        MIT
URL:            https://github.com/sammycage/lunasvg
Source0:        https://github.com/sammycage/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  plutovg-devel
BuildRequires:  stb_image_write-devel
# /oreon:deps
%description
LunaSVG is a standalone SVG rendering library in C++.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development headers and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DLUNASVG_LIBDIR="%{_libdir}" \
  -DLUNASVG_BUILD_EXAMPLES=ON \
  -DUSE_SYSTEM_PLUTOVG=ON
%cmake_build
%install
%cmake_install
chrpath -d %{_vpath_builddir}/examples/svg2png
install -Dpm0755 -t %{buildroot}%{_bindir} %{_vpath_builddir}/examples/svg2png
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n lunasvg-devel -f %{oreon_filedir}/lunasvg-devel.list

%changelog

%autochangelog
