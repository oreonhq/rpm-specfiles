%global source0_hash 55db4520617d859d88c0ee54965da815b7226d792b8cdc8debf92073559e0463
Name:           perl-Authen-Passphrase
Version:        0.008
Release:        1%{?dist}
Summary:        Hashed passwords/passphrases as objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Authen-Passphrase
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Authen-Passphrase-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Authen::DecHpwd)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(Crypt::Eksblowfish::Bcrypt)
BuildRequires:  perl(Crypt::Eksblowfish::Uklblowfish)
BuildRequires:  perl(Crypt::MySQL)
BuildRequires:  perl(Crypt::PasswdMD5)
BuildRequires:  perl(Crypt::UnixCrypt_XS)
BuildRequires:  perl(Data::Entropy::Algorithms)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD4)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
These Perl modules provide a passphrase recognizer. Its job is
to recognize whether an offered passphrase is the right one. Various
passphrase encoding schemes are supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Authen-Passphrase-%{version}
%oreon_prep
%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
