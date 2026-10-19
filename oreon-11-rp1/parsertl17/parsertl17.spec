%global source0_hash bb87bf2147317f9434cca7bb0f23e60d6c9934dca12ddd18ab8b750d754664c5
Name:           parsertl17
Summary:        The Modular Parser Generator
Epoch:          1
Version:        1.2.1
Release:        1%{?dist}
License:        BSL-1.0
URL:            https://github.com/BenHanson/parsertl17
Source0:        https://github.com/BenHanson/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{undefined fc43} && %{undefined fc42}
ExcludeArch:    %{ix86}
%endif
%global debug_package %{nil}
%global min_lexertl17 1:1.1.3
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  lexertl17-static
# /oreon:deps
%description %{common_description}

%package devel
Summary:        %{summary}
Provides:       parsertl17-static = %{epoch}:%{version}-%{release}
Conflicts:      parsertl14-devel
Requires:       lexertl17-devel >= %{min_lexertl17}
%description devel %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n parsertl17-%{version}

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate

%conf
# While the top-level CMakeLists.txt supports a BUILD_TESTING option, there are
# not yet any tests that can be built or run via CMake.
%cmake

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%set_build_flags
${CXX-g++} -I"${PWD}/include" ${CPPFLAGS} ${CXXFLAGS} -o include_test ${LDFLAGS} \
    tests/include_test/*.cpp
%files -f %{oreon_filedir}/main.list
%files -n parsertl17-devel -f %{oreon_filedir}/parsertl17-devel.list

%changelog

%autochangelog
