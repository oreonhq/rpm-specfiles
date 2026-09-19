%global source0_hash c36fd2b68d48c2e17417bf2873c78820f3ae02460fdf5976b8eeab887d59e16c

Name:           perl-Date-Handler
Version:        1.2
Release:        35%{?dist}
Summary:        Easy but complete date object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Handler
Source0:        https://cpan.metacpan.org/modules/by-module/Date/Date-Handler-%{version}.tar.gz
# Set POD encoding, CPAN RT#149879, proposed to an upstream.
Patch0:         Date-Handler-1.2-Set-an-encoding-for-POD.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
# For a iconv tool
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-es
BuildRequires:  glibc-langpack-fr
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
# Date::Handler::Test exhibts non-UTC zone and thus t/7intuitivedst.t would
# fail.
BuildRequires:  tzdata
# Date::Handler::new() defaults to en_US locale, bug #2240533.
Requires:       glibc-langpack-en
# To support non-UTC time zones
Recommends:     tzdata

%description
Date::Handler is a container for dates that holds all the methods to
transform itself from a time zone to a time zone and to format itself.

%package Test
Summary:        Test module for Date::Handler
Requires:       %{name} = %{version}-%{release}
# The test library exhibits America/Montreal time zone
Requires:       tzdata
Requires:       glibc-langpack-es
Requires:       glibc-langpack-fr
Conflicts:      perl-Date-Handler < 1.2-18

%description Test
This Perl module provides a series of test cases to be run during the
"make test" of the Date::Handler module.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Date-Handler-%{version}
find -type f -exec chmod 0644 {} +
iconv --from=ISO-8859-1 --to=UTF-8 README > README.new
touch -r README README.new
mv README.new README
chmod a+x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 --extended_tests
%{make_build}

%install
%{make_install}
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
make test

%files
%doc Changes README
%dir %{perl_vendorlib}/Date
%dir %{perl_vendorlib}/Date/Handler
%{perl_vendorlib}/Date/Handler/Constants.pm
%{perl_vendorlib}/Date/Handler/Delta.pm
%{perl_vendorlib}/Date/Handler/Range.pm
%{perl_vendorlib}/Date/Handler.pm
%{perl_vendorlib}/Date/Handler.pod
%{_mandir}/man3/Date::Handler.*
%{_mandir}/man3/Date::Handler::Delta.*
%{_mandir}/man3/Date::Handler::Range.*

%files Test
%{perl_vendorlib}/Date/Handler/Test.*
%{_mandir}/man3/Date::Handler::Test.3pm*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
