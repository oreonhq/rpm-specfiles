%global source0_hash b3a127bdba8e79010b239291415cbe3431333521e24477a814b586e1b4027360
Name:           TeXmacs
Version:        2.1.5
Release:        1%{?dist}
Summary:        Structured WYSIWYG scientific text editor
License:        GPL-2.0-or-later
URL:            http://www.texmacs.org
Source0:        http://www.texmacs.org/Download/ftp/tmftp/source/TeXmacs-%{version}-src.tar.gz
Patch0:         https://github.com/texmacs/texmacs/pull/73.patch
Patch1:         https://github.com/texmacs/texmacs/pull/107.patch
Patch2:         https://github.com/texmacs/texmacs/pull/109.patch
Requires:       ghostscript
Requires:       texmacs-fedora-fonts = %{version}-%{release}
Provides:       texmacs = %{version}-%{release}
Requires:       fig2ps
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  compat-guile18-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
BuildRequires:  freetype-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
GNU TeXmacs is a free scientific text editor, which was both inspired
by TeX and GNU Emacs. The editor allows you to write structured
documents via a WYSIWYG (what-you-see-is-what-you-get) and user
friendly interface.  New styles may be created by the user. The
program implements high-quality typesetting algorithms and TeX fonts,
which help you to produce professionally looking documents.

The high typesetting quality still goes through for automatically
generated formulas, which makes TeXmacs suitable as an interface for
computer algebra systems. TeXmacs also supports the Guile/Scheme
extension language, so that you may customize the interface and write
your own extensions to the editor.

In the future, TeXmacs is planned to evolve towards a complete
scientific office suite, with spreadsheet capacities, a technical
drawing editor and a presentation mode.

%package devel
Summary:        Development files for TeXmacs
Requires:       %{name} = %{version}-%{release}
%description devel
Development files required to create TeXmacs plugins.

%package -n texmacs-fedora-fonts
Summary:        Fonts for TeXmacs
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%description -n texmacs-fedora-fonts
TeXmacs font.

%prep

%autosetup -p1 -n TeXmacs
%{py3_shebang_fix} plugins/mathematica/bin/realpath.py

%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/texmacs.desktop
rm -f %{buildroot}%{_bindir}/fig2ps
rm -f %{buildroot}%{_mandir}/man*/fig2ps*
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_datadir}/TeXmacs/fonts/type1/ec/
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/ec/$i
done
cd ../la
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/la/$i
done
cd ../math
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/math/$i
done
popd
rm -f %{buildroot}%{_datadir}/icons/gnome/icon-theme.cache
find %{buildroot}%{_datadir}/mime/ -type f -maxdepth 1 -print | xargs rm -f
%oreon_autofiles TeXmacs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles texmacs-fedora-fonts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n TeXmacs-devel -f %{oreon_filedir}/TeXmacs-devel.list
%files -n texmacs-fedora-fonts -f %{oreon_filedir}/texmacs-fedora-fonts.list

%changelog

%autochangelog
