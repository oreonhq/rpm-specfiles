%global source0_hash 4def485db1eff4e139b4b5912202c0fd61c3aed2cec35bd5ab8bf7bbd83f5a75

Name:           perl-IO-Async-SSL
Version:        0.25
Release:        8%{?dist}
Summary:        Use SSL/TLS with IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Async-SSL/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-SSL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Future) >= 0.33
BuildRequires:  perl(IO::Async::Handle) >= 0.29
BuildRequires:  perl(IO::Async::Listener)
BuildRequires:  perl(IO::Async::Loop) >= 0.66
BuildRequires:  perl(IO::Async::OS)
BuildRequires:  perl(IO::Async::Protocol::Stream)
BuildRequires:  perl(IO::Async::Stream) >= 0.59
BuildRequires:  perl(IO::Async::Test) >= 0.68
BuildRequires:  perl(IO::Socket::SSL) >= 2.003
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Identity)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  /usr/bin/openssl /usr/bin/socat

%description
This module extends existing IO::Async classes with extra methods to allow
the use of SSL or TLS-based connections using IO::Socket::SSL. It does not
directly provide any methods or functions of its own.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Async-SSL-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes examples README
%license LICENSE
%{perl_vendorlib}/IO/Async/SSL*
%{_mandir}/man3/IO::Async::SSL*

%changelog
%autochangelog
