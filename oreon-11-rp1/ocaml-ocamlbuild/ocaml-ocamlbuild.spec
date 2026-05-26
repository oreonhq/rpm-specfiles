# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2ba6857f2991b7f69368e8db818b163d31cf5a367f15f5953bf8f01a77b3d4fc
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# NOTE: there is no devel subpackage because the main package *IS* a devel
# package.

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:          ocaml-ocamlbuild
Version:       0.16.1
Release:       5%{?dist}

Summary:       Build tool for OCaml libraries and programs

License:       LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:           https://github.com/ocaml/ocamlbuild
VCS:           git:%{url}.git
Source0:        https://github.com/ocaml/ocamlbuild/archive/0.16.1/ocamlbuild-0.16.1.tar.gz

BuildRequires: make
BuildRequires: ocaml >= 4.08
BuildRequires: ocaml-rpm-macros
BuildRequires: ncurses
BuildRequires: asciidoc
BuildRequires: python3-pygments

# Ocamlbuild can invoke tput; see src/display.ml
Requires:      ncurses

# This can be removed when F42 reaches EOL
Obsoletes:     %{name}-devel < 0.14.0-37
Provides:      %{name}-devel = %{version}-%{release}


%description
OCamlbuild is a build tool for building OCaml libraries and programs.


%package doc
Summary:       Documentation for %{name}
License:       CC0-1.0
BuildArch:     noarch


%description doc
This package contains the manual for %{name}.


%prep
%oreon_verify_sources
%autosetup -n ocamlbuild-%{version}


%build
make configure \
  OCAMLBUILD_PREFIX=%{_prefix} \
  OCAMLBUILD_BINDIR=%{_bindir} \
  OCAMLBUILD_LIBDIR=%{_libdir}/ocaml \
  OCAMLBUILD_MANDIR=%{_mandir} \
%ifarch %{ocaml_native_compiler}
  OCAML_NATIVE=true \
  OCAML_NATIVE_TOOLS=true
%else
  OCAML_NATIVE=false \
  OCAML_NATIVE_TOOLS=false
%endif

# Parallel builds fail.
make \
%ifarch %{ocaml_native_compiler}
     OCAMLC="ocamlc.opt -g" \
     OCAMLOPT="ocamlopt.opt -g"
%else
     OCAMLC="ocamlc -g" \
     OCAMLOPT="ocamlopt -g"
%endif

# Build the manual
asciidoc manual/manual.adoc


%install
%make_install CHECK_IF_PREINSTALLED=false

# The install copies ocamlbuild & ocamlbuild.{byte or native}.
# Symlink them instead.
pushd $RPM_BUILD_ROOT/usr/bin
%ifarch %{ocaml_native_compiler}
ln -sf ocamlbuild.native ocamlbuild
%else
ln -sf ocamlbuild.byte ocamlbuild
%endif
popd

%ocaml_files -n


%files -f .ofiles
%doc Changes Readme.md VERSION
%license LICENSE


%files doc
%license manual/LICENSE
%doc manual/manual.html


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.1-5
- Prepare for Oreon 11 (RP1)
