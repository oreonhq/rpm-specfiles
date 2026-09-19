%global source0_hash c88cf3423b01e6782e8986d7fe5304436ab84b0925c4498c6fdfa17ef9a37f5f

Summary:	Perl module implementing the Diffie-Hellman key exchange system
Name:		perl-Crypt-DH
Version:	0.07
Release:	40%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Url:		https://metacpan.org/release/Crypt-DH
Source0:	https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-DH-%{version}.tar.gz
BuildArch:	noarch
# =============== Module Build ==================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl(Module::Install::CheckLib)
BuildRequires:	perl(Module::Install::GithubMeta)
BuildRequires:	perl(Module::Install::ReadmeFromPod)
BuildRequires:	sed
# =============== Module Runtime ================
BuildRequires:	perl(Math::BigInt) >= 1.60
BuildRequires:	perl(Math::BigInt::GMP) >= 1.24
BuildRequires:	perl(strict)
# =============== Test Suite ====================
BuildRequires:	perl(Test::More)
# =============== Dependencies ==================
Requires:	perl(Math::BigInt) >= 1.60
Requires:	perl(Math::BigInt::GMP) >= 1.24

%description
Crypt::DH is a Perl implementation of the Diffie-Hellman key exchange system.
Diffie-Hellman is an algorithm by which two parties can agree on a shared
secret key, known only to them. The secret is negotiated over an insecure
network without the two parties ever passing the actual shared secret, or their
private keys, between them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-DH-%{version}

# Remove bundled dependencies
rm -rv inc/
sed -i -e '/^inc\// d' MANIFEST

# Remove unnecessary exec bits
find . -type f -print0 | xargs -0 chmod -c -x

# Fix line endings of documentation
sed -i -e 's/\r$//' README

%build
perl Makefile.PL --skipdeps \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README ToDo
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::DH.3*

%changelog
%autochangelog
