%global source0_hash ebd1f8afe8679a226fdcbcdb323788e6f63db57521b151473f2ff8c05c30f3aa

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl  https://github.com/backtracking/ptmap

Name:           ocaml-ptmap
Version:        2.0.5
Release:        28%{?dist}
Summary:        Maps over integers implemented as Patricia trees

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://backtracking.github.io/ptmap/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/ptmap-%{version}.tbz
# Fedora does not need the seq and stdlib-shims forward compatibility modules
Patch:          %{name}-compat.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.0.0

%description
OCaml implementation of an efficient maps over integers, from a paper by Chris
Okasaki.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ptmap-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license COPYING LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog
