%global source0_hash f3ca07fbe1577d45978cd8042b2b2d512df02dcb1b7bfb2ee7626761646b97bf
%global srcname obs-webkitgtk
%global commit 3c0978b399512440afdd4dccf744f2ffa0821317
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20231023
Name:           obs-studio-plugin-webkitgtk
Version:        0~git%{commitdate}.%{shortcommit}
Release:        9%{?dist}
Summary:        OBS Browser source plugin based on WebKitGTK
License:        GPL-2.0-or-later
URL:            https://github.com/fzwoch/obs-webkitgtk
Source0:        https://github.com/fzwoch/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
Supplements:    obs-studio%{?_isa}
Obsoletes:      obs-webkitgtk < %{version}-%{release}
Provides:       obs-webkitgtk = %{version}-%{release}
Provides:       obs-webkitgtk%{?_isa} = %{version}-%{release}
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
# /oreon:deps
%description
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
