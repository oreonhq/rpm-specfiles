%global source0_hash e54afa3c192c1753bc8075c0c7e126d5c495d9066e3f90a2588091149ac9ca40

%global myname minisat

Name:           minisat2
Version:        2.2.1
Release:        23%{?dist}
Summary:        Minimalistic SAT solver

License:        MIT
URL:            http://minisat.se/
# Debian has a newer version than the latest provided by upstream
Source0:        http://ftp.debian.org/debian/pool/main/m/%{name}/%{name}_%{version}.orig.tar.gz
#Source0:        http://minisat.se/downloads/%%{myname}-%%{version}.tar.gz
# Sent sources, test, patches (below) to upstream via email on 2008-07-08:
Source1:        http://www.dwheeler.com/essays/minisat-user-guide-1.0.html
Source2:        minisat2-test.in
# Man page courtesy of Debian
Source3:        minisat.1
# Debian patch to require a nonzero memory limit
Patch0:         %{name}-memory-limit.patch
# Debian patch to fix C++ syntax (for clang, but g++ needs it now too)
Patch1:         %{name}-clang-build.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
MiniSat is a minimalistic, open-source Boolean satisfiability problem
(SAT) solver, developed to help researchers and developers alike to get
started on SAT.  Together with SatELite, MiniSat was recently awarded in
the three industrial categories and one of the "crafted" categories of
the SAT 2005 competition.

A SAT solver can determine if it is possible to find assignments to
boolean variables that would make a given expression true, if the
expression is written with only AND, OR, NOT, parentheses, and boolean
variables.  If the expression is satisfiable, MiniSAT can also produce a
set of assignments that make the expression true.  Although the problem
is NP-complete, SAT solvers (like this one) are often able to decide
this problem in a reasonable time frame.

%package libs
Summary:        Minimalistic SAT solver library

%description libs
The MiniSat library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       zlib-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix a small C++11 infelicity
for fil in minisat/utils/Options.h minisat/simp/Main.cc; do
  sed -i.orig 's/"\(PRI[[:alnum:]]*\)/" \1 /' $fil
  touch -r $fil.orig $fil
  rm -f $fil.orig
done

# Use fPIC instead of fpic ... just in case
sed -i 's/fpic/fPIC/' Makefile

cp -p %{SOURCE1} minisat-user-guide.html
cp -p %{SOURCE2} .

%build
# %%{?_smp_mflags} leads to sporadic build failures
make lsh sh prefix=%{_prefix} libdir=%{_libdir} VERB=

# Test "minisat2-test.in" is a brief quote from
# http://www.satcompetition.org/2004/format-solvers2004.html
# Exit value is 10 for satisfiable, 20 for unsatisfiable
export LD_LIBRARY_PATH=$PWD/build/dynamic/lib
build/dynamic/bin/minisat minisat2-test.in minisat2-test.out || true

%install
%make_install prefix=%{_prefix} libdir=%{_libdir}

# We don't want the static library
rm %{buildroot}%{_libdir}/libminisat.a

# Fix permissions on the shared library
chmod a+x %{buildroot}%{_libdir}/libminisat.so.2.*

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 -p %{SOURCE3} %{buildroot}%{_mandir}/man1

%check
echo "RESULTS:"
cat minisat2-test.out
result=`head -1 minisat2-test.out`
if [ "$result" = "SAT" ]; then
  echo "SUCCESS - Correctly found that it was satisfiable"
  true
else
  echo "Failed test."
  false
fi

%ldconfig_scriptlets libs

%files
%doc doc/ReleaseNotes-2.2.0.txt
%doc minisat-user-guide.html
%doc minisat2-test.in
%doc minisat2-test.out
%{_bindir}/%{myname}
%{_mandir}/man1/minisat.1*

%files libs
%license LICENSE
%{_libdir}/lib%{myname}.so.2*

%files devel
%{_includedir}/%{myname}/
%{_libdir}/lib%{myname}.so

%changelog
%autochangelog
