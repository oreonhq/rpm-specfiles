%global source0_hash 766728bfc1456fd348d7224a06a2f040a2120a009e8420246860ad492bb37772

Name:           perl-Devel-Callsite
Version:        1.0.1
Release:        24%{?dist}
Summary:        Get caller return OP address and Perl interpreter context
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release//Devel-Callsite
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROCKY/Devel-Callsite-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl(:VERSION) >= 5.5.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(B)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
Get caller return OP address and Perl interpreter context.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Callsite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license Artistic gpl-2.0.txt
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
%autochangelog
