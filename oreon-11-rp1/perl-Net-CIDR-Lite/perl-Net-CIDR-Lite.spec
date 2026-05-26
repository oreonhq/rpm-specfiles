Name:           perl-Net-CIDR-Lite
Version:        0.22
Release:        14%{?dist}
Summary:        Perl extension for merging IPv4 or IPv6 CIDR addresses
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-CIDR-Lite
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STIGTSP/Net-CIDR-Lite-0.22.tar.gz
# oreon url source checksums begin
%global source0_sha256 4317d8cb341a617b9e0888da43c09cdffffcb0c9edf7b8c9928d742a563b8517
%global source0_file Net-CIDR-Lite-0.22.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# Explicit Requirements
# (none)

%description
Faster alternative to Net::CIDR when merging a large number of CIDR address
ranges. Works for IPv4 and IPv6 addresses.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Net-CIDR-Lite-0.22.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4317d8cb341a617b9e0888da43c09cdffffcb0c9edf7b8c9928d742a563b8517" || { echo "oreon: Source0 SHA256 mismatch for Net-CIDR-Lite-0.22.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Net-CIDR-Lite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::CIDR::Lite.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.22-14
- Prepare for Oreon 11 (RP1)
