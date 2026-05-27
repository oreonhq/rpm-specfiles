%global source0_hash 1c89f47dc4f127c4b9d3fb46c8386a40be45c36ef82e8df472418de9423fc5bb

%define libname libdwarves
%define libver 1

Name: dwarves
Version: 1.30
Release: 3%{?dist}
License: GPL-2.0-only
Summary: Debugging Information Manipulation Tools (pahole & friends)
URL: http://acmel.wordpress.com
Source: http://fedorapeople.org/~acme/dwarves/%{name}-%{version}.tar.xz
Requires: %{libname}%{libver} = %{version}-%{release}
BuildRequires: gcc
BuildRequires: cmake >= 2.8.12
BuildRequires: zlib-devel
BuildRequires: elfutils-devel >= 0.130

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release .
%cmake_build

%install
rm -Rf %{buildroot}
%cmake_install

%ldconfig_scriptlets -n %{libname}%{libver}

%files
%doc README.ctracer
%doc README.btf
%doc changes-v1.30
%doc NEWS
%{_bindir}/btfdiff
%{_bindir}/codiff
%{_bindir}/ctracer
%{_bindir}/dtagnames
%{_bindir}/fullcircle
%{_bindir}/pahole
%{_bindir}/pdwtags
%{_bindir}/pfunct
%{_bindir}/pglobal
%{_bindir}/prefcnt
%{_bindir}/scncopy
%{_bindir}/syscse
%{_bindir}/ostra-cg
%dir %{_datadir}/dwarves/
%dir %{_datadir}/dwarves/runtime/
%dir %{_datadir}/dwarves/runtime/python/
%defattr(0644,root,root,0755)
%{_mandir}/man1/pahole.1*
%{_datadir}/dwarves/runtime/Makefile
%{_datadir}/dwarves/runtime/linux.blacklist.cu
%{_datadir}/dwarves/runtime/ctracer_relay.c
%{_datadir}/dwarves/runtime/ctracer_relay.h
%attr(0755,root,root) %{_datadir}/dwarves/runtime/python/ostra.py*

%files -n %{libname}%{libver}
%{_libdir}/%{libname}.so.*
%{_libdir}/%{libname}_emit.so.*
%{_libdir}/%{libname}_reorganize.so.*

%files -n %{libname}%{libver}-devel
%doc MANIFEST README
%{_includedir}/dwarves/btf_encoder.h
%{_includedir}/dwarves/config.h
%{_includedir}/dwarves/ctf.h
%{_includedir}/dwarves/dutil.h
%{_includedir}/dwarves/dwarves.h
%{_includedir}/dwarves/dwarves_emit.h
%{_includedir}/dwarves/dwarves_reorganize.h
%{_includedir}/dwarves/elfcreator.h
%{_includedir}/dwarves/elf_symtab.h
%{_includedir}/dwarves/gobuffer.h
%{_includedir}/dwarves/hash.h
%{_includedir}/dwarves/libctf.h
%{_includedir}/dwarves/list.h
%{_includedir}/dwarves/rbtree.h
%{_libdir}/%{libname}.so
%{_libdir}/%{libname}_emit.so
%{_libdir}/%{libname}_reorganize.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30-3
- Import
