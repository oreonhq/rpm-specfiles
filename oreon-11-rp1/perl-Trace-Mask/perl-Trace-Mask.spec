%global source0_hash 8f252a8f7a696d6380c82bbe78546818928ca55071ad05577972dc09d7538e24

Name:           perl-Trace-Mask
Version:        0.000008
Release:        28%{?dist}
Summary:        Masking frames in stack traces
# License URLs in PODs are wrong
# <https://github.com/exodist/Trace-Mask/issues/2>.
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Trace-Mask
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Trace-Mask-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.03
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util) >= 1.10
BuildRequires:  perl(Scalar::Util) >= 1.10
# Test2 is the only versioned module in the perl-Test2
BuildRequires:  perl(Test2) >= 1.302026
BuildRequires:  perl(Test2::API)
# Test2::Suite is the only versioned module in the perl-Test-Suite
BuildRequires:  perl(Test2::Suite) >= 0.000030
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Subtest)
BuildRequires:  perl(Try::Tiny) >= 0.03
# Tests:
BuildRequires:  perl(Test2::Bundle::Extended)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Tools::Spec)
# Test2::Workflow is the only versioned module in the perl-Test2-Workflow
BuildRequires:  perl(Test2::Workflow) >= 0.000009
Requires:       perl(Scalar::Util) >= 1.10

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|List::Util|Scalar::Util)\\)$

%description
This is a specification packages can follow to define behaviors stack
tracers may choose to honor. If a module implements this specification than
any compliant stack tracer will render the stack trace as desired. This
package also provides some implementations (e.g. a Carp stack tracer).

%package Test
Summary:        Tools for testing Trace::Mask compliance
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Carp) >= 1.03
Requires:       perl(List::Util) >= 1.10
Requires:       perl(Scalar::Util) >= 1.10
# Test2 is the only versioned module in the perl-Test2
Requires:       perl(Test2) >= 1.302026
Requires:       perl(Test2::API)
# Test2::Suite is the only versioned module in the perl-Test-Suite
Requires:       perl(Test2::Suite) >= 0.000030
Requires:       perl(Test2::Tools::Compare)
Requires:       perl(Test2::Tools::Subtest)

%description Test
This package provides tools for testing tracers. This allows you to check
that a tracer complies with the Trace::Mask specifications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Trace-Mask-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
# README.md duplicates README's content
%doc Changes README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Trace/Mask/Test.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Trace::Mask::Test.*

%files Test
%{perl_vendorlib}/Trace/Mask/Test.pm
%{_mandir}/man3/Trace::Mask::Test.*

%changelog
%autochangelog
