%global source0_hash none

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl  https://github.com/gildor478/ocaml-fileutils

Name:           ocaml-fileutils
Version:        0.6.6
Release:        7%{?dist}
Summary:        OCaml library for common file and filename operations

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://gildor478.github.io/ocaml-fileutils/
VCS:            git:%{giturl}.git
Source0:        https://github.com/gildor478/ocaml-fileutils/releases/download/v0.6.6/fileutils-0.6.6.tbz

BuildRequires:  ocaml >= 4.14
BuildRequires:  ocaml-dune >= 2.9
%if 0%{?fedora}
BuildRequires:  ocaml-ounit-devel >= 2.0.0
%endif


%description
This library is intended to provide a basic interface to the most
common file and filename operations.  It provides several different
filename functions: reduce, make_absolute, make_relative...  It also
enables you to manipulate real files: cp, mv, rm, touch...

It is separated into two modules: SysUtil and SysPath.  The first one
manipulates real files, the second one is made for manipulating
abstract filenames.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n fileutils-%{version} -p1


%build
%dune_build


%install
%dune_install


# Do not run the tests (RHEL 7+ only) since they require ocaml-ounit.
%if 0%{?fedora} || 0%{?rhel} <= 6
%check
%dune_check
%endif


%files -f .ofiles
%license LICENSE.txt


%files devel -f .ofiles-devel
%doc README.md CHANGES.md
%license LICENSE.txt


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.6-7
- Prepare for Oreon 11 (RP1)
