%global source0_hash ca3f157a5e6bf293cfb2fea585b103ec87245d02eaee0b6ab832665e740016eb
%global appname include-what-you-use
%global toolchain clang
%global llvm_ver 21
%global __cc_clang clang-%{llvm_ver}
%global __cxx_clang clang++-%{llvm_ver}
%global __cpp_clang clang-cpp-%{llvm_ver}
%undefine _include_frame_pointers
Name: iwyu
Version: 0.26
Release:        1%{?dist}
License: NCSA
Summary:        C/C++ source files #include analyzer based on clang
URL: https://github.com/%{appname}/%{appname}
Source0:        https://github.com/%{appname}/%{appname}/archive/%{version}/%{appname}-%{version}.tar.gz
Provides: %{appname} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{appname}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  clang(major)
BuildRequires:  clang-devel(major)
BuildRequires:  cmake
BuildRequires:  compiler-rt(major)
BuildRequires:  libcxx-devel
BuildRequires:  llvm-devel(major)
BuildRequires:  llvm-static(major)
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
"Include what you use" means this: for every symbol (type, function, variable,
or macro) that you use in foo.cc (or foo.cpp), either foo.cc or foo.h should
include a .h file that exports the declaration of that symbol. (Similarly, for
foo_test.cc, either foo_test.cc or foo.h should do the including.) Obviously
symbols defined in foo.cc itself are excluded from this requirement.

This puts us in a state where every file includes the headers it needs to
declare the symbols that it uses. When every file includes what it uses,
then it is possible to edit any file and remove unused headers, without fear
of accidentally breaking the upwards dependencies of that file. It also
becomes easy to automatically track and update dependencies in the source
code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{appname}-%{version} -p1
%py3_shebang_fix *.py

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_PREFIX_PATH='%{_libdir}/llvm%{llvm_ver}/%{_lib}/cmake/clang;%{_libdir}/llvm%{llvm_ver}/%{_lib}/cmake/llvm' \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%ctest --exclude-regex "(cxx.test_(badinc|ms_inline_asm|precomputed_tpl_args)|driver.test_offload_openmp)"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
