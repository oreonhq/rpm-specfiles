%global source0_hash 6fc52453cb5fef4e47629d1ba6b7f4ea9f67069c3b6ef913aff43b5c0adf478b
Name:           perl-IO-Compress-Zstd
Version:        2.217
Release:        1%{?dist}
Summary:        Write zstd files/buffers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Compress-Zstd/
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/IO-Compress-Zstd-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Compress::Stream::Zstd)
BuildRequires:  perl(Compress::Stream::Zstd::Compressor)
BuildRequires:  perl(Compress::Stream::Zstd::Decompressor)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Compress::Base)
BuildRequires:  perl(IO::Compress::Base::Common)
BuildRequires:  perl(IO::Compress::Zip)
BuildRequires:  perl(IO::Compress::Zip::Constants)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Uncompress::AnyUncompress)
BuildRequires:  perl(IO::Uncompress::Base)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a Perl interface that allows writing zstd compressed
data to files or buffer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Compress-Zstd-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test COMPRESS_ZLIB_RUN_ALL=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
