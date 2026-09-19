%global source0_hash 6ff145cecdeabc7f3527653356795af4230df695b7d8704f96987a7f95443ed4

Name:           perl-Devel-Autoflush
Version:        0.06
Release:        34%{?dist}
Summary:        Set autoflush from the command line
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Devel-Autoflush
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Devel-Autoflush-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::CaptureOutput) >= 1.08
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(version)

# Filter bogus dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(strict\\)

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

%check
make test

%files
%doc Changes LICENSE README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
