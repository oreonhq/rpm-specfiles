%global source0_hash c6f4ab134672823413b50f07479b1a1b051f4cee42dd3ce7eb1583d6691b671d

Name:           perl-Data-IEEE754
Version:        0.02
Release:        18%{?dist}
Summary:        Pack and unpack big-endian IEEE 754 floats and doubles
License:        Artistic-2.0
URL:            https://metacpan.org/release/Data-IEEE754/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Data-IEEE754-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Bits)
BuildRequires:  perl(Test::More) >= 0.96
# Optional tests:
# CPAN::Meta not helful
# CPAN::Meta::Prereqs not helpful

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

%description
This Perl module provides some simple convenience functions for packing and
unpacking IEEE 754 floats and doubles. If you can require Perl 5.10 or greater
then this module is pointless. Just use the "d>" and "f>" pack formats
instead.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-IEEE754-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%dir %{perl_vendorlib}/Data
%{perl_vendorlib}/Data/IEEE754.pm
%{_mandir}/man3/Data::IEEE754.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
