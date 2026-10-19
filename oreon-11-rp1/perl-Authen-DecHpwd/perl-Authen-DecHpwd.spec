%global source0_hash f43a93bb02b41f7327d92f9e963b69505f67350a52e8f50796f98afc4fb3f177
Name:           perl-Authen-DecHpwd
Version:        2.007
Release:        1%{?dist}
Summary:        DEC VMS password hashing
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Authen-DecHpwd
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Authen-DecHpwd-%{version}.tar.gz
Requires:       perl(Data::Integer) >= 0.003
Requires:       perl(Scalar::String)
Requires:       perl(XSLoader)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Data::Integer)
BuildRequires:  perl(Digest::CRC)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::String)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements the SYS$HASH_PASSWORD password hashing function from
VMS (also known as LGI$HPWD), and some associated VMS username and password
handling functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Authen-DecHpwd-%{version}
%oreon_prep
%build

%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
