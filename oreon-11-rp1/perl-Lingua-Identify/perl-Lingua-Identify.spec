%global source0_hash 5a47cdb785e6f1f94adf501369365ad35181f0dc199b66dd42aac169848668a5
Name:           perl-Lingua-Identify
Summary:        Language identification
Version:        0.56
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-Identify
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/Lingua/Lingua-Identify-%{version}.tar.gz
Patch0:         Lingua-Identify-0.51-Fix-a-unit-test.patch
BuildArch:      noarch
Requires:       perl(Class::Factory::Util) >= 1.6
Requires:       perl(Text::Affixes) >= 0.07
Requires:       perl(Text::Ngram) >= 0.13
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Factory::Util|Text::Affixes|Text::Ngram)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Class::Factory::Util)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::Affixes)
BuildRequires:  perl(Text::ExtractWords)
BuildRequires:  perl(Text::Ngram)
BuildRequires:  perl(base)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Lingua-Identify-tools -f %{oreon_filedir}/perl-Lingua-Identify-tools.list

%changelog

%autochangelog
