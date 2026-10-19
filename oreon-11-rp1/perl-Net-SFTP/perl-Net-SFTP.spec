%global source0_hash 828e676ee35499127a47f3f3e5828d7f87d1b88eb55da3be2ab8dbdd83804f18
Name:           perl-Net-SFTP
Version:        0.12
Release:        1%{?dist}
Summary:        Secure File Transfer Protocol client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-SFTP
Source0:        https://cpan.metacpan.org/authors/id/L/LK/LKINLEY/Net-SFTP-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Int64)
BuildRequires:  perl(Net::SSH::Perl)
BuildRequires:  perl(Net::SSH::Perl::Buffer)
BuildRequires:  perl(Net::SSH::Perl::Constants)
BuildRequires:  perl(Test)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Net::SFTP is a pure-Perl implementation of the Secure File Transfer
Protocol (SFTP) - file transfer built on top of the SSH2 protocol.
Net::SFTP uses Net::SSH::Perl to build a secure, encrypted tunnel through
which files can be transferred and managed. It provides a subset of the
commands listed in the SSH File Transfer Protocol IETF draft, which can be
found at http://www.openssh.com/txt/draft-ietf-secsh-filexfer-00.txt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SFTP-%{version}
chmod a-x -c eg/*

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
