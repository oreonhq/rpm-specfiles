%global source0_hash 6b9b51e1a6225da279f8d09d9d75583d83977646a4cbd4c3e6e8dc4aa7b928b9
%global giturl  https://github.com/eprover/eprover
Name:		E
Version:	3.5.1
Release:        1%{?dist}
Summary:        Equational Theorem Prover
License:	(GPL-2.0-or-later OR LGPL-2.1-or-later) AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
URL:		https://www.eprover.org/
VCS:		git:%{giturl}.git
Source0:        %{giturl}/archive/%{name}-%{version}.tar.gz
Source1:	eprover.bbl
Patch:		%{name}-picosat.patch
ExcludeArch:	%{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  picosat-devel
BuildRequires:  tex(latex)
BuildRequires:  tex(supertabular.sty)
# /oreon:deps
%description
E is a purely equational theorem prover for full first-order logic.  That
means it is a program that you can stuff a mathematical specification (in
first-order format) and a hypothesis into, and which will then run forever,
using up all of your machines' resources.  Very occasionally it will find a
proof for the hypothesis and tell you so.

E's inference core is based on a modified version of the superposition
calculus for equational clausal logic.  Both clausification and reasoning on
the clausal form can be documented in checkable proof objects.

E was the best-performing open source software prover in the 2008 CADE ATP
System Competition (CASC) in the FOF, CNF, and UEQ divisions.  In the 2011
competition, it won second place in the FOF division, and placed highly in CNF
and UEQ.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n eprover-%{name}-%{version}

%conf
# Fix the character encoding of one file
iconv -f ISO8859-1 -t UTF-8 DOC/E-REMARKS > DOC/E-REMARKS.utf8
touch -r DOC/E-REMARKS DOC/E-REMARKS.utf8
mv -f DOC/E-REMARKS.utf8 DOC/E-REMARKS

# Preserve timestamps when installing
sed -i 's|cp \$1|cp -p $1|' development_tools/e_install

# Put the bibliography file where LaTeX will see it
cp -p %{SOURCE1} DOC

# Make sure we do not use the bundled picosat
rm -fr CONTRIB

%build

sed -e "s|^EXECPATH = .*|EXECPATH = %{buildroot}%{_bindir}|" \
    -e "s|^MANPATH = .*|MANPATH = %{buildroot}%{_mandir}/man1|" \
    -e "s|^CFLAGS.*|CFLAGS     = %{build_cflags} \$(BUILDFLAGS) -I../include|" \
    -e "s|^LDFLAGS.*|LDFLAGS    = %{build_ldflags}|" \
    -i Makefile.vars
make remake
ln -s eprover-ho PROVER/eprover
make man
cd DOC
bibtex eprover || :
pdflatex eprover
cd -
%install
%make_install
mv %{buildroot}%{_bindir}/eprover-ho %{buildroot}%{_bindir}/eprover
%oreon_autofiles main

%check

./PROVER/eprover -s --tstp-in EXAMPLE_PROBLEMS/TPTP/SYN190-1.p \
  | sed '/Freeing FVIndex/d' | tail -1 > test-results
echo "# SZS status Unsatisfiable" > test-expected-results
diff -u test-results test-expected-results
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
