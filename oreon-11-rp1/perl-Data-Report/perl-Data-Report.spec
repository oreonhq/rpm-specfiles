%global source0_hash d50c89dbd0eaebbaba31c0ede60356607ed56d5f7060d303550bfc2a72cc944d

Name:		perl-Data-Report
Version:	1.001
Release:	49%{?dist}
Summary:	A flexible plugin-driven reporting framework

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Data-Report
Source0:	https://cpan.metacpan.org/authors/id/JV/Data-Report-%{version}.tar.gz
Requires:       perl-interpreter
Requires:       perl-generators
Requires:       perl(:VERSION) >= 5.10.1
Requires:	perl(Text::CSV)

BuildArch:	noarch

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.5503

# For test suite
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::CSV)

%description
Data::Report is a framework for report generation.

You define the columns, add the data row by row, and get reports in
text, HTML, CSV and so on. Textual ornaments like extra empty lines,
dashed lines, and cell lines can be added in a way similar to HTML
style sheets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Report-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test TEST_VERBOSE=1

%install
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{__chmod} -R u+w %{buildroot}/*

%files
%doc
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
