%global source0_hash 081bf95ec9220af26cec89161e61bf73f9fbcbfeee1d9af15139e5d7b708f445

Name: 		perl-Text-Quoted
Version: 	2.10
Release: 	22%{?dist}
Summary: 	Extract the structure of a quoted mail message
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Text-Quoted
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/Text-Quoted-%{version}.tar.gz

BuildArch: 	noarch

BuildRequires: %{__perl}
BuildRequires: %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(Test::More)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

%description
Text::Quoted examines the structure of some text which may contain multiple
different levels of quoting, and turns the text into a nested data structure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Quoted-%{version}
rm -rf inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
%autochangelog
