%global source0_hash fd5c27a7e023dd5ed23bd2c3f5482848079997005c65f8e2661af7149f271bb6
Name:       perl-POE-Component-Pluggable
Version:    1.28
Release:        27%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        A base class for creating plugin-enabled POE components
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Component-Pluggable-%{version}.tar.gz
Url:        https://metacpan.org/release/POE-Component-Pluggable
BuildArch:  noarch
Requires:       perl(constant) >= 1.17
Requires:       perl(POE) >= 1.004
Requires:       perl(Task::Weaken)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(constant\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POE)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
