%global source0_hash bc64200261142f9a5f7e0786dc5ab24a6330bc19bd1e3e9bb4b6d7c31621b722

Name:           perl-HTML-RewriteAttributes
Version:        0.06
Release:        5%{?dist}
Summary:        Concise attribute rewriting
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-RewriteAttributes
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/HTML-RewriteAttributes-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(URI)
BuildRequires:  perl(Test::More)

BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

%description
HTML::RewriteAttributes is designed for simple yet powerful HTML attribute
rewriting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-RewriteAttributes-%{version}
rm -r inc/
sed -i -e '/^inc\/.*$/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
