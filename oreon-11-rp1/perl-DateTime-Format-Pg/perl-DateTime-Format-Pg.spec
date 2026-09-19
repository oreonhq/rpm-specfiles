%global source0_hash 38bb9666524dc384c3366f6342cb9656c50bac0f9716a3d44f1cf552ccbe0eb9

Name:           perl-DateTime-Format-Pg
Version:        0.16014
Release:        14%{?dist}
Summary:        Parse and format PostgreSQL dates and times
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-Pg
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/DateTime-Format-Pg-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime) >= 0.13
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::Builder) >= 0.72
BuildRequires:  perl(DateTime::TimeZone) >= 0.12
BuildRequires:  perl(DateTime::TimeZone::Floating)
BuildRequires:  perl(DateTime::TimeZone::UTC)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This module understands the formats used by PostgreSQL for its DATE, TIME,
TIMESTAMP, and INTERVAL data types. It can be used to parse these formats
in order to create DateTime or DateTime::Duration objects, and it can take
a DateTime or DateTime::Duration object and produce a string representing
it in a format accepted by PostgreSQL.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-Pg-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

# Remove optional tests
for F in t/99-pod.t t/99-pod-coverage.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
