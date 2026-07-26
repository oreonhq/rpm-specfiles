%global source0_hash fd0d824fd94bef3aae55b95e5ef19342b653fe3ff4fb561364e942c809eb616b

%global upstreamver 2-5-4

Name:           cxsc
Version:        %(tr - . <<< %{upstreamver})
Release:        33%{?dist}
Summary:        C++ library for Extended Scientific Computing

%global majver  %(cut -d. -f1 <<< %{version})

License:        LGPL-2.0-or-later
URL:            https://www2.math.uni-wuppertal.de/wrswt/xsc/cxsc_new.html
Source:         https://www2.math.uni-wuppertal.de/wrswt/xsc/%{name}/%{name}-%{upstreamver}.tar.gz
# Sent upstream 22 Jun 2016.  Fix an operator error.
Patch:          %{name}-operator.patch
# Sent upstream 22 Jun 2016.  Fix build problem on ppc64.
Patch:          %{name}-ppc64.patch
# Fix endianness detection
Patch:          %{name}-endian.patch
# Fix a sequence point error
Patch:          %{name}-seq.patch
# Fix a mistaken euro symbol which leads to LaTeX errors
Patch:          %{name}-euro.patch
# Fix access to an uninitialized variable
Patch:          %{name}-uninit.patch
# Do not allocate arrays with negative size
Patch:          %{name}-neg-alloc.patch
# Remove template IDs from constructors
Patch:          %{name}-template-id.patch
# Disambiguate the name "complex"
Patch:          %{name}-complex.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)

%description
C-XSC is the C language variant of the XSC (eXtensions for Scientific
Computing) project.  It provides routines that guarantee accuracy and
reliability of results.  Problem-solving routines with automatic result
verification have been developed for many standard problems of numerical
analysis, such as linear or nonlinear systems of equations, differential and
integral equations, etc. as well as for a large number of applications in
engineering and the natural sciences.  Some of the features of C-XSC are:
- Operator concept (user-defined operators)
- Overloading concept
- Module concept
- Dynamic arrays
- Controlled rounding
- Predefined arithmetic data types real, extended real, complex, interval,
  complex interval, and corresponding vector and matrix types
- Predefined arithmetic operators and elementary functions of the highest
  accuracy for the arithmetic data types
- Data type dotprecision for the exact representation of dot products
- Library of mathematical problem-solving routines with automatic result
  verification and high accuracy

%package devel
Summary:        Header files for developing applications that use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and library links for developing applications that use %{name}.

%package doc
# The project as a whole is LGPL-2.0-or-later.
# Doxygen adds files with other licenses.
# GPL-1.0-or-later: bc_s.png, bc_sd.png, bdwn.png, closed.png, doc.png,
#   docd.png, doxygen.css, doxygen.svg, folderclosed.png, folderopen.png,
#   nav_f.png, nav_fd.png, nav_g.png, nav_h.png, nav_hd.png, navtree.css,
#   open.png, splitbar.png, splitbard.png, sync_off.png, sync_on.png, tab_a.png,
#   tab_ad.png, tab_b.png, tab_bd.png, tab_h.png, tab_hd.png, tab_s.png,
#   tab_sd.png, tabs.css
# MIT: dynsections.js, jquery.js, menu.js, menudata.js, navtree.js, resize.js
License:        LGPL-2.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        API documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(js-jquery)

%description doc
API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{upstreamver}

%conf
# Don't set rpath
sed -i 's/\(RPATH[[:blank:]]*=\).*/\1/;' Makefile.in CToolbox/Makefile
sed -i '/LINKERPATH=-Wl,-R/d' install_cxsc

# Don't build with SSE2 support on platforms the script doesn't recognize
%ifnarch %{x86_64}
sed -i 's/ -mfpmath=sse -msse2//' install_cxsc.in
%endif

# Link with the BLAS and OpenMP libraries
sed -i 's/\$(RARI)/& -lflexiblas -lgomp/' src/Makefile
sed -i 's/(LIBS)/& -lflexiblas/' CToolbox/Makefile

# Install in the right place on 64-bit systems
if [ %{_libdir} != "%{_prefix}/lib" ]; then
  sed -e 's|\$(PREFIX)/lib$|$(PREFIX)/%{_lib}|' \
      -e 's|\$(PREFIX)/lib;|$(PREFIX)/%{_lib};|' \
      -i src/Makefile
fi

# Use an efficient representation for a_btyp on 64-bit systems
%if 0%{?__isa_bits} == 64
sed -ri 's/(#define SHORTABTYP) .*/\1 1/' src/rts/o_spec.h
sed -i 's/#if DEC_ALPHA_C+GNU_X86_64+CXSC_PPC64/#if 1/' src/rts/p88rts.h
%else
sed -ri 's/(#define SHORTABTYP) .*/\1 0/' src/rts/o_spec.h
sed -i 's/#if DEC_ALPHA_C+GNU_X86_64+CXSC_PPC64/#if 0/' src/rts/p88rts.h
%endif

# Remove spurious executable bits
chmod a-x src/fi_lib/*.{cpp,hpp}

# Remove throw() specifications for C++17 compatibility
for fil in $(find src -type f); do
  sed -e 's/\([[:blank:]]\)throw[[:blank:]]*([[:blank:]]*)/\1noexcept/g' \
      -e 's/^throw[[:blank:]]*([[:blank:]]*)/noexcept/g' \
      -e 's/[[:blank:]]throw[[:blank:]]*([^)]*)//g' \
      -e 's/^throw[[:blank:]]*([^)]*)//g' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
# FIXME: tests fail without -fno-inline.  Why?
%if 0%{?__isa_bits} == 64
use64=-DIS_64_BIT
%else
use64=
%endif
printf "yes\n\
gnu\n\
no\n\
yes\n\
%ifarch %{x86_64}
%{build_cxxflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA -DIS_64_BIT -fopenmp %{build_ldflags}\n\
64\n\
asm\n\
%elifarch %{power64}
%{build_cxxflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA -DIS_64_BIT -fopenmp %{build_ldflags}\n\
asm\n\
%else
%{build_cxxflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA $use64 -fopenmp -frounding-math -fno-inline %{build_ldflags}\n\
hard\n\
safe\n\
%endif
%{buildroot}%{_prefix}\n\
dynamic\n\
no\n" | ./install_cxsc

# The individual targets can be built in parallel, but specifying more than one
# to the same make invocation leads to build failures.
%make_build cxsc
%make_build libcxsc.so
mkdir usr
ln -s ../src usr/lib
ln -s lib%{name}.so.%{version} src/lib%{name}.so.%{majver}
ln -s lib%{name}.so.%{majver} src/lib%{name}.so
export LD_LIBRARY_PATH=$PWD/usr/lib
%make_build toolbox_dyn CXSCDIR=$PWD/usr

# Make the documentation
cd src
doxygen src-doxyfile

%install
make install_dyn PREFIX=%{buildroot}%{_prefix}

# Fix permissions on the library
chmod 0755 %{buildroot}%{_libdir}/lib%{name}.so.%{version}

# There are a lot of header files, so hide them in a private directory
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.{h,hpp,inl} %{buildroot}%{_includedir}/%{name}

# Don't package the example binaries
rm -fr %{buildroot}/%{_prefix}/examples

%check
sed -i 's/ASM$/ASM LD_LIBRARY_PATH/' Makefile
sed -i 's/export RPATH/export LD_LIBRARY_PATH/' CToolbox/Makefile
if [ %{_libdir} != "%{_prefix}/lib" ]; then
  sed -i 's|/lib|/%{_lib}|' CToolbox/Makefile
fi
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make toolboxtest_dyn

%files
%doc changelog README
%license docu/COPYING
%{_libdir}/lib%{name}.so.2{,.*}

%files devel
%doc examples
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files doc
%doc docu/apidoc

%changelog
%autochangelog
