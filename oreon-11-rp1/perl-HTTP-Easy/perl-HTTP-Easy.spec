%global source0_hash 9cf0f711007ef06bb7b18dbe45368249f6c0f67c40663877f7675815e0bf4801

Name:           perl-HTTP-Easy
Version:        0.04
Release:        8%{?dist}
Summary:        HTTP helpers for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/Mons/HTTP-Easy
Source0:        https://github.com/Mons/HTTP-Easy/archive/refs/tags/%{version}/HTTP-Easy-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(:VERSION) >= 5.8.8
# tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib::abs)
BuildRequires:  perl(URI)

%description
Set of useful helpers for HTTP work with Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Easy-%{version}

%build
unset AUTHOR
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
