%global source0_hash 14997334b994576c859452d72aadc3b9344c007820d3117193908d4540c6db5b
Name:           perl-Event-RPC
Version:        1.11
Release:        1%{?dist}
Summary:        Event based transparent client/server RPC framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Event-RPC
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRED/Event-RPC-%{version}.tar.gz
Patch0:         Event-RPC-1.08-Convert-to-UTF-8.patch
BuildArch:      noarch
Requires:       %{name}-format = %{version}-%{release}
Recommends:     perl(Event::RPC::Message::Sereal)
Requires:       perl(IO::Socket::INET)
Requires:       perl(IO::Socket::UNIX)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Sereal\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Event_RPC_Test2\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Event_RPC_Test
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(CBOR::XS)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Event)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Glib)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Sereal)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset EVENT_RPC_LOOP
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset EVENT_RPC_LOOP
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Event-RPC-Message-CBOR -f %{oreon_filedir}/perl-Event-RPC-Message-CBOR.list
%files -n perl-Event-RPC-Message-JSON -f %{oreon_filedir}/perl-Event-RPC-Message-JSON.list
%files -n perl-Event-RPC-Message-Sereal -f %{oreon_filedir}/perl-Event-RPC-Message-Sereal.list
%files -n perl-Event-RPC-Message-Storable -f %{oreon_filedir}/perl-Event-RPC-Message-Storable.list
%files -n perl-Event-RPC-tests -f %{oreon_filedir}/perl-Event-RPC-tests.list

%changelog

%autochangelog
