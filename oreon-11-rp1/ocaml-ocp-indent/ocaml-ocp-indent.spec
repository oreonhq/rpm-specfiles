%global source0_hash 8cae8863f823cc9c91c3bf2190f35a2b7614ae3b12a046ffcae146a5516b50e8
ExcludeArch: %{ix86}
%global giturl  https://github.com/OCamlPro/ocp-indent
Name:           ocaml-ocp-indent
Version:        1.10.0
Release:        1%{?dist}
Summary:        A simple tool to indent OCaml programs
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND QPL-1.0
URL:            https://www.typerex.org/ocp-indent.html
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/ocp-indent-%{version}.tar.gz
Patch:          %{name}-nonbreaking-space.patch
Requires:       emacs-filesystem >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       vim-filesystem
# oreon:deps
BuildRequires:  emacs-nw
BuildRequires:  emacs-tuareg
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib-devel
BuildRequires:  vim-enhanced
# /oreon:deps
%description
Ocp-indent is a simple tool and library to indent OCaml code.  It is based on
an approximate, tolerant OCaml parser and a simple stack machine; this is much
faster and more reliable than using regexps.  Presets and configuration
options are available, with the possibility to set them project-wide.
Ocp-indent supports most common syntax extensions, and is extensible for
others.

Includes:

- An indentor program, callable from the command-line or from within editors
- Bindings for popular editors
- A library that can be directly used by editor writers, or just for
  fault-tolerant/approximate parsing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-findlib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ocp-indent-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
sed -i '\@%{_datadir}/ocp-indent@d' .ofiles .ofiles-devel
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/ocp-indent/vim/* %{buildroot}%{vimfiles_root}
rm -fr %{buildroot}%{_datadir}/ocp-indent
cd %{buildroot}%{_emacs_sitelispdir}
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/ocp-indent-loaddefs.el\"))"
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv ocp-indent-loaddefs.el %{buildroot}%{_emacs_sitestartdir}
%_emacs_bytecompile ocp-indent.el
cd -
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n ocaml-ocp-indent-devel -f %{oreon_filedir}/ocaml-ocp-indent-devel.list

%changelog

%autochangelog
