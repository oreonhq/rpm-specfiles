%global source0_hash 42ed38e8eeb2ad6274fd850d23867fffd918d132ea33bd2b7363c992c2d48362

Name:           perl-POE-Component-Resolver
Version:        0.921
Release:        34%{?dist}
Summary:        Non-blocking getaddrinfo() resolver
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Resolver
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Resolver-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE) >= 1.311
BuildRequires:  perl(POE::Filter::Reference)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(Scalar::Util) >= 1.23
BuildRequires:  perl(Socket) > 2.001
BuildRequires:  perl(Storable) >= 2.18
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Time::HiRes) >= 1.9711
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(POE) >= 1.311
Requires:       perl(POE::Filter::Reference)
Requires:       perl(POE::Wheel::Run)
Requires:       perl(Socket) >= 2.001
Requires:       perl(Storable) >= 2.18
Requires:       perl(Time::HiRes) >= 1.9711

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(POE\\)
%global __requires_exclude %__requires_exclude|^perl\\(Socket\\)
%global __requires_exclude %__requires_exclude|^perl\\(Storable\\)
%global __requires_exclude %__requires_exclude|^perl\\(Time::HiRes\\)

%description
POE::Component::Resolver performs Socket::GetAddrInfo::getaddrinfo() calls
in subprocesses where they're permitted to block as long as necessary.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Resolver-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
# Remove resolver test which doesn't work in koji
rm -f t/01-basic.t
make test

%files
%doc CHANGES LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
