%global source0_hash ebf6217f48f537ae9a78126f0ecb4baa3d4820e3e26153ce250f3bffd05f6d0b

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_IO_Socket_IP_enables_optional_test
%else
%bcond_with perl_IO_Socket_IP_enables_optional_test
%endif

Name:           perl-IO-Socket-IP
Version:        0.43
Release:        522%{?dist}
Summary:        Drop-in replacement for IO::Socket::INET supporting both IPv4 and IPv6
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Socket-IP
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Socket-IP-0.43.tar.gz
# IO-Socket-IP-0.41 moved from ExtUtils::MakeMaker to Module::Build.
# It will make problems, because IO::Socket::IP is a dual-lived package and
# needs to be built very early on Perl bootstrap, but Module::Build is not
# a core package and thus not available in the early stage of bootstrapping.
# For this reason, we create Makefile.PL and use it instead of Build.PL.
Source1:        Makefile.PL
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket) >= 1.97
BuildRequires:  perl(strict)
buildrequires:  perl(warnings)
# Tests only
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Test2::V0)
%if %{with perl_IO_Socket_IP_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
%endif

%{?perl_default_filter}

%description
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, intended as a replacement for IO::Socket::INET. Most constructor
arguments and methods are provided in a backward-compatible way.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n IO-Socket-IP-%{version}
cp %{SOURCE1} .
chmod -x lib/IO/Socket/IP.pm
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/IO/*
%{_mandir}/man3/IO::Socket::IP*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.43-522
- Prepare for Oreon 11 (RP1)
