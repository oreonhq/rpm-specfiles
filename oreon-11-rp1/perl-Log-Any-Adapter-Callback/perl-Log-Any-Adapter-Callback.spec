%global source0_hash 7c01883265bdab65344257c1b1d1e69fbe300e7693dddeebb98f9f67310e07cd

Name:           perl-Log-Any-Adapter-Callback
Version:        0.102
Release:        7%{?dist}
Summary:        Send Log::Any logs to a subroutine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Log-Any-Adapter-Callback
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Log-Any-Adapter-Callback-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Log::Any::Adapter::Base)
BuildRequires:  perl(Log::Any::Adapter::Util)
# Tests:
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This adapter lets you specify callback subroutine to be called by
Log::Any's logging methods (like $log->debug(), $log->error(), etc) and
detection methods (like $log->is_warning(), $log->is_fatal(), etc.).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Any-Adapter-Callback-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Log*
%{_mandir}/man3/*

%changelog
%autochangelog
