%global source0_hash f6039bdb2894b200ee379e4a69ea9bd9ce37611c64738d2e7b94bb05ad75399c

Name:           perl-Catalyst-Plugin-I18N
Version:        0.10
Release:        45%{?dist}
Summary:        I18N for Catalyst
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-I18N
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-I18N-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(I18N::LangTags)
BuildRequires:  perl(I18N::LangTags::Detect)
BuildRequires:  perl(I18N::LangTags::List)
BuildRequires:  perl(inc::Module::Install) >= 0.87
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(Locale::Maketext::Simple) >= 0.19
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# not automatically detected
Requires:       perl(Locale::Maketext::Lexicon)

%{?perl_default_filter}

%description
Supports mo/po files and Maketext classes under your applications I18N
namespace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-I18N-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
