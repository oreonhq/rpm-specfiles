%global source0_hash 7937e4b74c3137dc9df0e9d691a5eae704164eb6e6088c7ba8e2efcbc0c72237

# Run optional test
%bcond_without perl_Types_UUID_enables_optional_test

Name:           perl-Types-UUID
Version:        0.004
Release:        28%{?dist}
Summary:        Type constraints for UUIDs
# CONTRIBUTING: (GPL-1.0-or-later OR Artistic-1.0-Perl) OR CC-BY-SA-2.0-UK
# COPYRIGHT:    LicenseRef-Fedora-Public-Domain
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ((GPL-1.0-or-later OR Artistic-1.0-Perl) OR CC-BY-SA-2.0-UK) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Types-UUID
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Types-UUID-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Tiny) >= 1.000000
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(UUID::Tiny) >= 1.02
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::TypeTiny)
%if %{with perl_Types_UUID_enables_optional_test}
# Optional tests:
BuildRequires:  perl(URI)
%endif
Requires:       perl(Type::Tiny) >= 1.000000
Requires:       perl(UUID::Tiny) >= 1.02

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Type::Tiny|UUID::Tiny)\\)$

%description
Types::UUID is a type constraint Perl library suitable for use with Moo/Moose
attributes, Kavorka sub signatures, and so forth.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Types_UUID_enables_optional_test}
Requires:       perl(URI)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Types-UUID-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
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
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS examples README
%dir %{perl_vendorlib}/Types
%{perl_vendorlib}/Types/UUID.pm
%{_mandir}/man3/Types::UUID.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
