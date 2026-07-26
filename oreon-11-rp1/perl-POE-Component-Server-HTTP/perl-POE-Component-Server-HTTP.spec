%global source0_hash b7a91cec78cfd838b51fb9c90989527c2c65c3a81b36ee098ae406a875bb6c82

Name:           perl-POE-Component-Server-HTTP
Version:        0.09
Release:        51%{?dist}
Summary:        Foundation of a POE HTTP Daemon
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-HTTP
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/POE-Component-Server-HTTP-%{version}.tar.gz
# Disable dependency on POE::API::Peek which is broken with perl-5.22,
# bug #1231252, CPAN RT#105463
Patch0:         POE-Component-Server-HTTP-0.09-Make-POE-API-Peek-optional.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# POE::Component::Server::HTTP not useful
# Run-time:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
# Data::Dumper is undocumented optional feature
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
# POE 0.3007 needed but future versions are 3-digit only
BuildRequires:  perl(POE) >= 0.300
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter::HTTPD)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::ConnCache)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(POE::Kernel)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML)
# Keep Data::Dumper optional
# POE 0.3007 needed but future versions are 3-digit only
Requires:  perl(POE) >= 0.300
Requires:  perl(POE::Component::Server::TCP)
Requires:  perl(POE::Driver::SysRW)
Requires:  perl(POE::Filter::HTTPD)
Requires:  perl(POE::Filter::Stream)
Requires:  perl(POE::Session)
Requires:  perl(POE::Wheel::ReadWrite)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(POE\\)$

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

%check
make test

%files
%doc Changes README test.perl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
