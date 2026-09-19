%global source0_hash 969b04c35b470556298e20ab46deb99968b997d09b71f477b8844ca85712c4ff

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-mlgmpidl
Version:        1.3.0
Release:        18%{?dist}
Summary:        OCaml interface to GMP and MPFR libraries
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception

URL:            https://github.com/nberth/mlgmpidl
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/mlgmpidl-%{version}.tar.gz
Source1:        mlgmpidl_test.ml
Source2:        mlgmpidl_test_result
# Remove dependency on the bigarray-compat forward compatibility shim
Patch:          %{name}-bigarray-compat.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  perl-interpreter
# BuildRequires for documentation build
BuildRequires:  tex(latex)
BuildRequires:  tex(ecrm1000.tfm)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  ghostscript-tools-dvipdf

%description
MLGMPIDL is an OCaml interface to the GMP and MPFR rational and real number
math libraries.  Although there is another such interface, this one is
different in that it provides a more imperative (rather than functional)
interface to conserve memory and that this one uses CAMLIDL to take care of
the C/OCaml interface in a convenient and modular way.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camlidl-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mlgmpidl-%{version} -p1

%conf
cp -p %{SOURCE1} %{SOURCE2} .

# Fix install on 64-bit platforms
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,/lib,%{_lib},g' Makefile
fi

# Build with debug information
sed -i 's/^OCAMLOPTFLAGS = -annot/& -g/' configure Makefile.config.in
sed -i 's/\$(OCAMLMKLIB)/& -g/' Makefile

%ifnarch %{ocaml_native_compiler}
# Fix build on bytecode-only architectures
sed -i 's/ocamlc\.opt/ocamlc/g;/ocamlopt\.opt/s/.*/ocamlopt=""/' configure
sed -i '/addprefix/s/OCAMLOPT/OCAMLC/g' Makefile
%endif

%build
# This is not an autoconf-generated script.  Do NOT use %%configure.
./configure \
%ifnarch %{ocaml_native_compiler}
  -no-native-plugins \
%endif
  -disable-profiling \
  -prefix %{ocamldir}

# Upstream Makefile is NOT safe to be called in parallel.
%ifarch %{ocaml_native_compiler}
make all
%else
make byte
%endif
make mlgmpidl.pdf
make html

%check
%ifarch %{ocaml_native_compiler}
ocamlopt -runtime-variant _pic -ccopt -L. -cclib -lgmp gmp.cmxa mlgmpidl_test.ml
%else
ocamlc -ccopt -L. -cclib -lgmp gmp.cma mlgmpidl_test.ml
export LD_LIBRARY_PATH=$PWD
%endif
./a.out > mlgmpidl_test_myresult
diff -u mlgmpidl_test_myresult mlgmpidl_test_result

%install
# Upstream Makefile is NOT safe to be called in parallel.
unset MAKEFLAGS

# Library uses ocamlfind install to install itself.  Set up environment
# so that it works.
export MLGMPIDL_PREFIX=$RPM_BUILD_ROOT%{_prefix}
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

%ifarch %{ocaml_native_compiler}
%make_install
%else
%make_install HAS_OCAMLOPT=
%endif

# Install the opam file
cp -p opam/opam $RPM_BUILD_ROOT%{ocamldir}/gmp

%ocaml_files

%files -f .ofiles
%doc README
%license COPYING

%files devel -f .ofiles-devel

%files doc
%doc README html mlgmpidl.pdf
%license COPYING

%changelog
%autochangelog
