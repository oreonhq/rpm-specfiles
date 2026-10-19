%global source0_hash cffcf135cd0622287d3b02154f7d6716495449fcaed03966621948e25ea5f742
%bcond_without perl_Archive_Extract_enables_perl_xz
Name:           perl-Archive-Extract
Epoch:          1
Version:        0.88
Release:        1%{?dist}
Summary:        Generic archive extracting mechanism
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Archive-Extract
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Archive-Extract-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(deprecate)
Requires:       perl(Archive::Tar)
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(IPC::Cmd) >= 0.64
Requires:       perl(Module::Load::Conditional) >= 0.66
Requires:       perl(Params::Check) >= 0.07
Requires:       %{name}-bz2
Requires:       %{name}-gz
Requires:       %{name}-lzma
Requires:       %{name}-tar
Requires:       %{name}-tbz
Requires:       %{name}-tgz
Requires:       %{name}-txz
Requires:       %{name}-Z
Requires:       %{name}-zip
Requires:       %{name}-xz
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|IPC::Cmd|Module::Load::Conditional|Params::Check)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Archive::Extract is a generic archive extraction mechanism.  It allows you to
extract any archive file of the type .tar, .tar.gz, .gz, .Z, tar.bz2, .tbz,
.bz2, .zip, .xz,, .txz, .tar.xz, or .lzma without having to worry how it does
so, or use different interfaces for each type by using either perl modules, or
command-line tools on your system.

# Decompressors:
# bz2:  bunzip2 || IO::Uncompress::Bunzip2
%package bz2-bunzip2
Summary:    Bzip2 decompressor for %{name} via bunzip2
Provides:   %{name}-bz2 = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   bzip2
%description bz2-bunzip2
%{summary}.

%package bz2-IO-Uncompress-Bunzip2
Summary:    Bzip2 decompressor for %{name} via IO::Uncompress::Bunzip2
Provides:   %{name}-bz2 = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(IO::Uncompress::Bunzip2)
%description bz2-IO-Uncompress-Bunzip2
%{summary}.

# gz:   gzip || Compress::Zlib
%package gz-gzip
Summary:    Gzip decompressor for %{name} via gzip
Provides:   %{name}-gz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   gzip
%description gz-gzip
%{summary}.

%package gz-Compress-Zlib
Summary:    Gzip decompressor for %{name} via Compress::Zlib
Provides:   %{name}-gz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(Compress::Zlib)
%description gz-Compress-Zlib
%{summary}.

# lzma: unlzma || IO::Uncompress::UnLzma || Compress::unLZMA
%package lzma-unlzma
Summary:    Lzma decompressor for %{name} via unlzma
Provides:   %{name}-lzma = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   xz-lzma-compat
%description lzma-unlzma
%{summary}.

%if %{with perl_Archive_Extract_enables_perl_xz}
%package lzma-IO-Uncompress-UnLzma
Summary:    Lzma decompressor for %{name} via IO::Uncompress::UnLzma
Provides:   %{name}-lzma = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(IO::Uncompress::UnLzma)
Obsoletes:  perl-Archive-Extract-lzma-Compress-unLZMA < 1:0.80-8
%description lzma-IO-Uncompress-UnLzma
%{summary}.
%endif

%if %{with perl_Archive_Extract_enables_perl_xz}
# Compress::unLZMA not yet packaged
#%%package lzma-Compress-unLZMA
#Summary:    Lzma decompressor for %%{name} via Compress::unLZMA
#Provides:   %%{name}-lzma = %%{epoch}:%%{version}-%%{release}
#Requires:   %%{name} = %%{epoch}:%%{version}-%%{release}
#Requires:   perl(Compress::unLZMA)
#%%description lzma-Compress-unLZMA
#%%{summary}.
%endif

# tar:  tar || Archive::Tar
%package tar-tar
Summary:    Tar decompressor for %{name} via tar
Provides:   %{name}-tar = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   tar
%description tar-tar
%{summary}.

%package tar-Archive-Tar
Summary:    Tar decompressor for %{name} via Archive::Tar
Provides:   %{name}-tar = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(Archive::Tar)
%description tar-Archive-Tar
%{summary}.

# tbz:  (tar && bunzip2) || (Archive::Tar && IO::Uncompress::Bunzip2)
%package tbz-tar-bunzip2
Summary:    Bzipped-tar decompressor for %{name} via tar an bunzip2
Provides:   %{name}-tbz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   tar
Requires:   bzip2
%description tbz-tar-bunzip2
%{summary}.

%package tbz-Archive-Tar-IO-Uncompress-Bunzip2
Summary:    Bzipped-tar decompressor for %{name} via Archive::Tar and IO::Uncompress::Bunzip2
Provides:   %{name}-tbz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(Archive::Tar)
Requires:   perl(IO::Uncompress::Bunzip2)
%description tbz-Archive-Tar-IO-Uncompress-Bunzip2
Bzipped-tar decompressor for %{name} via Archive::Tar and
IO::Uncompress::Bunzip2.

# tgz:  (tar && gzip) || (Archive::Tar && (Compress::Zlib || IO::Zlib))
%package tgz-tar-gzip
Summary:    Gzipped-tar decompressor for %{name} via tar and gzip
Provides:   %{name}-tgz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   tar
Requires:   gzip
%description tgz-tar-gzip
%{summary}.

%package tgz-Archive-Tar-Compress-Zlib
Summary:    Gzipped-tar decompressor for %{name} via Archive::Tar and Compress::Zlib
Provides:   %{name}-tgz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(Archive::Tar)
Requires:   perl(Compress::Zlib)
%description tgz-Archive-Tar-Compress-Zlib
Gzipped-tar decompressor for %{name} via Archive::Tar and
Compress::Zlib.

%package tgz-Archive-Tar-IO-Zlib
Summary:    Gzipped-tar decompressor for %{name} via Archive::Tar and IO::Zlib
Provides:   %{name}-tgz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(Archive::Tar)
Requires:   perl(IO::Zlib)
%description tgz-Archive-Tar-IO-Zlib
%{summary}.

# txz:  (tar && unxz) || (Archive::Tar && IO::Uncompress::UnXz)
%package txz-tar-unxz
Summary:    Xzed-tar decompressor for %{name} via tar and unxz
Provides:   %{name}-txz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   tar
Requires:   xz
%description txz-tar-unxz
%{summary}.

%if %{with perl_Archive_Extract_enables_perl_xz}
%package txz-Archive-Tar-IO-Uncompress-UnXz
Summary:    Xzed-tar decompressor for %{name} via Archive::Tar and IO::Uncompress::UnXz
Provides:   %{name}-txz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(Archive::Tar)
Requires:   perl(IO::Uncompress::UnXz)
%description txz-Archive-Tar-IO-Uncompress-UnXz
Xzed-tar decompressor for %{name} via Archive::Tar and
IO::Uncompress::UnXz.
%endif

# Z:    uncompress || Compress::Zlib
%package Z-uncompress
Summary:    Z decompressor for %{name} via uncompress
Provides:   %{name}-Z = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   ncompress
%description Z-uncompress
%{summary}.

%package Z-Compress-Zlib
Summary:    Z decompressor for %{name} via Compress::Zlib
Provides:   %{name}-Z = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(Compress::Zlib)
%description Z-Compress-Zlib
%{summary}.

# zip:  unzip || Archive::Zip
%package zip-unzip
Summary:    ZIP decompressor for %{name} via unzip
Provides:   %{name}-zip = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   unzip
%description zip-unzip
%{summary}.

%package zip-Archive-Zip
Summary:    ZIP decompressor for %{name} via Archive::Zip
Provides:   %{name}-zip = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(Archive::Zip)
%description zip-Archive-Zip
%{summary}.

# xz:   unxz || IO::Uncompress::UnXz
%package xz-unxz
Summary:    Xz decompressor for %{name} via unxz
Provides:   %{name}-xz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   xz
%description xz-unxz
%{summary}.

%if %{with perl_Archive_Extract_enables_perl_xz}
%package xz-IO-Uncompress-UnXz
Summary:    Xz decompressor for %{name} via IO::Uncompress::UnXz
Provides:   %{name}-xz = %{epoch}:%{version}-%{release}
Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   perl(IO::Uncompress::UnXz)
%description xz-IO-Uncompress-UnXz
%{summary}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Archive-Extract-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Archive-Extract-bz2-bunzip2 -f %{oreon_filedir}/perl-Archive-Extract-bz2-bunzip2.list
%files -n perl-Archive-Extract-bz2-IO-Uncompress-Bunzip2 -f %{oreon_filedir}/perl-Archive-Extract-bz2-IO-Uncompress-Bunzip2.list
%files -n perl-Archive-Extract-gz-gzip -f %{oreon_filedir}/perl-Archive-Extract-gz-gzip.list
%files -n perl-Archive-Extract-gz-Compress-Zlib -f %{oreon_filedir}/perl-Archive-Extract-gz-Compress-Zlib.list
%files -n perl-Archive-Extract-lzma-unlzma -f %{oreon_filedir}/perl-Archive-Extract-lzma-unlzma.list
%files -n perl-Archive-Extract-lzma-IO-Uncompress-UnLzma -f %{oreon_filedir}/perl-Archive-Extract-lzma-IO-Uncompress-UnLzma.list
%files -n perl-Archive-Extract-tar-tar -f %{oreon_filedir}/perl-Archive-Extract-tar-tar.list
%files -n perl-Archive-Extract-tar-Archive-Tar -f %{oreon_filedir}/perl-Archive-Extract-tar-Archive-Tar.list
%files -n perl-Archive-Extract-tbz-tar-bunzip2 -f %{oreon_filedir}/perl-Archive-Extract-tbz-tar-bunzip2.list
%files -n perl-Archive-Extract-tbz-Archive-Tar-IO-Uncompress-Bunzip2 -f %{oreon_filedir}/perl-Archive-Extract-tbz-Archive-Tar-IO-Uncompress-Bunzip2.list
%files -n perl-Archive-Extract-tgz-tar-gzip -f %{oreon_filedir}/perl-Archive-Extract-tgz-tar-gzip.list
%files -n perl-Archive-Extract-tgz-Archive-Tar-Compress-Zlib -f %{oreon_filedir}/perl-Archive-Extract-tgz-Archive-Tar-Compress-Zlib.list
%files -n perl-Archive-Extract-tgz-Archive-Tar-IO-Zlib -f %{oreon_filedir}/perl-Archive-Extract-tgz-Archive-Tar-IO-Zlib.list
%files -n perl-Archive-Extract-txz-tar-unxz -f %{oreon_filedir}/perl-Archive-Extract-txz-tar-unxz.list
%files -n perl-Archive-Extract-txz-Archive-Tar-IO-Uncompress-UnXz -f %{oreon_filedir}/perl-Archive-Extract-txz-Archive-Tar-IO-Uncompress-UnXz.list
%files -n perl-Archive-Extract-Z-uncompress -f %{oreon_filedir}/perl-Archive-Extract-Z-uncompress.list
%files -n perl-Archive-Extract-Z-Compress-Zlib -f %{oreon_filedir}/perl-Archive-Extract-Z-Compress-Zlib.list
%files -n perl-Archive-Extract-zip-unzip -f %{oreon_filedir}/perl-Archive-Extract-zip-unzip.list
%files -n perl-Archive-Extract-zip-Archive-Zip -f %{oreon_filedir}/perl-Archive-Extract-zip-Archive-Zip.list
%files -n perl-Archive-Extract-xz-unxz -f %{oreon_filedir}/perl-Archive-Extract-xz-unxz.list
%files -n perl-Archive-Extract-xz-IO-Uncompress-UnXz -f %{oreon_filedir}/perl-Archive-Extract-xz-IO-Uncompress-UnXz.list

%changelog

%autochangelog
