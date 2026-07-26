%global source0_hash 704005635afc79be5fce4d164652ebfb27b79c1034bfbe09d416efb80881954b

Name:           perl-POE-XS-Queue-Array
Version:        0.006
Release:        37%{?dist}
Summary:        XS implementation of POE::Queue::Array
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-XS-Queue-Array
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TONYC/POE-XS-Queue-Array-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
# Prefer XSLoader over DynaLoader
BuildRequires:  perl(POE::Queue)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(Config)
BuildRequires:  perl(Errno)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
# Prefer XSLoader over DynaLoader
Requires:       perl(XSLoader)

%description
This class is an implementation of the abstract POE::Queue interface. It
implements a priority queue using C, with an XS interface supplied.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-XS-Queue-Array-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files

%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
%autochangelog
