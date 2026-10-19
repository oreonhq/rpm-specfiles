%global source0_hash 677f68ba2cd2a824fae323fa82e183bf7e3d03c3c499c91d923bd6283796a743
Name: perl-Net-Telnet
Summary:        Interact with TELNET port or other TCP ports
Version: 3.05
Release:        1%{?dist}
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://metacpan.org/release/Net-Telnet
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JROGERS/Net-Telnet-%{version}.tar.gz
Requires: perl(IO::Socket::INET)
BuildArch: noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Net::Telnet allows you to make client connections to a TCP port and do
network I/O, especially to a port using the TELNET protocol. Simple I/O
methods such as print, get, and getline are provided. More sophisticated
interactive features are provided because connecting to a TELNET port
ultimately means communicating with a program designed for human interaction.
These interactive features include the ability to specify a time-out and to
wait for patterns to appear in the input stream, such as the prompt from a
shell. IPv6 support is available when using perl 5.14 or later.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Telnet-%{version} 

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
