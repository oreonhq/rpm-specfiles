%global source0_hash 5d1f5df48ce13b4dee1cc9f278ecdbf8177877b0b98815a4eb3c91c3466716f2

Name:           perl-Compress-LZF
Version:        3.8
Release:        36%{?dist}
Summary:        Extremely light-weight Lempel-Ziv-Free compression
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
## Not in the binary packages
# liblzf files:     BSD or GPLv2+
# perlmulticore.h:  Public Domain or CC0
URL:            https://metacpan.org/release/Compress-LZF
Source0:        https://cpan.metacpan.org/modules/by-module/Compress/Compress-LZF-%{version}.tar.gz
Patch0:         Compress-LZF-3.8-Unbundle-liblzf.patch
Patch1:         Compress-LZF-3.8-Unbundle-perlmulticore.patch
Patch2:         perl-Compress-LZF-c99.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  liblzf-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perlmulticore-static
# Module
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# Test Suite
BuildRequires:  perl(Storable)
# Dependencies
# (none)

Provides:       perl(Compress::LZF)
Provides:       perl(Compress::LZF)
%description
This is Perl binding to the LZF compression library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Compress-LZF-%{version}

# Unbundle liblzf
%patch -P 0 -p1

# Unbundle perlmulticore.h
%patch -P 1 -p1

# Compile in C99 mode
%patch -P 2 -p1

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
%license COPYING COPYING.Artistic COPYING.GNU
%doc Changes README
%{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/Compress/
%{_mandir}/man3/Compress::LZF.3*

%changelog
%autochangelog
