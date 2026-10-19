%global source0_hash 2cf345e33bed0ee4c325667e77dfc5bee8f12afd56318b7c9acf81ec875ecf6e
ExcludeArch: %{ix86}
%global debug_package %{nil}
Name:           ocaml-jst-config
Version:        0.17.0
Release:        1%{?dist}
Summary:        Compile-time configuration for Jane Street libraries
License:        MIT
URL:            https://github.com/janestreet/jst-config
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/jst-config/archive/v%{version}/jst-config-%{version}.tar.gz
Patch:          %{name}-gettid.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ppx-assert-devel
# /oreon:deps
%description
This package defines compile-time constants used in Jane Street libraries such
as Base, Core, and Async.

%package        devel
Summary:        Development files for %{name}
%description    devel
This package defines compile-time constants used in Jane Street libraries such
as Base, Core, and Async.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jst-config-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install -n
rm -f %{buildroot}%{ocamldir}/jst-config/*.{a,cma,cmi,cmt,cmx,cmxa,cmxs,ml}
sed -ri '/(archive|plugin)/d' \
        %{buildroot}%{ocamldir}/jst-config/{dune-package,META}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-jst-config-devel -f %{oreon_filedir}/ocaml-jst-config-devel.list

%changelog

%autochangelog
