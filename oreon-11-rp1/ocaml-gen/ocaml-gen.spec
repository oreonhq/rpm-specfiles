%global source0_hash 6893bf156bbaa4254ec5ec2ea5fe539030f2395bc5cd83ccb8fe3930cff89cb0

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl  https://github.com/c-cube/gen

Name:           ocaml-gen
Version:        1.1
Release:        18%{?dist}
Summary:        Simple, efficient iterators for OCaml

License:        BSD-2-Clause
URL:            https://c-cube.github.io/gen/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/gen-%{version}.tar.gz
# Fedora does not need the seq forward compatibility shim
Patch:          %{name}-seq.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 1.1
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-qcheck-devel
BuildRequires:  ocaml-qtest-devel

%description
Iterators for OCaml, both restartable and consumable.  The implementation
keeps a good balance between simplicity and performance.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gen-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGELOG.md
%license LICENSE

%files devel -f .ofiles-devel
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
