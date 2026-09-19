%global source0_hash 3936bd806af2920eaac2d78acf4ac725a882546b2cba19d241d47306bc43d558

Name:           perl-MooseX-Types-DateTime-ButMaintained
Version:        0.16
Release:        39%{?dist}
Summary:        DateTime related constraints and coercions for Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Types-DateTime-ButMaintained
Source0:        https://cpan.metacpan.org/authors/id/E/EC/ECARROLL/MooseX-Types-DateTime-ButMaintained-%{version}.tar.gz
# Accept DateTime::TimeZone::Tzfile object in place of DateTime::TimeZone,
# bug #1138185
Patch0:         MooseX-Types-DateTime-ButMaintained-0.16-Accept-DateTime-TimeZone-Tzfile-object-in-place-of-D.patch
# Accept DateTime::Locale::FromData object in place of DateTime::Locale,
# bug #1283970
Patch1:         MooseX-Types-DateTime-ButMaintained-0.16-Accept-DateTime-Locale-FromData-object.patch
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
# DateTime >= 0.4302 rounded to two places
BuildRequires:  perl(DateTime) >= 0.44
# DateTime::Locale >= 0.4001 rounded to two places
BuildRequires:  perl(DateTime::Locale) >= 0.41
BuildRequires:  perl(DateTime::TimeZone) >= 0.96
BuildRequires:  perl(Moose) >= 0.41
BuildRequires:  perl(MooseX::Types) >= 0.30
BuildRequires:  perl(MooseX::Types::Moose) >= 0.30
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Olson::Abbreviations) >= 0.03
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok) >= 0.02
# DateTime >= 0.4302 rounded to two places
Requires:       perl(DateTime) >= 0.44
# DateTime::Locale >= 0.4001 rounded to two places
Requires:       perl(DateTime::Locale) >= 0.41
Requires:       perl(DateTime::TimeZone) >= 0.96

# Do not export under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime(|::Locale|::TimeZone)\\)\\s*$

%description
This module packages several Moose::Util::TypeConstraints with coercions,
designed to work with the DateTime suite of objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-DateTime-ButMaintained-%{version}
%patch -P0 -p1
%patch -P1 -p1

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
# switch off cpan installation
PERL5_CPANPLUS_IS_RUNNING=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
