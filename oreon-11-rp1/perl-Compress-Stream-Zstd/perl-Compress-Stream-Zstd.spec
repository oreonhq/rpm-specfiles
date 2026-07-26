%global source0_hash b72d253c17999f6f7758969577046531dab3ab5ca52cdc762970fa967b75eb95

Name:           perl-Compress-Stream-Zstd
Version:        0.206
Release:        11%{?dist}
Summary:        Perl interface to the Zstd (Zstandard) (de)compressor
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://metacpan.org/release/Compress-Stream-Zstd/
Source0:        https://cpan.metacpan.org/modules/by-module/Compress/Compress-Stream-Zstd-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Unbundling is not possible, because libzstd-devel doesn't not contains
# 'compress/zstdmt_compress.h', which is used by lib/Compress/Stream/Zstd.xs 
Provides:       bundled(zstd) = 1.5.5

%description
The Compress::Stream::Zstd module provides an interface to the Zstd
(de)compressor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Compress-Stream-Zstd-%{version}

%build
%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md eg/
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Compress*
%{_mandir}/man3/*

%changelog
%autochangelog
