%global source0_hash e0bb2a7b38840cee9589aa0166bea838fd57779a2eeb9ede870af7d183ffe197

Name:           perl-HTML-Entities-Numbered
Version:        0.04
Release:        46%{?dist}
Summary:        Conversion of numbered HTML entities
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Entities-Numbered
Source0:        https://cpan.metacpan.org/modules/by-module/HTML/HTML-Entities-Numbered-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.32

%description
HTML::Entities::Numbered is a content conversion filter for named HTML
entities (symbols, mathematical symbols, Greek letters, Latin letters,
etc.). When an argument of name2decimal() or name2hex() contains some
nameable HTML entities, they will be replaced to numbered HTML entities.
And when an argument of name2decimal_xml() or name2hex_xml() contains
some nameable numbered HTML entities, they will be replaced to numbered
HTML entities except valid XML entities (the excepted "valid XML
entities" are the following five entities: &lt;, &gt;, &amp;, &quot;,
&apos;). By the same token, when an argument of decimal2name() or
hex2name() contains some nameable numbered HTML entities, they will be
replaced to named HTML entities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Entities-Numbered-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
