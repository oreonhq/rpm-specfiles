%global source0_hash b2748fb27c93da77ef5b06fd8c2ddfc2fd0ce5fd58375a8906b2aafbfc21fbf2
Name:           perl-LWP-Authen-Wsse
Version:        0.05
Release:        1%{?dist}
Summary:        Library for enabling X-WSSE authentication in LWP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Authen-Wsse
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUTRIJUS/LWP-Authen-Wsse-%{version}.tar.gz
Patch0:         LWP-Authen-Wsse-0.05-Work-around-Module-Install-only-supports-5.005-bug.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(English)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
LWP::Authen::Wsse allows LWP to authenticate against servers that are 
using the X-WSSE authentication scheme, as required by the Atom 
Authentication API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LWP-Authen-Wsse-%{version}
%patch -P0 -p1
# Remove bundles modules
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
