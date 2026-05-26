Name:           perl-Encode-EUCJPASCII
Version:        0.03
Release:        49%{?dist}
Summary:        EucJP-ascii - An eucJP-open mapping
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Encode-EUCJPASCII
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/Encode-EUCJPASCII-0.03.tar.gz
# oreon url source checksums begin
%global source0_sha256 f998d34d55fd9c82cf910786a0448d1edfa60bf68e2c2306724ca67c629de861
%global source0_file Encode-EUCJPASCII-0.03.tar.gz
# oreon url source checksums end

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Encode)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(Encode::CJKConstants)
BuildRequires:  perl(Encode::JP::JIS7)
BuildRequires:  perl-devel
%if !0%{?el6}
BuildRequires:  perl-Encode-devel
BuildRequires:  perl-generators
%endif

%{?perl_default_filter}

%description
This module provides eucJP-ascii, one of eucJP-open mappings, and its
derivative.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Encode-EUCJPASCII-0.03.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f998d34d55fd9c82cf910786a0448d1edfa60bf68e2c2306724ca67c629de861" || { echo "oreon: Source0 SHA256 mismatch for Encode-EUCJPASCII-0.03.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Encode-EUCJPASCII-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.03-49
- Prepare for Oreon 11 (RP1)
