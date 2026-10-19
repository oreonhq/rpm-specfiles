%global source0_hash bd79c48cdb1ee5430f748c45359f32743371710dcb8146945bfb4edba5f9ea60
%global _python_bytecompile_extra 0
Name:		lilypond
Version:	2.25.35
Release:        1%{?dist}
Summary:        A typesetting system for music notation
License:	GPL-3.0-only
URL:		https://lilypond.org
Source0:        https://lilypond.org/download/sources/v2.25/lilypond-%{version}.tar.gz
Source1:        century-schoolbook-l.metainfo.xml
Patch0:		lilypond-2.21.2-gcc44-relocate.patch
Requires:	ghostscript >= 8.15
Obsoletes: 	lilypond-fonts <= 2.12.1-1
Requires:	lilypond-emmentaler-fonts = %{version}-%{release}
Requires:	texlive-tex-gyre
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  flex
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ghostscript
BuildRequires:  guile30-devel
BuildRequires:  make
BuildRequires:  mftrace
BuildRequires:  pango-devel
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl-Pod-Parser
BuildRequires:  python3-devel
BuildRequires:  rsync
BuildRequires:  t1utils
BuildRequires:  texlive-metapost
# /oreon:deps
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
pushd $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
mkdir site-start.d
ln -s ../lilypond-init.el site-start.d
popd
%find_lang %{name}
mkdir -p $RPM_BUILD_ROOT%{_fontdir}
mv $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf/*.otf $RPM_BUILD_ROOT%{_fontdir}
rmdir $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf
ln -s %{_fontdir} $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lilypond-emmentaler-fonts -f %{oreon_filedir}/lilypond-emmentaler-fonts.list
%files -n lilypond-fonts-common -f %{oreon_filedir}/lilypond-fonts-common.list

%changelog

%autochangelog
