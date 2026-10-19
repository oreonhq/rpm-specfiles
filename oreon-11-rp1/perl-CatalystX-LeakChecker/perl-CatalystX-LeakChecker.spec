%global source0_hash 0e3aa438025adf775a631edaf7e2beb0a617f3894b40afbd875c2a57ed5bdbc0
Name:           perl-CatalystX-LeakChecker
Summary:        Debug memory leaks in Catalyst applications
Version:        0.06
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/CatalystX-LeakChecker-%{version}.tar.gz
URL:            https://metacpan.org/release/CatalystX-LeakChecker
BuildArch:      noarch
Requires:       perl(Catalyst) >= 5.8
Requires:       perl(Devel::Cycle) >= 1.11
Requires:       perl(namespace::clean) >= 0.05
Requires:       perl(PadWalker) >= 1.8
%{?perl_default_filter}
%{?perl_default_subpackage_tests}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::AttributeHelpers)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::SimpleTable)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl-generators
# /oreon:deps
%description
It's easy to create memory leaks in Catalyst applications and often
they're hard to find. This module tries to help you finding them by
automatically checking for common causes of leaks.  This module is
intended for debugging only. I suggest to not enable it in a production
environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CatalystX-LeakChecker-%{version}

%build

%{?perl_ext_env_unset}
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
