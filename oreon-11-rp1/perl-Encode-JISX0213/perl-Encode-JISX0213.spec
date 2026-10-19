%global source0_hash 5d0b1376717c6f0af1bc5b867899d398c404a14a247cb7a81ded5924e9f830f8
Name:           perl-Encode-JISX0213
Version:        0.04
Release:        1%{?dist}
Summary:        JIS X 0213 encoding
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Encode-JISX0213
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/Encode-JISX0213-%{version}.tar.gz
Requires:       perl(Encode::ISO2022) >= 0.03
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Encode::ISO2022\\)$
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Encode::ISO2022)
BuildRequires:  perl(Encode::ISOIRSingle)
BuildRequires:  perl(Encode::JISLegacy)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Encode-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package provides Perl encoding data for JIS X 0213.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Encode-JISX0213-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
