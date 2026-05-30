%global source0_hash 3406b9ca5a662a0075eed47fb78de1316b601c94f62a0ee34a5544db9baa3720

Name:           perl-Net-Server
Version:        2.014
Release:        10%{?dist}
Summary:        Extensible, general Perl server engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Server
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Server-%{version}.tar.gz


# Only initialize existing Net::SSLeay methods (RT#154333)
Patch0:         https://github.com/rhandom/perl-net-server/pull/Net-Server-2.014-Fix-using-OpenSSL-ENGINE-API-routines.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# BuildRequires:  perl(CGI)
# BuildRequires:  perl(CGI::Compile)
# BuildRequires:  perl(CGI::PSGI)
# BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
# BuildRequires:  perl(HTTP::Parser::XS)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Multiplex) >= 1.05
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
# BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL) >= 1.31
BuildRequires:  perl(IO::Socket::UNIX)
# BuildRequires:  perl(IPC::Open3)
# BuildRequires:  perl(IPC::Semaphore)
# BuildRequires:  perl(IPC::SysV)
# BuildRequires:  perl(Log::Log4perl)
# BuildRequires:  perl(Net::CIDR)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6)
# BuildRequires:  perl(Symbol)
# BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Time::HiRes)
# BuildRequires:  perl(Unix::Syslog)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(threads)
BuildRequires:  perl(Test::More)
 
# IO::Multiplex support is optional, but not including it causes build problems in some packages...
Requires:       perl(IO::Multiplex) >= 1.05
#  RHBZ#1395714: Optional dependency, including it so that the build matches runtime
Requires:       perl(IO::Socket::IP)

# Remove private test modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(NetServerTest\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(NetServerTest\\)$

%description
An extensible, class oriented module written in perl and intended to
be the back end layer of internet protocol servers.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n Net-Server-%{version}

# Do not want to pull in any packaging deps here.
chmod -c 644 examples/*

# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
# XXX Not possible to run in parallel
cd %{_libexecdir}/%{name} && exec prove -I . -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/net-server
%{_mandir}/man1/net-server.1*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.014-10
- Prepare for Oreon 11 (RP1)
