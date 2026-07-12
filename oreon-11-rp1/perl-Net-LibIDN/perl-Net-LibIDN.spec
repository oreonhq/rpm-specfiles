%global source0_hash 2f8acc9442b3866ec7dc63cd449fc693ae3e930d5d3e5e9430fbb6f393bdbb17

%global pkgname Net-LibIDN

Summary:        Perl bindings for GNU LibIDN
Name:           perl-Net-LibIDN
Version:        0.12
Release:        55%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source:        https://cpan.metacpan.org/authors/id/T/TH/THOR/%{pkgname}-%{version}.tar.gz
# Use distribution CFLAGS for tests, bug #1242794, CPAN RT#105853
Patch0:         Net-LibIDN-0.12-Respect-Config-s-cc-ccflags-and-ldflags.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libidn-devel >= 0.4.0
BuildRequires:  perl-interpreter >= 5.8.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(Test)

# Filter the Perl extension module
%{?perl_default_filter}

Provides:       perl(Net::LibIDN)
%description
Provides perl bindings for GNU Libidn, a C library for handling
Internationalized Domain Names according to IDNA (RFC 3490), in
a way very much inspired by Turbo Fredriksson's PHP-IDN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1
# Change man page encoding into UTF-8
for F in _LibIDN.pm; do
    iconv -f latin1 -t utf-8 < "$F" > "${F}.utf"
    sed -i -e '/^=encoding\s/ s/latin1/utf-8/' "${F}.utf"
    touch -r "$F" "${F}.utf"
    mv "${F}.utf" "$F"
done;

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} +
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} +
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license Artistic
%doc Changes README
%{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12-55
- Prepare for Oreon 11 (RP1)
