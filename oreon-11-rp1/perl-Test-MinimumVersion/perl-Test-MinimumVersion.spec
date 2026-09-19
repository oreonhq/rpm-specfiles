%global source0_hash 32a1ebcd803fa10eefca553bc3cedd43596a759dc3975adebd22688823c36aea

Name:		perl-Test-MinimumVersion
Version:	0.101083
Release:	9%{?dist}
Summary:	Check whether your code requires a newer perl
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-MinimumVersion
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-MinimumVersion-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	%{__make}
BuildRequires:	perl-generators
BuildRequires:	perl(base)
BuildRequires:  perl(CPAN::Meta) > 2.120900
BuildRequires:	perl(strict)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(Perl::MinimumVersion) >= 1.32
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Tester)
BuildRequires:	perl(YAML::Tiny) >= 1.40
BuildRequires:	perl(version) >= 0.70
BuildRequires:	perl(warnings)

Provides:       perl(Test::MinimumVersion) = %{version}
%description
Check whether your code requires a newer perl than you think.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-MinimumVersion-%{version}
find -type f -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Test
%{_mandir}/man3/*

%changelog
%autochangelog
