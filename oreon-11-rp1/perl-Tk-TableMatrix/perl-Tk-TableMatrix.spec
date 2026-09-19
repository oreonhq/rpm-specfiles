%global source0_hash d31708b8bbfddce9034540522b2e4ec58e70f2eb5b23ac593d2421ea90dbd0d6

Name:           perl-Tk-TableMatrix
Version:        1.29
Release:        13%{?dist}
Summary:        Perl module for creating and manipulating tables

# Automatically converted from old format: (GPL+ or Artistic) and BSD - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/Tk-TableMatrix
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/Tk-TableMatrix-%{version}.tar.gz

BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  libX11-devel
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::MMutil)

%{?perl_default_filter}

%description
The TableMatrix command creates a 2-dimensional grid of cells. The
table can use a Tcl array variable or Tcl command for data storage and
retrieval.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-TableMatrix-%{version}

# fix perms
chmod 644 COPYING README TableMatrix.pm TableMatrix.xs TableMatrix/Spreadsheet.pm \
  TableMatrix/SpreadsheetHideRows.pm pTk/license.terms pTk/mTk/license.terms
# copy license
cp -p pTk/license.terms license.terms.pTk
cp -p pTk/mTk/license.terms license.terms.mTk

# Fix end-of-line-encoding
touch -r demos/edit_styles.pl demos/edit_styles.pl.timestamps
sed -i 's/\r//' demos/edit_styles.pl
touch -r demos/edit_styles.pl.timestamps demos/edit_styles.pl
rm demos/edit_styles.pl.timestamps

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
chmod -x demos/*

%check
# disabled by default because it needs an x screen
%{?_with_tests:%{make_build} test}

%files
%doc ChangeLog COPYING README Changes
%doc license.terms.pTk license.terms.mTk
%doc demos
%{perl_vendorarch}/Tk/
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
