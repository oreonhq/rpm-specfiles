%global source0_hash aa9a083a231e4046170a5894644e3c59679c7dbd0aa2d1217dc85150df2c1e21
Summary:        Hashes (and objects based on hashes) with encrypting fields
Name:		perl-Tie-EncryptedHash
Version:	1.24
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Tie-EncryptedHash
Source0:        https://cpan.metacpan.org/modules/by-module/Tie/Tie-EncryptedHash-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Crypt::Blowfish)
Requires:	perl(Crypt::DES)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Tie::EncryptedHash augments Perl hash semantics to build secure, encrypting
containers of data. Tie::EncryptedHash introduces special hash fields that are
coupled with encrypt/decrypt routines to encrypt assignments at STORE() and
decrypt retrievals at FETCH(). By design, encrypting fields are associated with
keys that begin in single underscore. The remaining keyspace is used for
accessing normal hash fields, which are retained without modification.

While the password is set, a Tie::EncryptedHash behaves exactly like a standard
Perl hash. This is its transparent mode of access. Encrypting and normal fields
are identical in this mode. When password is deleted, encrypting fields are
accessible only as ciphertext. This is Tie::EncryptedHash's opaque mode of
access, optimized for serialization.

Encryption is done with Crypt::CBC(3), which encrypts in the cipher block
chaining mode with Blowfish, DES or IDEA. Tie::EncryptedHash uses Blowfish by
default, but can be instructed to employ any cipher supported by Crypt::CBC(3).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-EncryptedHash-%{version}

# Drop redundant shellbang in perl module
sed -i -e '/^#! *\/usr\/bin\/perl /d' lib/Tie/EncryptedHash.pm

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%check

make test
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
