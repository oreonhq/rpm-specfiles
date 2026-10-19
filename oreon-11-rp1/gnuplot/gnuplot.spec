%global source0_hash 73237f37f03306d68bfae133a9a50d5e9341384e198d5ab37eeca9ab534deed8
%global major 6
%global minor 0
%global patchlevel 5
%global x11_app_defaults_dir %{_datadir}/X11/app-defaults
%bcond_with wx
%bcond_with libcerf
Summary:        A program for plotting mathematical expressions and data
Name: gnuplot
Version: %{major}.%{minor}.%{patchlevel}
Release:        1%{?dist}
License: gnuplot and MIT
URL: http://www.gnuplot.info/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1: gnuplot-4.2.0-fonts.patch
Patch2: gnuplot-make.patch
Patch5: gnuplot-5.0.0-lua_checkint.patch
Patch7: gnuplot-5.2.2-doc.patch
Requires: %{name}-common = %{version}-%{release}
Requires: dejavu-sans-fonts
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
%if %{with libcerf}
%endif
%if %{with wx}
%endif
# oreon:deps
BuildRequires:  /usr/bin/texi2dvi
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  emacs
BuildRequires:  gd-devel
BuildRequires:  giflib-devel
BuildRequires:  latex2html
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libotf
BuildRequires:  libpng-devel
BuildRequires:  librsvg2
BuildRequires:  lua-devel
BuildRequires:  m17n-lib
BuildRequires:  make
BuildRequires:  openspecfun-devel
BuildRequires:  pango-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  tex(latex)
BuildRequires:  tex(subfigure.sty)
BuildRequires:  tex-tex4ht
BuildRequires:  texinfo
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-ec
BuildRequires:  zlib-devel
# /oreon:deps
%description
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

Install gnuplot if you need a graphics package for scientific data
representation.

This package provides a Qt based terminal version of gnuplot.

%package common
Summary: The common gnuplot parts
Obsoletes: emacs-gnuplot <= 5.0.0-3
Obsoletes: emacs-gnuplot-el <= 5.0.0-3
%description common
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

This subpackage contains common parts needed for all versions of gnuplot.

%package minimal
Summary: Minimal version of program for plotting mathematical expressions and data
Requires: %{name}-common = %{version}-%{release}
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
%description minimal
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

Install gnuplot-minimal if you need a minimal version of graphics package
for scientific data representation.

%if %{with wx}
%package wx
Summary: wxGTK interface for gnuplot
Requires: %{name}-common = %{version}-%{release}
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Provides: gnuplot
Obsoletes: gnuplot < 5.0.0-4
%description wx
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

This package provides a wxGTK based terminal version of gnuplot.
%endif

%package doc
Summary: Documentation fo bindings for the gnuplot main application
BuildArch: noarch
%description doc
The gnuplot-doc package contains the documentation related to gnuplot
plotting tool

%package latex
Summary: Configuration for LaTeX typesetting using gnuplot
Requires: %{name} = %{version}-%{release}
Requires: tex(latex), texlive-cm-super, texlive-ec, tex(utf8x.def), tex-preview
BuildArch: noarch
%description latex
The gnuplot-latex package contains LaTeX configuration file related to gnuplot
plotting tool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P1 -p1 -b .font
%patch -P2 -p1 -b .make
%patch -P5 -p1 -b .checkint
%patch -P7 -p1 -b .doc
sed -i -e 's:"/usr/lib/X11/app-defaults":"%{x11_app_defaults_dir}":' src/gplt_x11.c
chmod 644 src/getcolor.h
chmod 644 demo/html/webify.pl
chmod 644 demo/html/webify_svg.pl
chmod 644 demo/html/webify_canvas.pl

autoreconf -fiv

%build

rm -rf demo/plugin/*.so demo/plugin/*.o
%global _configure ../configure
%global configure_opts --with-readline=builtin \\\
 --enable-history-file --with-texdir=/usr/share/texlive/texmf-dist/tex/latex/gnuplot
mkdir minimal
cd minimal
%configure %{configure_opts} --disable-wxwidgets --without-qt %{?with_libcerf:--with-libcerf} %{!?with_libcerf:--without-libcerf}
%make_build
make -C docs
make -C docs html info
export GNUPLOT_PS_DIR=../../../term/PostScript
cp -al ../docs/psdoc docs/psdoc
make -C docs/psdoc ps_symbols.ps ps_fontfile_doc.pdf
rm -rf docs/htmldocs/images.idx
cd -
%if %{with wx}
mkdir wx
cd wx
%configure %{configure_opts} --without-qt %{?with_libcerf:--with-libcerf} %{!?with_libcerf:--without-libcerf}
%make_build
cd -
%endif
mkdir qt
cd qt
%configure %{configure_opts} --disable-wxwidgets --with-qt %{?with_libcerf:--with-libcerf} %{!?with_libcerf:--without-libcerf}
%make_build
cd -
%install
%if %{with wx}
make -C wx install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
mv $RPM_BUILD_ROOT%{_bindir}/gnuplot $RPM_BUILD_ROOT%{_bindir}/gnuplot-wx
%endif
make -C qt install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
mv $RPM_BUILD_ROOT%{_bindir}/gnuplot $RPM_BUILD_ROOT%{_bindir}/gnuplot-qt
install -p -m 755 minimal/src/gnuplot $RPM_BUILD_ROOT%{_bindir}/gnuplot-minimal
make -C minimal/docs install-info DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
mkdir -p $RPM_BUILD_ROOT%{x11_app_defaults_dir}
mv $RPM_BUILD_ROOT%{_datadir}/gnuplot/%{major}.%{minor}/app-defaults/Gnuplot $RPM_BUILD_ROOT%{x11_app_defaults_dir}/Gnuplot
rm -rf $RPM_BUILD_ROOT%{_libdir}/
ln -s gnuplot.1 $RPM_BUILD_ROOT/%{_mandir}/man1/gnuplot-qt.1
%if %{with wx}
ln -s gnuplot.1 $RPM_BUILD_ROOT/%{_mandir}/man1/gnuplot-wx.1
%endif
touch $RPM_BUILD_ROOT%{_bindir}/gnuplot 
%find_lang %{name} --with-man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%posttrans

/usr/sbin/alternatives --install %{_bindir}/gnuplot gnuplot %{_bindir}/gnuplot-qt 61
%posttrans minimal

/usr/sbin/alternatives --install %{_bindir}/gnuplot gnuplot %{_bindir}/gnuplot-minimal 40
%if %{with wx}
%posttrans wx

/usr/sbin/alternatives --install %{_bindir}/gnuplot gnuplot %{_bindir}/gnuplot-wx 50
%endif
%preun

if [ $1 = 0 ]; then
    /usr/sbin/alternatives --remove gnuplot %{_bindir}/gnuplot-qt || :
fi
%preun minimal

if [ $1 = 0 ]; then
    /usr/sbin/alternatives --remove gnuplot %{_bindir}/gnuplot-minimal || :
fi
%if %{with wx}
%preun wx

if [ $1 = 0 ]; then
    /usr/sbin/alternatives --remove gnuplot %{_bindir}/gnuplot-wx || :
fi
%endif
%post latex

[ -e %{_bindir}/texhash ] && %{_bindir}/texhash 2> /dev/null;
%files -f %{oreon_filedir}/main.list
%files -n gnuplot-common -f %{oreon_filedir}/gnuplot-common.list
%files -n gnuplot-minimal -f %{oreon_filedir}/gnuplot-minimal.list
%files -n gnuplot-doc -f %{oreon_filedir}/gnuplot-doc.list
%files -n gnuplot-latex -f %{oreon_filedir}/gnuplot-latex.list

%changelog

%autochangelog
