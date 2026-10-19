%global source0_hash 45819c1e54914783d4a1ca5633885035d74146778a1f74e1213cdb7b76340e71
%global forgeurl https://github.com/ArthurSonzogni/FTXUI
Version:        7.0.3
%forgemeta
Name:           ftxui
Release:        1%{?dist}
Summary:        A simple cross-platform C++ library for terminal based user interfaces
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/FTXUI-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake \
    -GNinja \
    -DFTXUI_BUILD_TESTS=OFF \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n ftxui-devel -f %{oreon_filedir}/ftxui-devel.list

%changelog

%autochangelog
