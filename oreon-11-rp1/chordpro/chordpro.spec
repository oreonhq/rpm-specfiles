%global source0_hash 554dfc744b882d8fa05f300dd8d1a06c4c547a4d91edf8bd19ba0c65ce616f9c
%global FullName App-Music-ChordPro
Name: chordpro
Summary:        Print songbooks (lyrics + chords)
License: Artistic-2.0
Version: 6.101.0
Release:        1%{?dist}
Source0:        https://cpan.metacpan.org/authors/id/J/JV/JV/%{FullName}-%{version}.tar.gz
Source1: README.ABC
Source2: README.LilyPond
Source3: README.WX
Patch1: chordpro-abc.patch
Patch2: chordpro-fonts.patch
Obsoletes: chordpro-abc == 6.050.4
URL: https://www.chordpro.org
BuildArch: noarch
%global __provides_exclude_from /*\\.pm$
%global __requires_exclude ChordPro|SVGPDF|JSON
Requires: perl(:VERSION) >= 5.26.0
Requires: perl(SVGPDF)                      >= 0.091
Requires: gnu-free-fonts-common
Requires: gnu-free-mono-fonts
Requires: gnu-free-sans-fonts
Requires: gnu-free-serif-fonts
Requires: perl(Data::Printer)               >= 1.001001
Requires: perl(File::Copy)                  >= 2.32
Requires: perl(File::HomeDir)               >= 1.004
Requires: perl(File::LoadLines)             >= 1.047
Requires: perl(FindBin)
Requires: perl(HarfBuzz::Shaper)	    >= 0.026
Requires: perl(Hash::Util)
Requires: perl(Image::Info)                 >= 1.41
Requires: perl(JSON::PP)                    >= 2.27203
Requires: perl(JSON::XS)                    >= 4.03
Requires: perl(LWP::Protocol::https)
Requires: perl(List::Util)                  >= 1.46
Requires: perl(Object::Pad)                 >= 0.818
Requires: perl(PDF::API2)                   >= 2.045
Requires: perl(Ref::Util)		    >= 0.204
Requires: perl(Scalar::Util)		    >= 1.63
Requires: perl(Storable)                    >= 3.08
Requires: perl(String::Interpolate::Named)  >= 1.06
Requires: perl(Text::Layout)                >= 0.045
Requires: perl(Unicode::Collate)
Requires: perl(Unicode::Normalize)
Requires: perl(Unicode::Normalize)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gnu-free-fonts-common
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Printer)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::LoadLines)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HarfBuzz::Shaper)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(Image::Info)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Object::Pad)
BuildRequires:  perl(PDF::API2)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(SVGPDF)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::Interpolate::Named)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Layout)
BuildRequires:  perl(Unicode::Collate)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-libs
# /oreon:deps
%description
ChordPro will read a text file containing the lyrics of one or many
songs plus chord information. ChordPro will then generate a
photo-ready, professional looking, impress-your-friends sheet-music
suitable for printing on your nearest printer.

To learn more about ChordPro, look for the man page or do
chordpro --help for the list of options.

To use the integrated support for ABC, please install CPAN module
JavaScript::QuickJS.

For more information about ChordPro, see https://www.chordpro.org.

%package gui
Summary: ChordPro graphical user interface
Requires: %{name} = %{version}-%{release}
Requires: perl(Wx) >= 0.99
%description gui
This package installs the requirements for the wxWidgets (GUI) version
of ChordPro.

To run the GUI version it is better (though not strictly necessary) to
install an updated version of the perl Wx module. See
https://github.com/sciurius/wxPerl for instructions.

%package lilypond
Summary: Support for ChordPro LilyPond embedding
Requires: %{name} = %{version}-%{release}
Requires: lilypond
%description lilypond
This packages installs the requirements for LilyPond support for ChordPro.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{FullName}-%{version}

# Fix version.
# perl -pi~ -e 's/6.080.0/6.080/' lib/ChordPro/Version.pm

%patch -P 1 -p0 -b .abc
%patch -P 2 -p0 -b .fonts

# Update outdated READMEs.
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .
cp -a %{SOURCE3} .

# Remove some stuff.
rm lib/ChordPro/res/linux/setup_desktop.sh
# LaTeX (not yet supported).
rm lib/ChordPro/Output/LaTeX.pm
rm lib/ChordPro/res/templates/*.tt
rm t/74_latex.t
# MarkDown (not yet supported).
rm lib/ChordPro/Output/Markdown.pm
rm t/73_md.t
# Use system package.
rm -fr lib/ChordPro/lib/SVGPDF*
# Fonts (use system fonts).
rm lib/ChordPro/res/fonts/Free*.ttf

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%check

make test
%install
%global share %{_datadir}/%{name}-%{version}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
echo "# Placeholder" > %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
mkdir -p %{buildroot}%{share}/lib
mkdir -p %{buildroot}%{_bindir}
find blib/lib -type f -name .exists -delete
find blib/lib -type d -printf "mkdir %{buildroot}%{share}/lib/%%P\n" | sh -x
find blib/lib ! -type d -printf "install -p -m 0644 %p %{buildroot}%{share}/lib/%%P\n" | sh -x
for script in chordpro wxchordpro ttc
do
  sed -e "s;for my .lib .*.;for my \$lib ( qw(%{share}/lib) ) {;" \
    < script/${script} >> %{buildroot}%{_bindir}/${script}
  chmod 0755 %{buildroot}%{_bindir}/${script}
  mkdir -p %{buildroot}%{_mandir}/man1
  pod2man blib/script/${script} > %{buildroot}%{_mandir}/man1/${script}.1
done
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
install -p -m 0664 \
    lib/ChordPro/res/icons/chordpro.png \
    lib/ChordPro/res/icons/chordpro-doc.png \
    %{buildroot}%{_datadir}/pixmaps/
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    lib/ChordPro/res/linux/org.%{name}.desktop
mkdir -p %{buildroot}%{_metainfodir}
cp -p lib/ChordPro/res/linux/org.%{name}.metainfo.xml \
    %{buildroot}%{_metainfodir}/org.%{name}.metainfo.xml
%{_fixperms} %{buildroot}/*
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%oreon_autofiles chordpro-gui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles chordpro-lilypond usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post gui

xdg-desktop-menu install --novendor %{share}/lib/ChordPro/res/linux/org.chordpro.desktop
xdg-icon-resource install --context mimetypes --size 256 %{share}/lib/ChordPro/res/icons/chordpro-doc.png x-chordpro-doc
xdg-mime install --novendor %{share}/lib/ChordPro/res/linux/chordpro.xml
update-desktop-database
update-mime-database %{_datadir}/mime
gtk-update-icon-cache %{_datadir}/icons/hicolor
%postun

[ $1 = 0 ] && rm -rf %{share}
%postun gui

if [ $1 = 0 ]; then
xdg-icon-resource uninstall --context mimetypes --size 256 x-chordpro-doc
fi
update-desktop-database
update-mime-database %{_datadir}/mime
gtk-update-icon-cache %{_datadir}/icons/hicolor
%files -f %{oreon_filedir}/main.list
%files -n chordpro-gui -f %{oreon_filedir}/chordpro-gui.list
%files -n chordpro-lilypond -f %{oreon_filedir}/chordpro-lilypond.list

%changelog

%autochangelog
