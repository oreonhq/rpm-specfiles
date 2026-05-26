Name:		perl-Class-Inspector
Version:	1.36
Release:	20%{?dist}
Summary:	Get information about a class and its structure
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Class-Inspector
Source0:	https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Class-Inspector-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 cc295d23a472687c24489d58226ead23b9fdc2588e522f0b5f0747741700694e
%global source0_file Class-Inspector-1.36.tar.gz
# oreon url source checksums end

BuildArch: noarch

BuildRequires:	%{__make}
BuildRequires:	perl-generators
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they aren't
always very friendly, and usually involve a relatively high level of Perl
wizardry, or strange and unusual looking code. Class::Inspector attempts to
provide an easier, more friendly interface to this information.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Class-Inspector-1.36.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cc295d23a472687c24489d58226ead23b9fdc2588e522f0b5f0747741700694e" || { echo "oreon: Source0 SHA256 mismatch for Class-Inspector-1.36.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Class-Inspector-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Class
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.36-20
- Prepare for Oreon 11 (RP1)
