%global source0_hash 3c5fa07f65ed77c029e20d246a104041148f1a9b47e37df63f37e51d02bd46a0

# Provide Locale::TextDomain::OO implementation in JavaScript
%bcond_without perl_Locale_TextDomain_OO_Util_enables_javascript

Name:           perl-Locale-TextDomain-OO-Util
Version:        4.002
Release:        20%{?dist}
Summary:        Lexical Utils for Locale::TextDomain::OO
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-TextDomain-OO-Util
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEFFENW/Locale-TextDomain-OO-Util-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(charnames)
BuildRequires:  perl(English)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::Differences) >= 0.60
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
This module provides methods for lexicon constants, to join and split
lexicon keys and to extract the gettext file header.

%if %{with perl_Locale_TextDomain_OO_Util_enables_javascript}
%package -n js-Locale-TextDomain-OO-Util
Summary:        Lexical Utils for Locale::TextDomain::OO in JavaScript
BuildRequires:  web-assets-devel
Requires:       js-jquery
Requires:       web-assets-filesystem

%description -n js-Locale-TextDomain-OO-Util
This package contains the Locale::TextDomain::OO utils as JavaScript.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-TextDomain-OO-Util-%{version}
sed -i -e 's/\r//' README Changes example/*
sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' example/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%if %{with perl_Locale_TextDomain_OO_Util_enables_javascript}
mkdir -p $RPM_BUILD_ROOT%{_jsdir}/js-Locale-TextDomain-OO-Util
cp -pr javascript/* $RPM_BUILD_ROOT%{_jsdir}/js-Locale-TextDomain-OO-Util
%endif

%check
make test

%files
%doc Changes example README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/Locale/TextDomain/OO/Util/JavaScript.pm
%exclude %{_mandir}/man3/Locale::TextDomain::OO::Util::JavaScript.3*

%if %{with perl_Locale_TextDomain_OO_Util_enables_javascript}
%files -n js-Locale-TextDomain-OO-Util
%{perl_vendorlib}/Locale/TextDomain/OO/Util/JavaScript.pm
%{_mandir}/man3/Locale::TextDomain::OO::Util::JavaScript.3*
%{_jsdir}/js-Locale-TextDomain-OO-Util
%endif

%changelog
%autochangelog
