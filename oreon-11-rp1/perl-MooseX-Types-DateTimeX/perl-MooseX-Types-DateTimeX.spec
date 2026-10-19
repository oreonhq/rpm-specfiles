%global source0_hash 3791c9c3ae5661f5669fc0e81b8481d22382a66d5a3b598d84073aba59b706c9
Name:           perl-MooseX-Types-DateTimeX
Version:        0.10
Release:        1%{?dist}
Summary:        Extensions to MooseX::Types::DateTime::ButMaintained
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Types-DateTimeX
Source0:        https://cpan.metacpan.org/authors/id/E/EC/ECARROLL/MooseX-Types-DateTimeX-%{version}.tar.gz
Patch0:         MooseX-Types-DateTimeX-0.10-fix_subtypes.patch
BuildArch:      noarch
Requires:       perl(DateTimeX::Easy) >= 0.085
Requires:       perl(Moose) >= 0.41
Requires:       perl(MooseX::Types) >= 0.04
Requires:       perl(MooseX::Types::DateTime::ButMaintained) >= 0.04
Requires:       perl(namespace::clean) >= 0.08
Requires:       perl(Time::Duration::Parse) >= 0.06
Conflicts:      perl(MooseX::Types::DateTime) < 0.05
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTimeX::Easy\\)$
%global __requires_exclude %__requires_exclude|^perl\\(MooseX::Types::DateTime::ButMaintained\\)$
%global __requires_exclude %__requires_exclude|^perl\\(namespace::clean\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Time::Duration::Parse\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::DateManip)
BuildRequires:  perl(DateTimeX::Easy)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::DateTime::ButMaintained)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(Time::Duration::Parse)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module builds on MooseX::Types::DateTime to add additional custom
types and coercions. Since it builds on an existing type, all coercions and
constraints are inherited.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-DateTimeX-%{version}
%patch -P0 -p1
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build

PERL5_CPANPLUS_IS_RUNNING=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
