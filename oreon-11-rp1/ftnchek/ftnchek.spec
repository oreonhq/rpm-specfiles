%global source0_hash d92212dc0316e4ae711f7480d59e16095c75e19aff6e0095db2209e7d31702d4

Name:           ftnchek
Version:        3.3.1
Release:        45%{?dist}
Summary:        Static analyzer for Fortran 77 programs

License:        MIT
URL:            http://www.dsm.fordham.edu/~ftnchek/
Source0:        http://www.dsm.fordham.edu/~ftnchek/download/ftnchek-3.3.1.tar.gz
Patch0:         ftnchek-3.3.1-datadir.patch
Patch1:         http://www.dsm.fordham.edu/~ftnchek/download/ftnchek-3.3.1-varfmt.patch
# Patch to support bison 2.6
Patch2:         ftnchek-3.3.1-bison26.patch
Patch3: ftnchek-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  groff, emacs
BuildRequires:  perl
BuildRequires: make
Requires:       emacs-filesystem
Obsoletes:      emacs-ftnchek < 3.3.1-21
Provides:       emacs-ftnchek = %{version}-%{release}
Obsoletes:      emacs-ftnchek-el < 3.3.1-21
Provides:       emacs-ftnchek-el = %{version}-%{release}

%description
ftnchek is a static analyzer for Fortran 77 programs. It is designed to
detect certain errors in a Fortran program that a compiler usually does
not. ftnchek is not primarily intended to detect syntax errors. Its
purpose is to assist the user in finding semantic errors. Semantic
errors are legal in the Fortran language but are wasteful or may cause
incorrect operation. For example, variables which are never used may
indicate some omission in the program; uninitialized variables contain
garbage which may cause incorrect results to be calculated; and variables
which are not declared may not have the intended type. ftnchek is
intended to assist users in the debugging of their Fortran program. It is
not intended to catch all syntax errors. This is the function of the
compiler. Prior to using ftnchek, the user should verify that the program
compiles correctly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .datadir
%patch -P1 -p1 -b .varfmt
%patch -P2 -p1 -b .bison26
%patch -P3 -p1
#Stop configure from overriding CFLAGS
sed -i -e 's/CFLAGS="-DUNIX.*"//' configure

%build
export CFLAGS="$RPM_OPT_FLAGS -DUNIX"
%configure
make || :
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/ftnchek
%makeinstall STRIP=/bin/true datadir=$RPM_BUILD_ROOT%{_datadir}/ftnchek \
             lispdir=$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/ftnchek

%files
%doc LICENSE README FAQ PATCHES
%{_bindir}/dcl2inc
%{_bindir}/ftnchek
%{_datadir}/ftnchek/
%{_mandir}/man1/dcl2inc.1*
%{_mandir}/man1/ftnchek.1*
%{_emacs_sitelispdir}/ftnchek/

%changelog
%autochangelog
