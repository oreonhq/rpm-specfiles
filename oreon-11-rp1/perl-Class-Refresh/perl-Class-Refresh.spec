%global source0_hash e3b0035355cbb35a2aee3f223688d578946a7a7c570acd398b28cddb1fd4beb3

Name:           perl-Class-Refresh
Version:        0.07
Release:        28%{?dist}
Summary:        Refresh your classes during run time
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Refresh
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/Class-Refresh-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Unload)
BuildRequires:  perl(Devel::OverrideGlobalRequire)
BuildRequires:  perl(Try::Tiny)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
# Optional tests:
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::Moose)
Requires:       perl(B)
Requires:       perl(Devel::OverrideGlobalRequire)

%description
During development, it is fairly common to cycle between writing code and
testing that code. Generally the testing happens within the test suite, but
frequently it is more convenient to test things by hand when tracking down
a bug, or when doing some exploratory coding. In many situations, however,
this becomes inconvenient - for instance, in a REPL, or in a stateful web
application, restarting from the beginning after every code change can get
pretty tedious. This module allows you to reload your application classes
on the fly, so that the code/test cycle becomes a lot easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Refresh-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
