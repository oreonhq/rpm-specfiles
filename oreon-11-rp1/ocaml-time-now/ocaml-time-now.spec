%global source0_hash fc85d6e46c4eb9370de9385f7bbfa6d57b4e48a9e96b20009007226b73f9530c
ExcludeArch: %{ix86}
Name:           ocaml-time-now
Version:        0.17.0
Release:        1%{?dist}
Summary:        Get the current time in OCaml
License:        MIT
URL:            https://github.com/janestreet/time_now
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/time_now/archive/v%{version}/time_now-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-jane-street-headers-devel
BuildRequires:  ocaml-jst-config-devel
BuildRequires:  ocaml-ppx-base-devel
BuildRequires:  ocaml-ppx-optcomp-devel
# /oreon:deps
%description
This package provides a single OCaml function to report the current time in
nanoseconds since the start of the Unix epoch.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-jane-street-headers-devel
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-enumerate-devel%{?_isa}
Requires:       ocaml-ppx-hash-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir time_now-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-time-now-devel -f %{oreon_filedir}/ocaml-time-now-devel.list

%changelog

%autochangelog
