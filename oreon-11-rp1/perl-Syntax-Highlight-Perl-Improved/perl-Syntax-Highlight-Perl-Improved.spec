%global source0_hash 01467878edc6bdf006e9557d13db131ab4f77e9dd1fd6492d209f0698c3b5c9e

Name:           perl-Syntax-Highlight-Perl-Improved
Version:        1.01
Release:        47%{?dist}
Summary:        Highlighting of Perl Syntactical Structures
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Highlight-Perl-Improved
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDCYL/Syntax-Highlight-Perl-Improved-101/Syntax-Highlight-Perl-Improved-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%{?perl_default_filter}

%description
This module provides syntax highlighting for Perl code. The design bias is
roughly line-oriented and streamed (i.e. processing a file line-by-line in a
single pass). Provisions may be made in the future for tasks related to "back-
tracking" (i.e. re-doing a single line in the middle of a stream) such as
speeding up state copying.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Syntax-Highlight-Perl-Improved-%{version}

# Get rid of non-UNIX end-of-lines
sed -i 's/\r//' viewperl
sed -i 's/\r//' README
sed -i 's/\r//' ChangeLog

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README viewperl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
