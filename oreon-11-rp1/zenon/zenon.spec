%global source0_hash 73811276ad0aa46e91e346bf38937d37b1b9930e0b9f6b0aa20a5c1959e3006e

%global debug_package %{nil}
%global rocqver 9.1.1
%global giturl  https://github.com/zenon-prover/zenon

Name:		zenon
Version:	0.8.5
Release:	39%{?dist}
Summary:	Automated theorem prover for first-order classical logic
License:	BSD-3-Clause
URL:		http://zenon-prover.org/
VCS:		git:%{giturl}.git
Source0:	%{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	http://zenon-prover.org/zenlpar07.pdf
Source2:	%{name}-tptp-COM003+2.p
Source3:	%{name}-tptp-ReadMe
# Basic documentation (man pages). Submitted upstream 2008-07-25:
Source4:	%{name}.1
Source5:	%{name}-format.5
# Update deprecated usage
Patch:          %{name}-deprecated.patch

# Rocq's plugin architecture requires cmxs files
ExclusiveArch:  %{ocaml_native_compiler}

BuildRequires:	coq-core-compat = %{rocqver}
BuildRequires:	rocq = %{rocqver}
BuildRequires:	rocq-stdlib
BuildRequires:	ghostscript
BuildRequires:	ImageMagick
BuildRequires:	make
BuildRequires:	ocaml

Requires:	rocq%{?_isa} = %{rocqver}
Requires:	rocq-stdlib%{?_isa}
Requires:	coreutils

%description
Zenon is an automated theorem prover for first order classical logic with
equality, based on the tableau method.  Zenon can read input files in TPTP,
Coq, Focal, and its own Zenon format.  Zenon can directly generate Coq proofs
(proof scripts or proof terms), which can be reinserted into Coq
specifications.  Zenon can also be extended.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

cp -p %{SOURCE1} .

# Generate debuginfo
sed -i 's/^\(CAMLFLAGS = \).*/\1-g/' Makefile

%build
./configure -prefix %{_prefix} -libdir %{_datadir}/%{name} -sum md5sum

mkdir examples
cp -p %{SOURCE2} examples/tptp-COM003+2.p
cp -p %{SOURCE3} examples/tptp-ReadMe

make %{?_smp_mflags} zenon.bin
cp -p zenon.bin zenon
# Use of %%{?_smp_mflags} sometimes leads to build failures
make coq

%install
%make_install

install -d %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_mandir}/man5/
cp -p %{SOURCE4} %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE5} %{buildroot}%{_mandir}/man5/

# Put the coq files where coq can find them
mkdir -p %{buildroot}%{_libdir}/coq/user-contrib
mv %{buildroot}%{_datadir}/%{name} %{buildroot}%{_libdir}/coq/user-contrib/Zenon

%check
# Sanity test. Can we prove TPTP v3.4.2 test COM003+2 (the halting problem)?
# tptp-ReadMe has test's license conditions ("must credit + note changes").
# TPTP from: http://www.cs.miami.edu/~tptp/TPTP/Distribution/TPTP-v3.4.2.tgz
result=`./zenon -p0 -itptp examples/tptp-COM003+2.p`
if [ "$result" = "(* PROOF-FOUND *)" ] ; then
 echo "Test succeeded"
else
 echo "TEST FAILED"
 false
fi

%files
%doc zenlpar07.pdf examples
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/coq/user-contrib/Zenon
%{_mandir}/man1/zenon.1*
%{_mandir}/man5/zenon-format.5*

%changelog
%autochangelog
