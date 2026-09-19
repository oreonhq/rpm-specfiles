%global source0_hash 32a50011e955ac6f3b79e0ce5356e4dd9d0430ab15e5630c736c6fe58efe2703

Name:           perl-Graphics-Toolkit-Color
Version:        1.972
Release:        2%{?dist}
Summary:        Color palette constructor
# lib/Graphics/Toolkit/Color.pm:        GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Name.pm:       GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Name/Constant.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Name/Scheme.pm:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Space.pm:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Space/Hub.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:      GPL-1.0-or-later OR Artistic-1.0-Perl
# README:       GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graphics-Toolkit-Color
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/Graphics-Toolkit-Color-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter) >= 5
# Optional run-time:
# Graphics::ColorNames::$schema, where $schema is a user-supplied string, is
# loaded under eval in Graphics::Toolkit::Color::Name::try_get_scheme(). These
# schemata are spread over many packages, we cannot and should not list all of
# them we know of. None of them is used at tests.
# Tests:
BuildRequires:  perl(Test::More) >= 1.3
Requires:       perl(Exporter) >= 5

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter|Test::More|)\\)$

%description
Read-only, color-holding Perl objects with methods to obtain their RGB, HSL,
and YIQ values and if possible a name. This is because humans access colors on
hardware level (eye) in RGB, on cognition level in HSL (brain) and on cultural
level (language) with names. There objects also have methods for measuring
color distances and generating related color objects like gradients and
complements. Having easy access to all three and some color math should enable
you to get the color palette you desire.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness 
Requires:       perl(Test::More) >= 1.3

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Graphics-Toolkit-Color-%{version}
chmod +x t/*.t

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
%doc Changes CONTRIBUTING README
%dir %{perl_vendorlib}/Graphics
%dir %{perl_vendorlib}/Graphics/Toolkit
%{perl_vendorlib}/Graphics/Toolkit/Color*
%{_mandir}/man3/Graphics::Toolkit::Color*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
