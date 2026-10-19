%global source0_hash f26f80c44cd49ca0d40ac000469a7ace2e4a3172e5c71ba5f3be70d5b9be0af8
%global commit 4bcdc19ca9a2a5b9817e3e501d0018b58bf577d0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           perl-File-Unpack2
Version:        2.02
Release:        1%{?dist}
Summary:        Strong archive file unpacker, based on mime-types
License:        (MIT OR GPL-1.0-or-later) AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
Source0:        %{name}-%{shortcommit}-repackaged.tar.gz
URL:            https://github.com/openSUSE/perl-File-Unpack2
Requires:       perl(File::LibMagic)
Requires:       perl(File::MimeInfo::Magic)
Requires:       perl(Compress::Raw::Lzma)
Requires:       perl(Compress::Raw::Bzip2)
Requires:       file >= 5.03
Requires:       shared-mime-info >= 0.60
Requires:       perl(BSD::Resource)
Requires:       perl(Compress::Raw::Zlib) >= 2.024
Requires:       perl(Filesys::Statvfs)
Requires:       xz
Requires:       lzip
Requires:       poppler-utils
Requires:       binutils
Requires:       bzip2
Requires:       cabextract
Requires:       cpio
Requires:       genisoimage
Requires:       gzip
Requires:       p7zip-plugins
Requires:       rpm
Requires:       sharutils
Requires:       tar
Requires:       unzip
Recommends:     unrar poppler-utils xz upx antiword
Recommends:     file-unpack == %version
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  file
BuildRequires:  gcc
BuildRequires:  lzip
BuildRequires:  make
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Bzip2)
BuildRequires:  perl(Compress::Raw::Lzma)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::LibMagic)
BuildRequires:  perl(File::MimeInfo::Magic)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filesys::Statvfs)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Text::Sprintf::Named)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  poppler-utils
BuildRequires:  shared-mime-info
BuildRequires:  xz
# /oreon:deps
%description
File::Unpack2 is an unpacker for archives and files
(bz2/gz/zip/tar/cpio/iso/rpm/deb/cab/lzma/7z/rar/...).  We call it strong,
because it is not fooled by file suffixes or multiple wrapped packages.  It
reliably detects mime types and recursively descends into each archive found
until it finally exposes all unpackable payload contents.  A precise log file
can be written, describing mime types and unpacking actions.  Most of the known
archive file formats are supported. Shell-script-style plugins can be added to
support additional formats.

%package -n file-unpack
Summary:        Command line tool to unpack anything
Requires:       %{name}%{?_isa} == %{version}-%{release}
License:        MIT OR GPL-1.0-or-later OR (GPL-1.0-or-later OR Artistic-1.0-Perl)
%description -n file-unpack
/usr/bin/file-unpack is a trivial command line frontend that
ships with the File::Unpack perl module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
(cd contrib && %{make_build} stringsx)
%install
%{make_install}
mv %{buildroot}/usr/bin/{file_unpack,file-unpack} || :
install -d       %{buildroot}/usr/share/File-Unpack/helper/
install helper/* %{buildroot}/usr/share/File-Unpack/helper/
%fdupes %{buildroot}/usr/share/File-Unpack/
ln -s file-unpack2 %{buildroot}/%{_bindir}/file_unpack
ln -s file-unpack2 %{buildroot}/%{_bindir}/unpack-file
ln -s file-unpack2 %{buildroot}/%{_bindir}/unpack-file-deep
ln -s file-unpack2 %{buildroot}/%{_bindir}/unpack-deep
ln -s file-unpack2 %{buildroot}/%{_bindir}/file-unpack-deep
cat <<EOF> file-unpack.pod
=pod
=head1 SYNOPSIS
EOF
perl file-unpack2.pl --help >> file-unpack2.pod && true
cat <<EOF1>> file-unpack2.pod
=head1 REFERENCES
See also C<perldoc File::Unpack>
EOF1
pod2man file-unpack2.pod > file-unpack2.1
rm file-unpack2.pod
echo <<EOF2>> MANIFEST
file-unpack2.1
EOF2
install -m0644 -D file-unpack2.1 %{buildroot}/%_mandir/man1/file-unpack2.1
ln -s file-unpack.1 %{buildroot}/%_mandir/man1/unpack_file2.1
install -m0755 -D contrib/stringsx %{buildroot}/%_bindir/stringsx
rm contrib/stringsx # so that the Manifest in make check is not confused.
%{_fixperms} %{buildroot}/*
%oreon_autofiles file-unpack usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n file-unpack -f %{oreon_filedir}/file-unpack.list

%changelog

%autochangelog
