%global source0_hash none

%bcond_without auto_set_build_flags

%if %{without auto_set_build_flags}
%undefine _auto_set_build_flags
%endif

Name: test
Version: 1
Release: 1
Summary: Test package for checking %%set_build_flag usage
License: MIT

BuildRequires: gcc gcc-c++ make
BuildRequires: annobin-annocheck

Source0: Makefile
Source1: main-c.c
Source2: hello-c.c
Source3: main-cpp.cpp
Source4: hello-cpp.cpp

%global debug_package %{nil}

%global build_and_check \
	make \
	%{!?with_auto_set_build_flags:!} annocheck hello-c hello-cpp \
	make clean

%description
Test package for checking %%set_build_flag usage

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -c -T
cp -a %{sources} .

%build
%build_and_check

%check 
%build_and_check

%install
%build_and_check
