%global source0_hash b2005a675a6eb799badf7ca4bd9b5fdbaeced43ae370441b59962f7fbb1a8245
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global giturl  https://github.com/mmottl/res
Name:           ocaml-res
Version:        5.0.2
Release:        6%{?dist}
Summary:        OCaml library for resizing arrays and strings
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://mmottl.github.io/res/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This OCaml-library consists of a set of modules which implement
automatically resizing (= reallocating) datastructures that consume a
contiguous part of memory. This allows appending and removing of
elements to/from arrays (both boxed and unboxed), strings (->
buffers), bit strings and weak arrays while still maintaining fast
constant-time access to elements.

There are also functors that allow the generation of similar modules
which use different reallocation strategies.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir res-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-res-devel -f %{oreon_filedir}/ocaml-res-devel.list

%changelog

%autochangelog
