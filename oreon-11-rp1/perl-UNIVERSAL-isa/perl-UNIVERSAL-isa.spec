Name:           perl-UNIVERSAL-isa
Version:        1.20171012
Release:        25%{?dist}
Summary:        Hack around module authors using UNIVERSAL::isa as a function
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-isa
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/UNIVERSAL-isa-1.20171012.tar.gz
# oreon url source checksums begin
%global source0_sha256 d16956036cb01c819dec7d294f6ef891be0bb64876989601354b293164da7f2b
%global source0_file UNIVERSAL-isa-1.20171012.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(overload)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Dependencies
# (none)

%description
Whenever you use "isa" in UNIVERSAL as a function, a kitten using
Test::MockObject dies. Normally, the kittens would be helpless, but
if they use UNIVERSAL::isa (the module whose docs you are reading),
the kittens can live long and prosper.

This module replaces UNIVERSAL::isa with a version that makes sure
that if it's called as a function on objects which override isa,
isa will be called on those objects as a method.

In all other cases the real UNIVERSAL::isa is just called directly.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/UNIVERSAL-isa-1.20171012.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d16956036cb01c819dec7d294f6ef891be0bb64876989601354b293164da7f2b" || { echo "oreon: Source0 SHA256 mismatch for UNIVERSAL-isa-1.20171012.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n UNIVERSAL-isa-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/UNIVERSAL::isa.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20171012-25
- Prepare for Oreon 11 (RP1)
