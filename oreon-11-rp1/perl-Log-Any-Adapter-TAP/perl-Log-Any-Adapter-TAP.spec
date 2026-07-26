%global source0_hash 131f0689b2b42b1b31449714c6eda8f811dd96a7c86748f1e03b239cfd0121c0

Name:           perl-Log-Any-Adapter-TAP
Version:        0.003003
Release:        21%{?dist}
Summary:        Logging adapter suitable for use in TAP testcases

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/Log-Any-Adapter-TAP/
Source0:        http://www.cpan.org/modules/by-module/Log/Log-Any-Adapter-TAP-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::Base)
BuildRequires:  perl(Log::Any::Proxy)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
When running testcases, you probably want to see some of your logging
output.  One sensible approach is to have all warn and more serious
messages emitted as diag output on STDERR, and less serious messages
emitted as note comments on STDOUT.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Log-Any-Adapter-TAP-%{version} -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
