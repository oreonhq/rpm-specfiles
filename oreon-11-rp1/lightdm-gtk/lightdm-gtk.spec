%global source0_hash a2ea9f0cc5dd8d2a4d81ff45ccc10498513ecec2f24437024abdb6ba016e702c
Summary:        LightDM GTK Greeter
Name:           lightdm-gtk
Version:        2.0.9
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/Xubuntu/lightdm-gtk-greeter
Source0:        https://github.com/Xubuntu/lightdm-gtk-greeter/archive/lightdm-gtk-greeter-%{version}.tar.gz
Source1:        60-lightdm-gtk-greeter.conf
Patch0:         fix_arm_compile.patch
Patch1:         lightdm-gtk_add-language-button-to-layout.patch
Patch2:         lightdm-gtk-greeter-1.8.5-add-cinnamon-badges.patch
Obsoletes:      lightdm-gtk2 < 1.8.5-15
Obsoletes:      lightdm-gtk-common < 2.0
Obsoletes:      lightdm-gtk-greeter < 1.1.5-4
Provides:       lightdm-gtk-greeter = %{version}-%{release}
Provides:       lightdm-greeter = 1.2
Requires:       lightdm%{?_isa}
%global bg_file_ext png
Supplements: (lightdm%{?_isa} and lightdm-autologin-greeter)
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  xfce4-dev-tools
# /oreon:deps
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
mkdir -p %{buildroot}%{_datadir}/lightdm-gtk-greeter/
rm -fv %{buildroot}%{_docdir}/lightdm-gtk-greeter/sample-lightdm-gtk-greeter.css
%oreon_autofiles main

%pre

%{_sbindir}/update-alternatives \
  --remove lightdm-greeter \
  %{_datadir}/xgreeters/lightdm-gtk-greeter.desktop 2> /dev/null ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
