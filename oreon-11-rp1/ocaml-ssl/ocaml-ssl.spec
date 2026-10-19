%global source0_hash 932726838c6bfd82727b24af660a37d3bc0b905ea3f80b07056fe0901d92ed6c
ExcludeArch: %{ix86}
%global forgeurl https://github.com/savonet/ocaml-ssl
%global commit ffc634d9adc8ebf5c6cc6cd5002233c4ab233798
Version:       0.7.0
%forgemeta
Name:           ocaml-ssl
Release:        1%{?dist}
Summary:        SSL bindings for OCaml
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/openssl
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  openssl-devel
# /oreon:deps
%description
SSL bindings for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ssl-devel -f %{oreon_filedir}/ocaml-ssl-devel.list

%changelog

%autochangelog
