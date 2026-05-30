%global source0_hash none

%global major 6
%global minor 0
%global patchlevel 4

%global x11_app_defaults_dir %{_datadir}/X11/app-defaults

%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without wx
%else
%bcond_with wx
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without libcerf
%else
%bcond_with libcerf
%endif

Summary: A program for plotting mathematical expressions and data
Name: gnuplot
Version: %{major}.%{minor}.%{patchlevel}
Release: 1%{?dist}
# MIT .. term/PostScript/aglfn.txt
License: gnuplot and MIT
URL: http://www.gnuplot.info/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Patch1: gnuplot-4.2.0-fonts.patch
# Fix out of tree parallel builds
# https://sourceforge.net/p/gnuplot/gnuplot-main/merge-requests/32/
Patch2: gnuplot-make.patch
# Fix for lua 5.5 - https://sourceforge.net/p/gnuplot/bugs/2859/
Patch3: https://sourceforge.net/p/gnuplot/bugs/_discuss/thread/c76f097014/7d60/attachment/possible_lua_fix.patch
Patch5: gnuplot-5.0.0-lua_checkint.patch
Patch7: gnuplot-5.2.2-doc.patch

Requires: %{name}-common = %{version}-%{release}
Requires: dejavu-sans-fonts
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives

#libedit-devel can not handle utf8, readline-devel is not legal with gnuplot, stick to builtin
BuildRequires: cairo-devel, gd-devel, giflib-devel, libotf, libpng-devel
# To produce gnuplot.info
BuildRequires: emacs
BuildRequires: librsvg2, libX11-devel, libXt-devel, lua-devel, m17n-lib
BuildRequires: openspecfun-devel
BuildRequires: pango-devel, tex(latex), tex(subfigure.sty)
BuildRequires: texlive-cm-super, tex-tex4ht, texinfo
BuildRequires: /usr/bin/texi2dvi
BuildRequires: zlib-devel, libjpeg-turbo-devel, texlive-ec, latex2html
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qt5compat-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-linguist
%if %{with libcerf}
BuildRequires: libcerf-devel >= 1.11
%endif
%if %{with wx}
BuildRequires: wxGTK-devel
%endif
BuildRequires: make
BuildRequires: autoconf, automake

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
#lets obsolete emacs-gnuplot until new upstream is found and package reintroduced
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P1 -p1 -b .font
%patch -P2 -p1 -b .make
%patch -P3 -p1 -b .lua5.5
%patch -P5 -p1 -b .checkint
%patch -P7 -p1 -b .doc
sed -i -e 's:"/usr/lib/X11/app-defaults":"%{x11_app_defaults_dir}":' src/gplt_x11.c
chmod 644 src/getcolor.h
chmod 644 demo/html/webify.pl
chmod 644 demo/html/webify_svg.pl
chmod 644 demo/html/webify_canvas.pl

autoreconf -fiv

%build
#remove binaries from source tarball
rm -rf demo/plugin/*.so demo/plugin/*.o

# avoid running configure in top level directory to prevent install failure on EL10 due to config.status check
%global _configure ../configure
%global configure_opts --with-readline=builtin \\\
 --enable-history-file --with-texdir=/usr/share/texlive/texmf-dist/tex/latex/gnuplot

# at first create minimal version of gnuplot for server SIG purposes
mkdir minimal
cd minimal
%configure %{configure_opts} --disable-wxwidgets --without-qt %{?with_libcerf:--with-libcerf} %{!?with_libcerf:--without-libcerf}
%make_build

# build docs
make -C docs
make -C docs html info
export GNUPLOT_PS_DIR=../../../term/PostScript
cp -al ../docs/psdoc docs/psdoc
make -C docs/psdoc ps_symbols.ps ps_fontfile_doc.pdf
rm -rf docs/htmldocs/images.idx
cd -

# create full version of gnuplot
%if %{with wx}
# With wxGTK support (Fedora only)
mkdir wx
cd wx
%configure %{configure_opts} --without-qt %{?with_libcerf:--with-libcerf} %{!?with_libcerf:--without-libcerf}
%make_build
cd -
%endif

# With Qt support
mkdir qt
cd qt
%configure %{configure_opts} --disable-wxwidgets --with-qt %{?with_libcerf:--with-libcerf} %{!?with_libcerf:--without-libcerf}
%make_build
cd -

%install
%if %{with wx}
# install wx
make -C wx install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
# rename binary
mv $RPM_BUILD_ROOT%{_bindir}/gnuplot $RPM_BUILD_ROOT%{_bindir}/gnuplot-wx
%endif

# install qt
make -C qt install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
# rename binary
mv $RPM_BUILD_ROOT%{_bindir}/gnuplot $RPM_BUILD_ROOT%{_bindir}/gnuplot-qt

# install minimal binary
install -p -m 755 minimal/src/gnuplot $RPM_BUILD_ROOT%{_bindir}/gnuplot-minimal

# install info
make -C minimal/docs install-info DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

#packaged by info package, updated by post-installation script, do not package here
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mkdir -p $RPM_BUILD_ROOT%{x11_app_defaults_dir}
mv $RPM_BUILD_ROOT%{_datadir}/gnuplot/%{major}.%{minor}/app-defaults/Gnuplot $RPM_BUILD_ROOT%{x11_app_defaults_dir}/Gnuplot
rm -rf $RPM_BUILD_ROOT%{_libdir}/

ln -s gnuplot.1 $RPM_BUILD_ROOT/%{_mandir}/man1/gnuplot-qt.1
%if %{with wx}
ln -s gnuplot.1 $RPM_BUILD_ROOT/%{_mandir}/man1/gnuplot-wx.1
%endif

#ghost provide /usr/bin/gnuplot
touch $RPM_BUILD_ROOT%{_bindir}/gnuplot 

%find_lang %{name} --with-man

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

%files -f %{name}.lang
%ghost %attr(0755,-,-) %{_bindir}/gnuplot
%doc Copyright
%{_bindir}/gnuplot-qt
%{_libexecdir}/gnuplot/%{major}.%{minor}/gnuplot_qt
%{_datadir}/gnuplot/%{major}.%{minor}/qt/

%files doc
%doc Copyright
%doc minimal/docs/psdoc/ps_guide.ps minimal/docs/psdoc/ps_symbols.ps minimal/docs/psdoc/ps_file.doc demo
%doc minimal/docs/psdoc/ps_fontfile_doc.pdf minimal/docs/html

%files common
%doc BUGS Copyright FAQ.pdf NEWS README RELEASE_NOTES
%{_mandir}/man1/gnuplot.1*
%{_mandir}/man1/gnuplot-qt.1*
%dir %{_datadir}/gnuplot
%dir %{_datadir}/gnuplot/%{major}.%{minor}
%dir %{_datadir}/gnuplot/%{major}.%{minor}/PostScript
%{_datadir}/gnuplot/%{major}.%{minor}/PostScript/*.ps
%{_datadir}/gnuplot/%{major}.%{minor}/PostScript/aglfn.txt
%dir %{_datadir}/gnuplot/%{major}.%{minor}/js
%{_datadir}/gnuplot/%{major}.%{minor}/js/*
%dir %{_datadir}/gnuplot/%{major}.%{minor}/lua/
%{_datadir}/gnuplot/%{major}.%{minor}/lua/gnuplot-tikz.lua
%{_datadir}/gnuplot/%{major}.%{minor}/colors_*
%{_datadir}/gnuplot/%{major}.%{minor}/gnuplot.gih
%{_datadir}/gnuplot/%{major}.%{minor}/gnuplotrc
%dir %{_libexecdir}/gnuplot
%dir %{_libexecdir}/gnuplot/%{major}.%{minor}
%{_libexecdir}/gnuplot/%{major}.%{minor}/gnuplot_x11
%{x11_app_defaults_dir}/Gnuplot
%{_infodir}/gnuplot.info*

%files minimal
%ghost %attr(0755,-,-) %{_bindir}/gnuplot
%doc Copyright
%{_bindir}/gnuplot-minimal

%if %{with wx}
%files wx
%ghost %attr(0755,-,-) %{_bindir}/gnuplot
%{_mandir}/man1/gnuplot-wx.1*
%doc Copyright
%{_bindir}/gnuplot-wx
%endif

%files latex
%doc Copyright
%{_texmf_vendor}/tex/latex/gnuplot/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{major}.%{minor}.%{patchlevel}-1
- Prepare for Oreon 11 (RP1)
