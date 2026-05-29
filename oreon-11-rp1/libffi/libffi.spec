%global source0_hash f3a3082a23b37c293a4fcd1053147b371f2ff91fa7ea1b2a52e335676bac82dc

%bcond_with bootstrap

%global multilib_arches %{ix86} x86_64

Name:		libffi
Version:	3.5.2
Release:	2%{?dist}
Summary:	A portable foreign function interface library
# No license change for 3.5.2
# No license change for 3.5.1
# No license change for 3.4.8
# No license change for 3.4.7
# No license change for 3.4.6
# The following SPDX licenses are extracted from the sources using
# ScanCode 32.0.8 on build libffi-3.4.4-7.fc40:
#
# MIT - Most of the project sources (Required)
# CC-PDDC - src/dlmalloc.c (Required)
# mit OR gpl-3.0 - ltmain.sh (Ignored)
# mit OR gpl-1.0-plus - ltmain.sh (Ignored)
# gpl-2.0-plus WITH libtool-exception-2.0 - ltmain.sh, libtool.m4, configure (Ignored, not shipped)
# warranty-disclaimer - ltmain.sh (Ignored)
# unknown-license-reference - ltmain.sh (Ignored)
# gpl-2.0-plus - Used by build system only (Ignored)
# gpl-2.0 - Used by build system only (Ignored)
# free-unknown - config.guess, config.sub (Ignored)
# fsf-ap - Used by build system only (Ignored)
# fsf-free - Used by build system only (Ignored)
# fsf-unlimited - Used by build system only (Ignored)
# fsf-unlimited-no-warranty - Used by build system only (Ignored)
# gpl-1.0-plus - False positive in texinfo.tex (Ignored)
# gpl-3.0-plus WITH tex-exception - texinfo.tex used in libffi-devel docs (Required)
# gpl-2.0-plus WITH autoconf-simple-exception-2.0 - Used by build system only (Ignored)
# gpl-3.0 - Used by build system only (Ignored)
# gpl-3.0-plus - Used by the testsuite only (Ignored)
# gpl-3.0-plus WITH autoconf-exception-2.0 - Used by build system only (Ignored)
# gpl-3.0-plus WITH autoconf-simple-exception - Used by build system only (Ignored)
# mpl-1.1 OR gpl-2.0-plus OR lgpl-2.1-plus - Not used in build (Ignored)
# public-domain - Used by build system only (Ignored)
# x11-xconsortium - Used by build system only (Ignored)
License:	MIT AND CC-PDDC AND (GPL-3.0-or-later WITH Texinfo-exception)
URL:		http://sourceware.org/libffi

Source0:        https://github.com/libffi/libffi/releases/download/v3.5.2/libffi-3.5.2.tar.gz
Source1:	ffi-multilib.h
Source2:	ffitarget-multilib.h

BuildRequires: make
BuildRequires: gcc
%if %{without bootstrap}
BuildRequires: gcc-c++
BuildRequires: dejagnu
%endif

%description
Compilers for high level languages generate code that follow certain
conventions.  These conventions are necessary, in part, for separate
compilation to work.  One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function.  A
calling convention also specifies where the return value for a function
is found.  

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function.  `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface.  A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language.  The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface.  A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.  

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
# --disable-multi-os-directory is used because otherwise, on riscv64, the
# library is installed under ${_libdir}/lp64d, which we don't want. Other
# architectures don't have the same problem so they're unaffected.
%configure --disable-static --disable-multi-os-directory
%make_build

%check
%if %{without bootstrap}
%make_build check
%endif

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Determine generic arch target name for multilib wrapper
basearch=%{_arch}
%ifarch %{ix86}
basearch=i386
%endif

mkdir -p $RPM_BUILD_ROOT%{_includedir}
%ifarch %{multilib_arches}
# Do header file switcheroo to avoid file conflicts on systems where you
# can have both a 32- and 64-bit version of the library, and they each need
# their own correct-but-different versions of the headers to be usable.
for i in ffi ffitarget; do
  mv $RPM_BUILD_ROOT%{_includedir}/$i.h $RPM_BUILD_ROOT%{_includedir}/$i-${basearch}.h
done
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/ffi.h
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/ffitarget.h
%endif

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_libdir}/libffi.so.8
%{_libdir}/libffi.so.8.2.0

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ffi*.h
%{_libdir}/*.so
%{_mandir}/man3/*.gz
%{_infodir}/libffi.info.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5.2-2
- Prepare for Oreon 11 (RP1)
