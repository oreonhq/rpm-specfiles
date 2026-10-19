%global source0_hash 9d6c1d28c29b137b1a5152e628083d8437577336d8bea191605dda20d55b3539
Name:           perl-Image-Info
Version:        1.45
Release:        1%{?dist}
Summary:        Image meta information extraction module for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Image-Info
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Image-Info-%{version}.tar.gz
BuildArch:      noarch
Requires:       rgb
Requires:       perl(Compress::Zlib)
Requires:       perl(IO::Scalar)
Provides:       perl(Image::Info)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Image::Xbm)
BuildRequires:  perl(Image::Xpm)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(PerlIO::scalar)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Strict)
BuildRequires:  perl(XML::LibXML::Reader)
BuildRequires:  perl(XML::SAX::PurePerl)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl extension allows you to extract meta information from
various types of image files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Image-Info-%{version}
chmod -c 644 exifdump imgdump

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
