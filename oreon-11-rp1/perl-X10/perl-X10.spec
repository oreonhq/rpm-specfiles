%global source0_hash 3dcee9d95614b2db70de608e933d42817f93fccd5b1f2f782b0846af487d9134

Name:      perl-X10
Summary:   Enables Perl to communicate with X10 devices
Version:   0.04
Release:   29%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:   GPL-3.0-only
URL:       https://metacpan.org/release/X10
Source:    https://cpan.metacpan.org/authors/id/R/RO/ROBF/X10-%{version}.tar.gz
Buildarch: noarch

BuildRequires: make
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: findutils

# Needed during build for the perl test
BuildRequires: perl(Astro::SunTime)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(File::Basename)
BuildRequires: perl(FileHandle)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(POSIX)
BuildRequires: perl(Storable)
BuildRequires: perl(strict)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(vars)

%description
X10 Perl module for the Firecracker, ActiveHome, and TwoWay/TW523 interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n X10-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}
# older Perls don't support the NO_PACKLIST flag
find %{buildroot} -type f -name .packlist -delete

%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%doc Changes README TODO
%doc macros.config scheduler.config

%{_mandir}/man1/x10client.1*
%{_mandir}/man1/x10server.1*

%{_bindir}/x10client
%{_bindir}/x10server

%{perl_vendorlib}/X10.pm
%{perl_vendorlib}/X10/

%changelog
%autochangelog
