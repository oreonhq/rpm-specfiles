%global source0_hash 225781230daba68ab1b991c3215c3e80d2c2f860532f114fef86c08bad6d2e70

%global commit d3bcbc7f74469b92162ca6995eb8506bf49188c0
%global commitdate 20220522
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		gtk-v4l
Version:	0.4
Release:	35.%{commitdate}git%{shortcommit}%{?dist}
Summary:	Video4Linux Device Preferences
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://github.com/jwrdegoede/gtk-v4l/
Source0:	https://github.com/jwrdegoede/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0: gtk-v4l-c99.patch
BuildRequires:	meson gcc
BuildRequires:	scrollkeeper
BuildRequires:	libv4l-devel >= 0.6
BuildRequires:	gtk3-devel >= 3.0
BuildRequires:	libgudev1-devel >= 151
# No users of the library ever materialized and the new meson buildsystem
# no longer builds the library
Obsoletes:	%{name}-devel < %{version}-%{release}
# No provides since -devel is simply gone, not provided by the main pkg

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

%files
%doc *.md
%license COPYING
%{_bindir}/gtk-v4l
%{_datadir}/applications/gtk-v4l.desktop

%changelog
%autochangelog
