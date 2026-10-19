%global source0_hash 49ad7db943b5e4989be1f68c1f0447cf9637554974ed5a3a47a4279a7f02302f
Name:           perl-MooseX-POE
Version:        0.215
Release:        39%{?dist}
Summary:        Illicit Love Child of Moose and POE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-POE
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GETTY/MooseX-POE-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Daemonize)
BuildRequires:  perl(MooseX::Declare)
BuildRequires:  perl(POE)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
%description
MooseX::POE::Object is a Moose wrapper around a POE::Session.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-POE-%{version}
find . -type f -exec chmod -c -x {} \;

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
