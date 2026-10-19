%global source0_hash 74f3f2e336c4b529775398bbd0e9ab3f40020b3730b5ce6d87ac0dababa6af64
%global io_compress_version 2.213
Name:           perl-Archive-Zip-SimpleZip
Version:        1.002
Release:        1%{?dist}
Summary:        Create Zip Archives
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Archive-Zip-SimpleZip/
Source0:        https://cpan.metacpan.org/modules/by-module/Archive/Archive-Zip-SimpleZip-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(IO::Compress::Base) >= %{io_compress_version}
Requires:       perl(IO::Compress::Bzip2) >= %{io_compress_version}
Requires:       perl(IO::Compress::Lzma) >= %{io_compress_version}
Requires:       perl(IO::Compress::RawDeflate) >= %{io_compress_version}
Requires:       perl(IO::Compress::Xz) >= %{io_compress_version}
Requires:       perl(IO::Compress::Zstd) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::Base) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::Bunzip2) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::RawInflate) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::UnLzma) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::UnXz) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::UnZstd) >= %{io_compress_version}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Compress::Adapter::Deflate)
BuildRequires:  perl(IO::Compress::Base)
BuildRequires:  perl(IO::Compress::Base::Common)
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Lzma)
BuildRequires:  perl(IO::Compress::RawDeflate)
BuildRequires:  perl(IO::Compress::Xz)
BuildRequires:  perl(IO::Compress::Zip)
BuildRequires:  perl(IO::Compress::Zip::Constants)
BuildRequires:  perl(IO::Compress::Zstd)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Uncompress::Base)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::RawInflate)
BuildRequires:  perl(IO::Uncompress::UnLzma)
BuildRequires:  perl(IO::Uncompress::UnXz)
BuildRequires:  perl(IO::Uncompress::UnZstd)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Archive::Zip::SimpleZip is a module that allows the creation of Zip
archives. For reading Zip archives, there is a companion module, called
Archive::Zip::SimpleUnzip, that can read Zip archives.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Archive-Zip-SimpleZip-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
