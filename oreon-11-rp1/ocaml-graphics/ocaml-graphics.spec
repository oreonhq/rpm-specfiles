%global source0_hash baa99f5316c26df0844ee68921f531e554aab7ea2a1c881f30bd8365309077b0
ExcludeArch: %{ix86}
%global giturl  https://github.com/ocaml/graphics
Name:           ocaml-graphics
Version:        5.2.0
Release:        1%{?dist}
Summary:        Portable drawing primitives for OCaml
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://ocaml.github.io/graphics/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/graphics-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
# /oreon:deps
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
%global oreon_srcdir graphics-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-graphics-devel -f %{oreon_filedir}/ocaml-graphics-devel.list
%files -n ocaml-graphics-doc -f %{oreon_filedir}/ocaml-graphics-doc.list

%changelog

%autochangelog
