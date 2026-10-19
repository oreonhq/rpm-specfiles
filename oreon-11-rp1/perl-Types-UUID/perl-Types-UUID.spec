%global source0_hash 7937e4b74c3137dc9df0e9d691a5eae704164eb6e6088c7ba8e2efcbc0c72237
%bcond_without perl_Types_UUID_enables_optional_test
Name:           perl-Types-UUID
Version:        0.004
Release:        28%{?dist}
Summary:        Type constraints for UUIDs
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ((GPL-1.0-or-later OR Artistic-1.0-Perl) OR CC-BY-SA-2.0-UK) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Types-UUID
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Types-UUID-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Types_UUID_enables_optional_test}
%endif
Requires:       perl(Type::Tiny) >= 1.000000
Requires:       perl(UUID::Tiny) >= 1.02
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Type::Tiny|UUID::Tiny)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TypeTiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(UUID::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Types-UUID-tests -f %{oreon_filedir}/perl-Types-UUID-tests.list

%changelog

%autochangelog
