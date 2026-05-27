%global source0_hash ba022a05b1adbec73712c46f233d8489fe13a1b9fc40a1fcceed9b52f90defc1

Name:           perl-Digest-CRC
Version:        0.24
Release:        13%{?dist}
Summary:        Generic CRC functions
License:        LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Digest-CRC
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLIMAUL/Digest-CRC-0.24.tar.gz

# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Fcntl)
# Dependencies
Requires:       perl(DynaLoader)
Requires:       perl(Symbol)

%description
The Digest::CRC module calculates CRC sums of all sorts. It contains wrapper
functions with the correct parameters for CRC-SAE-J1850, CRC-CCITT, CRC-16 and
CRC-32.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -qn Digest-CRC-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test TEST_VERBOSE=1

%files
%doc Changes README
%{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/Digest/
%{_mandir}/man3/Digest::CRC.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.24-13
- Prepare for Oreon 11 (RP1)
