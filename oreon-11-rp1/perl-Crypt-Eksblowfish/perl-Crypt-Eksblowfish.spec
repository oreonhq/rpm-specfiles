%global source0_hash 3cc7126d5841107237a9be2dc5c7fbc167cf3c4b4ce34678a8448b850757014c

Name:           perl-Crypt-Eksblowfish
Version:        0.009
Release:        46%{?dist}
Summary:        Eksblowfish block cipher
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-Eksblowfish
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Crypt-Eksblowfish-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Mix) >= 0.001
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64) >= 2.21
BuildRequires:  perl(parent)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::Pod) >= 1
BuildRequires:  perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
An object of this type encapsulates a keyed instance of the Eksblowfish
block cipher, ready to encrypt and decrypt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-Eksblowfish-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
%autochangelog
