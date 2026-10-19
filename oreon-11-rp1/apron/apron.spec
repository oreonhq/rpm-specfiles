%global source0_hash 5778fa1afaf0b36fe6a79989fc4374b0b3ece8a5e46a7ab195440209ccd67b1b
%global giturl  https://github.com/antoinemine/apron
Name:           apron
Version:        0.9.15
Summary:        Numerical abstract domain library
Release:        1%{?dist}
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://antoinemine.github.io/Apron/doc/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-weak.patch
Patch1:         %{name}-ocaml-bytecode.patch
Patch2:         %{name}-csdp.patch
Patch3:         %{name}-japron-link.patch
Patch4:         %{name}-hasvar.patch
Patch5:         %{name}-flint.patch
Patch6:         %{name}-ocaml-gc.patch
ExcludeArch:    %{ix86}
%ifarch %{java_arches}
%endif
%global sover %(cut -d. -f 1 <<< %{version})
%global __ocaml_requires_opts -i Coeff -i Dim -i Interval -i Lincons0 -i Linexpr0 -i Scalar -i Tcons0 -i Texpr0
# oreon:deps
BuildRequires:  csdp-devel
BuildRequires:  doxygen-latex
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glpk-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-mlgmpidl-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  perl-interpreter
BuildRequires:  ppl-devel
BuildRequires:  pplite-devel
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(etoc.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(listofitems.sty)
BuildRequires:  tex(newunicodechar.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  texinfo-tex
# /oreon:deps
%description
The APRON library is dedicated to the static analysis of the numerical
variables of a program by Abstract Interpretation.  The aim of such an
analysis is to infer invariants about these variables, like 1<=x+y<=z, which
holds during any execution of the program.

The APRON library is intended to be a common interface to various underlying
libraries/abstract domains and to provide additional services that can be
implemented independently from the underlying library/abstract domain.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glpk-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Provides:       bundled(js-jquery)
%description    devel
The %{name}-devel package contains libraries and signature files for developing
applications that use %{name}.

%package -n     ocaml-%{name}
Summary:        Ocaml interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n ocaml-%{name}
Ocaml interface to the APRON library.

%package -n     ocaml-%{name}-devel
Summary:        Development files for the Ocaml interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description -n ocaml-%{name}-devel
Development files for the Ocaml interface to the APRON library.

%ifarch %{java_arches}
%package -n     japron
Summary:        Java interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       javapackages-filesystem
%description -n japron
Java interface to the APRON library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n %{name}-%{version}
%patch -P0 -p0
%ifnarch %{ocaml_native_compiler}
%patch -P1 -p0
%endif
%autopatch -m2 -p0

%conf
# Fix library path for 64-bit installs
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's,\${apron_prefix}/lib,&64,' configure
  sed -i 's,/lib,&64,' vars.mk
fi

# Fix encodings
iconv -f iso8859-1 -t utf-8 Changes > Changes.utf8
touch -r Changes Changes.utf8
mv -f Changes.utf8 Changes

# Preserve timestamps when copying
sed -i 's/^\([[:blank:]]*cp[[:blank:]]\)/\1-p /' Makefile */Makefile

# Build with debuginfo
sed -i 's/^OCAMLOPTFLAGS =/& -g/' configure
sed -i 's|\$(OCAMLMKLIB) -L.*|& -g|' vars.mk

# Give the C++ library an soname
sed -i '/shared/s/\$(CXX)/$(CXX_APRON_DYLIB)/' apronxx/Makefile

# For reproducibility, omit timestamps from generated documentation
sed -i '/HTML_TIMESTAMP/s/= YES/= NO/' apronxx/doc/Doxyfile

%build

export CPPFLAGS='-D_GNU_SOURCE -I%{_includedir}/csdp'
export CFLAGS='%{build_cflags} -fsigned-char'
export CXXFLAGS='%{build_cxxflags} -fsigned-char'
export CSDP_PATH=%{_prefix}
%ifarch %{java_arches}
export JAVA_HOME='%{_jvmdir}/java'
export JAVA_TOOL_OPTIONS='-Dfile.encoding=UTF8'
./configure -prefix %{_prefix} -pplite-prefix %{_prefix} -no-strip -java-prefix %{_jvmdir}/java
%else
./configure -prefix %{_prefix} -pplite-prefix %{_prefix} -no-strip
%endif
sed -i 's/-Wall/& -Werror=format-security/' Makefile.config
touch apron/depend
make -C apron depend
make
make doc
make -C mlapronidl mlapronidl.pdf
%install
sed -i 's, install ,&-destdir %{buildroot}%{ocamldir} -ldconf ignore ,' \
    Makefile
mkdir -p %{buildroot}%{ocamldir}/stublibs
mkdir -p %{buildroot}%{_jnidir}
%ifarch %{java_arches}
make install INSTALL="install -p" APRON_PREFIX=%{buildroot}%{_prefix} \
  JAVA_PREFIX=%{buildroot}%{_jnidir}
mv %{buildroot}%{_libdir}/libj*.so %{buildroot}%{_jnidir}
%else
make install INSTALL="install -p" APRON_PREFIX=%{buildroot}%{_prefix}
%endif
rm -fr %{buildroot}%{_bindir}
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/apronxx \
   %{buildroot}%{_includedir}/oct %{buildroot}%{_includedir}/%{name}
find %{buildroot}%{_includedir} \( -name \*.h -o -name \*.hh \) \
     -perm /0111 -execdir chmod a-x {} +
rm -f %{buildroot}%{_libdir}/*.a
pushd %{buildroot}%{_libdir}
for f in lib*.so; do
  mv $f $f.%{version}
  ln -s $f.%{sover} $f
  ln -s $f.%{version} $f.%{sover}
done
popd
mkdir doc
mv apron/html doc/apron
mv apronxx/doc/html doc/apronxx
%oreon_autofiles apron-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ocaml-apron usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-apron-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make -C test APRON_INCLUDE=%{buildroot}%{_includedir}/%{name} \
  APRON_LIB=%{buildroot}%{ocamldir}/%{name} \
  CAMLIDL_PREFIX=%{buildroot}%{_libdir}
test/ctest1
%files -f %{oreon_filedir}/main.list
%files -n apron-devel -f %{oreon_filedir}/apron-devel.list
%files -n ocaml-apron -f %{oreon_filedir}/ocaml-apron.list
%files -n ocaml-apron-devel -f %{oreon_filedir}/ocaml-apron-devel.list

%changelog

%autochangelog
