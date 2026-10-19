%global source0_hash 64d38ceb52ef574cb314bdd693f7e4a9c9e483e80a58595db22f2df76a8a59e6
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-mew
Version:        0.1.0
Release:        1%{?dist}
Summary:        Modal Editing Witch
License:        MIT
URL:            https://github.com/kandu/mew
VCS:            git:%{url}.git
Source0:        https://github.com/kandu/mew/archive/%{version}/mew-%{version}.tar.gz
Patch:          %{name}-mathlib.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-trie-devel
# /oreon:deps
%description
This is the core module of mew, a general modal editing engine generator.  You
can provide `Key`, `Mode`, and `Concurrent` modules to define the real world
environment to get the core component of a modal editing engine.  The core
component supports recursive key mappings associated with user provided modes.
After the core component is generated, you may extended it with a translator
to interpret user key sequences to get a complete modal editing engine.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-trie-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mew-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-mew-devel -f %{oreon_filedir}/ocaml-mew-devel.list

%changelog

%autochangelog
