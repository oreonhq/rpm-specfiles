%global source0_hash 6a7aad5822c6be7894785472f10ae548aa2886c8286b47f90ac192067f05e754
Summary:        A Perl interface for making and serving XML-RPC calls
Name:           perl-Frontier-RPC
Version:        0.07b4p1
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Frontier-RPC
Source0:        https://cpan.metacpan.org/authors/id/R/RT/RTFIREFLY/Frontier-RPC-%{version}.tar.gz
Patch0:         perl-frontier-raw-call.patch
Patch1:         perl-frontier-raw-serve.patch
Patch2:         perl-frontier-undef-scalar.patch
Patch3:         security-xml-external-entity.patch
Patch4:         apache2.patch
Patch5:         Frontier-RPC-0.07b4p1-Respect-proxy-setting-for-HTTPS.patch
BuildArch:      noarch
Requires:       perl-Frontier-RPC-doc = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%package Client
Summary:        Frontier-RPC-Client Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl-Frontier-RPC-doc = %{?epoch:%{epoch}:}%{version}-%{release}
%package doc
Summary:        Frontier-RPC-Client Perl module documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
%description
Frontier::RPC implements UserLand Software's XML RPC (Remote
Procedure Calls using Extensible Markup Language).  Frontier::RPC
includes both a client module for making requests to a server and
several server modules for implementing servers using CGI, Apache,
and standalone with HTTP::Daemon.

%description Client
Frontier::RPC::Client implements UserLand Software's XML RPC (Remote
Procedure Calls using Extensible Markup Language).  Frontier::RPC::Client
includes just client module for making requests to a server.

%description doc
Documentation and examples to Frontier::RPC and Frontier::RPC::Client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Frontier-RPC-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Frontier-RPC-Client -f %{oreon_filedir}/perl-Frontier-RPC-Client.list
%files -n perl-Frontier-RPC-doc -f %{oreon_filedir}/perl-Frontier-RPC-doc.list

%changelog

%autochangelog
