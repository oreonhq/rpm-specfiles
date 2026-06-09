%global source0_hash 6c492d0c7b4a40e7674d088191d3aa11f373bb1da60762e098b8ee2dda96ef22
%global source1_hash 3f7d8be8ef6ecc7167d39b10d66954ec734280b5bdcd57f7d9eafe429d11c22a

Name:           wordnet
Version:        3.0
Release:        50%{?dist}
Summary:        A lexical database for the English language

License:        MIT and GPL-2.0-or-later
URL:            http://wordnet.princeton.edu/
Source0:        https://wordnetcode.princeton.edu/%{version}/WordNet-%{version}.tar.bz2
# Updated database
Source1:        https://wordnetcode.princeton.edu/wn3.1.dict.tar.gz
Patch0:        wordnet-3.0-CVE-2008-2149.patch
Patch1:        wordnet-3.0-CVE-2008-3908.patch
Patch2:        wordnet-3.0-fix_man.patch
Patch3:        wordnet-3.0-fix_resourcedir_path.patch
Patch4:        wordnet-3.0-src_stubs_c.patch
# wordnet-3.0-wishwn_manpage.patch is GPL-2.0-or-later
Patch5:        wordnet-3.0-wishwn_manpage.patch
Patch6:        wordnet-3.0-use_system_tk_headers.patch
Patch7:        wordnet-3.0-libtool.patch
# Bug #585206
Patch8:        wordnet-3.0-error_message.patch
# Bug #1037386
Patch9:        wordnet-3.0-Pass-compilation-with-Werror-format-security.patch
Patch10:        wordnet-tcl9-ansi-args.patch
BuildRequires:  automake >= 1.8
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  tar
BuildRequires:  tcl-devel
BuildRequires:  tk-devel

%description
WordNet is a large lexical database of English, developed under the direction
of George A. Miller. Nouns, verbs, adjectives and adverbs are grouped into sets
of cognitive synonyms (synsets), each expressing a distinct concept. Synsets
are interlinked by means of conceptual-semantic and lexical relations. The
resulting network of meaningfully related words and concepts can be navigated
with the browser. WordNet is also freely and publicly available for download.
WordNet's structure makes it a useful tool for computational linguistics and
natural language processing.


%package browser
Summary:    Tk browser for WordNet
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   font(:lang=en)

%description browser
This package contains graphical browser for WordNet database.


%package devel
Summary:    The development libraries and header files for WordNet
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the libraries and header files required to create
applications based on WordNet.


%package doc
Summary:    Manual pages for WordNet in alternative formats
BuildArch:  noarch

%description doc
This package contains manual pages for WordNet package in HTML, PDF,
and PostScript format.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n WordNet-%{version}
%patch 0 -p1 -b .cve-2008-2149
%patch 1 -p1 -b .cve-2008-3908
%patch 2 -p1 -b .fix_man
%patch 3 -p1 -b .fix_resourcedir_path
%patch 4 -p1 -b .src_stubs_c
%patch 5 -p1 -b .wishwn_manpage
sed -e '/man_MANS/ s/$/ wishwn.1/' -i doc/man/Makefile.am
%patch 6 -p1 -b .use_system_tk_headers
%patch 7 -p1 -b .libtool
%patch 8 -p1 -b .error_message
%patch 9 -p1 -b .format
%patch 10 -p1 -b .tcl9-ansi-args
# delete the include/tk dir, since we do not use the included tk headers
rm -rf include/tk
# Update a database
tar -xozf %{SOURCE1}
# Remove database byproducts brought by the database update
rm -rf dict/dbfiles


%build
libtoolize && aclocal
autoupdate
autoreconf -i
export CFLAGS="%{?optflags} -DUSE_INTERP_RESULT"
export CXXFLAGS="%{?optflags} -DUSE_INTERP_RESULT"
%configure --enable-static=no --prefix=%{_datadir}/wordnet-%{version}/
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
# delete the libWN.la files (reasoning in the packaging guidelines)
rm -f  $RPM_BUILD_ROOT%{_libdir}/libWN.la
# Remove duplicate copies of docs installed by make install
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/doc
# Remove useless Makefiles installed by %%doc
rm -rf doc/{html,ps,pdf}/Makefile*


%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/wn
%{_mandir}/man1/grind.1.gz
%{_mandir}/man1/wn.1.gz
%{_mandir}/man1/wnintro.1.gz
%{_mandir}/man5/*.5.gz
%{_mandir}/man7/*.7.gz
%{_datadir}/%{name}-%{version}/
%exclude %{_datadir}/%{name}-%{version}/lib/wnres/
%{_libdir}/libWN.so.*

%files browser
%{_bindir}/wishwn
%{_bindir}/wnb
%{_mandir}/man1/wishwn.1.gz
%{_mandir}/man1/wnb.1.gz
%{_datadir}/%{name}-%{version}/lib/wnres/

%files devel
%{_mandir}/man3/*.3.gz
%{_includedir}/wn.h
%{_libdir}/libWN.so

%files doc
%doc COPYING doc/{html,ps,pdf}


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-50
- Import
