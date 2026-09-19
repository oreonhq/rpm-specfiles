%global source0_hash none

# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 0

Name:		lilypond
Version:	2.25.35
Release:	1%{?dist}
Summary:	A typesetting system for music notation

License:	GPL-3.0-only
URL:		https://lilypond.org
Source0:	https://lilypond.org/download/sources/v2.25/lilypond-%{version}.tar.gz
Source1:        century-schoolbook-l.metainfo.xml
Patch0:		lilypond-2.21.2-gcc44-relocate.patch

Requires:	ghostscript >= 8.15
Obsoletes: 	lilypond-fonts <= 2.12.1-1
Requires:	lilypond-emmentaler-fonts = %{version}-%{release}

Requires:	texlive-tex-gyre

BuildRequires:  gcc-c++
BuildRequires:  t1utils bison flex ImageMagick gettext
BuildRequires:  python3-devel
BuildRequires:  mftrace >= 1.1.19
BuildRequires:  guile30-devel
BuildRequires:  ghostscript >= 8.15
BuildRequires:  pango-devel >= 1.12.0
BuildRequires:  fontpackages-devel
BuildRequires:	perl-Pod-Parser perl(Math::Trig)
BuildRequires:	rsync
BuildRequires:  texlive-metapost
BuildRequires:  make
BuildRequires:  cairo-devel

%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

%package emmentaler-fonts
Summary:        Lilypond emmentaler fonts
Requires:       fontpackages-filesystem
Requires:	lilypond-fonts-common = %{version}-%{release}
BuildArch:	noarch

%description emmentaler-fonts
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

These are the emmentaler fonts included in the package.

%package fonts-common
Summary:        Lilypond fonts common dir
Requires:       fontpackages-filesystem
Obsoletes:      lilypond-texgyre-cursor-fonts <= 2.23.11-1
Obsoletes:      lilypond-texgyre-heros-fonts <= 2.23.11-1
Obsoletes:      lilypond-texgyre-schola-fonts <= 2.23.11-1
Obsoletes:      lilypond-c059-fonts <= 2.23.11-1
Obsoletes:      lilypond-nimbus-fonts <= 2.23.11-1
BuildArch:	noarch

%description fonts-common
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

This contains the directory common to all lilypond fonts.

%prep
%setup -q

%patch -P 0 -p0

%build
PYTHON=/usr/bin/python3
export PYTHON
%configure --disable-checking \
	--enable-documentation=no \
        --enable-cairo-backend \
	--with-texgyre-dir=/usr/share/texlive/texmf-dist/fonts/opentype/public/tex-gyre/
make %{?_smp_mflags} bytecode

%install
make install-bytecode DESTDIR=$RPM_BUILD_ROOT package_infodir=%{_infodir} \
	vimdir=%{_datadir}/vim/vimfiles

# Symlink lilypond-init.el in emacs' site-start.d directory
pushd $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
mkdir site-start.d
ln -s ../lilypond-init.el site-start.d
popd

%find_lang %{name}

mkdir -p $RPM_BUILD_ROOT%{_fontdir}
mv $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf/*.otf $RPM_BUILD_ROOT%{_fontdir}
rmdir $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf
ln -s %{_fontdir} $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf

%files -f %{name}.lang
%license COPYING
%doc AUTHORS.txt DEDICATION INSTALL.txt
%doc NEWS.txt README.md ROADMAP VERSION
%{_bindir}/*
%{_datadir}/lilypond
%{_datadir}/emacs/site-lisp
%{_datadir}/vim/vim*
%{_libdir}/%{name}/%{version}/ccache/lily/

%files emmentaler-fonts
%dir %{_datadir}/fonts/lilypond/
%{_datadir}/fonts/lilypond/emmentaler*otf

%files fonts-common
%doc COPYING

%changelog
%autochangelog
