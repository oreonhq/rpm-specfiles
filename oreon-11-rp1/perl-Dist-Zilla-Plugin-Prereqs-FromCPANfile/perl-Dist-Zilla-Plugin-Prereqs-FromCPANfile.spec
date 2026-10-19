%global source0_hash 948c3e31c13223800da7336c93b7222b5e4d1d865d9837a7427069ff4d6774d4
Name:           perl-Dist-Zilla-Plugin-Prereqs-FromCPANfile
Version:        0.08
Release:        1%{?dist}
Summary:        Parse cpanfile for Dist::Zilla prerequisites
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Prereqs-FromCPANfile
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-Prereqs-FromCPANfile-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
Requires:       perl(Dist::Zilla) >= 4.300017
Requires:       perl(Module::CPANfile) >= 0.903
Requires:       perl(Try::Tiny) >= 0.1
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::CPANfile|Try::Tiny)\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is is a Dist::Zilla plugin to read cpanfile to determine prerequisites
for your distribution. This does the opposite of what
Dist::Zilla::Plugin::CPANFile does, which is to create a cpanfile using the
prerequisites collected elsewhere.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-Prereqs-FromCPANfile-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
