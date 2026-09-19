%global source0_hash 498099472def866b448bf62f4182dfadf59472e13f24cb8664a671ca79b67015

Name:       perl-HTML-TagCloud 
Version:    0.38
Release:    36%{?dist}
# lib/HTML/TagCloud.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 
Summary:    Generate An HTML Tag Cloud 
Source:     https://cpan.metacpan.org/authors/id/R/RO/ROBERTSD/HTML-TagCloud-%{version}.tar.gz
Url:        https://metacpan.org/release/HTML-TagCloud
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Test::More)
# optional tests
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
The HTML::TagCloud module enables you to generate "tag clouds" in HTML. Tag
clouds serve as a textual way to visualize terms and topics that are used
most frequently. The tags are sorted alphabetically and a larger font is
used to indicate more frequent term usage.

This module provides a simple interface to generating a CSS-based HTML tag
cloud. You simply pass in a set of tags, their URL and their count.  This
module outputs style-sheet-based HTML.  You may use the included CSS or use
your own.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-TagCloud-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
