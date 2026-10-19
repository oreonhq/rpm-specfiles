%global source0_hash 1be18e70f5d8a6b03566c3619b62836a26094fc7208fde46ab7b32ee64116170
ExcludeArch: %{ix86}
%bcond test 0
Name:           ocaml-cinaps
Version:        0.15.1
Release:        27%{?dist}
Summary:        Trivial Metaprogramming tool using the OCaml toplevel
License:        MIT
URL:            https://github.com/ocaml-ppx/cinaps
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-ppx/cinaps/archive/v%{version}/cinaps-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  help2man
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-re-devel
# /oreon:deps
%description
Cinaps is a trivial Metaprogramming tool for OCaml using the OCaml toplevel.

It is intended for two purposes:
- when you want to include a bit of generated code in a file, but writing a
  proper generator/ppx rewriter is not worth it;
- when you have many repeated blocks of similar code in your program, to help
  writing and maintaining them.

It is not intended as a general preprocessor, and in particular can only be
used to generate static code that is independent of the system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cinaps-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N --version-string=%{version} \
  -n 'Trivial Metaprogramming tool using the OCaml toplevel' \
  %{buildroot}%{_bindir}/cinaps > %{buildroot}%{_mandir}/man1/cinaps.1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with test}
%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-cinaps-devel -f %{oreon_filedir}/ocaml-cinaps-devel.list

%changelog

%autochangelog
