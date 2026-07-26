%global source0_hash 9b9644d7351db699e57ddba7c767bb4153e6e988ccf45ead2fb238a3bd75cdc7

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifarch %{ocaml_native_compiler}
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif

Name:           ocaml-compiler-libs-janestreet
Version:        0.17.0
Release:        10%{?dist}
Summary:        OCaml compiler libraries repackaged

License:        MIT
URL:            https://github.com/janestreet/ocaml-compiler-libs
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ocaml-compiler-libs-%{version}.tar.gz

BuildRequires:  ocaml >= 5.2.0
BuildRequires:  ocaml-dune >= 1.5.1

%description
This package exposes the OCaml compiler libraries repackaged under the
toplevel names Ocaml_common, Ocaml_bytecomp, Ocaml_optcomp, etc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ocaml-compiler-libs-%{version}

%build
%dune_build

%install
%dune_install

%files -f .ofiles
%doc README.org
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
