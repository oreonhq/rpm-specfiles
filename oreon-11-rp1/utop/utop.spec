%global source0_hash 4a1735aa9ca714fcd95b3e4f583261362985dd5ca7e93e848af3ba16523a1ec1
ExcludeArch: %{ix86}
%global debug_package %{nil}
%global giturl  https://github.com/ocaml-community/utop
Name:           utop
Version:        2.17.0
Release:        1%{?dist}
Summary:        Improved toplevel for OCaml
License:        BSD-3-Clause
URL:            https://ocaml-community.github.io/utop/
VCS :           git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-version.patch
Provides:       ocaml-%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  emacs-nw
BuildRequires:  emacs-tuareg
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lambda-term-devel
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-lwt-react-devel
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-xdg-devel
BuildRequires:  ocaml-zed-devel
# /oreon:deps
%description
utop is an improved toplevel (i.e., Read-Eval-Print Loop) for OCaml.  It can
run in a terminal or in Emacs.  It supports line editing, history, real-time
and context sensitive completion, colors, and more.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-findlib%{?_isa}
Requires:       ocaml-lambda-term-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-zed-devel%{?_isa}
%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n emacs-utop
Summary:        Emacs front end for utop
BuildArch:      noarch
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       emacs-tuareg
Recommends:     emacs-company
%description -n emacs-utop
This package contains an Emacs front end for utop, an improved toplevel for
OCaml.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%dune_build
cd src/top
emacs -batch --no-init-file --no-site-file \
    --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/utop-loaddefs.el\"))"
%_emacs_bytecompile utop.el
cd -
%install
%dune_install
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cp -p src/top/utop-loaddefs.* %{buildroot}%{_emacs_sitestartdir}
cp -p src/top/utop.elc %{buildroot}%{_emacs_sitelispdir}
%oreon_autofiles emacs-utop usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n utop-devel -f %{oreon_filedir}/utop-devel.list
%files -n emacs-utop -f %{oreon_filedir}/emacs-utop.list

%changelog

%autochangelog
