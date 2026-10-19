%global source0_hash c0d1143bd9659a2996f25898912c0ba48bd0dba38c7bb4ae8ea406c257f6184e
%bcond_without mathinit
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%bcond_without	license_dir
%else
%bcond_with	license_dir
%endif
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:           arprec
Version:        2.2.20
Release:        1%{?dist}
Summary:        Software package for performing arbitrary precision arithmetic
License:        LicenseRef-Callaway-BSD
URL:            http://crd.lbl.gov/~dhbailey/mpdist
Source0:        http://crd.lbl.gov/~dhbailey/mpdist/%{name}-%{version}.tar.gz
Source1:        %{url}/BSD-LBNL-License.doc
Patch0:         arprec-2.2.19-fix_istream_logic.patch
# oreon:deps
BuildRequires:  catdoc
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  qd-devel
# /oreon:deps
%description
ARPREC is a software package for performing arbitrary precision
arithmetic.  It consists of a revision and extension of Bailey's
earlier MPFUN package, enhanced with special IEEE numerical
techniques.  Features include:

  * Written in C++ for broad portability and fast execution.

  * Includes C++ and Fortran 90/95 interfaces based on custom data-types
    and operator/function overloading, which permit the library to be
    used with only minor modifications for many conventional C++ and
    Fortran-90 programs.

  * Includes all of the usual arithmetic operations, as well as many
    transcendental functions, including cos, sin, tan, arccos, arcsin,
    arctan, exp, log, log10, erf, gamma and Bessel functions.

  * Supports three arbitrary precision data-types: mp_real, mp_int
    and mp_complex.

  * Supports many mixed-mode operations between arbitrary precision
    variables or constants and conventional variables or constants.

  * Includes special library routines, incorporating advanced
    algorithms for extra-high precision (above 1000 digits) computation.

  * Includes a number of sample application programs, including programs
    for quadrature (numerical definite integrals), PLSQ (integer relation
    finding) and polynomial root finding.

  * Includes the "Experimental Mathematician's Toolkit".  This is a
    self-contained interactive program that performs many operations
    typical of modern experimental mathematics, including arithmetic
    expressions, common transcendental functions, infinite series
    evaluation, definite integrals, polynomial roots, user-defined
    functions, all evaluated to a user-defined level of numeric
    precision, up to 1000 decimal digits.

%package data
Summary:        Data files for %{name}-tools
BuildArch:      noarch
%description data
This package contains data-files used with %{name}-tools.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development files and headers for %{name}.

%package doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description doc
This package contains the documentation and some brief examples.

%package tools
Summary:        Interactive high-precision arithmetic computing environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-data    = %{version}-%{release}
%description tools
This is a complete interactive high-precision arithmetic computing
environment.  One enters expressions in a Mathematica-style syntax,
and the operations are performed using the ARPREC package, with a
level of precision that can be set from 100 to 1000 decimal digit
accuracy.  Variables and vector arrays can be defined and referenced.
This program supports all basic arithmetic operations, common
transcendental and combinatorial functions, multi-pair PSLQ (one-,
two- or three-level versions), high-precision quadrature, i.e. numeric
integration (Gaussian, error function or tanh-sinh), and summation of
series.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -cp 1

pushd %{name}

# Pull-in upstream's .doc-license.
%{__cp} -a %{SOURCE1} .

# Create an user-friendly ascii-text from original .doc-license.
%{_bindir}/catdoc -d utf-8 %{SOURCE1} | \
  %{__sed} -e 's!\f!!g' > BSD-LBNL-License.txt && \
  /bin/touch -r %{SOURCE1} BSD-LBNL-License.txt

# Remove some unneeded and obsoleted files.
%{_bindir}/find . -depth -name '._*' -print0 | %{_bindir}/xargs -0 %{__rm} -rf
%{_bindir}/find . -depth -name '.[dD][sS]_[sS]tore' -print0 | \
  %{_bindir}/xargs -0 %{__rm} -rf

# The testsuite is a good example for using this lib.  So let's store it's
# files in another location before they get cluttered with intermediate stuff.
%{__cp} -a tests examples
%{__rm} -rf examples/Makefile*

# Get all pre-build quads-data from mathinit.
%{__sed} -i -e 's!nquadopt = 1!nquadopt = 3!g' toolkit/mathinit.f

# Use the pre-build data-files in mathtool.
%{__sed} -i -e 's!const\.dat!%{_datadir}/%{name}/&!g' \
  -e 's!quad.*\.dat!%{_datadir}/%{name}/&!g' toolkit/mathtool.f

# Make arprec-config multilib-friendly.  Substitute original script
# with a wrapper-script for pkg-config.
%{__cat} << EOS > arprec-config.rpmbuild
#!/bin/sh
# arprec-config.  Generated during rpmbuild.
pc=\`which pkg-config\`

usage()
{
  %{__cat} << EOF
Usage: arprec-config [OPTIONS]
Options:
    [--prefix]
    [--exec-prefix]
    [--version]
    [--libs]
    [--fc]
    [--fclibs]
    [--fcflags]
    [--fmainlib]
    [--cxx]
    [--cxxflags]
    [--configure-args]
EOF
  exit $1
}

while test \$# -gt 0; do
  case "\$1" in
  -*=*) optarg=\`echo "\$1" | sed 's/[-_a-zA-Z0-9]*=//'\` ;;
  *) optarg= ;;
  esac

  case \$1 in
    --prefix)
      \$pc --variable=prefix %{name}
      ;;
    --exec-prefix)
      \$pc --variable=exec_prefix %{name}
      ;;
    --version)
      \$pc --modversion %{name}
      ;;
    --libs)
      \$pc --libs %{name}
      ;;
    --cxx)
      \$pc --variable=cxx %{name}
      ;;
    --configure-args)
      \$pc --variable=configure_args %{name}
      ;;
    --fclibs)
      \$pc --variable=fclibs %{name}
      ;;
    --fcflags)
      \$pc --variable=fcflags %{name}
      ;;
    --fmainlib)
      \$pc --variable=fmainlib %{name}
      ;;
    --cxxflags)
      \$pc --variable=cxxflags %{name}
      ;;
    --fc)
      \$pc --variable=fc %{name}
      ;;
    *)
      usage 1 1>&2
      ;;
  esac
  shift
done
EOS

# Create a template for pkg-config.  This will be used by the modified
# arprec-config as well.
%{__cat} << EOF > %{name}.pc
############################
# Pkg-Config file for @name@
############################

prefix=@prefix@
exec_prefix=\${prefix}

bindir=@bindir@
datarootdir=@datadir@
datadir=\${datarootdir}/@name@
includedir=@includedir@
libdir=@libdir@
mandir=@mandir@
sharedstatedir=@sharedstatedir@
sysconfdir=@sysconfdir@

configure_args=@configure_args@
cxx=@cxx@
cxxflags=@cxxflags@
fc=@fc@
fcflags=-I${includedir}/@name@ @fcflags@
fclibs=@fclibs@
fmainlib=@fmainlib@

Name:           @name@
Version:        @version@
Description:    @name@ - @summary@

Libs:           @libs@
Cflags:         -I\${includedir}
EOF

popd

%build

pushd %{name}
%{_bindir}/autoupdate
%{_bindir}/autoreconf -fiv
%configure \
  --disable-static \
  --enable-qd \
  --enable-shared
%make_build
make toolkit
%{__chmod} +x %{name}-config
%{__sed} -i -e 's!@prefix@!%{_prefix}!g' \
  -e 's!@bindir@!%{_bindir}!g' \
  -e 's!@datadir@!%{_datadir}!g' \
  -e 's!@name@!%{name}!g' \
  -e 's!@includedir@!%{_includedir}!g' \
  -e 's!@libdir@!%{_libdir}!g' \
  -e 's!@mandir@!%{_mandir}!g' \
  -e 's!@sharedstatedir@!%{_sharedstatedir}!g' \
  -e 's!@sysconfdir@!%{_sysconfdir}!g' \
  -e 's!@version@!%{version}!g' \
  -e 's!@summary@!Software package for performing arbitrary precision arithmetic!g' \
  -e "s~@libs@~$(./%{name}-config --libs)~g" \
  -e "s~@configure_args@~$(./%{name}-config --configure-args)~g" \
  -e "s~@cxx@~$(./%{name}-config --cxx)~g" \
  -e "s~@cxxflags@~$(./%{name}-config --cxxflags)~g" \
  -e "s~@fc@~$(./%{name}-config --fc)~g" \
  -e "s~@fcflags@~$(./%{name}-config --fcflags)~g" \
  -e "s~@fclibs@~$(./%{name}-config --fclibs)~g" \
  -e "s~@fmainlib@~$(./%{name}-config --fmainlib)~g" \
  %{name}.pc
%{__chmod} -x %{name}-config
pushd toolkit
%if %{with mathinit}
./mathinit
%else
/bin/touch const.dat quadgs.dat quaderf.dat quadts.dat
%endif
popd
popd
%install
pushd %{name}
%make_install
%{__rm} -rf %{buildroot}%{_bindir}/%{name}-config \
  %{buildroot}%{_datadir}/* %{buildroot}%{_libdir}/*.la
%{__mkdir} -p %{buildroot}%{_datadir}/%{name} %{buildroot}%{_libdir}/pkgconfig
for tool in toolkit/.libs/math*
do
  %{__install} -pm 0755 ${tool} \
    %{buildroot}%{_bindir}/%{name}-`basename ${tool}`
done
%{__install} -pm 0755 %{name}-config.rpmbuild %{buildroot}%{_bindir}/%{name}-config
%{__install} -pm 0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig
%{__install} -pm 0644 toolkit/*.dat %{buildroot}%{_datadir}/%{name}
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/%{name}-math*
%{__mkdir} -p %{buildroot}%{_pkgdocdir}/{examples,toolkit}
%{__install} -pm 0644 AUTHORS* BSD-LBNL-License* ChangeLog* \
  COPYING* NEWS* README* doc/* \
  %{buildroot}%{_pkgdocdir}
%{__install} -pm 0644 examples/* %{buildroot}%{_pkgdocdir}/examples
%{__install} -pm 0644 toolkit/README* %{buildroot}%{_pkgdocdir}/toolkit
%if %{with license}
%{__rm} -rf BSD-LBNL-License* COPYING*
%endif
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build -C %{name} check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
