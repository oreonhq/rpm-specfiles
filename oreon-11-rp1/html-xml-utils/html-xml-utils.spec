%global source0_hash 888a31631a7a70308bb2f333e077d0416f4bb78317f8697ffb4a95187f677301

Name:           html-xml-utils
Version:        8.7
Release:        1%{?dist}
Summary:        A number of simple utilities for manipulating HTML and XML files

# All files W3C except openurl.c which has two BSD-3-Clause functions
License:        W3C AND BSD-3-Clause
URL:            https://www.w3.org/Tools/HTML-XML-utils/
Source:         %{url}/%{name}-%{version}.tar.gz
# Fix C23 incompatibilities
Patch:          %{name}-c23.patch
# Fix a libcurl warning
Patch:          %{name}-libcurl.patch

BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gperf
BuildRequires: libcurl-devel
BuildRequires: libidn2-devel
BuildRequires: make

%description
A number of simple utilities for manipulating HTML and XML files. See Manpages
for each specific command.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Force generated files to be regenerated
rm dtd.c html.c scan.c unent.c

%build
export CFLAGS='%{build_cflags} -DYY_NO_INPUT'
%configure
# Occasional failures when building in parallel:
# /bin/sh: line 1: ./cexport: Text file busy
make

%install
%make_install
# Install license separately so it has appropriate metadata
rm %{buildroot}%{_docdir}/html-xml-utils/COPYING

%check
make check

%files
%{_bindir}/hxaddid
%{_bindir}/hxcite
%{_bindir}/hxcite-mkbib
%{_bindir}/hxcount
%{_bindir}/hxextract
%{_bindir}/hxclean
%{_bindir}/hxcopy
%{_bindir}/hxprune
%{_bindir}/hxnsxml
%{_bindir}/hxprintlinks
%{_bindir}/hxincl
%{_bindir}/hxindex
%{_bindir}/hxmkbib
%{_bindir}/hxmultitoc
%{_bindir}/hxname2id
%{_bindir}/hxnormalize
%{_bindir}/hxnum
%{_bindir}/hxpipe
%{_bindir}/hxremove
%{_bindir}/hxselect
%{_bindir}/hxtabletrans
%{_bindir}/hxtoc
%{_bindir}/hxuncdata
%{_bindir}/hxunent
%{_bindir}/hxunpipe
%{_bindir}/hxunxmlns
%{_bindir}/hxwls
%{_bindir}/hxxmlns
%{_bindir}/hxref
%{_bindir}/xml2asc
%{_bindir}/asc2xml
%{_mandir}/man1/hxaddid.1*
%{_mandir}/man1/asc2xml.1*
%{_mandir}/man1/hxcite.1*
%{_mandir}/man1/hxcite-mkbib.1*
%{_mandir}/man1/hxcopy.1*
%{_mandir}/man1/hxcount.1*
%{_mandir}/man1/hxextract.1*
%{_mandir}/man1/hxclean.1*
%{_mandir}/man1/hxprune.1*
%{_mandir}/man1/hxincl.1*
%{_mandir}/man1/hxindex.1*
%{_mandir}/man1/hxmkbib.1*
%{_mandir}/man1/hxmultitoc.1*
%{_mandir}/man1/hxname2id.1*
%{_mandir}/man1/hxnormalize.1*
%{_mandir}/man1/hxnum.1*
%{_mandir}/man1/hxpipe.1*
%{_mandir}/man1/hxprintlinks.1*
%{_mandir}/man1/hxremove.1*
%{_mandir}/man1/hxtabletrans.1*
%{_mandir}/man1/hxtoc.1*
%{_mandir}/man1/hxuncdata.1*
%{_mandir}/man1/hxunent.1*
%{_mandir}/man1/hxunpipe.1*
%{_mandir}/man1/hxunxmlns.1*
%{_mandir}/man1/hxwls.1*
%{_mandir}/man1/xml2asc.1*
%{_mandir}/man1/hxxmlns.1*
%{_mandir}/man1/hxref.1*
%{_mandir}/man1/hxselect.1*
%{_mandir}/man1/hxnsxml.1*
%license COPYING
%doc AUTHORS TODO README 

%changelog
%autochangelog
