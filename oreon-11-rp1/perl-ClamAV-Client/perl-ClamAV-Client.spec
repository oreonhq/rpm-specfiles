%global source0_hash 2cf05681145d745269d6712c5ad424a10f381494123f568884d958d257e75246

Name:           perl-ClamAV-Client
Summary:        Client class for the ClamAV clamd virus scanner daemon
Version:        0.11
Release:        38%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ClamAV-Client
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMEHNLE/clamav-client/ClamAV-Client-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)

# These are not found by rpmbuild
Requires:       perl(IO::Socket::INET)
Requires:       perl(IO::Socket::UNIX)

%{?perl_default_filter}

%description
ClamAV::Client is a class acting as a client for a ClamAV clamd virus
scanner daemon. The daemon may run locally or on a remote system as
ClamAV::Client can use both Unix domain sockets and TCP/IP sockets. The
full functionality of the clamd client/server protocol is supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ClamAV-Client-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc CHANGES README
%{_mandir}/man3/ClamAV*
%{perl_vendorlib}/ClamAV

%changelog
%autochangelog
