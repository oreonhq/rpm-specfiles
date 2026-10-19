%global source0_hash e6b3614e72b5e6b0735c2cdf2c6c01e889094565ccaa543a53c2badc121125ae
Name:           perl-PerlIO-locale
Version:        0.10
Release:        1%{?dist}
Summary:        PerlIO layer to use the encoding of the current locale
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlIO-locale
Source0:        https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/PerlIO-locale-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
