%global source0_hash 5a47cdb785e6f1f94adf501369365ad35181f0dc199b66dd42aac169848668a5

Name:           perl-Lingua-Identify
Summary:        Language identification
Version:        0.56
Release:        31%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-Identify
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/Lingua/Lingua-Identify-%{version}.tar.gz

# https://rt.cpan.org/Public/Bug/Display.html?id=83071
Patch0:         Lingua-Identify-0.51-Fix-a-unit-test.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Factory::Util) >= 1.6
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(locale)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Affixes) >= 0.07
BuildRequires:  perl(Text::ExtractWords)
BuildRequires:  perl(Text::Ngram) >= 0.13
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Class::Factory::Util) >= 1.6
Requires:       perl(Text::Affixes) >= 0.07
Requires:       perl(Text::Ngram) >= 0.13

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Factory::Util|Text::Affixes|Text::Ngram)\\)$

%description
Lingua::Identify identifies the language a given string or file is written in.

%package tools
Summary:        Tools related to Lingua::Identify
Requires:       %{name} == %{version}-%{release}
Requires:       perl(Text::Affixes) >= 0.07
Requires:       perl(Text::Ngram) >= 0.13

%description tools
Tools related to Lingua::Identify.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-Identify-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{_mandir}/man3/Lingua::Identify*
%{perl_vendorlib}/Lingua

%files tools
%{_bindir}/langident
%{_bindir}/make-lingua-identify-language
%{_mandir}/man1/langident.1*
%{_mandir}/man1/make-lingua-identify-language.1*

%changelog
%autochangelog
