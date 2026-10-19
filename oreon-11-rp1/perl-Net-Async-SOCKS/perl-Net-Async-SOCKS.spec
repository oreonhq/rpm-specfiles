%global source0_hash 24721a94ccedd15b05003eb3099a0d83a03dcfbbe2f86a75895bec8fed28be3e
Name:           perl-Net-Async-SOCKS
Version:        0.003
Release:        1%{?dist}
Summary:        Some degree of SOCKS5 proxy support in IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Async-SOCKS/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Net-Async-SOCKS-%{version}.tar.gz
Patch0:         Net-Async-SOCKS-0.003-noRefcount.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Future)
BuildRequires:  perl(IO::Async)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Stream)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Protocol::SOCKS)
BuildRequires:  perl(Protocol::SOCKS::Client)
BuildRequires:  perl(Protocol::SOCKS::Constants)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::HexString)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Currently provides a very basic implementation of SOCKS_connect:

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Async-SOCKS-%{version}
# incorrectly tries to require Test::Refcount which is not used
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
