%global source0_hash 4d6368a27492d86011fde5ca0cf386dce7c49cd425aa3d9b063ca6ec373a6ef3
%bcond check 0
%global debug_package %{nil}
%global project concurrentqueue
Name:           moodycamel-%{project}
Version:        1.0.5
Release:        1%{?dist}
Summary:        An industrial-strength lock-free queue for C++
License:        (BSD-2-Clause OR BSL-1.0) AND BSD-3-Clause AND Zlib
URL:            https://github.com/cameron314/%{project}
Source0:        https://github.com/cameron314/%{project}/archive//v%{version}/%{name}-%{version}.tar.gz
Patch:          %{project}-install-noarch-to-share.diff
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
License:        (BSD-2-Clause OR BSL-1.0) AND Zlib
BuildArch:      noarch
Requires:       cmake-filesystem
%description    devel

The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{project}-%{version}
# fix wrong-file-end-of-line-encoding
touch -r README.md README.md.tstamp
sed -i 's/\r$//' README.md
touch -r README.md.tstamp README.md

%build

%cmake
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%make_build -C tests/unittests
./build/bin/unittests --disable-prompt
%endif
%files -f %{oreon_filedir}/main.list
%files -n moodycamel-concurrentqueue-devel -f %{oreon_filedir}/moodycamel-concurrentqueue-devel.list

%changelog

%autochangelog
