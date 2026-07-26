%global source0_hash e6b3614e72b5e6b0735c2cdf2c6c01e889094565ccaa543a53c2badc121125ae

Name:           perl-PerlIO-locale
Version:        0.10
Release:        40%{?dist}
Summary:        PerlIO layer to use the encoding of the current locale
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlIO-locale
Source0:        https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/PerlIO-locale-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(strict)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%{?perl_default_filter}

%description
This is mostly a per-file-handle version of the open pragma, when used under
the form:
   
use open ':locale';

The encoding for the opened file will be set to the encoding corresponding to
the locale currently in effect, if perl can guess it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PerlIO-locale-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE='%{optflags}'
make %{?_smp_mflags}

%install
make pure_install DESTDIR='%{buildroot}'
find '%{buildroot}' -type f -name '*.bs' -size 0 -delete
%{_fixperms} '%{buildroot}'/*

%check
make test

%files
%doc README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PerlIO*
%{_mandir}/man3/*

%changelog
%autochangelog
