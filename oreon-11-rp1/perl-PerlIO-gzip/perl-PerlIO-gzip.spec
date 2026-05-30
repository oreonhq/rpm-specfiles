%global source0_hash 4848679a3f201e3f3b0c5f6f9526e602af52923ffa471a2a3657db786bd3bdc5

Name:           perl-PerlIO-gzip
Version:        0.20
Release:        31%{?dist}
Summary:        Perl extension to provide a PerlIO layer to gzip/gunzip
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlIO-gzip
Source0:        https://cpan.metacpan.org/modules/by-module/PerlIO/PerlIO-gzip-%{version}.tar.gz


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
BuildRequires:  zlib-devel
# Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(:WITH_PERLIO)

# Avoid provides from private perl objects
%{?perl_default_filter}

%description
PerlIO::gzip provides a PerlIO layer that manipulates files in the format
used by the gzip program. Compression and decompression are implemented.

This is akin to Compress::Zlib, except that it operates at the lower PerlIO
layer.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n PerlIO-gzip-%{version}

%build
perl Makefile.PL \
  INSTALLDIRS=vendor \
  OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/PerlIO/
%{perl_vendorarch}/PerlIO/
%{_mandir}/man3/PerlIO::gzip.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20-31
- Prepare for Oreon 11 (RP1)
