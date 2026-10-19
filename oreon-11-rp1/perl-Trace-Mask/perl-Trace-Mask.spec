%global source0_hash 8f252a8f7a696d6380c82bbe78546818928ca55071ad05577972dc09d7538e24
Name:           perl-Trace-Mask
Version:        0.000008
Release:        28%{?dist}
Summary:        Masking frames in stack traces
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Trace-Mask
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Trace-Mask-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Scalar::Util) >= 1.10
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|List::Util|Scalar::Util)\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Bundle::Extended)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Suite)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::Tools::Subtest)
BuildRequires:  perl(Test2::Workflow)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
Requires:       perl(Test2) >= 1.302026
Requires:       perl(Test2::API)
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Trace-Mask-Test -f %{oreon_filedir}/perl-Trace-Mask-Test.list

%changelog

%autochangelog
