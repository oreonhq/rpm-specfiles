%global source0_hash 635b408b6bfbd559a3ae2f6067d367ce1868be5f2ed2a470480fb6cc54b816af

Name:           perl-IO-Async-Loop-Mojo
Version:        0.07
Release:        6%{?dist}
Summary:        Use IO::Async with Mojolicious
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Async-Loop-Mojo/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-Loop-Mojo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(IO::Async::Loop) >= 0.49
BuildRequires:  perl(IO::Async::LoopTests) >= 0.76
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mojolicious) >= 2.65
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
This subclass of IO::Async::Loop uses Mojo::Reactor to perform its IO
operations. It allows the use of IO::Async-based code or modules from
within a Mojolicious application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Async-Loop-Mojo-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
