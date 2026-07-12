%global source0_hash b9318c526497b5cb32dc0d8616020af02f5e746d592b95ce44ce0e00ea04047d

Name:           perl-Test-Future-IO-Impl
Version:        0.21
Release:        1%{?dist}
Summary:        Acceptance tests for Future::IO implementations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Test-Future-IO-Impl
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Future-IO-Impl-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
# runtime requirements
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
Requires:       perl(IO::Socket::INET)
Conflicts:      perl-Future-IO < 0.14

%{?perl_default_filter}

Provides:       perl(Test::Future::IO::Impl)
Provides:       perl(Test::Future::IO::Impl)
%description
This module contains a collection of acceptance tests for implementations
of Future::IO.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Future-IO-Impl-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%changelog
%autochangelog
