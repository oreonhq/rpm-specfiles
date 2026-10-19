%global source0_hash 03bf4bae6908a947582485c2a0b8f96428f39f97efd540573a613632be56ad2a
ExcludeArch: %{ix86}
%global giturl  https://github.com/ocsigen/lwt
Name:           ocaml-lwt
Version:        6.1.2
Release:        1%{?dist}
Summary:        OCaml lightweight thread library
License:        MIT AND BSD-2-Clause
URL:            https://ocsigen.org/lwt
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/lwt-%{version}.tar.gz
Patch:          %{name}-mathlib.patch
Patch:          %{name}-ppxlib-0.36.patch
Obsoletes:      ocaml-lwt-luv < 5.7.0
# oreon:deps
BuildRequires:  libev-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocplib-endian-devel
BuildRequires:  ocaml-ppx-let-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-react-devel
# /oreon:deps
%description
Lwt is a lightweight thread library for Objective Caml.  This library
is part of the Ocsigen project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ocplib-endian-devel%{?_isa}
Requires:       libev-devel%{?_isa}
Obsoletes:      ocaml-lwt-luv-devel < 5.7.0
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        react
Summary:        Helpers for using React with Lwt
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    react
Helpers for using React with Lwt.

%package        react-devel
Summary:        Development files for ocaml-lwt-react
Requires:       %{name}-react%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-react-devel%{?_isa}
%description    react-devel
The %{name}-react-devel package contains libraries and signature files for
developing applications that use %{name}-react.

%package        ppx
Summary:        PPX syntax for Lwt
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    ppx
PPX syntax for Lwt, providing something similar to async/await from JavaScript.

%package        ppx-devel
Summary:        Development files for ocaml-lwt-ppx
Requires:       %{name}-ppx%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}
%description    ppx-devel
The %{name}-ppx-devel package contains libraries and signature files for
developing applications that use %{name}-ppx.

%package        retry
Summary:        Utilities for retrying Lwt computations
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    retry
Utilities for retrying Lwt computations.

%package        retry-devel
Summary:        Development files for ocaml-lwt-retry
Requires:       %{name}-retry%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description    retry-devel
The %{name}-retry-devel package contains libraries and signature files for
developing applications that use %{name}-retry.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lwt-%{version} -p1

# It looks like one test fails.
# Actually, it looks like all the "mcast" tests fail in koji.
# They should probably be disabled via a patch, but this works for now.
sed 's,test_mcast "mcast-join-loop" true true;,(*test_mcast "mcast-join-loop" true true;*),' -i test/unix/test_mcast.ml
sed 's,test_mcast "mcast-join-noloop" true false;,(*test_mcast "mcast-join-noloop" true false;*),' -i test/unix/test_mcast.ml
sed 's,test_mcast "mcast-nojoin-loop" false true;,(*test_mcast "mcast-nojoin-loop" false true;*),' -i test/unix/test_mcast.ml
sed 's,test_mcast "mcast-nojoin-noloop" false false;,(*test_mcast "mcast-nojoin-noloop" false false;*),' -i test/unix/test_mcast.ml

%build

dune exec src/unix/config/discover.exe -- --save \
     --use-libev true --use-pthread true
%dune_build
%install
%dune_install -s
rm -rf %{buildroot}%{ocamldir}/lwt_ppx_let
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch s390x
%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-lwt-devel -f %{oreon_filedir}/ocaml-lwt-devel.list
%files -n ocaml-lwt-react -f %{oreon_filedir}/ocaml-lwt-react.list
%files -n ocaml-lwt-react-devel -f %{oreon_filedir}/ocaml-lwt-react-devel.list
%files -n ocaml-lwt-ppx -f %{oreon_filedir}/ocaml-lwt-ppx.list
%files -n ocaml-lwt-ppx-devel -f %{oreon_filedir}/ocaml-lwt-ppx-devel.list
%files -n ocaml-lwt-retry -f %{oreon_filedir}/ocaml-lwt-retry.list
%files -n ocaml-lwt-retry-devel -f %{oreon_filedir}/ocaml-lwt-retry-devel.list

%changelog

%autochangelog
