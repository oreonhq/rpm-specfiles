%global source0_hash 222bfb7ec1fdfa465e32da3dc4abed2edc7364bbe19e8e3c513c7d585b0109ad

Name:           perl-HTML-StripScripts
Version:        1.06
Release:        29%{?dist}
Summary:        Strip scripting constructs out of HTML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-StripScripts
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DRTECH/HTML-StripScripts-%{version}.tar.gz
# https://github.com/clintongormley/perl-html-stripscripts/pull/4
Patch1:         perl-HTML-StripScripts-1.06-CVE-2023-24038.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
This module strips scripting constructs out of HTML, leaving as much non-
scripting markup in place as possible. This allows web applications to
display HTML originating from an untrusted source without introducing XSS
(cross site scripting) vulnerabilities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-StripScripts-%{version}
%patch -P 1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
