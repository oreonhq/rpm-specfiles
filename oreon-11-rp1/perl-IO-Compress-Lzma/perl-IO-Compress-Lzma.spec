%global source0_hash 3462ecd1e67e85d5e4fa911bc6d8e38a884ba1d6e90a03535f0d28fe2ad0aacf

# Perform optional tests
%if 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
%bcond_with perl_IO_Compress_Lzma_enables_optional_test
%else
%bcond_without perl_IO_Compress_Lzma_enables_optional_test
%endif

Name:		perl-IO-Compress-Lzma
Version:	2.217
Release:	1%{?dist}
Summary:	Read and write lzma compressed data
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/IO-Compress-Lzma
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Compress-Lzma-%{version}.tar.gz



BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(lib)
# Module Runtime
BuildRequires:	perl(bytes)
BuildRequires:	perl(Compress::Raw::Lzma) >= %{version}
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::Compress::Base) >= %{version}
BuildRequires:	perl(IO::Compress::Base::Common) >= %{version}
BuildRequires:	perl(IO::Uncompress::Base) >= %{version}
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Carp)
BuildRequires:	perl(Compress::Raw::Zlib) >= 2
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Compress::Zip)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Uncompress::AnyUncompress)
BuildRequires:	perl(IO::Uncompress::Unzip)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	xz, xz-lzma-compat
%if %{with perl_IO_Compress_Lzma_enables_optional_test}
# Optional Tests
BuildRequires:	lzip
BuildRequires:	perl(Encode)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::CPAN::Meta::JSON)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	/usr/bin/7z
%endif
# Dependencies
# (none)

Provides:       perl(IO::Uncompress::UnXz)
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

%check
make test COMPRESS_ZLIB_RUN_MOST=1

%files
%doc Changes README examples/*
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Compress::Lzip.3*
%{_mandir}/man3/IO::Compress::Lzma.3*
%{_mandir}/man3/IO::Compress::Xz.3*
%{_mandir}/man3/IO::Uncompress::UnLzip.3*
%{_mandir}/man3/IO::Uncompress::UnLzma.3*
%{_mandir}/man3/IO::Uncompress::UnXz.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.217-1
- Import
