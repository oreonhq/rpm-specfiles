%global source0_hash c98280a23a28e1be145b7a5e47b6474b85be69c8e75dbc2b9ef0e85233c05d62

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-camlimages
Version:        5.0.5
Release:        10%{?dist}
Summary:        OCaml image processing library
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception

URL:            https://gitlab.com/camlspotter/camlimages
VCS:            git:%{url}.git
Source0:        https://gitlab.com/camlspotter/camlimages/-/archive/%{version}/camlimages-%{version}.tar.gz
# Expose a dependency on the math library so RPM can see it
Patch0:         %{name}-mathlib.patch
# OCaml 5.0 compatibility
Patch1:         %{name}-ocaml5.patch
# Add :standard to C flags
# https://gitlab.com/camlspotter/camlimages/-/commit/c3898f58d14af54d04d9cbc576bc5b1be7d98f6d
Patch2:         %{name}-standard-flags.patch
# Adapt to the Caml -> Stdlib change in ocaml-base 0.17
Patch3:         %{name}-base-0.17.patch

BuildRequires:  ghostscript
BuildRequires:  giflib-devel
BuildRequires:  ocaml >= 4.12.1
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune >= 3.2
BuildRequires:  ocaml-dune-configurator-devel >= 2.0.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-graphics-devel
BuildRequires:  ocaml-lablgtk-devel >= 2.18.6
BuildRequires:  ocaml-stdio-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  rgb

Requires:       ghostscript
Requires:       rgb

%description
This is an image processing library, which provides some basic
functions of image processing and loading/saving various image file
formats. In addition the library can handle huge images that cannot be
(or can hardly be) stored into the memory (the library automatically
creates swap files and escapes them to reduce the memory usage).

%package        devel
Summary:        Development files for camlimages
Requires:       %{name}%{?_isa} = %{version}-%{release} 
Requires:       ocaml-graphics-devel%{?_isa}
Requires:       ocaml-lablgtk-devel%{?_isa}

%description    devel
The camlimages-devel package provides libraries and headers for 
developing applications using camlimages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n camlimages-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md Changes.txt
%license License.txt

%files devel -f .ofiles-devel

%changelog
%autochangelog
