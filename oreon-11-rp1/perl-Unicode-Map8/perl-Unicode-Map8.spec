%global source0_hash af1e85b8ebad93a9c520bf0851948dd3ba6cf11336764891ce2b62b6b6a92b6e

Name:           perl-Unicode-Map8
Version:        0.13
Release:        53%{?dist}
Summary:        Mapping table between 8-bit chars and Unicode for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Unicode-Map8
Source0:        https://cpan.metacpan.org/modules/by-module/Unicode/Unicode-Map8-%{version}.tar.gz
Patch0:         perl-Unicode-Map8-0.12-declaration.patch
Patch1:         perl-Unicode-Map8-0.12-type.patch
Patch2:         perl-Unicode-Map8-0.13-recode.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Unicode::String) >= 2.00
BuildRequires:  perl(vars)
# Script Runtime
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Unicode::CharName)
# Test Suite
# (no additional dependencies)
# Dependencies
# (no additional dependencies)

%{?perl_default_filter}

Provides:       perl(Unicode::Map8)
%description
The Unicode::Map8 class implements efficient mapping tables between
8-bit character sets and 16 bit character sets like Unicode.  About
170 different mapping tables between various known character sets and
Unicode is distributed with this package.  The source of these tables
is the vendor mapping tables provided by Unicode, Inc. and the code
tables in RFC 1345.  New maps can easily be installed.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Unicode-Map8-%{version}

# Patches from openSUSE to fix test suite on x86_64
%patch -P 0 -p0
%patch -P 1 -p0

# Re-code docs as UTF8
%patch -P 2


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}


%check
make test


%files
%doc Changes README
%{_bindir}/umap
%{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/Unicode/
%{_mandir}/man1/umap.1*
%{_mandir}/man3/Unicode::Map8.3*


%changelog
%autochangelog
