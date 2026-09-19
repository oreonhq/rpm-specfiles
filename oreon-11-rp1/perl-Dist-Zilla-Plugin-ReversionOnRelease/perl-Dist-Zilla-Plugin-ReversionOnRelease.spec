%global source0_hash e5be619fc0a264d1fa2bf1dee2edfac04a1accc95fea650ab3c7f81db70bc305

Name:           perl-Dist-Zilla-Plugin-ReversionOnRelease
Version:        0.06
Release:        27%{?dist}
Summary:        Bump and reversion version on release
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-ReversionOnRelease
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-ReversionOnRelease-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# This is a Dist::Zilla plugin
BuildRequires:  perl(Dist::Zilla) >= 4.2
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(Dist::Zilla::Role::FileFinderUser)
BuildRequires:  perl(Moose)
BuildRequires:  perl(version)
BuildRequires:  perl(Version::Next) >= 0.002
# Tests:
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
# Optional tests:
BuildRequires:  perl(Dist::Zilla::Plugin::VersionFromModule)
# This is a Dist::Zilla plugin
Requires:       perl(Dist::Zilla) >= 4.2
Requires:       perl(Dist::Zilla::Role::FileMunger)
Requires:       perl(Dist::Zilla::Role::FileFinderUser)
Requires:       perl(Version::Next) >= 0.002

# Remove under-specified dependenices
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Version::Next\\)$

%description
This is a Dist::Zilla plugin that bumps version (a la perl-reversion -bump)
in-place with the .pm files inside lib. You should most likely use this
plugin in combination with Dist::Zilla::Plugin::VersionFromModule so that
current VERSION is taken out of your main module, and then the released
file is written back after the release with
Dist::Zilla::Plugin::CopyFilesFromRelease.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-ReversionOnRelease-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
