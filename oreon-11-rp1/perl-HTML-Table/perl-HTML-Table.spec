%global source0_hash f6dd9066cde6a818a2c0eb2bcfdb6e5ef3de030fff6beeadfff3732ef1c32805

Name:           perl-HTML-Table
Version:        2.08a
Release:        48%{?dist}
Summary:        Create HTML tables using simple interface
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Table
Source0:        https://cpan.metacpan.org/modules/by-module/HTML/HTML-Table-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
HTML::Table is used to generate HTML tables for CGI scripts.  By using the
methods provided fairly complex tables can be created, manipulated, then
 printed from Perl scripts.  The module also greatly simplifies creating
tables within tables from Perl.  It is possible to create an entire table
using the methods provided and never use an HTML tag.

HTML::Table also allows for creating dynamically sized tables via its addRow
and addCol methods.  These methods automatically resize the table if passed
more cell values than will fit in the current table grid.

Methods are provided for nearly all valid table, row, and cell tags specified
for HTML 3.0.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Table-%{version}
for f in Changes lib/HTML/Table.pm
do
   iconv -f ISO-8859-1 -t UTF-8 -o ${f}.UTF-8 $f
   mv ${f}.UTF-8 $f
done

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
