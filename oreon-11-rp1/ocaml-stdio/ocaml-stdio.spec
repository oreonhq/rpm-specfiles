%global source0_hash e7cb473d4bffcf419f307c658cf2599fab03a2b4fe655bfd0be699f8f7af176e

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-stdio
Version:        0.17.0
Release:        %autorelease
Summary:        Jane Street Standard I/O library for OCaml

License:        MIT
URL:            https://github.com/janestreet/stdio
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/stdio-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0

%description
Stdio provides input/output functions for OCaml.  It re-exports the buffered
channels of the stdlib distributed with OCaml but with some improvements.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n stdio-%{version}

%build
%dune_build

%install
%dune_install

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
