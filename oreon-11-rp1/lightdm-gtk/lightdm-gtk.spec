%global source0_hash 3e3113135726a2e8aed4d7b6a886d54d54b692f69805934b2d7ce8bc2776b657

Summary:        LightDM GTK Greeter
Name:           lightdm-gtk
Version:        2.0.8
Release:        16%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/Xubuntu/lightdm-gtk-greeter
Source0:        https://github.com/Xubuntu/lightdm-gtk-greeter/archive/lightdm-gtk-greeter-%{version}.tar.gz
Source1:        60-lightdm-gtk-greeter.conf
Patch0:         fix_arm_compile.patch
Patch1:         lightdm-gtk_add-language-button-to-layout.patch

# tweak default config

## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=1178498
# (lookaside cache)
Patch2:         lightdm-gtk-greeter-1.8.5-add-cinnamon-badges.patch

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  xfce4-dev-tools

Obsoletes:      lightdm-gtk2 < 1.8.5-15
Obsoletes:      lightdm-gtk-common < 2.0
Obsoletes:      lightdm-gtk-greeter < 1.1.5-4
Provides:       lightdm-gtk-greeter = %{version}-%{release}
Provides:       lightdm-greeter = 1.2

Requires:       lightdm%{?_isa}

# for default background/wallpaper
%if 0%{?fedora} >= 42
%global bg_file_ext jxl
Requires:       jxl-pixbuf-loader
%else
%global bg_file_ext png
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
%global background %{_datadir}/backgrounds/default.%{bg_file_ext}
Requires:       desktop-backgrounds-compat
%endif
%if 0%{?rhel} && 0%{?rhel} < 8
%global background %{_datadir}/backgrounds/day.%{bg_file_ext}
Requires:       system-logos
%endif
# owner of HighContrast gtk/icon themes
# disabled because the package got retired, but that means icons are
# broken in high contrast mode:
# https://bugzilla.redhat.com/show_bug.cgi?id=2398086
# https://bugzilla.redhat.com/show_bug.cgi?id=881352
# Requires:       gnome-themes-standard

# Fix issue with lightdm-autologin-greeter pulled in basic-desktop netinstall.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1481192
Supplements: (lightdm%{?_isa} and lightdm-autologin-greeter)

%description
A LightDM greeter that uses the GTK3 toolkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lightdm-gtk-greeter-lightdm-gtk-greeter-%{version} -p1

%if 0%{?background:1}
sed -i.background -e "s|#background=.*|background=%{background}|" \
  data/lightdm-gtk-greeter.conf
%endif

%build
sh autogen.sh
%configure \
  --disable-silent-rules \
  --disable-static \
  --disable-libindicator \
  --enable-at-spi-command="%{_libexecdir}/at-spi-bus-launcher --launch-immediately" \
  --enable-kill-on-sigterm

%make_build

%install
%make_install

install -m644 -p -D %{SOURCE1} \
  %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/60-lightdm-gtk-greeter.conf

%find_lang lightdm-gtk-greeter 

# create/own GREETER_DATA_DIR
mkdir -p %{buildroot}%{_datadir}/lightdm-gtk-greeter/

## unpackaged files
rm -fv %{buildroot}%{_docdir}/lightdm-gtk-greeter/sample-lightdm-gtk-greeter.css

%pre
%{_sbindir}/update-alternatives \
  --remove lightdm-greeter \
  %{_datadir}/xgreeters/lightdm-gtk-greeter.desktop 2> /dev/null ||:

%files -f lightdm-gtk-greeter.lang
%license COPYING
%doc AUTHORS NEWS README.md
%doc data/sample-lightdm-gtk-greeter.css
%config(noreplace) %{_sysconfdir}/lightdm/lightdm-gtk-greeter.conf
%{_sbindir}/lightdm-gtk-greeter
%{_datadir}/xgreeters/lightdm-gtk-greeter.desktop
%dir %{_datadir}/lightdm-gtk-greeter/
%{_datadir}/icons/hicolor/scalable/places/*badge-symbolic.svg
%{_datadir}/lightdm/lightdm.conf.d/60-lightdm-gtk-greeter.conf

%changelog
%autochangelog
