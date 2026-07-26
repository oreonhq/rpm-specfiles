%global source0_hash c67f3ff343caa593a3fb0471dc98ec48f2bef3b4b4d2e00ba26e3393ceec0741

Name:           perl-GIS-Distance-Fast
Version:        0.16
Release:        11%{?dist}
Summary:        C implementation of GIS::Distance formulas
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GIS-Distance-Fast
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/GIS-Distance-Fast-%{version}.tar.gz
# Link to libm and fix linking by using EU::MM instead of buggy M::B::Tiny,
# <https://github.com/bluefeet/GIS-Distance-Fast/issues/1>
Patch0:         GIS-Distance-Fast-0.12-Build-using-ExtUtils-MakeMaker-and-link-to-math-libr.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.12
# Run-time:
BuildRequires:  perl(GIS::Distance::Formula) >= 0.17
BuildRequires:  perl(namespace::clean) >= 0.24
BuildRequires:  perl(parent)
BuildRequires:  perl(strictures) >= 2
# XSLoader || DynaLoader
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(GIS::Distance) >= 0.17
BuildRequires:  perl(Test2::V0) >= 0.000094
Requires:       perl(GIS::Distance::Formula) >= 0.17
Requires:       perl(namespace::clean) >= 0.24
# XSLoader || DynaLoader
Requires:       perl(XSLoader)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((GIS::Distance|GIS::Distance::Formula|namespace::clean|Test2::V0)\\)$

%description
This Perl module reimplements some, but not all, of the formulas that
come with GIS::Distance in the C programming language. C code is generally
much faster than the Perl equivalent.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(GIS::Distance) >= 0.17
Requires:       perl(Test2::V0) >= 0.000094

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n GIS-Distance-Fast-%{version}
# Normalize shenangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
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
%doc Changes README.md
%dir %{perl_vendorarch}/auto/GIS
%dir %{perl_vendorarch}/auto/GIS/Distance
%{perl_vendorarch}/auto/GIS/Distance/Fast
%dir %{perl_vendorarch}/GIS
%dir %{perl_vendorarch}/GIS/Distance
%{perl_vendorarch}/GIS/Distance/Fast
%{perl_vendorarch}/GIS/Distance/Fast.pm
%{_mandir}/man3/GIS::Distance::Fast.*
%{_mandir}/man3/GIS::Distance::Fast::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
