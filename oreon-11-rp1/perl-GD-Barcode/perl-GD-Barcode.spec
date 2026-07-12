%global source0_hash 1384dbbe99513d17a16045e6f659110a6dcd11a7a445114a42518bcef08bd2a6

# Perform optional tests
%bcond_without perl_GD_Barcode_enables_optional_test

# Break a build cycle perl-Business-ISBN → perl-GD-Barcode
%if %{with perl_GD_Barcode_enables_optional_test} && !%{defined perl_bootstrap}
%define optional_test 1
%else
%define optional_test 0
%endif

Name:           perl-GD-Barcode
Version:        2.02
Release:        2%{?dist}
Summary:        Create barcode image with GD
# see Barcode.pm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GD-Barcode
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/GD-Barcode-2.02.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
buildrequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(GD)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(ok)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
%if %{optional_test}
# Optional tests
BuildRequires:  perl(Business::ISBN) >= 3.007
BuildRequires:  perl(Test2::Require::Module)
%endif
# definitely not picked up automagically.
Requires:       perl(GD)

Provides:       perl(GD::Barcode::EAN13)
Provides:       perl(GD::Barcode)
%description
GD::Barcode is a subclass of GD and allows you to create barcode images 
with GD. 

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{optional_test}
Requires:       perl(Business::ISBN) >= 3.007
%endif
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n GD-Barcode-%{version}
%if !%{optional_test}
rm t/business-isbn-png-barcode.t
perl -i -ne 'print $_ unless m{^t/business-isbn-png-barcode\.t\b}' MANIFEST
%endif
for i in `find sample/ -type f`; do
    perl -pi -e 's/\r//' $i
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

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
%doc Changes README sample
%{perl_vendorlib}/GD*
%{_mandir}/man3/GD::Barcode*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
