%global source0_hash 3188ab1127f2caba97df65c84f69db0ec70c64e5d70f296f9a2674fa79c112cc

Name:           perl-Beanstalk-Client
Version:        1.07
Release:        37%{?dist}
Summary:        Client class to talk to a beanstalkd server
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Beanstalk-Client
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBARR/Beanstalk-Client-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Socket)
BuildRequires:  perl(YAML::Syck)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
# Optional tests:
# JSON::XS is not used

%description
Beanstalk::Client provides a Perl API of protocol version 1.0 to the
beanstalkd server, a fast, general-purpose, in-memory work-queue service by
Keith Rarick.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Beanstalk-Client-%{version}
rm -rf inc/*
sed -i -e '/^inc\//d' MANIFEST

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
%doc Changes README
%{perl_vendorlib}/Beanstalk
%{_mandir}/man3/Beanstalk::*

%changelog
%autochangelog
