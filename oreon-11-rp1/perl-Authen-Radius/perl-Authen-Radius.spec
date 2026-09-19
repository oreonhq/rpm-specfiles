%global source0_hash c15361fc905dcdc156e5126686123ec079f02ad0d24c87c2729eb153d02bf0ce

Name:           perl-Authen-Radius
Version:        0.33
Release:        4%{?dist}
Summary:        Provide simple Radius client facilities
License:        Artistic-2.0
URL:            https://metacpan.org/release/Authen-Radius
Source0:        https://cpan.metacpan.org/modules/by-module/Authen/Authen-Radius-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper) >= 1
BuildRequires:  perl(Data::HexDump) >= 0.02
BuildRequires:  perl(Digest::MD5) >= 2.20
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO) >= 1.12
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Net::IP) >= 1.26
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional Tests
# (none)
# Dependencies
Requires:       perl(Data::Dumper) >= 1
Requires:       perl(Data::HexDump) >= 0.02
Requires:       perl(Digest::MD5) >= 2.20
Requires:       perl(IO) >= 1.12
Requires:       perl(Net::IP) >= 1.26

# Filter unversioned dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Data::Dumper\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Data::HexDump\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Digest::MD5\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Net::IP\\)\\s*$

%description
The Authen::Radius module provides a simple class that allows you to
send/receive Radius requests/responses to/from a Radius server.

You can just authenticate usernames/passwords via Radius, or completely
imitate AAA requests and process server responses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-Radius-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Authen/
%{_mandir}/man3/Authen::Radius.3*

%changelog
%autochangelog
