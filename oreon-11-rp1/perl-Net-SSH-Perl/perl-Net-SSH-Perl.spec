%global source0_hash d8c18570ad813c01d6824607b7ebda987f590b10e2aa536dffabbe2920482e82

Summary:	SSH (Secure Shell) client
Name:		perl-Net-SSH-Perl
Version:	2.144
Release:	2%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Net-SSH-Perl
Source0:	https://cpan.metacpan.org/modules/by-module/Net/Net-SSH-Perl-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	gcc
#BuildRequires:	gnupg2
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::Manifest) >= 1.21
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(constant)
BuildRequires:	perl(Crypt::Cipher::AES)
BuildRequires:	perl(Crypt::Cipher::Blowfish)
BuildRequires:	perl(Crypt::Cipher::DES)
BuildRequires:	perl(Crypt::Curve25519)		>= 0.05
BuildRequires:	perl(Crypt::Digest::MD5)
BuildRequires:	perl(Crypt::Digest::SHA1)
BuildRequires:	perl(Crypt::Digest::SHA256)
BuildRequires:	perl(Crypt::Digest::SHA512)
BuildRequires:	perl(Crypt::DSA::Key)
BuildRequires:	perl(Crypt::IDEA)
BuildRequires:	perl(Crypt::Mac::HMAC)
BuildRequires:	perl(Crypt::Misc)
BuildRequires:	perl(Crypt::PK::DH)
BuildRequires:	perl(Crypt::PK::DSA)
BuildRequires:	perl(Crypt::PK::ECC)
BuildRequires:	perl(Crypt::PK::RSA)
BuildRequires:	perl(Crypt::PRNG)
BuildRequires:	perl(CryptX)			>= 0.032
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(if)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(IO::Socket::Socks)
BuildRequires:	perl(Math::GMP)			>= 1.04
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Socket)
BuildRequires:	perl(strict)
BuildRequires:	perl(String::CRC32)		>= 1.2
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Tie::Handle)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Optional Functionality
BuildRequires:	perl(Digest::BubbleBabble)
# Test Suite
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)		>= 0.61
# Dependencies
Requires:	perl(Digest::BubbleBabble)
Requires:	perl(File::Basename)
Requires:	perl(File::Path)
Requires:	perl(Term::ReadKey)

%description
Net::SSH::Perl is a mostly-Perl module implementing an SSH (Secure Shell)
client. It is compatible with both the SSH-1 and SSH-2 protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SSH-Perl-%{version}

%build
# Protocol support (select one)
# 1=SSH1 2=SSH2 3=Both
echo 3 | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE LICENSE_ARTISTIC LICENSE_GNU
%doc Changes README eg ToDo
%{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/Net/
%{_mandir}/man3/Net::SSH::Perl*.3*

%changelog
%autochangelog
