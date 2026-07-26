%global source0_hash 20833acb43447d94af6ab595a777e48cda75206c37b163d244f2ea8462a1aaf6

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-expat
Version:        1.3.0
Release:        17%{?dist}
Summary:        OCaml wrapper for the Expat XML parsing library
License:        MIT

URL:            https://github.com/whitequark/ocaml-expat
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  pkgconfig(expat)

%description
An ocaml wrapper for the Expat XML parsing library. It allows you to
write XML-Parsers using the SAX method. An XML document is parsed on
the fly without needing to load the entire XML-Tree into memory.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       expat-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Fix the ounit name, build with Fedora flags, and make libraries with debuginfo
sed -e 's/oUnit/ounit2/g' \
    -e 's|-O2 -I\$(EXPAT_INCDIR)|%{build_cflags}|' \
    -e 's/\$(OCAMLMKLIB)/& -g/' \
    -i Makefile

# We do not need the README in the doc output
rm doc/README

%build
make depend
make -j1 all \
%ifarch %{ocaml_native_compiler}
  allopt \
  OCAMLC="ocamlc.opt -g" \
  OCAMLOPT="ocamlopt.opt -g"
%endif

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
%ocaml_files

%files -f .ofiles
%doc README changelog
%license LICENCE

%files devel -f .ofiles-devel
%doc README changelog
%license LICENCE

%changelog
%autochangelog
