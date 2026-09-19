%global source0_hash b2b2f8774cddab6e3e49d34988efafe8fe0d500ff6d57b61f86614095bf1423e

%if !%{defined perl_bootstrap}
# Run optional tests.
# Disabled because perl-Geo-Point was retired (bug #1748923).
# Build-cycle: perl-GIS-Distance → perl-Geo-Point → perl-Geo-Distance
%bcond_with perl_GIS_Distance_enables_optional_test
# Use optimized implementation in C
# Build-cycle: perl-GIS-Distance-XS → perl-GIS-Distance
%bcond_without perl_GIS_Distance_enables_xs
%endif

Name:           perl-GIS-Distance
Version:        0.20
Release:        8%{?dist}
Summary:        Calculate geographic distances
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GIS-Distance
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/GIS-Distance-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Measure::Length)
BuildRequires:  perl(Const::Fast) >= 0.014
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(namespace::clean) >= 0.24
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strictures) >= 2
%if %{with perl_GIS_Distance_enables_xs}
# Optional run-time:
BuildRequires:  perl(GIS::Distance::Fast) >= 0.13
%endif
# Tests:
BuildRequires:  perl(Test2::V0) >= 0.000094
%if %{with perl_GIS_Distance_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Geo::Point) >= 0.95
BuildRequires:  perl(Test2::Require::Module)
%endif
Requires:       perl(Const::Fast) >= 0.014
%if %{with perl_GIS_Distance_enables_xs}
Recommends:     perl(GIS::Distance::Fast) >= 0.13
%endif
Requires:       perl(namespace::clean) >= 0.24

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Const::Fast|Geo::Point|namespace::clean|Test2::V0)\\)$

%description
This Perl module calculates distances between geographic points on, at the
moment, planet Earth. Various "FORMULAS" are available that provide different
levels of accuracy versus speed.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test2::V0) >= 0.000094
%if %{with perl_GIS_Distance_enables_optional_test}
Requires:       perl(Geo::Point) >= 0.95
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GIS-Distance-%{version}
%if !%{with perl_GIS_Distance_enables_optional_test}
rm t/geo_point.t
perl -i -ne 'print $_ unless m{^t/geo_point\.t}' MANIFEST
%endif
# Normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset GEO_DISTANCE_PP GIS_DISTANCE_PP
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset GEO_DISTANCE_PP GIS_DISTANCE_PP
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README.md
%dir %{perl_vendorlib}/GIS
%{perl_vendorlib}/GIS/Distance
%{perl_vendorlib}/GIS/Distance.pm
%{_mandir}/man3/GIS::Distance.*
%{_mandir}/man3/GIS::Distance::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
