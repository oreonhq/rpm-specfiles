%global source0_hash 59a762acd704f045a0f5ad5e5ba5d8ef05138fcc027840665a312103c7c02111
Name:		perl-Image-ExifTool
Version:	13.44
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Utility for reading and writing image meta info
URL:		http://www.sno.phy.queensu.ca/%7Ephil/exiftool/
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXIFTOOL/Image-ExifTool-%{version}.tar.gz
BuildArch:	noarch
Requires:       perl(FileHandle)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Compress::Raw::Lzma)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Compress::Brotli)
BuildRequires:  perl(IO::Compress::RawDeflate)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Uncompress::Brotli)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::RawInflate)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(POSIX::strptime)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
ExifTool is a Perl module with an included command-line application for
reading and writing meta information in image, audio, and video files.
It reads EXIF, GPS, IPTC, XMP, JFIF, MakerNotes, C2PA JUMBF, GeoTIFF,
ICC Profile, Photoshop IRB, FlashPix, AFCP, ID3 and Lyric3 meta
information from JPG, JP2, TIFF, GIF, PNG, MNG, JNG, MIFF, EPS, PS, AI,
PDF, PSD, BMP, THM, CRW, CR2, MRW, NEF, PEF, ORF, DNG, and many other
types of images. ExifTool also extracts information from the maker
notes of many digital cameras by various manufacturers including Apple,
Canon, Casio, DJI, FLIR, FujiFilm, GE, Google, GoPro, HP, JVC/Victor,
Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Nintendo, Olympus/Epson,
Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx, Ricoh, Samsung, Sanyo,
Sigma/Foveon, and Sony.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Image-ExifTool-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
