%global source0_hash fa5c1a9e41b36969cbee0dbe1a6274f0fa652c338bf49c223efd64d2dc7da5ec
Name:           perl-Mojo-RabbitMQ-Client
Version:        0.3.1
Release:        19%{?dist}
Summary:        Mojo::IOLoop based RabbitMQ client
License:        Artistic-2.0 AND LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/Mojo-RabbitMQ-Client
Source0:        https://cpan.metacpan.org/authors/id/S/SE/SEBAPOD/Mojo-RabbitMQ-Client-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Mojo::EventEmitter)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Net::AMQP) >= 0.06
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::AMQP\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(List::Util\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::Home)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Parameters)
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Net::AMQP)
BuildRequires:  perl(Net::AMQP::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

TEST_RMQ='' MOJO_RABBITMQ_DEBUG="" MOJO_CONNECT_TIMEOUT="" ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
