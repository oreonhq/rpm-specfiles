%global source0_hash debd1345ac0116232390af64552d15948b5dc7200e287730235f7ff42098f3c5

Name:           ocaml-crowbar
Version:        0.2.2
Release:        %autorelease
Summary:        Code fuzzer for OCaml

License:        MIT
URL:            https://github.com/stedolan/crowbar
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/crowbar-%{version}.tar.gz

# The american-fuzzy-lop package is currently only built for x86_64
ExclusiveArch:  %{x86_64}

BuildRequires:  american-fuzzy-lop
BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-afl-persistent-devel >= 1.1
BuildRequires:  ocaml-calendar-devel >= 2.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-dune >= 2.9
BuildRequires:  ocaml-fpath-devel
BuildRequires:  ocaml-pprint-devel
BuildRequires:  ocaml-uucp-devel
BuildRequires:  ocaml-uunf-devel
BuildRequires:  ocaml-uutf-devel

Requires:       american-fuzzy-lop

%description
Crowbar is a library for testing code, combining QuickCheck-style
property-based testing and the magical bug-finding powers of American Fuzzy
Lop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-afl-persistent-devel%{?_isa}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-ocplib-endian-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n crowbar-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
