%global source0_hash 05912170e9872c5898cd62647518bd5c58c214fd1f7ca8ebb967f87c46af480e
Name:           perl-Image-PNG-Libpng
Version:        0.60
Release:        1%{?dist}
Summary:        Perl interface to the libpng library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
SourceLicense:  (%{license}) AND LicenseRef-Fedora-UltraPermissive AND GPL-2.0-or-later
URL:            https://metacpan.org/release/Image-PNG-Libpng
Source0:        Image-PNG-Libpng-%{version}_repackaged.tar.gz
Source1:        repackage.sh
Patch0:         Image-PNG-Libpng-0.58-Remove-tests-depending-on-proprietary-files.patch
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IPNGLT\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(IPNGLT\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libpng)
# /oreon:deps
%description
Image::PNG::Libpng is a Perl library for accessing the contents of PNG
(Portable Network Graphics) images. It enables Perl to read and write files in
the PNG format.

%package tools
Summary:        Tools for inspecting PNG images
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Suggests:       perl(Data::Validate::URI)
Suggests:       perl(JSON::Create)
Suggests:       perl(LWP::Simple)
%description tools
pnginspect tool prints a text representation of the data within a PNG image
file to standard output. If you have Data::Validate::URI and LWP::Simple
installed, you can also use it to examine PNG files on the web.

%package tests
Summary:        Tests for %{name}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-UltraPermissive
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n Image-PNG-Libpng-%{version}
# Do not install author scripts
for F in get-pixel.pl nicemake.pl t/make-tEXT.pl; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL --check INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
unset ORIGINAL_ZLIB
prove -I . -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset ORIGINAL_ZLIB
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Image-PNG-Libpng-tools -f %{oreon_filedir}/perl-Image-PNG-Libpng-tools.list
%files -n perl-Image-PNG-Libpng-tests -f %{oreon_filedir}/perl-Image-PNG-Libpng-tests.list

%changelog

%autochangelog
