%global source0_hash 5851aa7252dad952084529173640232562dec4a7c440209f196d53d4a5a8074d
Summary:        A GUI text editor for systems with X
Name: nedit
Version: 5.8
Release:        1%{?dist}
Source0:        http://sourceforge.net/projects/nedit/files/nedit-source/nedit-%{version}-src.tar.gz
Source1: nedit.desktop
Source2: nedit-icon.png
Patch0: nedit-5.5-security.patch
Patch1: 0001-Force-C89-on-gcc-linux-to-prevent-accidental-changes.patch
Patch2: nedit-5.7-makefiles.patch
Patch3: nedit-5.6-utf8.patch
Patch5: nedit-5.7-nc-manfix.patch
Patch6: nedit-5.5-visfix.patch
Patch8: nedit-5.5-scroll.patch
URL: http://sourceforge.net/projects/nedit/
License: GPL-2.0-only
Requires: xorg-x11-fonts-ISO8859-1-75dpi
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libXau-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  make
BuildRequires:  motif-devel
BuildRequires:  perl(Pod::Man)
# /oreon:deps
%description
NEdit is a GUI text editor for the X Window System. NEdit is
very easy to use, especially if you are familiar with the
Macintosh or Microsoft Windows style of interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .security
%patch -P1 -p1 -b .c89
%patch -P2 -p1 -b .makefiles
%patch -P3 -p1 -b .utf8
%patch -P5 -p1 -b .nc-manfix
%patch -P6 -p1 -b .visfix
%patch -P8 -p1 -b .scroll

%build

pushd doc
make VERSION='NEdit 5.8' man
popd
make linux C_OPT_FLAGS="$RPM_OPT_FLAGS"
%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
mv source/nc source/nedit-client
install -m 755 source/nedit source/nedit-client $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 doc/nedit.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit.1x
mv doc/nc.man doc/nedit-client.man
install -p -m 644 doc/nedit-client.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit-client.1x
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/nedit.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category "Development;" \
        %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
