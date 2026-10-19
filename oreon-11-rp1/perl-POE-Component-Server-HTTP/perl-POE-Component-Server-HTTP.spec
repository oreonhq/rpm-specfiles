%global source0_hash b7a91cec78cfd838b51fb9c90989527c2c65c3a81b36ee098ae406a875bb6c82
Name:           perl-POE-Component-Server-HTTP
Version:        0.09
Release:        1%{?dist}
Summary:        Foundation of a POE HTTP Daemon
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-HTTP
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/POE-Component-Server-HTTP-%{version}.tar.gz
Patch0:         POE-Component-Server-HTTP-0.09-Make-POE-API-Peek-optional.patch
BuildArch:      noarch
Requires:  perl(POE) >= 0.300
Requires:  perl(POE::Component::Server::TCP)
Requires:  perl(POE::Driver::SysRW)
Requires:  perl(POE::Filter::HTTPD)
Requires:  perl(POE::Filter::Stream)
Requires:  perl(POE::Session)
Requires:  perl(POE::Wheel::ReadWrite)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(POE\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::ConnCache)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter::HTTPD)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Kernel)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
POE::Component::Server::HTTP (PoCo::HTTPD) is a framework for building
custom HTTP servers based on POE. It is loosely modeled on the ideas of
apache and the mod_perl/Apache module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Server-HTTP-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
