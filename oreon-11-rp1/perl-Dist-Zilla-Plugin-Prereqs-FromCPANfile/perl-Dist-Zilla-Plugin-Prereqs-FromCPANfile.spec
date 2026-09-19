%global source0_hash 948c3e31c13223800da7336c93b7222b5e4d1d865d9837a7427069ff4d6774d4

Name:           perl-Dist-Zilla-Plugin-Prereqs-FromCPANfile
Version:        0.08
Release:        27%{?dist}
Summary:        Parse cpanfile for Dist::Zilla prerequisites
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Prereqs-FromCPANfile
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-Prereqs-FromCPANfile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Dist::Zilla) >= 4.300017
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Module::CPANfile) >= 0.903
BuildRequires:  perl(Moose)
BuildRequires:  perl(Try::Tiny) >= 0.1
# Tests:
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
Requires:       perl(Dist::Zilla) >= 4.300017
Requires:       perl(Module::CPANfile) >= 0.903
Requires:       perl(Try::Tiny) >= 0.1

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::CPANfile|Try::Tiny)\\)$

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

%check
./Build test

%files
%license LICENSE
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
