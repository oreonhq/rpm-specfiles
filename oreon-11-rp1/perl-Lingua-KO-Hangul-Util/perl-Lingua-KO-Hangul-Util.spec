%global source0_hash 23f186698affa1a0197e3a8615af3ab5eed6a0d55bf36914a52479ba22642a29

Name:           perl-Lingua-KO-Hangul-Util
Version:        0.28
Release:        28%{?dist}
Summary:        Utility functions for Hangul in Unicode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-KO-Hangul-Util
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SADAHIRO/Lingua-KO-Hangul-Util-%{version}.tar.gz
# Build
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(bytes)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# Tests only
# -

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-KO-Hangul-Util-%{version}

%build
perl enableXS
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Lingua
%{_mandir}/man3/*

%changelog
%autochangelog
