%global source0_hash 3791c9c3ae5661f5669fc0e81b8481d22382a66d5a3b598d84073aba59b706c9

Name:           perl-MooseX-Types-DateTimeX
Version:        0.10
Release:        47%{?dist}
Summary:        Extensions to MooseX::Types::DateTime::ButMaintained
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Types-DateTimeX
Source0:        https://cpan.metacpan.org/authors/id/E/EC/ECARROLL/MooseX-Types-DateTimeX-%{version}.tar.gz
# https://rt.cpan.org/Public/Bug/Display.html?id=73467
Patch0:         MooseX-Types-DateTimeX-0.10-fix_subtypes.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTimeX::Easy) >= 0.085
BuildRequires:  perl(Moose) >= 0.41
BuildRequires:  perl(MooseX::Types) >= 0.04
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::DateTime::ButMaintained) >= 0.04
BuildRequires:  perl(namespace::clean) >= 0.08
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::Duration::Parse) >= 0.06
BuildRequires:  perl(warnings)
# Tests only:
# perl(DateTime::Format::DateManip) missing in META.yml
BuildRequires:  perl(DateTime::Format::DateManip)
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok) >= 0.02
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

%check
make test

%files
%doc Changes
%dir %{perl_vendorlib}/MooseX
%{perl_vendorlib}/MooseX/Types*
%{_mandir}/man3/MooseX::Types::DateTimeX*

%changelog
%autochangelog
