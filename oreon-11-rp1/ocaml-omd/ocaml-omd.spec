%global source0_hash 42c8c0ce1676eb3c1cfa67548823334cf51114519078d249882eacdfc214d932
Name:           ocaml-omd
Version:        2.0.0~alpha1
Release:        1%{?dist}
Summary:        Extensible Markdown library and tool in "pure OCaml"
License:        ISC
URL:            https://github.com/ocaml/omd
Source0:        https://github.com/ocaml/omd/archive/%{version}/omd-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  help2man
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
# /oreon:deps
%description
Omd is an OCaml library designed to parse, manipulate, and print
Markdown into different formats.  In addition to the library, a
command-line tool omd is included to easily convert markdown into HTML.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir omd-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N --version-string=%{version} -o %{buildroot}%{_mandir}/man1/omd.1 \
  -n 'Convert markdown to HTML' %{buildroot}%{_bindir}/omd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-omd-devel -f %{oreon_filedir}/ocaml-omd-devel.list

%changelog

%autochangelog
