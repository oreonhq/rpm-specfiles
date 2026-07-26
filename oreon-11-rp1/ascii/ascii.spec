%global source0_hash 309aa75fcc46921b3ac1bb2a6742e6e343049529ea5b4859564625be742a013c

Name:           ascii
Version:        3.31
Release:        1%{?dist}
URL:            http://www.catb.org/~esr/ascii/
Source0:        http://www.catb.org/~esr/ascii/ascii-%{version}.tar.gz
BuildRequires:  xmlto, gcc
BuildRequires:  make

License:        BSD-2-Clause
Summary:        Interactive ascii name and synonym chart

%description
The ascii utility provides easy conversion between various byte representations
and the American Standard Code for Information Interchange (ASCII) character
table.  It knows about a wide variety of hex, binary, octal, Teletype mnemonic,
ISO/ECMA code point, slang names, XML entity names, and other representations.
Given any one on the command line, it will try to display all others.  Called
with no arguments it displays a handy small ASCII chart.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%make_build ascii ascii.1 CFLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
cp ascii $RPM_BUILD_ROOT%{_bindir}
cp ascii.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%{_mandir}/man1/ascii.1*
%{_bindir}/ascii
%doc README.adoc NEWS.adoc ascii.adoc
%license COPYING

%changelog
%autochangelog
