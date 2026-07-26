%global source0_hash c988b7769a59749631c3c98ba5edd1d2fe91f5dc380b5e0593c073c92f4bee01

Name:           ocaml-intrinsics-kernel
Version:        0.17.1
Release:        %autorelease
Summary:        OCaml interface to CPU intrinsics

License:        MIT
URL:            https://github.com/janestreet/ocaml_intrinsics_kernel
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ocaml_intrinsics_kernel-%{version}.tar.gz
# Use the popcnt instruction only if the running CPU supports it
Patch:          %{name}-popcnt.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0

%description
The ocaml_intrinsics_kernel library provides an OCaml interface to operations
that have dedicated hardware instructions on some micro-architectures.
Currently, it provides the following operations:

- conditional select

See ocaml_intrinsics for details.  Unlike ocaml_intrinsics,
ocaml_intrinsics_kernel can be used by programs compiled to javascript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ocaml_intrinsics_kernel-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
