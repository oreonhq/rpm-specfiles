%global source0_hash 56309a21f21e737b604f03e7d760f5df953b4a14663b0a7051f8a02bce7cc86a

Name:           bwbasic
Version:        3.20g
Release:        1%{?dist}
Summary:        Bywater BASIC Interpreter

# All files GPL-2.0-only except unixio.h which is public domain
License:        GPL-2.0-only AND LicenseRef-Fedora-Public-Domain
URL:            https://yeolpishack.net/repos/ChipMaster/bwBASIC
Source:         %{url}/archive/v%{version}.tar.gz
# Separate compilation and linking steps to use appropriate Fedora
# flags
Patch:          CompileLink.patch
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  make

%description
The Bywater BASIC Interpreter (bwBASIC) implements a large
superset of the ANSI Standard for Minimal BASIC (X3.60-1978),
a significant subset of the ANSI Standard for Full BASIC
(X3.113-1987), and many classic BASIC dialects in C.  bwBASIC 
seeks to be as portable as possible.

%package doc
Summary:  Documentation and examples for bwBASIC
BuildArch:  noarch

%description doc
Documentation and code examples for use with the Bywater
BASIC Interpreter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1
# Use Fedora build flags
sed -i 's|^CFLAGS=-s -ansi|^CFLAGS=-s -ansi %{build_cflags}|g' Makefile
sed -i 's|^LDFLAGS=|^LDFLAGS=%{build_ldflags} -nostartfiles|g' Makefile

dos2unix DOCS/*.txt
dos2unix README
dos2unix BAS-EXAMPLES/*.bas
chmod -x GUI/bwbasic.desktop

%build
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
install bwbasic %{buildroot}/%{_bindir}
install renum %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_docdir}/bwbasic
cp -p -r BAS-EXAMPLES %{buildroot}/%{_docdir}/bwbasic
cp -p -r DOCS %{buildroot}/%{_docdir}/bwbasic

%check
./bwbasic BAS-EXAMPLES/end.bas 
./bwbasic BAS-EXAMPLES/abs.bas 
./bwbasic BAS-EXAMPLES/assign.bas 
./bwbasic BAS-EXAMPLES/random.bas 

%files
%license COPYING
%doc README
%{_bindir}/bwbasic
%{_bindir}/renum

%files doc
%license COPYING
%dir %{_docdir}/bwbasic
%dir %{_docdir}/bwbasic/BAS-EXAMPLES
%{_docdir}/bwbasic/BAS-EXAMPLES/*.bas
%{_docdir}/bwbasic/BAS-EXAMPLES/*.inp
%{_docdir}/bwbasic/BAS-EXAMPLES/*.pro
%dir %{_docdir}/bwbasic/DOCS
%{_docdir}/bwbasic/DOCS/*.txt
%{_docdir}/bwbasic/DOCS/*.HTM

%changelog
%autochangelog
