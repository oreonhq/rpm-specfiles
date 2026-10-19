%global source0_hash 7da3e2d9a171eb0a038f592ecad3ff2bb2550f3496d87b3b29ad0cf4430c0db4
%bcond_with bootstrap
%global multilib_arches %{ix86} x86_64
Name:		libffi
Version:	3.8.0
Release:        1%{?dist}
Summary:        A portable foreign function interface library
License:	MIT AND CC-PDDC AND (GPL-3.0-or-later WITH Texinfo-exception)
URL:		http://sourceware.org/libffi
Source0:        https://github.com/libffi/libffi/releases/download/v%{version}/libffi-%{version}.tar.gz
Source1:	ffi-multilib.h
Source2:	ffitarget-multilib.h
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  dejagnu
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

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
basearch=%{_arch}
%ifarch %{ix86}
basearch=i386
%endif
mkdir -p $RPM_BUILD_ROOT%{_includedir}
%ifarch %{multilib_arches}
for i in ffi ffitarget; do
  mv $RPM_BUILD_ROOT%{_includedir}/$i.h $RPM_BUILD_ROOT%{_includedir}/$i-${basearch}.h
done
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/ffi.h
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/ffitarget.h
%endif
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libffi-devel -f %{oreon_filedir}/libffi-devel.list

%changelog

%autochangelog
