%global source0_hash 319cbf319e9fc92065a5407ce47eb868d73566f3d4840a56832734e4579df947
%define libname libdwarves
%define libver 1
Name: dwarves
Version: 1.32
Release:        1%{?dist}
License: GPL-2.0-only
Summary:        Debugging Information Manipulation Tools (pahole & friends)
URL: http://acmel.wordpress.com
Source0:        http://fedorapeople.org/~acme/dwarves/%{name}-%{version}.tar.xz
Requires: %{libname}%{libver} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  elfutils-devel
BuildRequires:  gcc
BuildRequires:  zlib-devel
# /oreon:deps
%description
dwarves is a set of tools that use the debugging information inserted in ELF
binaries by compilers such as GCC, used by well known debuggers such as GDB,
and more recent ones such as systemtap.

Utilities in the dwarves suite include pahole, that can be used to find
alignment holes in structs and classes in languages such as C, C++, but not
limited to these.

It also extracts other information such as CPU cacheline alignment, helping
pack those structures to achieve more cache hits.

These tools can also be used to encode and read the BTF type information format
used with the Linux kernel bpf syscall, using 'pahole -J' and 'pahole -F btf'.

A diff like tool, codiff can be used to compare the effects changes in source
code generate on the resulting binaries.

Another tool is pfunct, that can be used to find all sorts of information about
functions, inlines, decisions made by the compiler about inlining, etc.

One example of pfunct usage is in the fullcircle tool, a shell that drivers
pfunct to generate compileable code out of a .o file and then build it using
gcc, with the same compiler flags, and then use codiff to make sure the
original .o file and the new one generated from debug info produces the same
debug info.

Pahole also can be used to use all this type information to pretty print raw
data according to command line directions.

Headers can have its data format described from debugging info and offsets from
it can be used to further format a number of records.

The btfdiff utility compares the output of pahole from BTF and DWARF to make
sure they produce the same results.

%package -n %{libname}%{libver}
Summary: Debugging information  processing library
%description -n %{libname}%{libver}
Debugging information processing library.

%package -n %{libname}%{libver}-devel
Summary: Debugging information library development files
Requires: %{libname}%{libver} = %{version}-%{release}
%description -n %{libname}%{libver}-devel
Debugging information processing library development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%cmake -DCMAKE_BUILD_TYPE=Release .
%cmake_build
%install
rm -Rf %{buildroot}
%cmake_install
%ldconfig_scriptlets -n %{libname}%{libver}
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdwarves1 -f %{oreon_filedir}/libdwarves1.list
%files -n libdwarves1-devel -f %{oreon_filedir}/libdwarves1-devel.list

%changelog

%autochangelog
