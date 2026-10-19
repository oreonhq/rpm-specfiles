%global source0_hash 369de1a4a5652899a39a45598326248d9c72f02c16812a50e868b7401f634d89
Name:           perl-PDF-API2
Version:        2.048
Release:        1%{?dist}
Summary:        Perl module for creation and modification of PDF files
License:        LGPL-2.1-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (MIT OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/PDF-API2
Source0:        https://cpan.metacpan.org/authors/id/S/SS/SSIMMS/PDF-API2-%{version}.tar.gz
Source1:        COPYING-PDF_API2_Basic_PDF-Martin_Hosken
Patch1:         font-location.patch
Patch2:         PDF-API2-2.033-Use-libtiff-to-decode-image-data-in-TIFF-fixing-RT-1.patch
BuildArch:      noarch
Requires:       dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       dejavu-serif-fonts
Requires:       perl(Compress::Zlib) >= 1.0
Requires:       perl(Storable)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Compress::Zlib\\)$
Provides:       perl(PDF::API2)
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  libtiff-tools
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Font::TTF::Font)
BuildRequires:  perl(GD)
BuildRequires:  perl(Graphics::TIFF)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A Perl Module Chain to facilitate the Creation and Modification of High-Quality
"Portable Document Format (aka. PDF)" Files.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       ImageMagick
Requires:       libtiff-tools
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n PDF-API2-%{version}
install -m 0644 %{SOURCE1} ./

# fix interpreter in example files
for file in contrib/pdf-{de,}optimize.pl; do
    perl -MConfig -pi -e 's|^#!.*perl\b|$Config{startperl}|' "$file"
done

# make mode on included contrib 0644 to keep from triggering
# rpmlint warning and additional auto-requires
chmod a-x contrib/*

# recode Changes as UTF-8
iconv -f iso-8859-1 -t utf-8 < Changes > Changes.utf8
mv -f Changes.utf8 Changes

# Help file to recognise the Perl scripts and normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/author-critic.t
rm -f %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
perl -i -pe 's{\^\blib\b}{^%{perl_vendorlib}}' %{buildroot}/%{_libexecdir}/%{name}/t/00-all-usable.t
perl -i -pe 's{\blib\b}{%{perl_vendorlib}/PDF}' %{buildroot}/%{_libexecdir}/%{name}/t/00-all-usable.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
rm -rf %{buildroot}/%{perl_vendorlib}/PDF/API2/fonts
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PDF-API2-tests -f %{oreon_filedir}/perl-PDF-API2-tests.list

%changelog

%autochangelog
