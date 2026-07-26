%global source0_hash 8bb517fa9a1818246eb8c4ce34ee1489fbebb4b92defa3a25d13cab8d23ec685

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-integers
Version:        0.7.0
Release:        22%{?dist}
Summary:        Various signed and unsigned integer types for OCaml

License:        MIT
URL:            https://github.com/yallop/ocaml-integers
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fedora does not need stdlib-shims, which is for older OCaml systems
Patch:          %{name}-stdlib-shims.patch

BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-dune

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
The ocaml-integers library provides a number of 8-, 16-, 32- and 64-bit signed
and unsigned integer types, together with aliases such as `long` and `size_t`
whose sizes depend on the host platform.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE.md
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
