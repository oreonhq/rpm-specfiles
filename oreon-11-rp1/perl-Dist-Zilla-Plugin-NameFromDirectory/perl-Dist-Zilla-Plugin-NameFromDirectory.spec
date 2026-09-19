%global source0_hash 2e1307c963b81cd0f92b00116e2a60e93fd31853bda16b1dbf8e29ccbc178a86

Name:           perl-Dist-Zilla-Plugin-NameFromDirectory
Version:        0.04
Release:        27%{?dist}
Summary:        Guess distribution name from the current directory
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-NameFromDirectory
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-NameFromDirectory-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# This is a Dist::Zilla plugin
BuildRequires:  perl(Dist::Zilla) >= 4.300030
BuildRequires:  perl(Dist::Zilla::Role::NameProvider)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Path::Tiny) >= 0.053
# Tests:
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
# This is a Dist::Zilla plugin
Requires:       perl(Dist::Zilla) >= 4.300030
Requires:       perl(Dist::Zilla::Role::NameProvider)
Requires:       perl(Path::Tiny) >= 0.053

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Path::Tiny\\)$

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

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
