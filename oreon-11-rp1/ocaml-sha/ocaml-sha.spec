%global source0_hash 6de5b12139b1999ce9df4cc78a5a31886c2a547c9d448bf2853f8b53bcf1f1b1

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-sha
Version:        1.15.4
Release:        17%{?dist}
Summary:        Binding to the SHA cryptographic functions

License:        ISC
URL:            https://github.com/djs55/ocaml-sha
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/v%{version}/sha-%{version}.tbz

# The OCaml version packaged in Fedora is recent enough, no need to shim stdlib.
Patch1:         ocaml-sha-remove-stdlib-shims-dep.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel

%description
A binding for SHA interface code in OCaml.  This packages offers the
same interface as the MD5 digest included in the OCaml standard library.
It currently provides SHA1, SHA256 and SHA512 hash functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sha-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGES.md
%license LICENSE.md

%files devel -f .ofiles-devel
%doc README.md CHANGES.md
%license LICENSE.md

%changelog
%autochangelog
