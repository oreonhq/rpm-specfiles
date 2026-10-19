%global source0_hash ed9bcf88d781767ad6a7c0480aff09d5889f2fc500dda0d1620a1786d4e44490
ExcludeArch: %{ix86}
Name:           ocaml-pcre
Version:        8.0.5
Release:        3%{?dist}
Summary:        Perl compatibility regular expressions (PCRE) for OCaml
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/mmottl/pcre-ocaml
VCS:            git:%{url}.git
Source0:        https://github.com/mmottl/pcre-ocaml/releases/download/%{version}/pcre-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  pcre-devel
# /oreon:deps
%description
Perl compatibility regular expressions (PCRE) for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pcre-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pcre-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-pcre-devel -f %{oreon_filedir}/ocaml-pcre-devel.list

%changelog

%autochangelog
