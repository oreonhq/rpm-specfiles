%global source0_hash fa5c1a9e41b36969cbee0dbe1a6274f0fa652c338bf49c223efd64d2dc7da5ec

Name:           perl-Mojo-RabbitMQ-Client
Version:        0.3.1
Release:        19%{?dist}
Summary:        Mojo::IOLoop based RabbitMQ client
# Automatically converted from old format: Artistic 2.0 and BSD - review is highly recommended.
License:        Artistic-2.0 AND LicenseRef-Callaway-BSD

URL:            https://metacpan.org/release/Mojo-RabbitMQ-Client
Source0:        https://cpan.metacpan.org/authors/id/S/SE/SEBAPOD/Mojo-RabbitMQ-Client-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(strict)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::Home)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Parameters)
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Net::AMQP) >= 0.06
BuildRequires:  perl(Net::AMQP::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(constant)
# test requirements
BuildRequires:  perl(Test::Exception) >= 0.43
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Mojo::EventEmitter)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Net::AMQP) >= 0.06

%{?perl_default_filter}

## Filter unneeded Requires with RPM
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::AMQP\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(List::Util\\)$

%description
Mojo::RabbitMQ::Client is a rewrite of AnyEvent::RabbitMQ to work on top of
Mojo::IOLoop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojo-RabbitMQ-Client-%{version}
rm -rf inc

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_RMQ='' MOJO_RABBITMQ_DEBUG="" MOJO_CONNECT_TIMEOUT="" ./Build test

%files
%doc examples Changes README.md
%license LICENSE
%{perl_vendorlib}/auto
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
%autochangelog
