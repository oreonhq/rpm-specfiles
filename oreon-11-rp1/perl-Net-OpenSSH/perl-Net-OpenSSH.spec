%global source0_hash 8780e62f01b1cf0db43c9cb705c94ff4949b032233be4be91fc91abc791539f8
Name:           perl-Net-OpenSSH
Version:        0.84
Release:        1%{?dist}
Summary:        Perl SSH client package implemented on top of OpenSSH
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-OpenSSH
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-OpenSSH-%{version}.tar.gz
BuildArch:      noarch
Requires:       openssh-clients
Requires:       perl(File::Glob)
Suggests:       perl(IO::Pty)
Suggests:       perl(Net::SFTP::Foreign) >= 1.47
Requires:       perl(Object::Remote::Role::Connector::PerlInterpreter)
Suggests:       perl(Sys::Hostname)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Net::OpenSSH is a secure shell client package implemented on top of OpenSSH
binary client (ssh).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-OpenSSH-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
