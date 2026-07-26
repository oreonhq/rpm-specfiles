%global source0_hash 8a6cb97aea2f5cfa4fad85d8c39c0ff27822a598626aba4e7f456e0f6d1ff30a

# Run optional test
%{bcond_without perl_Data_Float_enables_optional_test}

Name:           perl-Data-Float
Version:        0.015
Release:        3%{?dist}
Summary:        Details of the floating point data type
# README:       GPL-1.0-or-later OR Artistic-1.0-Perl
# SECURITY.md:  Relicensed by the author from CC-BY-SA-4.0 to
#               GPL-1.0-or-later OR Artistic-1.0-Perl
#               <https://github.com/robrwo/Data-Float/issues/3>
#               Later, CC-BY-SA-4.0 changed to CC0-1.0.
#               Later, CC0-1.0 changed to 0BSD which isn't virulent.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Float
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Data-Float-%{version}.tar.gz
# License clarification for SECURITY.md
Source1:        security.md.license_clarification
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
%if %{with perl_Data_Float_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
%endif
Requires:       perl(constant)
Requires:       perl(integer)

%description
This module is about the native floating point numerical data type. A floating
point number is one of the types of datum that can appear in the numeric part
of a Perl scalar. This module supplies constants describing the native
floating point type, classification functions, and functions to manipulate
floating point values at a low level.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Float-%{version}
install -m 0644 %{SOURCE1} security.md.license_clarification

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# POD tests only work on ./lib modules
rm %{buildroot}%{_libexecdir}/%{name}/t/pod_*.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license security.md.license_clarification
%doc Changes README SECURITY.md
%dir %{perl_vendorlib}/Data
%{perl_vendorlib}/Data/Float.pm
%{_mandir}/man3/Data::Float.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
