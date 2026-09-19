%global source0_hash 6a5a48c5888f4d05c604df339a79f8a1028db56ac0a0c85755537f739fb6e2de

Name:           perl-DateTime-Format-Natural
Version:        1.25
Release:        1%{?dist}
Summary:        Create machine readable date/time with natural parsing logic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-Natural
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCHUBIGER/DateTime-Format-Natural-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::HiRes)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(Params::Validate) >= 1.15
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::MockTime::HiRes)
BuildRequires:  perl(Test::More)
Requires:       perl(Params::Validate) >= 1.15

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Params::Validate\\)$

%description
DateTime::Format::Natural takes a string with a human readable date/time
and creates a machine readable one by applying natural parsing logic.

%package Test
Summary:        Common test routines/data for perl-DateTime-Format-Natural
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Test
The DateTime::Format::Natural::Test class exports common test routines.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-Natural-%{version}
for f in Changes README; do
        iconv -f iso8859-1 -t utf-8 $f >$f.conf && mv $f.conf $f
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*.t
# Does not work for modules which are placed in %{perl_vendorlib}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-load.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%doc Changes README
%dir %{perl_vendorlib}/DateTime
%dir %{perl_vendorlib}/DateTime/Format
%{perl_vendorlib}/DateTime/Format/Natural
%exclude %{perl_vendorlib}/DateTime/Format/Natural/Test.pm
%{perl_vendorlib}/DateTime/Format/Natural.pm
%{_bindir}/dateparse
%{_mandir}/man1/dateparse.*
%{_mandir}/man3/DateTime::Format::Natural.*
%{_mandir}/man3/DateTime::Format::Natural::*
%exclude %{_mandir}/man3/DateTime::Format::Natural::Test.*

%files Test
%{perl_vendorlib}/DateTime/Format/Natural/Test.pm
%{_mandir}/man3/DateTime::Format::Natural::Test.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
