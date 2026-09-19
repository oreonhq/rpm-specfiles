%global source0_hash c82bfd106208ebedd8c264300e939010f87eed83e6f6339e3a6cf8f66caeed54

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-camlidl
Version:        1.13
Release:        4%{?dist}
Summary:        Stub code generator and COM binding for Objective Caml
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

%global shortversion %(tr -d . <<< %{version})
%global giturl  https://github.com/xavierleroy/camlidl

URL:            https://xavierleroy.org/camlidl/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/camlidl%{shortversion}.tar.gz

# Patch sent upstream on 2020-05-20.
# Pass -g option to ocamlmklib.
Patch:          0001-Pass-g-option-to-ocamlmklib.patch

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros

%description
CamlIDL is a stub code generator and COM binding for Objective Caml.

CamlIDL comprises two parts:

* A stub code generator that generates the C stub code required for
  the Caml/C interface, based on an MIDL specification. (MIDL stands
  for Microsoft's Interface Description Language; it looks like C
  header files with some extra annotations, plus a notion of object
  interfaces that look like C++ classes without inheritance.)

* A (currently small) library of functions and tools to import COM
  components in Caml applications, and export Caml code as COM
  components.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n camlidl-camlidl%{shortversion} -p1

%conf
sed -e 's|^OCAMLLIB=.*|OCAMLLIB=%{_libdir}/ocaml|' \
    -e 's|^BINDIR=.*|BINDIR=%{buildroot}%{_bindir}|' \
    -e 's|^CFLAGS=.*|CFLAGS=%{build_cflags}|' \
%ifarch %{ocaml_native_compiler}
    -e 's|^OCAMLC=.*|OCAMLC=ocamlc.opt -g|' \
    -e 's|^OCAMLOPT=.*|OCAMLOPT=ocamlopt.opt -g|' \
%endif
    < config/Makefile.unix \
    > config/Makefile

# Remove files we do not want to package with the tests
find . \( -name .cvsignore -o -name .gitignore \) -delete

# Preserve timestamps
sed -i 's/cp/cp -p/' runtime/Makefile.unix

%build
# Parallel builds will fail.
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml/caml
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml/stublibs
mkdir -p $RPM_BUILD_ROOT/%{_bindir}

%make_install
%ocaml_files

%files -f .ofiles
%license LICENSE

%files devel -f .ofiles-devel
%doc README Changes docs tests
%license LICENSE

%changelog
%autochangelog
