%global source0_hash 662c910f774e9fee3a19c4e057f380581ab2fc4ee52da4761304ac9c31b8869d

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-findlib
Version:        1.9.8
Release:        8%{?dist}
Summary:        Objective CAML package manager and build helper
License:        MIT

URL:            http://projects.camlcity.org/projects/findlib.html
VCS:            git:https://github.com/ocaml/ocamlfind.git
Source0:        http://download.camlcity.org/download/findlib-%{version}.tar.gz

# Fix the toolbox build with OCaml 5.x
Patch0:         %{name}-toolbox.patch

BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-labltk-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  m4, ncurses-devel
BuildRequires:  make
Requires:       ocaml

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Topdirs -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings


%description
Objective CAML package manager and build helper.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n findlib-%{version}

# Fix character encoding
iconv -f ISO8859-1 -t UTF-8 doc/README > doc/README.utf8
touch -r doc/README doc/README.utf8
mv doc/README.utf8 doc/README

# Fix the OCaml core man directory
sed -i 's,/usr/local/man,%{_mandir},' configure

# Build an executable that is not damaged by stripping
sed -i 's/\(custom=\)-custom/\1-output-complete-exe/' configure

# Skip broken test for ocamlopt -g
sed -i '/^ocamlopt -g/d' configure


%build
ocamlc -version
ocamlc -where
(cd tools/extract_args && make)
tools/extract_args/extract_args -o src/findlib/ocaml_args.ml ocamlc ocamlcp ocamlmktop ocamlopt ocamldep ocamldoc ||:
cat src/findlib/ocaml_args.ml
./configure -config %{_sysconfdir}/findlib.conf \
  -bindir %{_bindir} \
  -sitelib `ocamlc -where` \
  -mandir %{_mandir} \
  -with-toolbox
%make_build all
%ifarch %{ocaml_native_compiler}
%make_build opt
%endif
rm doc/guide-html/TIMESTAMP


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
%make_install \
     OCAMLFIND_BIN=%{_bindir} \
     OCAMLFIND_CONF=%{_sysconfdir} \
     OCAMLFIND_MAN=%{_mandir}
rmdir $RPM_BUILD_ROOT%{_mandir}/man3

%ocaml_files
sed -i '/etc/d' .ofiles


%files -f .ofiles
%doc LICENSE doc/README
%config(noreplace) %{_sysconfdir}/findlib.conf


%files devel -f .ofiles-devel
%doc LICENSE doc/README doc/guide-html


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.8-8
- Prepare for Oreon 11 (RP1)
