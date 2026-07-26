%global source0_hash 4c02200577c2b235a163a09bfaa152bf000fe5f1499ad80ce16ab66808949362

Name:           perl-Net-XMPP
Version:        1.05
Release:        31%{?dist}
Summary:        XMPP Perl Library
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Net-XMPP
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-XMPP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Authen::SASL) >= 2.12
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::Stream) >= 1.24
# Tests only
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::Online)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::Tiny)
Requires:       perl(Authen::SASL) >= 2.12
REquires:       perl(XML::Stream) >= 1.24

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Authen::SASL\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::Stream\\)$

%description
Net::XMPP provides a Perl user with access to the Extensible
Messaging and Presence Protocol (XMPP).

For more information about XMPP visit:

     http://www.xmpp.org

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-XMPP-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
# Cannot resolve hostnames in koji
%{?!_with_network_tests: rm t/roster.t t/gtalk.t t/memory_*.t }
./Build test

%files
%license LICENSE
%doc README CHANGES examples
%{perl_vendorlib}/Net*
%{_mandir}/man3/Net::XMPP*.3*

%changelog
%autochangelog
