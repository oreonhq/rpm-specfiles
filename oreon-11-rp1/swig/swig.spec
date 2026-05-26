# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 40162a706c56f7592d08fd52ef5511cb7ac191f3593cf07306a0a554c6281fcf
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# We can skip tests
%bcond_without testsuite

%if %{without testsuite}
%global tcl 0
%global guile 0
%global lualang 0
%global perllang 0
%global phplang 0
%global rubylang 0
%global python3lang 0
%global golang 0
%global octave 0
%global Rlang 0
%global javalang 0
%global ocamllang 0
%endif

%{!?tcl:%global tcl 1}
%{!?lualang:%global lualang 1}
%{!?perllang:%global perllang 1}
%{!?rubylang:%global rubylang 1}
%{!?python3lang:%global python3lang 1}

# PHP drop support for 32-bit builds since Fedora 41.
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11
%ifarch %{ix86}
%global phplang 0
%endif
%endif
%{!?phplang:%global phplang 1}

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
%ifarch %{ix86}
%{!?ocamllang:%global ocamllang 0}
%else
%{!?ocamllang:%global ocamllang 1}
%endif

%if 0%{?rhel}
%{!?golang:%global golang 0}
%{!?guile:%global guile 0}
%{!?octave:%global octave 0}
%{!?Rlang:%global Rlang 0}
%bcond_with build_ccache_swig
%else
%{!?guile:%global guile 1}
%{!?octave:%global octave 1}
# R-core requires tcl < 9.0.0
%{!?Rlang:%global Rlang 0}
%bcond_without build_ccache_swig
%endif

%ifarch %{ix86}
%{!?javalang:%global javalang 0}
%else
# Temporary disable java tests, because they doesn't pass with java-21-openjdk
# https://github.com/swig/swig/issues/2767
%{!?javalang:%global javalang 1}
%endif

# Do not run Go tests, they failed with 4.0.0 on ppc64le, s390
%ifarch x86_64 %{arm} aarch64
%{!?golang:%global golang 1}
%else
%{!?golang:%global golang 0}
%endif

Summary: Connects C/C++/Objective C to some high-level programming languages
Name:    swig
Version: 4.4.1
Release: 5%{?dist}
License: GPL-3.0-or-later AND BSD-3-Clause
URL:     https://www.swig.org/
Source0: http://downloads.sourceforge.net/project/swig/swig/swig-%{version}/swig-%{version}.tar.gz
# Define the part of man page sections
Source1: description.h2m
%if %{with build_ccache_swig}
Source2: description-ccache.h2m
Source3: ccache-swig.sh
Source4: ccache-swig.csh
%endif

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-interpreter, pcre2-devel
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: autoconf, automake, gawk, dos2unix
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: sed
BuildRequires: perl-devel
BuildRequires: perl(base)
BuildRequires: perl(Config)
BuildRequires: perl(Devel::Peek)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(fields)
BuildRequires: perl(Math::BigInt)
BuildRequires: perl(strict)
BuildRequires: perl(Test::More)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
BuildRequires: boost-devel
# Need when Source/CParse/parser.y is patched
BuildRequires: bison
%if %{tcl}
BuildRequires: tcl-devel >= 9.0.0
%endif
%if %{guile}
BuildRequires: guile-devel
%endif
%if %{octave}
BuildRequires: octave-devel
%endif
%if %{golang}
BuildRequires: golang
BuildRequires: golang-bin
%ifnarch s390x
BuildRequires: golang-shared
%endif
BuildRequires: golang-src
%endif
%if %{lualang}
BuildRequires: lua-devel
%endif
%if %{rubylang}
BuildRequires: ruby-devel
%endif
%if %{Rlang}
BuildRequires: R-devel
%endif
%if %{javalang}
BuildRequires: java, java-devel
%endif
%if %{phplang}
BuildRequires: php, php-devel
%endif
%if %{ocamllang}
BuildRequires: ocaml
BuildRequires: ocaml-findlib
%endif

%description
Simplified Wrapper and Interface Generator (SWIG) is a software
development tool for connecting C, C++ and Objective C programs with a
variety of high-level programming languages. SWIG is used with different
types of target languages including common scripting languages such as
Javascript, Perl, PHP, Python, Tcl and Ruby. The list of supported
languages also includes non-scripting languages such as C#, D, Go language,
Java including Android, Lua, OCaml, Octave, Scilab and R. Also several
interpreted and compiled Scheme implementations (Guile, MzScheme/Racket)
are supported. SWIG is most commonly used to create high-level interpreted
or compiled programming environments, user interfaces, and as a tool for
testing and prototyping C/C++ software.

%if %{with build_ccache_swig}
%package -n ccache-swig
Summary:   Fast compiler cache
License:   GPL-2.0-or-later
Requires:  swig
Conflicts: swig < 3.0.8-2

%description -n ccache-swig
ccache-swig is a compiler cache. It speeds up re-compilation of C/C++/SWIG
code by caching previous compiles and detecting when the same compile is
being done again. ccache-swig is ccache plus support for SWIG.
%endif

%package doc
Summary:   Documentation files for SWIG
License:   BSD-3-Clause
BuildArch: noarch

%description doc
This package contains documentation for SWIG and useful examples

%package gdb
Summary:   Commands for easier debugging of SWIG
License:   BSD-3-Clause
Requires:  swig

%description gdb
This package contains file with commands for easier debugging of SWIG
in gdb.

%if %{python3lang}
%package -n python%{python3_pkgversion}-swig
Summary:   Python package metadata for SWIG
Requires:  swig = %{version}-%{release}
BuildArch: noarch

%description -n python%{python3_pkgversion}-swig
This package registers swig as installed for Python with pip for the
purpose of using "swig" in build-system.requires of a pyproject.toml file.
%endif

%prep
%oreon_verify_sources
%autosetup -p1

for all in CHANGES README; do
    iconv -f ISO88591 -t UTF8 < $all > $all.new
    touch -r $all $all.new
    mv -f $all.new $all
done

%build
%if %{golang}
# Go tests are failing due to binutils changes related to linker setting as
# documented at https://bugzilla.redhat.com/show_bug.cgi?id=2428281
# Use workaround decribed in the bugzilla.
export LDFLAGS="$LDFLAGS -Wl,-z,notext"
%endif

./autogen.sh

# Disable maximum compile warnings when octave is supported, because Octave
# code produces lots of the warnings demanded by strict ISO C and ISO C++.
# It causes that log had more then 600M.
%configure \
%if %{ocamllang}
  --with-ocaml \
%else
  --without-ocaml \
%endif
%if %{python3lang}
  --with-python3=python3 \
%else
  --without-python3 \
%endif
%if %{phplang}
  --with-php \
%else
  --without-php \
%endif
%if ! %{perllang}
  --without-perl5 \
%endif
%if ! %{tcl}
  --without-tcl \
%endif
%if ! %{javalang}
  --without-java \
%endif
%if ! %{Rlang}
  --without-r \
%endif
%if ! %{golang}
  --without-go \
%endif
%if ! %{guile}
  --without-guile \
%endif
%if %{octave}
  --with-octave=%{_bindir}/octave \
  --without-maximum-compile-warnings \
%endif
%if %{without build_ccache_swig}
  --disable-ccache \
%endif
;
%{make_build}

%if %{with testsuite}
# Test suite
make check PY3=1
%endif

%install
# Remove all arch dependent files in Examples/ created during tests
make clean-examples

pushd Examples/
# Remove all arch dependent files in Examples/
find -type f -name 'Makefile.in' -delete -print

# We don't want to ship files below.
rm -rf test-suite
find -type f -name '*.dsp' -delete -print
find -type f -name '*.dsw' -delete -print

# Convert files to UNIX format
for all in `find -type f`; do
    dos2unix -k $all
    chmod -x $all
done
popd

%{make_install}

#################################################
# Use help output for generating of man page swig
echo "Options:" >help_swig
%{buildroot}%{_bindir}/swig --help >>help_swig

# Update the output to be correctly formatted be help2man
sed -i -e 's/^\(\s\+-[^-]\+\)- \(.*\)$/\1 \2/' help_swig
sed -i -e 's/^\(\s\+-\w\+-[^-]*\)- \(.*\)$/\1 \2/' help_swig

# Generate a helper script that will be used by help2man
cat >h2m_helper_swig <<'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "" || cat help_swig
EOF
chmod a+x h2m_helper_swig

# Generate man page
help2man -N --section 1 ./h2m_helper_swig --include %{SOURCE1} -o %{name}.1

%if %{with build_ccache_swig}
########################################################
# Use help output for generating of man page ccache-swig
%{buildroot}%{_bindir}/ccache-swig -h >>help_ccache

# Update the output to be correctly formatted be help2man
sed -i -e '/compiler cache/ d' help_ccache
sed -i -e '/Copyright/ d' help_ccache
sed -i -e 's/^Usage:/[synopsis]/' help_ccache
sed -i -e 's/^Options:/[options]/' help_ccache
sed -i -e 's/^\s\+/ /' help_ccache
sed -i -e 's/^\(-[^- ] <\w\+>\s\+\) \(\w.\+\)$/ \1 \2/' help_ccache
sed -i -e 's/^\(-[^- ]\s\+\) \(\w.\+\)$/ \1 \2/' help_ccache

# Generate a helper script that will be used by help2man
cat >h2m_helper_ccache <<'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo ""
[ "$1" == "--help" ] && echo "" || echo ""
EOF
chmod a+x h2m_helper_ccache

cat %{SOURCE2} >>help_ccache
sed -i -e 's#@DOCDIR@#%{_docdir}#' help_ccache

# Generate man page
help2man -N --section 1 ./h2m_helper_ccache --include help_ccache -o ccache-swig.1
%endif

# Add man page for swig to repository
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/
%if %{with build_ccache_swig}
install -p -m 0644 ccache-swig.1 %{buildroot}%{_mandir}/man1/
%endif

# Quiet some rpmlint complaints - remove empty file
rm -f %{buildroot}%{_datadir}/%name/%{version}/octave/std_carray.i

%if %{with build_ccache_swig}
# Enable ccache-swig by default
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
install -dm 755 %{buildroot}%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d
%endif

# Add swig.gdb sub-package gdb
mkdir -p %{buildroot}%{_datadir}/%{name}/gdb
install -pm 644 Tools/swig.gdb %{buildroot}%{_datadir}/%{name}/gdb

%if %{python3lang}
# Create python package metadata
mkdir -p %{buildroot}%{python3_sitelib}/swig-%{version}.dist-info
echo "rpm" > %{buildroot}%{python3_sitelib}/swig-%{version}.dist-info/INSTALLER
cat > %{buildroot}%{python3_sitelib}/swig-%{version}.dist-info/METADATA <<_EOF
Metadata-Version: 2.1
Name: swig
Version: %{version}
_EOF
%endif


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/gdb
%{_mandir}/man1/swig.1*
%license LICENSE LICENSE-GPL LICENSE-UNIVERSITIES
%doc ANNOUNCE CHANGES CHANGES.current
%doc COPYRIGHT README TODO

%if %{with build_ccache_swig}
%files -n ccache-swig
%{_bindir}/ccache-swig
%config(noreplace) %{_sysconfdir}/profile.d/ccache-swig.*sh
%{_mandir}/man1/ccache-swig.1*
%endif

%files doc
%license LICENSE LICENSE-GPL LICENSE-UNIVERSITIES
%doc Doc Examples COPYRIGHT

%files gdb
%{_datadir}/%{name}/gdb

%if %{python3lang}
%files -n python%{python3_pkgversion}-swig
%{python3_sitelib}/swig-%{version}.dist-info/
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4.1-5
- Prepare for Oreon 11 (RP1)
