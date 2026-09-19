%global source0_hash 4e2a4701b584b7fc27f8df33bb345b653a28d0733ecf5c66ee3cbbcff3fd1557

Name:           ocaml-afl-persistent
Version:        1.4
Release:        %autorelease
Summary:        Persistent-mode American Fuzzy Lop for OCaml

License:        MIT
URL:            https://github.com/stedolan/ocaml-afl-persistent
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# The american-fuzzy-lop package is currently only built for x86_64
ExclusiveArch:  %{x86_64}

BuildRequires:  american-fuzzy-lop
BuildRequires:  ocaml >= 4.05
BuildRequires:  ocaml-dune >= 2.9

Requires:       american-fuzzy-lop

%description
This package enables running the American Fuzzy Lop fuzzing tool in persistent
mode in OCaml projects.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
./config.sh
%dune_build

%install
%dune_install

%check
cd test
./test.sh

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
