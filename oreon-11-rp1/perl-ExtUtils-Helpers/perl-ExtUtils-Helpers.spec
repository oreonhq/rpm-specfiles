Name:		perl-ExtUtils-Helpers
Version:	0.028
Release:	4%{?dist}
Summary:	Various portability utilities for module builders
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/ExtUtils-Helpers
Source0:	https://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-Helpers-0.028.tar.gz
# oreon url source checksums begin
%global source0_sha256 c8574875cce073e7dc5345a7b06d502e52044d68894f9160203fcaab379514fe
%global source0_file ExtUtils-Helpers-0.028.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module (File::Copy only needed for VMS support, not packaged)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(strict)
BuildRequires:	perl(Text::ParseWords) >= 3.24
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Cwd)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More)
# Dependencies
# (none)

%description
This module provides various portable helper functions for module building
modules.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ExtUtils-Helpers-0.028.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c8574875cce073e7dc5345a7b06d502e52044d68894f9160203fcaab379514fe" || { echo "oreon: Source0 SHA256 mismatch for ExtUtils-Helpers-0.028.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n ExtUtils-Helpers-%{version}

# Don't include VMS and Windows helpers, which may pull in unwelcome dependencies
rm -f lib/ExtUtils/Helpers/{VMS,Windows}.pm
perl -ni -e 'print unless /^lib\/ExtUtils\/Helpers\/(VMS|Windows)\.pm$/;' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/ExtUtils/
%{_mandir}/man3/ExtUtils::Helpers.3*
%{_mandir}/man3/ExtUtils::Helpers::Unix.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.028-4
- Prepare for Oreon 11 (RP1)
