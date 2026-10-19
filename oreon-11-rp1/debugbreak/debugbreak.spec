%global source0_hash 62089680cc1cd0857519e2865b274ed7534bfa7ddfce19d72ffee41d4921ae2f
Name:           debugbreak
Summary:        Break into the debugger programmatically
Version:        1.0
Release:        1%{?dist}
URL:            https://github.com/scottt/debugbreak
License:        BSD-2-Clause
Source0:        https://github.com/scottt/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
%global debug_package %{nil}
%global common_description %{expand:
debugbreak.h allows you to put breakpoints in your C/C++ code with a call to
debug_break().
  • Include one header file and insert calls to debug_break() in the code where
    you wish to break into the debugger.
  • Supports GCC, Clang and MSVC.
  • Works well on ARM, AArch64, i686, x86-64, POWER and has a fallback code
    path for other architectures.
  • Works like the DebugBreak() function provided by Windows and QNX.}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  make
# /oreon:deps
%description %{common_description}

%package devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       debugbreak-static = %{version}-%{release}
%description devel %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build -f GNUmakefile CFLAGS="${CFLAGS} -I." CXXFLAGS="${CXXFLAGS} -I."
%install
install -t '%{buildroot}%{_includedir}' -D -p -m 0644 debugbreak.h
install -t '%{buildroot}%{_datadir}/debugbreak' -D -p -m 0644 debugbreak-gdb.py
%oreon_autofiles debugbreak-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

find test -type f -perm /0111 ! -name 'trap' |
  while read -r exe
  do
    tee "${exe}-rpm-test.gdb" <<EOF
set pagination off
set logging file ${exe}-rpm-test.txt
set logging on
file ${exe}
run
bt
set logging off
quit
EOF
    gdb -q -x "${exe}-rpm-test.gdb" --batch </dev/null || :
    grep -E 'SIG(TRAP|ILL)' "${exe}-rpm-test.txt"
  done
%files -f %{oreon_filedir}/main.list
%files -n debugbreak-devel -f %{oreon_filedir}/debugbreak-devel.list

%changelog

%autochangelog
