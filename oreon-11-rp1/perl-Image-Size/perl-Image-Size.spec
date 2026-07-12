%global source0_hash 53c9b1f86531cde060ee63709d1fda73cabc0cf2d581d29b22b014781b9f026b

%if 0%{?rhel} == 8
%bcond_without graphics_magick
%else
%bcond_with graphics_magick
%endif

Name:           perl-Image-Size
Version:        3.300
Release:        34%{?dist}
Summary:        Determine the size of images in several common formats in Perl
# Automatically converted from old format: LGPLv2 or Artistic 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 OR Artistic-2.0
URL:            https://metacpan.org/release/Image-Size
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJRAY/Image-Size-%{version}.tar.gz
# WEBP: use proper endian-agnostic extractor 
# https://github.com/rjray/image-size/commit/37609b9079cc2449589fa436baa2e08a3e2b427d
Patch0:         perl-Image-Size-3.300-endian-fix.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(bytes)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
%if %{with graphics_magick}
BuildRequires:  perl(Graphics::Magick)
%else
BuildRequires:  perl(Image::Magick)
%endif
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Compress::Zlib)
Requires:       perl(Cwd)
Requires:       perl(File::Spec)
%if %{with graphics_magick}
Recommends:     perl(Graphics::Magick)
%else
Recommends:     perl(Image::Magick)
%endif
Requires:       perl(Symbol)

Provides:       perl(Image::Size)
%description
Image::Size is a library based on the image-sizing code in the wwwimagesize
script, a tool that analyzes HTML files and adds HEIGHT and WIDTH tags to
IMG directives. Image::Size has generalized that code to return a raw (X, Y)
pair, and included wrappers to pre-format that output into either HTML or
a set of attribute pairs suitable for the CGI.pm library by Lincoln Stein.
Currently, Image::Size can size images in XPM, XBM, GIF, JPEG, PNG, MNG, TIFF,
the PPM family of formats (PPM/PGM/PBM) and if Image::Magick is installed,
the formats supported by it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Image-Size-%{version}
%patch -P0 -p1 -b .endianfix

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
chmod -R u+w %{buildroot}/*

%check
make test

%files
%doc ChangeLog README
%{_bindir}/imgsize
%{perl_vendorlib}/Image/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*


%changelog
%autochangelog
