%global source0_hash f43a93bb02b41f7327d92f9e963b69505f67350a52e8f50796f98afc4fb3f177

Name:           perl-Authen-DecHpwd
Version:        2.007
Release:        29%{?dist}
Summary:        DEC VMS password hashing
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Authen-DecHpwd
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Authen-DecHpwd-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Integer) >= 0.003
BuildRequires:  perl(Digest::CRC) >= 0.14
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::String)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
Requires:       perl(Data::Integer) >= 0.003
Requires:       perl(Scalar::String)
Requires:       perl(XSLoader)

%description
This module implements the SYS$HASH_PASSWORD password hashing function from
VMS (also known as LGI$HPWD), and some associated VMS username and password
handling functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Authen-DecHpwd-%{version}

%build
%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Authen*
%{_mandir}/man3/*

%changelog
%autochangelog
