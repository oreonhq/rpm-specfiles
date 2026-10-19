%global source0_hash 99414da7609b92a02474ef4b49ecda15edc8cbba5229341b124e7e4695c39610
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
ExcludeArch: %{ix86}
%bcond bootstrap 0
Name:           ocaml-yojson
Version:        3.0.0
Release:        1%{?dist}
Summary:        An optimized parsing and printing library for the JSON format
License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/yojson
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-community/yojson/releases/download/%{version}/yojson-%{version}.tbz
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
# /oreon:deps
%description
Yojson is an optimized parsing and printing library for the JSON
format. It addresses a few shortcomings of json-wheel including 2x
speedup, polymorphic variants and optional syntax for tuples and
variants.

ydump is a pretty-printing command-line program provided with the
yojson package.

The program atdgen can be used to derive OCaml-JSON serializers and
deserializers from type definitions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%if %{without bootstrap}
%package        five
Summary:        Parsing and printing library for the JSON5 format
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    five
Yojson-five is a parsing and printing library for the JSON5 format.  It
supports parsing JSON5 to Yojson.Basic.t and Yojson.Safe.t types.

%package        five-devel
Summary:        Development files for %{name}-five
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-five%{?_isa} = %{version}-%{release}
Requires:       ocaml-sedlex-devel%{?_isa}
%description    five-devel
The %{name}-five-devel package contains libraries and signature
files for developing applications that use %{name}-five.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir yojson-%{version}
%oreon_prep
%build

%if %{with bootstrap}
%dune_build -p yojson
%else
%dune_build -p yojson,yojson-five
%endif
%install
%if %{with bootstrap}
%dune_install -s yojson
%else
%dune_install -s yojson yojson-five
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%if %{with bootstrap}
%dune_check -p yojson
%else
%dune_check -p yojson,yojson-five
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-yojson-devel -f %{oreon_filedir}/ocaml-yojson-devel.list

%changelog

%autochangelog
