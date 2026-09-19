%global source0_hash d75ba8b558988b3fdffa12ff62a55f0f1aaff8aa73b708bff3701ff88a2b8757

Name:           perl-JSON-RPC
Version:        1.06
Release:        32%{?dist}
Summary:        Perl implementation of JSON-RPC 1.1 protocol
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-RPC
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/JSON-RPC-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(JSON) >= 2
BuildRequires:  perl(LWP::UserAgent) >= 2.001
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Router::Simple)
Obsoletes:      perl-JSON-RPC-legacy < %{version}
Provides:       perl-JSON-RPC-legacy = %{version}

%{?perl_default_filter}

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

%check
./Build test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/JSON/RPC.pm
%{perl_vendorlib}/JSON/RPC/Constants.pm
%{perl_vendorlib}/JSON/RPC/Dispatch.pm
%{perl_vendorlib}/JSON/RPC/Legacy.pm
%{perl_vendorlib}/JSON/RPC/Legacy/Client.pm
%{perl_vendorlib}/JSON/RPC/Legacy/Procedure.pm
%{perl_vendorlib}/JSON/RPC/Parser.pm
%{perl_vendorlib}/JSON/RPC/Procedure.pm
%{perl_vendorlib}/JSON/RPC/Test.pm
%{_mandir}/man3/*

%files Apache2
%{perl_vendorlib}/JSON/RPC/Legacy/Server.pm
%{perl_vendorlib}/JSON/RPC/Legacy/Server/Apache2.pm

%files CGI
%{perl_vendorlib}/JSON/RPC/Legacy/Server.pm
%{perl_vendorlib}/JSON/RPC/Legacy/Server/CGI.pm

%files Daemon
%{perl_vendorlib}/JSON/RPC/Legacy/Server.pm
%{perl_vendorlib}/JSON/RPC/Legacy/Server/Daemon.pm

%changelog
%autochangelog
