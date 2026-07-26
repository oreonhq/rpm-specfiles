%global source0_hash cffcf135cd0622287d3b02154f7d6716495449fcaed03966621948e25ea5f742

# Enable LZMA and XZ support via pure-Perl implementation
%if 0%{?rhel}
%bcond_with perl_Archive_Extract_enables_perl_xz
%else
%bcond_without perl_Archive_Extract_enables_perl_xz
%endif

Name:           perl-Archive-Extract
# Epoch to compete with core module from perl.spec
Epoch:          1
Version:        0.88
Release:        15%{?dist}
Summary:        Generic archive extracting mechanism
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Archive-Extract
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Archive-Extract-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
# Prefer Archive::Tar to suppress warnings, bug #1217352, CPAN RT#104121
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(if)
BuildRequires:  perl(IPC::Cmd) >= 0.64
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load::Conditional) >= 0.66
BuildRequires:  perl(Params::Check) >= 0.07
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(deprecate)
# Prefer Archive::Tar to suppress warnings, bug #1217352, CPAN RT#104121
Requires:       perl(Archive::Tar)
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(IPC::Cmd) >= 0.64
Requires:       perl(Module::Load::Conditional) >= 0.66
Requires:       perl(Params::Check) >= 0.07
# Decompressors:
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

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|IPC::Cmd|Module::Load::Conditional|Params::Check)\\)$

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
# perl-Extract-Archive-lzma-Compress-unLZMA removed because Compress::unLZMA
# is not yet packaged
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

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files bz2-bunzip2
%files bz2-IO-Uncompress-Bunzip2
%files gz-gzip
%files gz-Compress-Zlib
%files lzma-unlzma
%if %{with perl_Archive_Extract_enables_perl_xz}
%files lzma-IO-Uncompress-UnLzma
%endif
%if %{with perl_Archive_Extract_enables_perl_xz}
#%%files lzma-Compress-unLZMA
%endif
%files tar-tar
%files tar-Archive-Tar
%files tbz-tar-bunzip2
%files tbz-Archive-Tar-IO-Uncompress-Bunzip2
%files tgz-tar-gzip
%files tgz-Archive-Tar-Compress-Zlib
%files tgz-Archive-Tar-IO-Zlib
%files txz-tar-unxz
%if %{with perl_Archive_Extract_enables_perl_xz}
%files txz-Archive-Tar-IO-Uncompress-UnXz
%endif
%files Z-uncompress
%files Z-Compress-Zlib
%files zip-unzip
%files zip-Archive-Zip
%files xz-unxz
%if %{with perl_Archive_Extract_enables_perl_xz}
%files xz-IO-Uncompress-UnXz
%endif

%changelog
%autochangelog
