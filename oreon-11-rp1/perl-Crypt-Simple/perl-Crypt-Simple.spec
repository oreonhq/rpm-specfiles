%global source0_hash 3db6e7754eaa425ab2d958d40b62d2026b0b186cd576ee352b4c172fb52d8e17

Name:           perl-Crypt-Simple
Version:        0.06
Release:        55%{?dist}
Summary:        Encrypt stuff simply 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Crypt-Simple
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KASEI/Crypt-Simple-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker) 
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This little module will convert all your data into nice base64 text that
you can save in a text file, send in an email, store in a cookie or web
page, or bounce around the Net. The data you encrypt can be as simple or
as complicated as you like.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-Simple-%{version}

%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
#find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
# For noarch packages: vendorlib
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
