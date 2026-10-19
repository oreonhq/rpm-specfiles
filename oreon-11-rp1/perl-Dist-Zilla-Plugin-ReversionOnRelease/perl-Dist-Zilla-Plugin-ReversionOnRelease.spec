%global source0_hash e5be619fc0a264d1fa2bf1dee2edfac04a1accc95fea650ab3c7f81db70bc305
Name:           perl-Dist-Zilla-Plugin-ReversionOnRelease
Version:        0.06
Release:        1%{?dist}
Summary:        Bump and reversion version on release
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-ReversionOnRelease
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-ReversionOnRelease-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::Zilla) >= 4.2
Requires:       perl(Dist::Zilla::Role::FileMunger)
Requires:       perl(Dist::Zilla::Role::FileFinderUser)
Requires:       perl(Version::Next) >= 0.002
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Version::Next\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::Plugin::VersionFromModule)
BuildRequires:  perl(Dist::Zilla::Role::FileFinderUser)
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Version::Next)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
