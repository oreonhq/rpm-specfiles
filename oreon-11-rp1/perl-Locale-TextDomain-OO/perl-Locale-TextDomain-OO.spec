%global source0_hash b51783e1a89620213ea2a83e45baec3aa86e9cbe1e9fa5b9f74f8749b0540e38

Name:           perl-Locale-TextDomain-OO
Version:        1.036
Release:        20%{?dist}
Summary:        Perl object-oriented Interface to Uniforum Message Translation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-TextDomain-OO
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEFFENW/Locale-TextDomain-OO-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load) >= 0.19
BuildRequires:  perl(Clone)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Locale::MO::File) >= 0.09
BuildRequires:  perl(Locale::PO) >= 0.24
BuildRequires:  perl(Locale::TextDomain::OO::Util::ExtractHeader) >= 3.006
BuildRequires:  perl(Locale::TextDomain::OO::Util::JoinSplitLexiconKeys) >= 2.002
BuildRequires:  perl(Locale::Utils::PlaceholderBabelFish) >= 0.001
BuildRequires:  perl(Locale::Utils::PlaceholderMaketext) >= 1.000
BuildRequires:  perl(Locale::Utils::PlaceholderNamed) >= 1.000
BuildRequires:  perl(Moo) >= 1.003001
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Singleton)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny) >= 0.052
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Sub) >= 0.09
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(JSON) >= 2.50
BuildRequires:  perl(Test::Differences) >= 0.60
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(utf8)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

Requires:       perl(Class::Load) >= 0.19
Requires:       perl(Locale::MO::File) >= 0.09
Requires:       perl(Locale::PO) >= 0.24
Requires:       perl(Locale::TextDomain::OO::Util::ExtractHeader) >= 3.006
Requires:       perl(Locale::TextDomain::OO::Util::JoinSplitLexiconKeys) >= 2.002
Requires:       perl(Locale::Utils::PlaceholderBabelFish) >= 0.001
Requires:       perl(Locale::Utils::PlaceholderMaketext) >= 1.000
Requires:       perl(Locale::Utils::PlaceholderNamed) >= 1.000
Requires:       perl(Moo) >= 1.003001
Requires:       perl(MooX::Singleton)
Requires:       perl(Path::Tiny) >= 0.052
Requires:       perl(Tie::Sub) >= 0.09

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Locale::(MO::File|PO)\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Locale::TextDomain::OO::Util::(ExtractHeader|JoinSplitLexiconKeys)\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Locale::Utils::Placeholder(BabelFish|Maketext|Named)\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\((Class::Load|Path::Tiny|Tie::Sub)\\)\\s*$
%global __requires_exclude_from .*%{_docdir}
%global __provides_exclude_from .*%{_docdir}

%description
These modules provide a high-level interface to Perl message translation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-TextDomain-OO-%{version}
for i in `find javascript -type f` README Changes; do
    sed -i -e 's/\r//' $i
done
for i in `find example -type f` ; do
    sed -i -e 's/\r//' $i
    sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' $i
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes example javascript  README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
