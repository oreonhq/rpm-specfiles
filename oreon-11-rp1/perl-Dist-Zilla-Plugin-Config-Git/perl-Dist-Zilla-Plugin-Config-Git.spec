%global source0_hash 502f35869dd0841cb985e707d025ec65d14dd4f389c624870026874f9bdf82a5
Name:           perl-Dist-Zilla-Plugin-Config-Git
Version:        0.92
Release:        1%{?dist}
Summary:        Dist::Zilla configuration for a Git repository
License:        Artistic-2.0
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Config-Git
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBYRD/Dist-Zilla-Plugin-Config-Git-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::Zilla::Role::Plugin) >= 1.000
Requires:       perl(Moose) >= 0.34
Requires:       perl(MooseX::Types) >= 0.06
Requires:       perl(namespace::clean) >= 0.06
Requires:       perl(String::Errf) >= 0.001
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Moose|MooseX::Types|namespace::clean|String::Errf)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Dist::Zilla::Role::Plugin)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(String::Errf)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a Dist::Zilla configuration plugin for Git repository/branch
information.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-Config-Git-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
