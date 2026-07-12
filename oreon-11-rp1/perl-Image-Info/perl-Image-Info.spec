%global source0_hash 9d6c1d28c29b137b1a5152e628083d8437577336d8bea191605dda20d55b3539

Name:           perl-Image-Info
Version:        1.45
Release:        4%{?dist}
Summary:        Image meta information extraction module for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Image-Info
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Image-Info-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# Build
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Image::Xbm)
BuildRequires:  perl(Image::Xpm)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(PerlIO::scalar)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML::Reader)
BuildRequires:  perl(XML::Simple)
# Run
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Symbol)
# Tests
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(Test::Strict)
BuildRequires:  perl(XML::SAX::PurePerl)
Requires:       rgb
Requires:       perl(Compress::Zlib)
Requires:       perl(IO::Scalar)

Provides:       perl(Image::Info)
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

%check
make test

%files
%doc CHANGES CREDITS README TODO exifdump imgdump
%{perl_vendorlib}/Bundle/
%{perl_vendorlib}/Image/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
