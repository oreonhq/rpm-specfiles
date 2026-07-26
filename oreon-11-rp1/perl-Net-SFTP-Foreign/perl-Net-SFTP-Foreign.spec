%global source0_hash 6c7d64250876873da434800e5060a8bef7a46451d81f817e37e43cfda51a0f7a

# require perl-net-sftp only on fedora
%if 0%{?fedora}
%global with_net_sftp        1
%endif

Name:		perl-Net-SFTP-Foreign
Version:	1.93
Release:	16%{?dist}
Summary:	SSH File Transfer Protocol client

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Net-SFTP-Foreign
Source0:	http://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-SFTP-Foreign-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(lib)
BuildRequires:	perl(Math::BigInt)
%{?with_net_sftp:BuildRequires:	perl(Net::SFTP)}
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Tie::Handle)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(warnings)
BuildRequires:	perl(warnings::register)

#Requires:	perl(bytes) # Needed only in Perl <= 5.8.x
Requires:	perl(Encode)
Requires:	perl(IO::Dir)
Requires:	perl(IO::File)
Requires:	perl(IO::Pty)
Requires:	perl(Math::BigInt)
Requires:	perl(Sort::Key)
Requires:	openssh-clients

%{?perl_default_filter}

%description
Net::SFTP::Foreign is a Perl client for the SFTP version 3 as defined in the SSH
File Transfer Protocol IETF draft, draft-ietf-secsh-filexfer-02.txt, included on
this package distribution, on the rfc directory.

Net::SFTP::Foreign uses any compatible ssh command installed on the system (for
instance, OpenSSH ssh) to establish the secure connection to the remote server.

A wrapper module Net::SFTP::Foreign::Compat is also provided for compatibility
with Net::SFTP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SFTP-Foreign-%{version}
rm lib/Net/SFTP/Foreign/Backend/Windows.pm
# Normalize end-of-lines
for F in rfc/draft-ietf-secsh-scp-sftp-ssh-uri-04.txt; do
    tr -d "\r" < "$F" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README debug.txt TODO rfc samples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
