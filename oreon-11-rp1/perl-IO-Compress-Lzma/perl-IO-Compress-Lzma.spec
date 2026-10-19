%global source0_hash b6f13b2e405dc413503d88ffaa92f280402fe3992f45a3e6b1a59aed7a60d834
%if 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
%bcond_with perl_IO_Compress_Lzma_enables_optional_test
%else
%bcond_without perl_IO_Compress_Lzma_enables_optional_test
%endif
Name:		perl-IO-Compress-Lzma
Version:	2.224
Release:        1%{?dist}
Summary:        Read and write lzma compressed data
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/IO-Compress-Lzma
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/IO-Compress-Lzma-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_IO_Compress_Lzma_enables_optional_test}
%endif
Provides:       perl(IO::Uncompress::UnXz)
# oreon:deps
BuildRequires:  /usr/bin/7z
BuildRequires:  coreutils
BuildRequires:  lzip
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Lzma)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Compress::Base)
BuildRequires:  perl(IO::Compress::Base::Common)
BuildRequires:  perl(IO::Compress::Zip)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Uncompress::AnyUncompress)
BuildRequires:  perl(IO::Uncompress::Base)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  xz
BuildRequires:  xz-lzma-compat
# /oreon:deps
%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the lzma library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Compress-Lzma-%{version}

# Remove bundled test modules
rm -rv t/Test/
perl -i -ne 'print $_ unless m{^t/Test/}' MANIFEST

# Remove spurious exec permissions
chmod -c -x examples/*

# Fix shellbangs in examples
perl -pi -e 's|^#!/usr/local/bin/perl\b|#!/usr/bin/perl|' \
	examples/lzcat examples/lzstream examples/xzcat examples/xzstream

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test COMPRESS_ZLIB_RUN_MOST=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
