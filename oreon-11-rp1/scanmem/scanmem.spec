%global source0_hash f02054b91322cf41517506158fcb74554e9fc6644e696f8aa25e5acf162d374b
%global __python %{__python3}
Name:           scanmem
Summary:        Memory scanner
Version:        0.17
Release:        1%{?dist}
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
VCS:            https://github.com/scanmem/scanmem.git
URL:            https://github.com/scanmem/scanmem
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name} < 0.17
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
scanmem is a simple interactive debugging utility, used to locate the address
of a variable in an executing process. This can be used for the analysis or
modification of a hostile process on a compromised machine, reverse
engineering, or as a "pokefinder" to cheat at video games.

%package libs
Summary:        Memory scanner library
Obsoletes:      %{name} < 0.17
%description libs
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package -n gameconqueror
Summary:        CheatEngline-alike interface for scanmem
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       polkit
Requires:       python3-gobject-base
Requires:       gtk3
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  %{_bindir}/appstream-util
%description -n gameconqueror
GameConqueror is a GUI front-end for scanmem, providing more features, such as:
* Flexible syntax for searching
* Easier and multiple variable locking
* Better process finder
* Memory browser/editor

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i -e "1s|.*|#!%{__python3}|" gui/GameConqueror.py

%build

./autogen.sh
%configure --enable-gui --disable-static
%make_build
%install
%make_install
rm -vf %{buildroot}%{_libdir}/lib%{name}.la
rm -vrf %{buildroot}%{_datadir}/doc/%{name}/
find %{buildroot}%{_datadir}/gameconqueror/ -type f -name '*.py[co]' -print -delete
%find_lang GameConqueror
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gameconqueror
%oreon_autofiles gameconqueror usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
desktop-file-validate %{buildroot}%{_datadir}/applications/GameConqueror.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/GameConqueror.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n scanmem-libs -f %{oreon_filedir}/scanmem-libs.list
%files -n scanmem-devel -f %{oreon_filedir}/scanmem-devel.list
%files -n gameconqueror -f %{oreon_filedir}/gameconqueror.list

%changelog

%autochangelog
