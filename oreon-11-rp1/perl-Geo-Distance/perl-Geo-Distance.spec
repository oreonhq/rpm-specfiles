%global source0_hash 2c673dd57c86208370da100f75f0482531b05306aa5f72107b0eae90b6ceb615

Name:           perl-Geo-Distance
Version:        0.25
Release:        17%{?dist}
Summary:        Calculate distances and closest locations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Geo-Distance
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/Geo-Distance-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Const::Fast) >= 0.014
BuildRequires:  perl(GIS::Distance) >= 0.14
BuildRequires:  perl(GIS::Distance::Constants) >= 0.14
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0) >= 0.000094
# Optional tests:
BuildRequires:  perl(DBD::SQLite) >= 1.46
Requires:       perl(Const::Fast) >= 0.014
Requires:       perl(GIS::Distance) >= 0.14
Requires:       perl(GIS::Distance::Constants) >= 0.14

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Const::Fast|GIS::Distance(::Constants)?)|Test2::V0\\)$

%description
This Perl library aims to provide as many tools to make it as simple as
possible to calculate distances between geographic points, and anything
that can be derived from that. Currently there is support for finding the
closest locations within a specified distance, to find the closest number
of points to a specified point, and to do basic point-to-point distance
calculations.

This Perl module is deprecated, use GIS::Distance instead.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite) >= 1.46
Requires:       perl(GIS::Distance) >= 0.14
Requires:       perl(Test2::V0) >= 0.000094

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Geo-Distance-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README.md
%dir %{perl_vendorlib}/Geo
%{perl_vendorlib}/Geo/Distance.pm
%{_mandir}/man3/Geo::Distance.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
