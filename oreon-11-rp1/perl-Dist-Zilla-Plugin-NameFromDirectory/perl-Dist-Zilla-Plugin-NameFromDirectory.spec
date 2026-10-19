%global source0_hash 2e1307c963b81cd0f92b00116e2a60e93fd31853bda16b1dbf8e29ccbc178a86
Name:           perl-Dist-Zilla-Plugin-NameFromDirectory
Version:        0.04
Release:        1%{?dist}
Summary:        Guess distribution name from the current directory
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-NameFromDirectory
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-NameFromDirectory-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::Zilla) >= 4.300030
Requires:       perl(Dist::Zilla::Role::NameProvider)
Requires:       perl(Path::Tiny) >= 0.053
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Path::Tiny\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::Role::NameProvider)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a Dist::Zilla plugin to guess distribution name (when it's not set in
dist.ini) from the current working directory.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-NameFromDirectory-%{version}

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
