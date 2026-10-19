%global source0_hash 7201bfa24fb6625f4c5f8f1d46860900346777fc3a30f58ca9f1c186eaa9f333
Name:		gpick
Version:	    0.4
Release:        1%{?dist}
Summary:        Advanced color picker
License:	    BSD-3-Clause
URL:		    http://gpick.org
%{?shortcommit:
Source0:        https://github.com/thezbyg/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
%{!?shortcommit:
Patch0:		    gpick-0.4-lua-5.5.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openthreads)
BuildRequires:  ragel
# /oreon:deps
%description
Advanced color picker

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{?shortcommit:
%autosetup -p1 -n %{name}-%{commit}}
%{!?shortcommit:
%autosetup -n %{name}-%{version}}
mkdir .git

# Delete external libraries and only use system dependencies to build GPick
rm -rf extern
echo "INTERNAL_EXPAT=False" >> user-config.py
echo "INTERNAL_LUA=False" >> user-config.py
echo "LOCALEDIR=\"%{_datadir}/locale\"" >> user-config.py

echo "%{version}" > .version

%build

%cmake \
	-DCFLAGS="%{optflags} -Wl,--as-needed" \
	-DCXXFLAGS="%%{optflags} -Wl,--as-needed --std=c++17" \
	-DLDFLAGS="%%{optflags} -Wl,--as-needed" \
	-DPREFER_VERSION_FILE=True \
	-DLUA_TYPE="C"
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.%{name}.metainfo.xml
%find_lang %{name}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
