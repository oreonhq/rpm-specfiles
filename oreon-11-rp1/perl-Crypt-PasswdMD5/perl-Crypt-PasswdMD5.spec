%global cpan_version 1.42

Name:           perl-Crypt-PasswdMD5
# Keep 1-digit version because of history
Version:        %(echo '%{cpan_version}' | sed 's/\.\(.\)/.\1./')
Release:        11%{?dist}
Summary:        Provides interoperable MD5-based crypt() functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-PasswdMD5
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-PasswdMD5-%{cpan_version}.tgz
Patch0:         Crypt-PasswdMD5-1.42-d:md5-version.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Digest::MD5) >= 2.53
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 1.001002
# Dependencies:

%description
This package provides MD5-based crypt() functions.

%prep
%setup -q -n Crypt-PasswdMD5-%{cpan_version}

# Specify version requirement for Digest::MD5
# This avoids the need to add an explicit dependency in the spec file
# and the need to filter the underspecified auto-generated dependency
%patch -P0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::PasswdMD5.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %(echo'%{cpan_version}'|sed's/.(.)/../')-11
- Prepare for Oreon 11 (RP1)
