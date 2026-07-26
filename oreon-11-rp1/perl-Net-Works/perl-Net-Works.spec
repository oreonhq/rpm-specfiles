%global source0_hash 0ac9b23dfbca184e28729b245394bc6693aadb6fc451caa995b4b719ec0ee9ff

Name:           perl-Net-Works
Version:        0.22
Release:        18%{?dist}
Summary:        API for IP addresses and networks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Works
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Net-Works-%{version}.tar.gz
BuildArch:      noarch
# Math::Int128 is not available on 32-bit platforms, bugs #1871738, #1871739.
ExcludeArch:    %{arm32} %{ix86}
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Math::Int128) >= 0.06
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::autoclean) >= 0.16
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket) >= 1.99
BuildRequires:  perl(Sub::Quote)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)

%description
The NetAddr::IP module is very complete, correct, and useful. However, its
API design is a bit crufty. This package provides an alternative API that
aims to address the biggest problems with that module's API, as well as
adding some additional features.

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

%setup -q -n Net-Works-%{version}
# Remove author and release tests that are skipped by default
rm t/author-* t/release-*
perl -i -ne 'print $_ unless m{\At\/(?:author|release)-}' MANIFEST
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
%doc Changes README.md
%dir %{perl_vendorlib}/Net
%{perl_vendorlib}/Net/Works
%{perl_vendorlib}/Net/Works.pm
%{_mandir}/man3/Net::Works.*
%{_mandir}/man3/Net::Works::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
