%global source0_hash d8862955c6d74e5846b3f580b1605d2428b11d97a410d86e2fb13e857cd3a744
Name:           spdlog
Version:        1.17.0
Release:        2%{?dist}
License:        MIT
Summary:        Super fast C++ logging library
URL:            https://github.com/gabime/%{name}
Source0:        https://github.com/gabime/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-fmt_external.patch
# oreon:deps
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  google-benchmark-devel
BuildRequires:  ninja-build
BuildRequires:  systemd-devel
# /oreon:deps
%description
This is a packaged version of the gabime/spdlog C++ logging
library available at Github.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libstdc++-devel%{?_isa}
Requires:       fmt-devel%{?_isa}
%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
find . -name '.gitignore' -delete
sed -e "s,\r,," -i README.md

%build

%cmake -G Ninja \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_BUILD_TYPE=Release \
    -DSPDLOG_BUILD_SHARED=ON \
    -DSPDLOG_BUILD_EXAMPLE=OFF \
    -DSPDLOG_BUILD_BENCH=OFF \
    -DSPDLOG_BUILD_TESTS=ON \
    -DSPDLOG_INSTALL=ON \
    -DSPDLOG_FMT_EXTERNAL=ON
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n spdlog-devel -f %{oreon_filedir}/spdlog-devel.list
