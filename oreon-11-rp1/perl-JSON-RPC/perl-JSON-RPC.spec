%global source0_hash d75ba8b558988b3fdffa12ff62a55f0f1aaff8aa73b708bff3701ff88a2b8757
Name:           perl-JSON-RPC
Version:        1.06
Release:        1%{?dist}
Summary:        Perl implementation of JSON-RPC 1.1 protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-RPC
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/JSON-RPC-%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      perl-JSON-RPC-legacy < %{version}
Provides:       perl-JSON-RPC-legacy = %{version}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(CGI)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Router::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
# /oreon:deps
%description
JSON-RPC is a stateless and light-weight remote procedure call (RPC)
protocol for inter-networking applications over HTTP. It uses JSON as the
data format for of all facets of a remote procedure call, including all
application data carried in parameters.

%package Apache2
Summary:   JSON-RPC server for mod_perl2
Obsoletes: perl-JSON-RPC-legacy-server < %{version}
Provides:  perl-JSON-RPC-legacy-server = %{version}
%package CGI
Summary:   JSON-RPC server for CGI scripts
Obsoletes: perl-JSON-RPC-legacy-server < %{version}
Provides:  perl-JSON-RPC-legacy-server = %{version}
%package Daemon
Summary:   JSON-RPC standalone daemon
Obsoletes: perl-JSON-RPC-legacy-server < %{version}
Provides:  perl-JSON-RPC-legacy-server = %{version}
%description Apache2
JSON-RPC is a stateless and light-weight remote procedure call (RPC)
protocol for inter-networking applications over HTTP. It uses JSON as the
data format for of all facets of a remote procedure call, including all
application data carried in parameters. This is the mod_perl2 server
implementation.

%description CGI
JSON-RPC is a stateless and light-weight remote procedure call (RPC)
protocol for inter-networking applications over HTTP. It uses JSON as the
data format for of all facets of a remote procedure call, including all
application data carried in parameters. This is the CGI server
implementation.

%description Daemon
JSON-RPC is a stateless and light-weight remote procedure call (RPC)
protocol for inter-networking applications over HTTP. It uses JSON as the
data format for of all facets of a remote procedure call, including all
application data carried in parameters. This is the standalone daemon
to serve JSON-RPC requests.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-RPC-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-JSON-RPC-Apache2 -f %{oreon_filedir}/perl-JSON-RPC-Apache2.list
%files -n perl-JSON-RPC-CGI -f %{oreon_filedir}/perl-JSON-RPC-CGI.list
%files -n perl-JSON-RPC-Daemon -f %{oreon_filedir}/perl-JSON-RPC-Daemon.list

%changelog

%autochangelog
