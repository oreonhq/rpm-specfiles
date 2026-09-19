%global source0_hash a630ca401753866955f1173848ab5b4ac4ad5ca6ad9087f11cdf91dde85119bc

Name:           perl-Math-Int128
Version:        0.22
Release:        20%{?dist}
Summary:        Manipulate 128-bit integers in Perl
# lib/Math/Int128.pm:                   GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Math/Int128/die_on_overflow.pm:   GPL-1.0-or-later OR Artistic-1.0-Perl
# Makefile.PL:                          GPL-1.0-or-later OR Artistic-1.0-Perl
# ppport.h:                             GPL-1.0-or-later OR Artistic-1.0-Perl
# README.md:                            GPL-1.0-or-later OR Artistic-1.0-Perl
# strtoint128.h:                        BSD-3-Clause
## Unbundled
# inc/Capture/Tiny.pm:                  GPL-1.0-or-later OR Artistic-1.0-Perl
# inc/Config/AutoConf.pm:               GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
URL:            https://metacpan.org/release/Math-Int128
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Math-Int128-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
# Module::CAPIMaker not used
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::AutoConf)
# ExtUtils:CBuilder for Config::AutoConf->check_default_headers()
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::Int64) >= 0.51
BuildRequires:  perl(overload)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::More) >= 0.96
# This software needs a compiler with a 128-bit integer type. GCC for 32-bit
# targets does not support it. Bugs #1871733, #1871735.
ExcludeArch:    %{arm32} %{ix86}

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)

%description
This module adds support for 128-bit integers, signed and unsigned, to Perl.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# blib not used
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Int128-%{version}
# Remove the bundled modules
rm -r ./inc
perl -i -ne 'print $_ unless m{\Ainc/}' MANIFEST
# Remove release and author tests which are skipped by default
rm t/author-* t/release-*
perl -i -ne 'print $_ unless m{\At\/(?:author|release)-}' MANIFEST
# Extract license texts
perl -ne '$t=1 if m{Copyright}; $t=0 if m{\*/}; s/^ \*//; print $_ if $t' \
    <strtoint128.h >LICENSE.BSD
# Help generators to recognize Perl scripts
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
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE.BSD
%doc Changes README.md
%dir %{perl_vendorarch}/auto/Math
%{perl_vendorarch}/auto/Math/Int128
%dir %{perl_vendorarch}/Math
%{perl_vendorarch}/Math/Int128
%{perl_vendorarch}/Math/Int128.pm
%{_mandir}/man3/Math::Int128.*
%{_mandir}/man3/Math::Int128::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
