%global source0_hash add9ac79ff973528ad36c86858238bac4f59896c27dbf285cbe6a4d425fca17a

Summary: A GUI text editor for systems with X
Name: nedit
Version: 5.7
Release: 22%{?dist}
Source: http://sourceforge.net/projects/nedit/files/nedit-source/nedit-%{version}-src.tar.gz
Source1: nedit.desktop
Source2: nedit-icon.png
Patch0: nedit-5.5-security.patch
# https://sourceforge.net/p/nedit/git/ci/838292fe4034fc4ab4567f1d87193a4e6a57eca0/
Patch1: 0001-Force-C89-on-gcc-linux-to-prevent-accidental-changes.patch
# Append to Fedora's C_OPT_FLAGS and LD_OPT_FLAGS rather than overriding them.
Patch2: nedit-5.7-makefiles.patch
Patch3: nedit-5.6-utf8.patch
Patch5: nedit-5.7-nc-manfix.patch
Patch6: nedit-5.5-visfix.patch
Patch8: nedit-5.5-scroll.patch
URL: http://sourceforge.net/projects/nedit/
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Requires: xorg-x11-fonts-ISO8859-1-75dpi
BuildRequires: make
BuildRequires:  gcc
BuildRequires: motif-devel, libXau-devel, libXpm-devel, libXmu-devel
BuildRequires: desktop-file-utils
# Needed for generating manpages; see doc/Makefile
BuildRequires: perl(Pod::Man)

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
# Upstream really doesn't want you generating the manpages, but they forgot to
# include the manpages in 5.7. So generate them.
make VERSION='NEdit 5.7' man
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

%files
%doc README ReleaseNotes
%{_mandir}/*/*
%{_bindir}/*
%{_prefix}/share/applications/*
%{_datadir}/icons/hicolor/

%changelog
%autochangelog
