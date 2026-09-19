%global source0_hash baa99f5316c26df0844ee68921f531e554aab7ea2a1c881f30bd8365309077b0

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml/graphics

Name:           ocaml-graphics
Version:        5.2.0
Release:        %autorelease
Summary:        Portable drawing primitives for OCaml

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://ocaml.github.io/graphics/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/graphics-%{version}.tar.gz

BuildRequires:  ocaml >= 4.09.0
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)

%description
The graphics library provides a set of portable drawing primitives.  Drawing
takes place in a separate window that is created when `Graphics.open_graph` is
called.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel%{?_isa}
Requires:       libXft-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains developer documentation for
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n graphics-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%files doc
%license LICENSE
%doc examples

%changelog
%autochangelog
