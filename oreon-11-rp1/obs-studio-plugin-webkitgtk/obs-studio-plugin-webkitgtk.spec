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
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc

BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
%if 0%{?rhel} && 0%{?rhel} < 10
BuildRequires:  pkgconfig(webkit2gtk-4.0)
%else
BuildRequires:  pkgconfig(webkit2gtk-4.1)
%endif

Supplements:    obs-studio%{?_isa}

# Replace older packages
Obsoletes:      obs-webkitgtk < %{version}-%{release}
Provides:       obs-webkitgtk = %{version}-%{release}
Provides:       obs-webkitgtk%{?_isa} = %{version}-%{release}

ExcludeArch:    %{ix86}

%description
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

%if 0%{?rhel} && 0%{?rhel} < 10
# Use webkit2gtk-4.0 API module for older RHEL
sed -e 's/webkit2gtk-4.1/webkit2gtk-4.0/g' -i meson.build
%endif

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_libexecdir}/obs-plugins/%{srcname}*
%{_libdir}/obs-plugins/%{srcname}*

%changelog
%autochangelog
