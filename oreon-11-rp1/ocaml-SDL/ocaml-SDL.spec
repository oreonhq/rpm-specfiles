%global source0_hash abfb295b263dc11e97fffdd88ea1a28b46df8cc2b196777093e4fe7f509e4f8f
ExcludeArch: %{ix86}
Name:           ocaml-SDL
Version:        0.9.1
Release:        76%{?dist}
Summary:        OCaml bindings for SDL
License:        LGPL-2.1-or-later
URL:            https://ocamlsdl.sourceforge.net/
Source0:        https://downloads.sourceforge.net/ocamlsdl/ocamlsdl-%{version}.tar.gz
Source1:        ocamlsdl-0.7.2-htmlref.tar.gz
Patch1:         ocamlsdl-0.9.1-safe-string.patch
Patch2:         ocamlsdl-0.9.1-ocaml5.patch
Patch3:         ocamlsdl-0.9.1-ocaml5-blocking-section.patch
# oreon:deps
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgl-devel
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
Runtime libraries to allow programs written in OCaml to write to SDL 
(Simple DirectMedia Layer) interfaces.

%package        devel
Summary:        Development files for ocamlSDL
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The ocamlSDL-devel package provides libraries and headers for developing 
applications using ocamlSDL

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ocamlsdl-%{version}
%oreon_prep
%build

%configure
%ifnarch %{ocaml_native_compiler}
sed -i 's/^\(OCAMLOPT =\).*/\1/' makefile.config.gcc
%endif
%make_build
%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-SDL-devel -f %{oreon_filedir}/ocaml-SDL-devel.list

%changelog

%autochangelog
