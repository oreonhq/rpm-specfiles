%global source0_hash a90eadf9c8af24a516bb9a1b67061f641853f90b8fee9ffc24d2bb9720e8b99b

Name:           perl-Metrics-Any
Version:        0.10
Release:        8%{?dist}
Summary:        Abstract collection of monitoring metrics
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Metrics-Any/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Metrics-Any-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Errno)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test2::V0)

%{?perl_default_filter}

Provides:       perl(Metrics::Any)
Provides:       perl(Metrics::Any::Adapter)
Provides:       perl(Metrics::Any::Adapter::Test)
Provides:       perl(Metrics::Any)
%description
Provides a central location for modules to report monitoring metrics, such
as counters of the number of times interesting events have happened, and
programs to collect up and send those metrics to monitoring services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Metrics-Any-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Metrics*
%{_mandir}/man3/Metrics*

%changelog
%autochangelog
