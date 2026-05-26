Name:           perl-Text-vFile-asData
Version:        0.08
Release:        40%{?dist}
Summary:        Parse vFile formatted files into data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-vFile-asData
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Text-vFile-asData-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 b291ab5e0f987c5172560a692234711a75e4596d83475f72d01278369532f82a
%global source0_file Text-vFile-asData-0.08.tar.gz
# oreon url source checksums end
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Class::Accessor::Chained)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

# for improved tests
BuildRequires:  perl(Test::Pod) >= 1.00

# rpm doesn't catch this
Requires:       perl(Class::Accessor::Chained::Fast)

%description
Text::vFile::asData reads vFile format files, such as vCard (RFC 2426) and
vCalendar (RFC 2445).

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Text-vFile-asData-0.08.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b291ab5e0f987c5172560a692234711a75e4596d83475f72d01278369532f82a" || { echo "oreon: Source0 SHA256 mismatch for Text-vFile-asData-0.08.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Text-vFile-asData-%{version}

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.08-40
- Prepare for Oreon 11 (RP1)
