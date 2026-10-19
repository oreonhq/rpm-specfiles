%global source0_hash 6ff145cecdeabc7f3527653356795af4230df695b7d8704f96987a7f95443ed4
Name:           perl-Devel-Autoflush
Version:        0.06
Release:        1%{?dist}
Summary:        Set autoflush from the command line
License:        Apache-2.0
URL:            https://metacpan.org/release/Devel-Autoflush
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Devel-Autoflush-%{version}.tar.gz
BuildArch:      noarch
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(strict\\)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::CaptureOutput)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a hack to set autoflush for STDOUT and STDERR from the
command line or from PERL5OPT for code that needs it but doesn't have it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Autoflush-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
