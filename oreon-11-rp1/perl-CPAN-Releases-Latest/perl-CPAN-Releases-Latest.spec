%global source0_hash 76ee12701df4c177dcf3c4f3e87c62cb1ca87643f025c177230ba0d8cddf1c9b
Name:           perl-CPAN-Releases-Latest
Version:        0.08
Release:        1%{?dist}
Summary:        Find latest release of all distributions on CPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Releases-Latest
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/CPAN-Releases-Latest-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Time::Duration::Parse)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(MetaCPAN::Client)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(autodie)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module constructs a list of all distributions on CPAN, by default
using the MetaCPAN API. The generated index is cached locally. It will let you
iterate over the index, either release by release, or distribution by
distribution.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-Releases-Latest-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
