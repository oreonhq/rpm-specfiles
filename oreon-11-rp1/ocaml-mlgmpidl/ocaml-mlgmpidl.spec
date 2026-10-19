%global source0_hash 51a25f51068b1439ae71469ae506b1637d4e6f782a00955317bdff0f41ec49f8
ExcludeArch: %{ix86}
Name:           ocaml-mlgmpidl
Version:        1.3.0
Release:        1%{?dist}
Summary:        OCaml interface to GMP and MPFR libraries
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/nberth/mlgmpidl
VCS:            git:%{url}.git
Source0:        https://github.com/nberth/mlgmpidl/archive/%{version}/mlgmpidl-%{version}.tar.gz
Source1:        mlgmpidl_test.ml
Source2:        mlgmpidl_test_result
Patch:          %{name}-bigarray-compat.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  perl-interpreter
BuildRequires:  tex(ecrm1000.tfm)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(latex)
# /oreon:deps
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

./configure \
%ifnarch %{ocaml_native_compiler}
  -no-native-plugins \
%endif
  -disable-profiling \
  -prefix %{ocamldir}
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
unset MAKEFLAGS
export MLGMPIDL_PREFIX=$RPM_BUILD_ROOT%{_prefix}
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
%ifarch %{ocaml_native_compiler}
%make_install
%else
%make_install HAS_OCAMLOPT=
%endif
cp -p opam/opam $RPM_BUILD_ROOT%{ocamldir}/gmp
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-mlgmpidl-devel -f %{oreon_filedir}/ocaml-mlgmpidl-devel.list
%files -n ocaml-mlgmpidl-doc -f %{oreon_filedir}/ocaml-mlgmpidl-doc.list

%changelog

%autochangelog
