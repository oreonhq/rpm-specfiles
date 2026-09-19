%global source0_hash 734767e83620eadd80dc466b67102cc55643a2278d20c304b75d401f075fbd13

Name:           perl-Net-IP-Minimal
Version:        0.06
Release:        33%{?dist}
Summary:        Minimal functions from Net::IP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IP-Minimal
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Net-IP-Minimal-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Exporter)
# Tests only
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)

%description
Net::IP is very feature complete, but I found I was only using three of its
functions and it uses quite a bit of memory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IP-Minimal-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
