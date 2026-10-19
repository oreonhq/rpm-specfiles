%global source0_hash b47b7f9333abb491eaaec6345a14e7f93956d143944c14b8164a7fd1b224bd6f
%bcond_with file-keepass-kdbx
%bcond_with pass-otp
%bcond_with posix-1003
%bcond_with file-kdbx-xs
%bcond_with crypt-stream-serpent
%bcond_with crypt-stream-twofish
%bcond_with math-bigint
Name:		perl-File-KDBX
Version:	0.906
Release:        12%{?dist}
Summary:        Encrypted database to store secret text and files
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/File-KDBX
Source0:        https://cpan.metacpan.org/authors/id/C/CC/CCM/File-KDBX-%{version}.tar.gz
BuildArch:	noarch
%if 0%{?with_math-bigint}
%endif
%if 0%{?with_file-keepass-kdbx}
%endif
%if 0%{?with_pass-otp}
%endif
%if 0%{?with_posix-1003}
%endif
%if 0%{?with_file-kdbx-xs}
%endif
%if 0%{?with_crypt-stream-serpent}
%endif
%if 0%{?with_crypt-stream-twofish}
%endif
Recommends:	perl(B::COW)
Requires:	perl(Carp)
Requires:	perl(Compress::Raw::Zlib)
Requires:	perl(Config)
Requires:	perl(Crypt::Cipher::AES)
Requires:	perl(Crypt::Stream::ChaCha) >= 0.048
Requires:	perl(Crypt::Stream::Salsa20) >= 0.055
Requires:	perl(Data::Dumper)
Requires:	perl(File::Temp)
Requires:	perl(IO::Compress::Gzip)
Requires:	perl(IO::Uncompress::Gunzip)
%if 0%{?with_math-bigint}
Requires:	perl(Math::BigInt) >= 1.993
%endif
Requires:	perl(Scope::Guard)
Requires:	perl(Text::ParseWords)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B::COW)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::Argon2)
BuildRequires:  perl(Crypt::Cipher)
BuildRequires:  perl(Crypt::Cipher::AES)
BuildRequires:  perl(Crypt::Digest)
BuildRequires:  perl(Crypt::Mac::HMAC)
BuildRequires:  perl(Crypt::Misc)
BuildRequires:  perl(Crypt::Mode::CBC)
BuildRequires:  perl(Crypt::PRNG)
BuildRequires:  perl(Crypt::Stream::ChaCha)
BuildRequires:  perl(Crypt::Stream::Salsa20)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::KeePass)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Iterator::Simple)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Loaded)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Reader)
BuildRequires:  perl(blib)
BuildRequires:  perl(boolean)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
File::KDBX provides everything you need to work with KDBX databases. A KDBX
database is a hierarchical object database which is commonly used to store
secret information securely. It was developed for the KeePass password
safe.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir File-KDBX-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
