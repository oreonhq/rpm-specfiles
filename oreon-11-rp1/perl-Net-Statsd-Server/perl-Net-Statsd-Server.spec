%global source0_hash 22b1f551907ed285d43eb00aa083195a9d1aa9ae2c1be10d8bb30fb5235a64f2

%define username   statsdpl
%define groupname  statsdpl
%define daemon     statsd-perl

Name:           perl-Net-Statsd-Server
Version:        0.20
Release:        30%{?dist}
Summary:        Library for the Perl port of Flickr/Etsy's statsd metrics daemon
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Statsd-Server
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Statsd-Server-%{version}.tar.gz
Source1:        %{daemon}.service
Source2:        %{daemon}.js
Source3:        %{daemon}.logrotate
Patch1:         Net-Statsd-Server-0.20-makefile.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Handle::UDP)
BuildRequires:  perl(AnyEvent::Log)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Strict)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
# HTTP::Request not used at tests
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(lib)
# LWP::UserAgent not used at tests
# RRDs not used at tests
BuildRequires:  perl(Socket)
BuildRequires:  perl(Time::HiRes)
# Tests:
BuildRequires:  perl(Test::More)

%description
Net::Statsd::Server is the server component of statsd. It implements a daemon
that listens on a given host/port for incoming UDP packets and dispatches them
to whatever you want, including Graphite or your console.  Look into the
Net::Statsd::Server::Backend::* name space to know all the possibilities, or
write a back-end yourself.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Statsd-Server-%{version}
%patch -P1 -p1
mv bin/statsd bin/%{daemon}
for F in exampleConfig.js localConfig.js logConfig.js rrdConfig.js; do
    mv bin/"$F" "$F"
done
rm -Rf t/integration-tests/

# Create a sysusers.d config file
cat >perl-net-statsd-server.sysusers.conf <<EOF
g statsdpl -
u statsdpl - 'Perl Statsd' /run/%{daemon} -
EOF

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{daemon}.service
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{daemon}.js
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{daemon}
mkdir -p -m 750 $RPM_BUILD_ROOT%{_localstatedir}/log/%{daemon}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

install -m0644 -D perl-net-statsd-server.sysusers.conf %{buildroot}%{_sysusersdir}/perl-net-statsd-server.conf

%check
STATSD_BINARY=$RPM_BUILD_ROOT/usr/bin/%{daemon} make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n statsd-perl
Summary:        A Perl port of Flickr/Etsy's statsd metrics daemon
BuildRequires:  systemd-units
Requires:       %{name} = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:  statsd

%description -n statsd-perl
Implements a daemon that listens on a given host/port for incoming UDP packets
and dispatches them to whatever you want, including Graphite or your console.
Look into the Net::Statsd::Server::Backend::* name space to know all the
possibilities, or write a back-end yourself.

%post -n statsd-perl
%systemd_post %{daemon}.service

%preun -n statsd-perl
%systemd_preun %{daemon}.service

%postun -n statsd-perl
%systemd_postun_with_restart %{daemon}.service

%files -n statsd-perl
%doc README exampleConfig.js localConfig.js logConfig.js rrdConfig.js
%{_mandir}/man1/*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{daemon}.js
%config(noreplace) %{_sysconfdir}/logrotate.d/%{daemon}
%{_unitdir}/%{daemon}.service
%attr(750, %{username}, %{groupname}) %{_localstatedir}/log/%{daemon}
%{_sysusersdir}/perl-net-statsd-server.conf

%changelog
%autochangelog
