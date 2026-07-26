%global source0_hash 14997334b994576c859452d72aadc3b9344c007820d3117193908d4540c6db5b

Name:           perl-Event-RPC
Version:        1.11
Release:        3%{?dist}
Summary:        Event based transparent client/server RPC framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Event-RPC
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRED/Event-RPC-%{version}.tar.gz
# Normalize documenation encoding
Patch0:         Event-RPC-1.08-Convert-to-UTF-8.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CBOR::XS)
BuildRequires:  perl(Event)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Glib)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(JSON::XS) >= 3
BuildRequires:  perl(Sereal) >= 3
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(utf8)
# Optional run-time:
BuildRequires:  perl(IO::Socket::SSL)
# Tests:
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests:
# Benchmark not used
# TODO:  Split dependencies on an event controller ||(AnyEvent Event Glib)
# Dependent on a format: ||(Sereal CBOR::XS JSON::XS Storable).
# The requires in lib/Event/RPC/Message.pm are void, CPAN RT#107405.
# Sereal is recommended, Storable is backward-compatible but insecure.
Requires:       %{name}-format = %{version}-%{release}
Recommends:     perl(Event::RPC::Message::Sereal)
Requires:       perl(IO::Socket::INET)
Requires:       perl(IO::Socket::UNIX)

# Filter documentation's dependencies
%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Sereal\\)$

# Hide private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Event_RPC_Test2\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Event_RPC_Test

%description
Event::RPC supports you in developing Event based networking client/server
applications with transparent object/method access from the client to the
server. Network communication is optionally encrypted using IO::Socket::SSL.
Several event loop managers are supported due to an extensible API. Currently
Event, Glib, and AnyEvent are implemented. The latter lets you use nearly
every event loop implementation available for Perl.

%package Message-CBOR
Summary:        CBOR message format for Event::RPC
Requires:       perl(Event::RPC::Message::SerialiserBase)
Provides:       %{name}-format = %{version}-%{release}

%description Message-CBOR
This implements CBOR message format for Event::RPC Perl RPC framework.

%package Message-JSON
Summary:        JSON message format for Event::RPC
Requires:       perl(Event::RPC::Message::SerialiserBase)
Provides:       %{name}-format = %{version}-%{release}

%description Message-JSON
This implements JSON message format for Event::RPC Perl RPC framework.

%package Message-Sereal
Summary:        Sereal message format for Event::RPC
Requires:       perl(Event::RPC::Message)
Requires:       perl(Sereal) >= 3
Provides:       %{name}-format = %{version}-%{release}

%description Message-Sereal
This implements Sereal message format for Event::RPC Perl RPC framework.

%package Message-Storable
Summary:        Storable message format for Event::RPC
Requires:       perl(Event::RPC::Message)
Provides:       %{name}-format = %{version}-%{release}

%description Message-Storable
This implements Storable message format for Event::RPC Perl RPC framework.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       coreutils
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Event-RPC-%{version}
%patch -P0 -p1
# Normalize permissions
chmod +x t/06.object2.t
chmod -x examples/*.pl

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
#!/bin/bash
set -e
# t/Event_RPC_Test_Server.pm writed to CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset EVENT_RPC_LOOP
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset EVENT_RPC_LOOP
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes examples README
%dir %{perl_vendorlib}/Event/
%{perl_vendorlib}/Event/RPC
%{perl_vendorlib}/Event/RPC.pm
%exclude %{perl_vendorlib}/Event/RPC/Message/CBOR.pm
%exclude %{perl_vendorlib}/Event/RPC/Message/JSON.pm
%exclude %{perl_vendorlib}/Event/RPC/Message/Sereal.pm
%exclude %{perl_vendorlib}/Event/RPC/Message/Storable.pm
%{_mandir}/man3/Event::RPC.3*
%{_mandir}/man3/Event::RPC::*.3*
%exclude %{_mandir}/man3/Event::RPC::Message::CBOR.3*
%exclude %{_mandir}/man3/Event::RPC::Message::JSON.3*
%exclude %{_mandir}/man3/Event::RPC::Message::Sereal.3*
%exclude %{_mandir}/man3/Event::RPC::Message::Storable.3*

%files Message-CBOR
%{perl_vendorlib}/Event/RPC/Message/CBOR.pm
%{_mandir}/man3/Event::RPC::Message::CBOR.3*

%files Message-JSON
%{perl_vendorlib}/Event/RPC/Message/JSON.pm
%{_mandir}/man3/Event::RPC::Message::JSON.3*

%files Message-Sereal
%{perl_vendorlib}/Event/RPC/Message/Sereal.pm
%{_mandir}/man3/Event::RPC::Message::Sereal.3*

%files Message-Storable
%{perl_vendorlib}/Event/RPC/Message/Storable.pm
%{_mandir}/man3/Event::RPC::Message::Storable.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
