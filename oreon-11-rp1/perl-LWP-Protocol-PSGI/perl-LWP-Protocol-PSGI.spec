%global source0_hash a4bc72f4376843fcfb25ed543232e8921334d13629f24518599c44194c1a7312

Name:           perl-LWP-Protocol-PSGI
Version:        0.11
Release:        19%{?dist}
Summary:        Override LWP's HTTP/HTTPS backend with your own PSGI application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Protocol-PSGI
Source0:        https://cpan.metacpan.org/modules/by-module/LWP/LWP-Protocol-PSGI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

%description
LWP::Protocol::PSGI is a module to hijack any code that uses LWP::UserAgent
underneath such that any HTTP or HTTPS requests can be routed to your own
PSGI application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LWP-Protocol-PSGI-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
