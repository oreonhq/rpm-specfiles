%global source0_hash c4c384155fabb34889d76b616065483f94c8310fa0147236d009c68cd4a85c93
%global tarball_version %%(echo %{version} | tr '~' '.')
%global __provides_exclude_from ^%{_libdir}/eog/plugins/.*\\.so$
Name:           eog-plugins
Version:        44.1
Release:        1%{?dist}
Summary:        A collection of plugins for the eog image viewer
License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/EyeOfGnome/Plugins
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{version}.tar.xz
Patch0:         eog-plugins-disable-postasa-plugin-by-default.patch
Requires:       eog-plugin-exif-display%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-export-to-folder%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-fit-to-width%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-fullscreenbg%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-light-theme%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-map%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-maximize-windows%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-pythonconsole%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-send-by-mail%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-slideshowshuffle%{?_isa} = %{version}-%{release}
Obsoletes:      eog-plugin-postasa < %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(eog)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
It's a collection of plugins for use with the Eye of GNOME Image Viewer.
The included plugins provide a map view for where the picture was taken,
display of Exif information, Zoom to fit, etc.

%package        data
Summary:        Common data required by plugins
BuildArch:      noarch
Requires:       eog
Obsoletes:      eog-plugin-hide-titlebar < 42~alpha-1
%description    data
Common files required by all plugins.

%package -n     eog-plugin-exif-display
Summary:        eog exif-display plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
%description -n eog-plugin-exif-display
The eog exif-display plugin.

%package -n     eog-plugin-export-to-folder
Summary:        eog export-to-folder plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}
%description -n eog-plugin-export-to-folder
The eog export-to-folder plugin.

%package -n     eog-plugin-fit-to-width
Summary:        eog fit-to-width plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
%description -n eog-plugin-fit-to-width
The eog fit-to-width plugin.

%package -n     eog-plugin-fullscreenbg
Summary:        eog fullscreenbg plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}
%description -n eog-plugin-fullscreenbg
The eog fullscreenbg plugin.

%package -n     eog-plugin-light-theme
Summary:        eog light-theme plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
%description -n eog-plugin-light-theme
The eog light-theme plugin.

%package -n     eog-plugin-map
Summary:        eog map plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
%description -n eog-plugin-map
The eog map plugin.

%package -n     eog-plugin-maximize-windows
Summary:        eog maximize-windows plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}
%description -n eog-plugin-maximize-windows
The eog maximize-windows plugin.

%package -n     eog-plugin-pythonconsole
Summary:        eog pythonconsole plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}
%description -n eog-plugin-pythonconsole
The eog pythonconsole plugin.

%package -n     eog-plugin-send-by-mail
Summary:        eog send-by-mail plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
%description -n eog-plugin-send-by-mail
The eog send-by-mail plugin.

%package -n     eog-plugin-slideshowshuffle
Summary:        eog slideshowshuffle plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}
%description -n eog-plugin-slideshowshuffle
The eog slideshowshuffle plugin.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/eog/plugins/
%find_lang %{name}
%oreon_autofiles eog-plugin-exif-display usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-export-to-folder usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-fit-to-width usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-fullscreenbg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-light-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-map usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-maximize-windows usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-pythonconsole usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-send-by-mail usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles eog-plugin-slideshowshuffle usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n eog-plugins-data -f %{oreon_filedir}/eog-plugins-data.list
%files -n eog-plugin-exif-display -f %{oreon_filedir}/eog-plugin-exif-display.list
%files -n eog-plugin-export-to-folder -f %{oreon_filedir}/eog-plugin-export-to-folder.list
%files -n eog-plugin-fit-to-width -f %{oreon_filedir}/eog-plugin-fit-to-width.list
%files -n eog-plugin-fullscreenbg -f %{oreon_filedir}/eog-plugin-fullscreenbg.list
%files -n eog-plugin-light-theme -f %{oreon_filedir}/eog-plugin-light-theme.list
%files -n eog-plugin-map -f %{oreon_filedir}/eog-plugin-map.list
%files -n eog-plugin-maximize-windows -f %{oreon_filedir}/eog-plugin-maximize-windows.list
%files -n eog-plugin-pythonconsole -f %{oreon_filedir}/eog-plugin-pythonconsole.list
%files -n eog-plugin-send-by-mail -f %{oreon_filedir}/eog-plugin-send-by-mail.list
%files -n eog-plugin-slideshowshuffle -f %{oreon_filedir}/eog-plugin-slideshowshuffle.list

%changelog

%autochangelog
