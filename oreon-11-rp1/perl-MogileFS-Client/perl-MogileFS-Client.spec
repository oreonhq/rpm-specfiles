%global source0_hash 7b9e4effc3ade60363af940f5c3babbf608d3ff9a3357c0d778463da382ea4f2

%global cpan_name MogileFS-Client

Name:           perl-%{cpan_name}
Version:        1.17
Release:        34%{?dist}
Summary:        Client library for the MogileFS distributed file system
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(fields)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::WrapTie) >= 2.102
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(LWP)
BuildRequires:  perl(Test::More)
Requires:       perl(IO::WrapTie) >= 2.102

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IO::WrapTie\\)$

%description
This module is a client library for the MogileFS distributed file system.
The class method 'new' creates a client object against a particular
mogilefs tracker and domain. This object may then be used to store and
retrieve content easily from MogileFS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES TODO
%{perl_vendorlib}/MogileFS
%{_mandir}/man3/MogileFS::Client.*

%changelog
%autochangelog
