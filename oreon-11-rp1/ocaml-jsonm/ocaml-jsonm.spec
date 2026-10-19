%global source0_hash d4bb68e30acad2ccc38bd9bc89637cf5480ee262a24f05c23d7d87276e7abdea
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-jsonm
Version:        1.0.2
Release:        1%{?dist}
Summary:        Non-blocking streaming JSON codec for OCaml
License:        ISC
URL:            https://erratique.ch/software/jsonm
VCS:            git:https://erratique.ch/repos/jsonm.git
Source0:        https://github.com/dbuenzli/jsonm/archive/v%{version}/jsonm-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
BuildRequires:  ocaml-uutf-devel
# /oreon:deps
%description
Jsonm is an OCaml non-blocking streaming codec to decode and encode the JSON
data format.  It can process JSON text without blocking on IO and without a
complete in-memory representation of the data.

The uncut codec also processes whitespace and (non-standard) JSON with
JavaScript comments.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jsonm-%{version}

%conf
# Topkg does watermark replacements only if run inside a git checkout.  Github
# tarballs do not come with a .git directory.  Therefore, we do the watermark
# replacement manually.
for fil in $(find . -type f); do
  sed -e 's,%%%%VERSION%%%%,v%{version},' \
      -e 's,%%%%VERSION_NUM%%%%,%{version},' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build

ocaml pkg/pkg.ml build --tests true --dev-pkg false
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-jsonm-devel -f %{oreon_filedir}/ocaml-jsonm-devel.list

%changelog

%autochangelog
