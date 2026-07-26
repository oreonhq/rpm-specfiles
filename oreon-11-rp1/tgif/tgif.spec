%global source0_hash 2f24e9fecafae6e671739bd80691a06c9d032bdd1973ca164823e72ab1c567ba

Name:		tgif
Version:	4.2.5
Release:	35%{?dist}
Summary:	2-D drawing tool

# convkinput.c	HPND
# convxim.c	HPND
# rmcast/rmchat/rmchat.c	GPL-2.0-or-later	unused
# Overall	QPL-1.0
# SPDX confirmed
License:	QPL-1.0 AND HPND
URL:		http://bourbon.usc.edu/tgif/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-QPL-%{version}.tar.gz
# http://tyche.pu-toyama.ac.jp/~a-urasim/tgif/
Patch10:	tgif-textcursor-a-urasim.patch
# Check below later
Patch101:	tgif-QPL-4.1.45-size-debug.patch
Patch102:	tgif-QPL-4.2.5-format-security.patch
Patch103:	tgif-c99.patch
Patch104:	tgif-QPL-4.2.5-c23-prototype.patch

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	imake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libXmu-devel
BuildRequires:	libidn-devel
BuildRequires:	zlib-devel
Requires:	ghostscript
Requires:	netpbm-progs
Requires:	xorg-x11-fonts-75dpi
Requires:	xorg-x11-fonts-ISO8859-1-75dpi

%description
Tgif  -  Xlib based interactive 2-D drawing facility under
X11.  Supports hierarchical construction of  drawings  and
easy  navigation  between  sets  of drawings.  It's also a
hyper-graphics (or hyper-structured-graphics)  browser  on
the World-Wide-Web.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-QPL-%{version}
# Upstream says the below is wrong, for now dropping
#%%patch10 -p0 -b textcursor
# Check later
#%%patch101 -p1 -b .size
%patch -P102 -p1 -b .format
%patch -P103 -p1 -b .c99
%patch -P104 -p1 -b .c23

%{__perl} -pi \
	-e 's,JISX-0208-1983-0,EUC-JP,g' \
	po/ja/ja.po
sed -i \
	-e 's|charset= koi8-r|charset=ISO-8859-1|' \
	po/fr/fr.po

# use scalable bitmap font
%{__sed} \
	-e s,alias\-mincho,misc\-mincho,g \
	-e s,alias\-gothic,jis\-fixed,g \
	-i po/ja/Tgif.ad

# Fix desktop file
%{__sed} -i.icon -e 's|Icon=tgif|Icon=tgificon|' \
	po/ja/tgif.desktop

# Fix installation path for icon files
%{__sed} -i.path \
	-e '/InstallNonExec.*hicolor/s|\$(TGIFDIR)|\$(DATADIR)/icons/|' \
	-e '/MakeDirectories.*hicolor/s|\$(TGIFDIR)|\$(DATADIR)/icons/|' \
	Imakefile

%build
%{__cp} -pf Tgif.tmpl-linux Tgif.tmpl
%{__sed} -i.mode -e 's|0664|0644|' Tgif.tmpl

xmkmf
%{__sed} -i.mode -e 's|0444|0644|' Makefile
DEFOPTS='-DOVERTHESPOT -DUSE_XT_INITIALIZE -D_ENABLE_NLS -DPRINT_CMD=\"lpr\" -DA4PAPER'
%{__make} %{?_smp_mflags} \
	CC="%{__cc} %{optflags}" \
	MOREDEFINES="$DEFOPTS" \
	TGIFDIR=%{_datadir}/tgif/ \
	LOCAL_LIBRARIES="-lXmu -lXt -lX11" \
	tgif

pushd po
xmkmf 
%{__sed} -i.mode -e 's|0444|0644|' Makefile
%{__make} \
	Makefile \
	Makefiles \
	depend \
	all
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT/

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT/ \
	BINDIR=%{_libexecdir}/ \
	TGIFDIR=%{_datadir}/tgif/ \
	INSTALLFLAGS="-cp" \
	DATADIR=%{_datadir} \
	install \
	install.man

# wrap tgif
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}/
%{__install} -cpm 0755 po/ja/tgif-wrapper.sh \
	$RPM_BUILD_ROOT%{_bindir}/%{name}

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/tgif/*.obj
%{__install} -cpm 0644 *.obj \
	$RPM_BUILD_ROOT%{_datadir}/tgif/

# Japanese specific
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/X11/ja/app-defaults/
%{__install} -cpm 0644 \
	po/ja/Tgif.ad \
	$RPM_BUILD_ROOT%{_datadir}/X11/ja/app-defaults/Tgif

pushd po
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT/ \
	INSTALLFLAGS="-cp" \
	install
popd

# desktop file & icon
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install \
	--remove-category 'Application' \
	--remove-category 'X-Fedora' \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	po/ja/tgif.desktop

%{find_lang} tgif

%files -f %{name}.lang
%doc AUTHORS
%doc ChangeLog
%license Copyright
%doc HISTORY
%license LICENSE.QPL
%doc README*
%doc VMS_MAKE_TGIF.COM 
%doc example.tex 
%doc po/ja/README.jp

%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}.1x*

%{_datadir}/%{name}/
# Currently no package owns the following directories
%dir %{_datadir}/X11/ja/
%dir %{_datadir}/X11/ja/app-defaults/
%{_datadir}/X11/ja/app-defaults/Tgif

%{_datadir}/icons/hicolor/*/apps/%{name}icon.png
%{_datadir}/applications/*%{name}.desktop

%changelog
%autochangelog
