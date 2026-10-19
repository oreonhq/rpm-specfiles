%global source0_hash 3188ab1127f2caba97df65c84f69db0ec70c64e5d70f296f9a2674fa79c112cc
Name:           perl-Beanstalk-Client
Version:        1.07
Release:        1%{?dist}
Summary:        Client class to talk to a beanstalkd server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Beanstalk-Client
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBARR/Beanstalk-Client-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
