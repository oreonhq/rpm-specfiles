%global source0_hash acb499aa7206eb9db21eb85357a74521bfe3bdae4a6416d50a7c75b939cf56fe

Name:           perl-Meta-Builder
Version:        0.004
Release:        21%{?dist}
Summary:        Tools for creating Meta objects to track custom metrics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Meta-Builder
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Meta-Builder-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fennec::Lite)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

%description
Meta programming is becoming more and more popular. The popularity of Meta
programming comes from the fact that many problems are made significantly
easier. There are a few specialized Meta tools out there, for instance
Class:MOP which is used by Moose to track class metadata.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Meta-Builder-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
