%global source0_hash da863b42b81235fdcf45eb32c04fb8bde22ff446a779cfb6f989730a35103160
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%bcond test 0
Name:           ocaml-sexplib
Version:        0.17.0
Epoch:          1
Release:        1%{?dist}
Summary:        Automated S-expression conversion
License:        MIT AND BSD-3-Clause
URL:            https://github.com/janestreet/sexplib
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/sexplib/archive/v%{version}/sexplib-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-base-quickcheck-devel
BuildRequires:  ocaml-core-kernel-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-expect-test-helpers-core-devel
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-parsexp-devel
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-sexplib0-devel
BuildRequires:  vim-filesystem
# /oreon:deps
%description
This package contains a library for serializing OCaml values to and from
S-expressions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       ocaml-num-devel%{?_isa}
Requires:       ocaml-parsexp-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        vim
Summary:        Support for sexplib syntax in vim
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       vim-filesystem
%description    vim
This package contains a vim syntax file for Sexplib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sexplib-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
mkdir -p %{buildroot}%{vimfiles_root}/syntax
cp -p vim/syntax/sexplib.vim %{buildroot}%{vimfiles_root}/syntax
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with test}
%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-sexplib-devel -f %{oreon_filedir}/ocaml-sexplib-devel.list
%files -n ocaml-sexplib-vim -f %{oreon_filedir}/ocaml-sexplib-vim.list

%changelog

%autochangelog
