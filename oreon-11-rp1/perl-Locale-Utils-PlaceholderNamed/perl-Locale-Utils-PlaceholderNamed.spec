%global source0_hash 6fd78ea239b5c359ba9422753766f638ee4f90cd21751a59b386155e2a45a6bd

Name:           perl-Locale-Utils-PlaceholderNamed
Version:        1.004
Release:        25%{?dist}
Summary:        Utils to expand named placeholders
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-Utils-PlaceholderNamed
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEFFENW/Locale-Utils-PlaceholderNamed-%{version}.tar.gz
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
BuildRequires:  perl(Moo) >= 1.003001
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::Differences) >= 0.60
# Test::Exception not used
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Moo) >= 1.003001

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)$

%description
This module provides utils to expand named placeholders.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-Utils-PlaceholderNamed-%{version}
sed -i -e 's/\r//' README Changes example/* javascript/Locale/Utils/*
sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' example/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes example javascript README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
