%global source0_hash 8e268182d8651fb2066587c4ea54dbccc152703b1584f9224f3201d25210b6d4

Name:           geomorph
Version:        0.62
Release:        26%{?dist}
Summary:        A height field editor for Linux
License:        GPL-2.0-only
URL:            http://geomorph.sourceforge.net
Source0:        http://sourceforge.net/projects/geomorph/files/geomorph/%{version}/%{name}-%{version}.tar.gz
Source1:        geomorph.desktop
Source2:        geomorph.appdata.xml
Source3:        geomorph.png
Patch0:         geomorph-format-security.patch
Patch1:         geomorph-array-bounds.patch
Patch2:         geomorph-glxbadcontext.patch
Patch3:         geomorph-gnusource.patch
Patch4:         geomorph-x_alloc.patch
Patch5:         geomorph-missing-string-headers.patch
Patch6:         geomorph-missing-custom-headers.patch
Patch7:         geomorph-define-get_current_dir_name-function.patch
Patch8:         geomorph-explicit-braces.patch
Patch9:         geomorph-int-to-pointer-cast.patch
Patch10:        geomorph-uninitialized-values.patch
Patch11:        geomorph-return-functions.patch
Patch12:        geomorph-printf-format.patch
Patch13:        geomorph-pointer-to-int-cast.patch
Patch14:        geomorph-pointer-sign.patch
Patch15:        geomorph-remove-gettext-at-compile-time.patch
Patch16:        geomorph-arg-not-used.patch
Patch17:        geomorph-incompatible-pointer-types.patch
Patch18:        geomorph-no-common.patch
#Patch20:        geomorph-update-autotools.patch
Patch30:        geomorph-crater_struct_free.patch

BuildRequires:  gcc
BuildRequires:  gtkglext-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires: make
#BuildRequires:  /usr/bin/autoreconf
#BuildRequires:  gettext-devel
#BuildRequires:  automake
Requires:       povray

%description
Geomorph is a height field generator and editor for the Linux operating system.
A height field is a kind of topographic map.  It is a 2D projection of a 
3D landscape.
Geomorph generates square images and shows a 3D preview of the resulting
landscape.  The resulting 2D image can be processed with a tool like Povray
for rendering the landscape.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}
%patch -P0 -p1 -b .format-security
%patch -P1 -p1 -b .array-bounds
%patch -P2 -p1 -b .glxbadcontext
%patch -P3 -p1 -b .gnusource
%patch -P4 -p1 -b .x_alloc
%patch -P5 -p1 -b .missing-string-headers
%patch -P6 -p1 -b .missing-custom-headers
%patch -P7 -p1 -b .define-get_current_dir_name-function
%patch -P8 -p1 -b .explicit-braces
%patch -P9 -p1 -b .int-to-pointer-cast
%patch -P10 -p1 -b .uninitialized-values
%patch -P11 -p1 -b .return-functions
%patch -P12 -p1 -b .printf-format
%patch -P13 -p1 -b .pointer-to-int-cast
%patch -P14 -p1 -b .pointer-sign
%patch -P15 -p1 -b .remove-gettext-at-compile-time
%patch -P16 -p1 -b .arg-not-used
%patch -P17 -p1 -b .incompatible-pointer-types
%patch -P18 -p1 -b .no-common.patch
#%%patch -P20 -p1 -b .update-autotools
%patch -P30 -p1 -b .crater_struct_free
#autoreconf -vfi

# to avoid rpmlint warnings
# Remove exe bit from pixmaps
find . -name \*.xpm -exec chmod -x {} \;
# Switch to UTF-8
for file in LISEZMOI AFAIRE FAQ-fr
do
    iconv -f ISO-8859-1 -t UTF-8 $file > $file.utf8
    touch -r $file $file.utf8
    mv -f $file.utf8 $file
done
# Tarball contains an already compiled app.
# Remove and recompile it.
%{__rm} -f scenes/colmap

# Remove Hardcoded path
for file in install-step1-dir install-step2-rcfile install-step3-menu \
    install-step4-desktop install-user src/app/app.c src/app/main.c
do
    sed -i -e '/^VERSION/ s#=.*#=%{version}#g' \
        -e 's#/usr/local/share/geomorph#%{_datadir}/geomorph#g' \
        $file
done

%build
%configure \
    --disable-rpath

pushd scenes
%{__cc} ${RPM_OPT_FLAGS} -Wl,-z,relro,-z,now -o colmap colmap.c
popd
make %{?_smp_mflags}

%install
make install DESTDIR="%{buildroot}"
%find_lang %{name}
mv %{buildroot}%{_datadir}/geomorph/%{version}/scenes/colmap %{buildroot}%{_bindir}/
%{__rm} -f %{buildroot}%{_datadir}/geomorph/%{version}/scenes/colmap.c
# Create directories
%{__mkdir_p} %{buildroot}%{_datadir}/icons
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__mkdir_p} %{buildroot}%{_datadir}/appdata
# Copy new desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
# Copy icon file
%{__cp} %{SOURCE3} %{buildroot}%{_datadir}/icons
%{__cp} GeoMorph.xpm %{buildroot}%{_datadir}/icons
# Copy appdata
%{__cp} %{SOURCE2} %{buildroot}%{_datadir}/appdata

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%doc ABOUT-NLS AFAIRE AUTHORS ChangeLog FAQ FAQ-fr LISEZMOI NEWS README TODO geomorphrc_de geomorphrc_en geomorphrc_fr
%{_bindir}/geomorph
%{_bindir}/colmap
%{_datadir}/geomorph
%{_datadir}/applications/geomorph.desktop
%{_datadir}/icons/geomorph.png
%{_datadir}/icons/GeoMorph.xpm
%{_datadir}/appdata/geomorph.appdata.xml

%changelog
%autochangelog
