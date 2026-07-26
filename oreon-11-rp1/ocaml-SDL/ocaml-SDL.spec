%global source0_hash 4f40c28cf671f1e260f7e7ce1cee848660f4f0f1d4801e7959dd0a412f2d1cae

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-SDL
Version:        0.9.1
Release:        76%{?dist}
Summary:        OCaml bindings for SDL
License:        LGPL-2.1-or-later

URL:            https://ocamlsdl.sourceforge.net/
Source0:        https://downloads.sourceforge.net/ocamlsdl/ocamlsdl-%{version}.tar.gz
Source1:        ocamlsdl-0.7.2-htmlref.tar.gz

# Fix for safe-string in OCaml 4.06.
Patch1:         ocamlsdl-0.9.1-safe-string.patch

# Adapt to changes in OCaml 5.0
Patch2:         ocamlsdl-0.9.1-ocaml5.patch
Patch3:         ocamlsdl-0.9.1-ocaml5-blocking-section.patch

BuildRequires:  make
BuildRequires:  ocaml-lablgl-devel
BuildRequires:  SDL_gfx-devel, SDL_ttf-devel, SDL_mixer-devel, SDL_image-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros

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

%autosetup -p1 -n ocamlsdl-%{version} -a 1

%build
%configure
%ifnarch %{ocaml_native_compiler}
# The configure step sets OCAMLOPT to "no", but the Makefile expects it to be
# the empty string on bytecode-only architectures
sed -i 's/^\(OCAMLOPT =\).*/\1/' makefile.config.gcc
%endif
%make_build

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
%ocaml_files

%files -f .ofiles
%doc README AUTHORS NEWS
%license COPYING

%files devel -f .ofiles-devel
%doc htmlref/

%changelog
%autochangelog
