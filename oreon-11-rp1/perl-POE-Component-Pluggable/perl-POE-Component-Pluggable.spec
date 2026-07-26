%global source0_hash fd5c27a7e023dd5ed23bd2c3f5482848079997005c65f8e2661af7149f271bb6

Name:       perl-POE-Component-Pluggable
Version:    1.28
Release:    27%{?dist}
# lib/POE/Component/Pluggable.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    A base class for creating plugin-enabled POE components
Source:     https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Component-Pluggable-%{version}.tar.gz
Url:        https://metacpan.org/release/POE-Component-Pluggable
BuildArch:  noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant) >= 1.17
BuildRequires:  perl(Exporter)
# Reverse dependency on POE because this is a POE plugin
BuildRequires:  perl(POE) >= 1.004
BuildRequires:  perl(Scalar::Util)
# Test::Weaken for Scalar::Util
BuildRequires:  perl(Task::Weaken)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More) >= 0.47
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
Requires:       perl(constant) >= 1.17
# Reverse dependency on POE because this is a POE plugin
Requires:       perl(POE) >= 1.004
# Test::Weaken for Scalar::Util
Requires:       perl(Task::Weaken)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(constant\\)$

%description
POE::Component::Pluggable is a base class for creating plugin enabled
POE Components. It is a generic port of POE::Component::IRC's plugin
system. If your component dispatches events to registered POE sessions,
then POE::Component::Pluggable may be a good fit for you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Pluggable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes examples/ README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
