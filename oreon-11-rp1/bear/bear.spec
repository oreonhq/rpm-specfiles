%global source0_hash 9f9d0236bf0751cb4f5d747c077697f396546ba1ad8653c2e9b7192ea47df14a
Name:           bear
Version:        4.2.2
Release:        1%{?dist}
Summary:        Tool that generates a compilation database for clang tooling
License:        GPL-3.0-or-later
URL:            https://github.com/rizsotto/%{name}
Source0:        https://github.com/rizsotto/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
%ifarch %{valgrind_arches}
%endif
%global _lto_cflags %{nil}
# oreon:deps
BuildRequires:  /usr/bin/more
BuildRequires:  /usr/bin/xargs
BuildRequires:  cmake
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(gtest)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(spdlog)
BuildRequires:  fakeroot
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gmock-devel
BuildRequires:  grpc-plugins
BuildRequires:  make
BuildRequires:  pkgconfig(grpc++)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  python3
BuildRequires:  python3dist(lit)
# /oreon:deps
%description
Build ear produces compilation database in JSON format. This database describes
how single compilation unit should be processed and can be used by Clang
tooling.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Bear-%{version}
%oreon_prep
%build

for f in $(ls test/bin/); do
    sed -i "s|^#\!/usr/bin/env\s\+python\s\?$|#!%{__python3}|" test/bin/$f
done
%ifarch s390x
rm -vf test/cases/intercept/valgrind/shell_commands_intercepted.sh
%endif
%cmake -DENABLE_FUNC_TESTS=ON -DENABLE_UNIT_TESTS=ON
%cmake_build
%install
%cmake_install
mv %{buildroot}/%{_docdir}/Bear %{buildroot}/%{_docdir}/bear
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
