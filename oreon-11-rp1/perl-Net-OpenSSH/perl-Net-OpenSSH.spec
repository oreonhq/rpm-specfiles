%global source0_hash 8780e62f01b1cf0db43c9cb705c94ff4949b032233be4be91fc91abc791539f8

Name:           perl-Net-OpenSSH
Version:        0.84
Release:        7%{?dist}
Summary:        Perl SSH client package implemented on top of OpenSSH
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-OpenSSH
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-OpenSSH-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
# Data::Dumper not used at tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
# File::Glob not used at tests
BuildRequires:  perl(File::Spec)
# Moo not used at tests
# Object::Remote::Role::Connector::PerlInterpreter not used at tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
# Sys::Hostname not used at tests
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       openssh-clients
Requires:       perl(File::Glob)
Suggests:       perl(IO::Pty)
Suggests:       perl(Net::SFTP::Foreign) >= 1.47
Requires:       perl(Object::Remote::Role::Connector::PerlInterpreter)
Suggests:       perl(Sys::Hostname)

# Needed to stop the sample scripts pulling in more perl packages.
%{?perl_default_filter}

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

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
