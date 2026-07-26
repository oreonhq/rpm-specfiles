%global source0_hash 9fbdb479ba76fcb991eaf627f80e64dab093720054f643530ad036f927274bf9

Name:           perl-Crypt-CipherSaber
Version:        1.01
Release:        30%{?dist}
Summary:        Perl module implementing CipherSaber encryption
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-CipherSaber
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-CipherSaber-%{version}.tar.gz
# Fix parsing encrypted file, bug #1104075, CPAN RT#28370
Patch0:         Crypt-CipherSaber-1.01-Fix-reading-IV-with-new-lines-from-a-file.patch
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util) >= 1.4.2
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
Requires:       perl(Scalar::Util) >= 1.4.2

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Scalar::Util\\)$

%description
The Crypt::CipherSaber module implements CipherSaber encryption, described
at http://ciphersaber.gurus.com/. It is simple, fairly speedy, and
relatively secure algorithm based on RC4.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-CipherSaber-%{version}
%patch -P0 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Crypt
%{_mandir}/man3/Crypt::CipherSaber.3pm*

%changelog
%autochangelog
