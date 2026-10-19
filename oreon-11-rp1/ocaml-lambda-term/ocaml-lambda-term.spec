%global source0_hash 0d2ec92d3c3c2e0bd93bb4c7e7bb2d2ffca313405d713304f54202997845b5ff
ExcludeArch: %{ix86}
Name:           ocaml-lambda-term
Version:        3.4.1
Release:        1%{?dist}
Summary:        Terminal manipulation library for OCaml
License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/lambda-term
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-community/lambda-term/archive/%{version}/lambda-term-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-lwt-react-devel
BuildRequires:  ocaml-mew-vi-devel
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-zed-devel
# /oreon:deps
%description
Lambda-term is a cross-platform library for manipulating the terminal. It
provides an abstraction for keys, mouse events, colors, as well as a set of
widgets to write curses-like applications.

The main objective of lambda-term is to provide a higher level functional
interface to terminal manipulation than, for example, ncurses, by providing
a native OCaml interface instead of bindings to a C library.

Lambda-term integrates with zed to provide text editing facilities in
console applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-lwt-react-devel%{?_isa}
Requires:       ocaml-mew-vi-devel%{?_isa}
Requires:       ocaml-uucp-devel%{?_isa}
Requires:       ocaml-zed-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lambda-term-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
mkdir -p %{buildroot}%{_datadir}/lambda-term
mv %{buildroot}%{_datadir}/lambda-term{rc,-inputrc} %{buildroot}%{_datadir}/lambda-term
sed -e 's,%{_datadir}/lambda-termrc,%{_datadir}/lambda-term,' \
    -e '\,%{_datadir}/lambda-term-inputrc,d' \
    -i .ofiles
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-lambda-term-devel -f %{oreon_filedir}/ocaml-lambda-term-devel.list

%changelog

%autochangelog
