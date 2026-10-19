%global source0_hash 7c71c7c3cbe953234dfe25bcc1ad7edb0e1f5a0578601f5523bc6070262a3817
Name:           perl-Net-SSH
Version:        0.09
Release:        1%{?dist}
Summary:        Perl extension for secure shell
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-SSH
Source0:        https://cpan.metacpan.org/authors/id/I/IV/IVAN/Net-SSH-%{version}.tar.gz
BuildArch:      noarch
Requires:       openssh-clients
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements a Perl interface to ssh.  It is a simple
wrapper around the system `ssh' command.  For an all-perl
implementation that does not require the system `ssh' command, see
Net::SSH::Perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SSH-%{version}
chmod 644 -c Changes README SSH.pm

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
