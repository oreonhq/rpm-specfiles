%global source0_hash 368fbfd4d3bc140078fdc46c68f75b6d1a4cc421f58447b401af45a7d41f4e58
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-camomile
Version:        2.1.0
Release:        1%{?dist}
Summary:        Unicode library for OCaml
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND ICU AND Unicode-3.0
URL:            https://github.com/ocaml-community/Camomile
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-community/Camomile/archive/refs/tags/v2.1.0.tar.gz#/Camomile-2.1.0.tar.gz
Patch1:         0001-Camomile-locales-eo.txt-Fix-license-by-importing-dat.patch
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-site-devel
BuildRequires:  ocaml-stdlib-random-devel
# /oreon:deps
%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camlp-streams-devel%{?_isa}
Requires:       ocaml-dune-site-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
%description    data
The %{name}-data package contains data files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Camomile-%{version}
%oreon_prep
%build

%ifarch %{power64}
ulimit -Hs 65536
ulimit -Ss 65536
%endif
%dune_build
%install
%dune_install
sed -i '\@%{_datadir}@d' .ofiles
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-camomile-devel -f %{oreon_filedir}/ocaml-camomile-devel.list
%files -n ocaml-camomile-data -f %{oreon_filedir}/ocaml-camomile-data.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-21
- Prepare for Oreon 11 (RP1)
