%global source0_hash 78fa6084cd067b7a7d930d1fe1cb7eb9dcd1a90c73017e570213b47a3762eb4f
ExcludeArch: %{ix86}
%global srcname jane-street-headers
%global debug_package %{nil}
Name:           ocaml-%{srcname}
Version:        0.17.0
Release:        1%{?dist}
Summary:        Jane Street header files
License:        MIT
URL:            https://github.com/janestreet/jane-street-headers
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This package contains C header files shared between various Jane Street
packages.

%package        devel
Summary:        Development files for %{name}
%description    devel
This package contains C header files shared between various Jane Street
packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%dune_build
%install
%dune_install
rm -f %{buildroot}%{ocamldir}/%{srcname}/*.{cma,cmi,cmt,cmx,cmxa,cmxs,ml}
sed -ri '/(archive|plugin)/d' \
        %{buildroot}%{ocamldir}/%{srcname}/{dune-package,META}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-jane-street-headers-devel -f %{oreon_filedir}/ocaml-jane-street-headers-devel.list

%changelog

%autochangelog
