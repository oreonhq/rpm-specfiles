%global source0_hash a9e3a51dc7a5eb3fbcf97138ea53f68830af4a36cbe0d562ec0c32904f28a8f8

Name:           perl-ExtUtils-InstallPAR
Version:        0.03
Release:        48%{?dist}
Summary:        Install .par's into any installed perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-InstallPAR
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-InstallPAR-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::InferConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(PAR::Dist) >= 0.40
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(ExtUtils::InferConfig)

%description
This module installs PAR distributions (i.e. .par files) into any perl
installation on the system. The PAR::Dist module can install into the
currently running perl by default and provides the necessary parameters to
override any installation directories. Figuring out how to use those
overrides in order to install into an arbitrary perl installation on the
system may be beyond most users, however. Hence this convenience wrapper
using ExtUtils::InferConfig to automatically determine the typical site
installation paths of any perl interpreter than can be executed by the
current user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-InstallPAR-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
