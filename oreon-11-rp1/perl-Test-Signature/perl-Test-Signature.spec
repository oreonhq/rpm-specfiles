%global source0_hash 48792c788a6068893600c522fc27210a22b58d7959f345ea6a67c8644458c2fc

# noarch, but to avoid *.list files interfering with signature test
%global debug_package %{nil}

# Similarly, for package note feature
%undefine _package_note_file

# Store keys in a temp directory
%global gnupghome %(mktemp --directory)

Name:           perl-Test-Signature
Version:        1.11
Release:        36%{?dist}
Summary:        Automated SIGNATURE testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Signature
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Signature-%{version}.tar.gz
# Audrey Tang's public key (3C3501A0), from the Module::Signature 0.61 distribution
Source1:        AUDREY2006.pub
# Petr Pisar's public key (4B528393E6A3B0DFB2EF3A6412C9C5C767C6FAA2)
Source2:        ppisar2011.pub
Patch0:         Test-Signature-1.11-Fix-building-on-Perl-without-.-in-INC.patch 
Patch1:         Test-Signature-1.11-Resign-patched-code.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Dependencies of bundled Module::Install
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
# Module Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Test::Pod) >= 0.95
# Dependencies
# Package just skips (or, optionally, fails) testing if Module::Signature not installed
Requires:       perl(Module::Signature)
# Likewise, needs Socket to connect to keyserver
Requires:       perl(Socket)

Provides:       perl(Test::Signature)
%description
Module::Signature allows you to verify that a distribution has not been
tampered with. Test::Signature lets that be tested as part of the
distribution's test suite.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Signature-%{version}

# Fix building on Perl without "." in @INC (CPAN RT#121760)
%patch -P 0 -p1
# Required to pass tests after patching
%patch -P 1 -p1

# Import upstream's GPG key so we don't need to fetch it from a keyserver
# when running the signature test
export GNUPGHOME=%{gnupghome}
gpg2 --import %{SOURCE1}
gpg2 --import %{SOURCE2}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
export GNUPGHOME=%{gnupghome}
make test

%clean
rm -rf %{buildroot} %{gnupghome}

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Signature.3*

%changelog
%autochangelog
