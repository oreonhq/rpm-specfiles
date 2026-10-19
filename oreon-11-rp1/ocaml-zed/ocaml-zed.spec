%global source0_hash 4b6a3085d682327269fe69ff0d7eb9a2f8532f41ee57a42f27f48b7fdc3b058c
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-zed
Version:        3.2.3
Release:        19%{?dist}
Summary:        Abstract engine for text editing in OCaml
License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/zed
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-community/zed/archive/%{version}/zed-%{version}.tar.gz
Patch0:         %{name}-uchar.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-uucp-devel
BuildRequires:  ocaml-uuseg-devel
BuildRequires:  ocaml-uutf-devel
# /oreon:deps
%description
Zed is an abstract engine for text editing.  It can be used to
write text editors, editing widgets, readlines, ...  You just
have to connect an engine to your inputs and rendering functions
to get an editor.

Zed provides: editing state management, multiple cursor support,
key-binding helpers, and general purpose unicode rope
manipulation functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-react-devel%{_isa}
Requires:       ocaml-result-devel%{_isa}
Requires:       ocaml-uucp-devel%{_isa}
Requires:       ocaml-uuseg-devel%{_isa}
Requires:       ocaml-uutf-devel%{_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir zed-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-zed-devel -f %{oreon_filedir}/ocaml-zed-devel.list

%changelog

%autochangelog
