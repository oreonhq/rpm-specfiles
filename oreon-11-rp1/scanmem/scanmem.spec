%global source0_hash f02054b91322cf41517506158fcb74554e9fc6644e696f8aa25e5acf162d374b

%global __python %{__python3}

Name:           scanmem
Summary:        Memory scanner
Version:        0.17
Release:        23%{?dist}.1
# Automatically converted from old format: GPLv3+ and LGPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
VCS:            https://github.com/scanmem/scanmem.git
URL:            https://github.com/scanmem/scanmem
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  readline-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Remove after F29
Obsoletes:      %{name} < 0.17

%description
scanmem is a simple interactive debugging utility, used to locate the address
of a variable in an executing process. This can be used for the analysis or
modification of a hostile process on a compromised machine, reverse
engineering, or as a "pokefinder" to cheat at video games.

%package libs
Summary:        Memory scanner library
# Remove after F29
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
# No libtool, please
rm -vf %{buildroot}%{_libdir}/lib%{name}.la
# We install docs ourselves
rm -vrf %{buildroot}%{_datadir}/doc/%{name}/
# No need to do bytecode compilation for us
find %{buildroot}%{_datadir}/gameconqueror/ -type f -name '*.py[co]' -print -delete
%find_lang GameConqueror

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gameconqueror

%check
make check
desktop-file-validate %{buildroot}%{_datadir}/applications/GameConqueror.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/GameConqueror.appdata.xml

%files
%doc README
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%files libs
%license gpl-3.0.txt lgpl-3.0.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files -n gameconqueror -f GameConqueror.lang
%{_datadir}/applications/GameConqueror.desktop
%{_mandir}/man1/gameconqueror.1*
%{_datadir}/gameconqueror/
%{_datadir}/icons/hicolor/*/apps/GameConqueror.png
%{_bindir}/gameconqueror
%{_datadir}/polkit-1/actions/org.freedesktop.gameconqueror.policy
%{_datadir}/appdata/GameConqueror.appdata.xml

%changelog
%autochangelog
