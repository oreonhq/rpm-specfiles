%global source0_hash ff89a9b36b38e24563c538ef3792d3fffdc4b38978662c394e593ead1ca92887

Name:           perl-Imager
Version:        1.029
Release:        2%{?dist}
Summary:        Perl extension for Generating 24 bit Images
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Imager
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TONYC/Imager-%{version}.tar.gz
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel >= 4.0.8
BuildRequires:  t1lib-devel
# rgb.txt, c.f. lib/Imager/Color.pm
BuildRequires:  rgb
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
# Unused BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Liblist)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(B)
BuildRequires:  perl(bignum)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(Tie::Handle)
# Optional tests only
BuildRequires:  perl(Affix::Infix2Postfix)
BuildRequires:  perl(CPAN::Meta) >= 2.110580
BuildRequires:  perl(Image::Math::Constrain)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       pkgconfig
Requires:       rgb
# Unused Requires:       perl(File::Spec)
Requires:       perl(warnings::register)
Requires:       perl(XSLoader)

%{?perl_default_filter}

# Imager-1.020 disabled Imager::Font::T1 and Freetype 1.x fonts by default
# Installing Imager no longer installs Imager::Font::T1 by default.
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Imager::Font::T1\\)

%description
Imager is a module for creating and altering images. It can read and
write various image formats, draw primitive shapes like lines,and
polygons, blend multiple images together in various ways, scale, crop,
render text and more.

%package Test
Requires: perl-Imager = %{version}-%{release}
Summary: perl-Imager's Test module

%description Test
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Imager-%{version}
find -executable -type f -exec chmod -x {} \;
perl -MConfig -pi -e 's|^#!perl|$Config{startperl}|' samples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README samples
%{perl_vendorarch}/auto/Imager*
%exclude %{perl_vendorarch}/Imager/Test.pm
%{perl_vendorarch}/Imager*
%exclude %{_mandir}/man3/Imager::Test.3pm*
%{_mandir}/man3/Imager*

%files Test
%dir %{perl_vendorarch}/Imager
%{perl_vendorarch}/Imager/Test.pm
%{_mandir}/man3/Imager::Test.3pm*

%changelog
%autochangelog
