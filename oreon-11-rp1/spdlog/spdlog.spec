# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d8862955c6d74e5846b3f580b1605d2428b11d97a410d86e2fb13e857cd3a744

Name: spdlog
Version: 1.17.0
Release: 1%{?dist}
Summary: Fast C++ logging library
License: MIT
URL: https://github.com/gabime/spdlog
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz#/spdlog-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: fmt-devel
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
Spdlog is a fast C++ logging library with synchronous and asynchronous
logging support.

%package devel
Summary: Development files for spdlog
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: fmt-devel

%description devel
Headers and build metadata for applications using spdlog.

%prep
%oreon_sha256
%autosetup

%build
%cmake \
  -G Ninja \
  -DSPDLOG_BUILD_SHARED=ON \
  -DSPDLOG_FMT_EXTERNAL=ON \
  -DSPDLOG_BUILD_EXAMPLE=OFF \
  -DSPDLOG_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%check
cat > spdlog-smoke.cpp <<'EOF'
#include <spdlog/spdlog.h>
int main() {
    spdlog::info("spdlog smoke test");
    return 0;
}
EOF
g++ spdlog-smoke.cpp -I%{buildroot}%{_includedir} \
  -L%{buildroot}%{_libdir} -Wl,-rpath,%{buildroot}%{_libdir} \
  -lspdlog -lfmt -pthread -o spdlog-smoke
./spdlog-smoke

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_libdir}/libspdlog.so.1*

%files devel
%{_includedir}/spdlog/
%{_libdir}/libspdlog.so
%{_libdir}/pkgconfig/spdlog.pc
%{_libdir}/cmake/spdlog/

%changelog
%autochangelog
