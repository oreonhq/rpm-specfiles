%global source0_hash none

Name:           tuxpaint
Version:        0.9.35
Release:        4%{?dist}

Epoch:          1
Summary:        Drawing program designed for young children

License:        GPL-2.0-or-later
URL:            http://www.tuxpaint.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         desktop.patch
Patch1:         includes.patch
PAtch2:         const.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  SDL2_gfx-devel
BuildRequires:  SDL2_Pango-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  freetype-devel >= 2.0
BuildRequires:  gettext
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  netpbm-devel
BuildRequires:	fribidi-devel
BuildRequires:	gperf
BuildRequires:  ImageMagick
BuildRequires:  libimagequant-devel
BuildRequires:  xdg-utils
BuildRequires:  perl-interpreter

# This should guarantee the proper permissions on
# all of the /usr/share/icons/hicolor/* directories.
Requires:       hicolor-icon-theme

%description
"Tux Paint" is a free drawing program designed for young children
(kids ages 3 and up). It has a simple, easy-to-use interface,
fun sound effects, and a cartoon mascot who helps you along.

%package devel
Summary:	Development files for tuxpaint extensions/plugins
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files for tuxpaint extensions/plugins

%prep
%setup -q
%patch -P 0 -p0 -b .desktop
%patch -P 1 -p0 -b .includes
%patch -P 2 -p0 -b .const

sed -i -e '/\/gnome\/apps\/Graphics/d' Makefile
find docs -type f -exec perl -pi -e 's/\r\n/\n/' {} \;
find docs -type f -perm /100 -exec chmod a-x {} \;

make PREFIX=%{_prefix} MAGIC_PREFIX=%{_libdir}/tuxpaint/plugins tp-magic-config

%build
%set_build_flags
make %{?_smp_mflags} \
    PREFIX=%{_prefix} \
    OPTFLAGS="$CFLAGS -std=gnu17" \
    LDFLAGS="$LDFLAGS -L%{_libdir}" \
    MAGIC_CFLAGS="$CFLAGS \$(SDL_CFLAGS) -Isrc" \
    MAGIC_PREFIX=%{_libdir}/tuxpaint/plugins

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
make install PKG_ROOT=$RPM_BUILD_ROOT PREFIX=%{_prefix} \
    COMPLETIONDIR=$RPM_BUILD_ROOT%{bash_completions_dir} \
    X11_ICON_PREFIX=$RPM_BUILD_ROOT%{_datadir}/pixmaps/ \
    GNOME_PREFIX=%{_prefix} \
    KDE_PREFIX="" \
    KDE_ICON_PREFIX=%{_datadir}/icons \
    MAGIC_PREFIX=$RPM_BUILD_ROOT%{_libdir}/tuxpaint/plugins
find $RPM_BUILD_ROOT -type d|xargs chmod 0755
%find_lang %{name}

for d in 16x16 22x22 32x32 48x48 64x64 96x96 128x128 192x192; do
    install -D -m0644 data/images/icon${d}.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${d}/apps/tuxpaint.png
done

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
    --add-category KidsGame \
    --delete-original \
    src/tuxpaint.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.tuxpaint.Tuxpaint.appdata.xml

#purge bundled fonts
rm -rf $RPM_BUILD_ROOT%{_datadir}/tuxpaint/fonts/*

ln -s /usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf %{buildroot}%{_datadir}/tuxpaint/fonts/default_font.ttf

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%files -f %{name}.lang
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%doc docs
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/tuxpaint.png
%{_datadir}/pixmaps/*
%{_libdir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%{bash_completions_dir}/010_tuxpaint-completion.bash
%{_metainfodir}/org.tuxpaint.Tuxpaint.appdata.xml

%files devel
%doc %{_datadir}/doc/%{name}-%{version}/
%{_includedir}/tuxpaint/

%changelog
%autochangelog
