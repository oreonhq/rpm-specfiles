%global source0_hash 225781230daba68ab1b991c3215c3e80d2c2f860532f114fef86c08bad6d2e70
%global commit d3bcbc7f74469b92162ca6995eb8506bf49188c0
%global commitdate 20220522
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		gtk-v4l
Version:	0.4
Release:        1%{?dist}
Summary:        Video4Linux Device Preferences
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://github.com/jwrdegoede/gtk-v4l/
Source0:        https://github.com/jwrdegoede/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0: gtk-v4l-c99.patch
Obsoletes:	%{name}-devel < %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libgudev1-devel
BuildRequires:  libv4l-devel
BuildRequires:  meson
BuildRequires:  scrollkeeper
# /oreon:deps
%description
gtk-v4l is a Video4Linux Web camera control app

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
