%global source0_hash 72b907aa64f8bcf053f2ecbc8a2e243c6de353a94ecaf579ff2c4e3ae5d7e13c

Summary:       Enlightened terminal emulator
Name:          eterm
Version:       0.9.6
Release:       43%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
Source0:       http://www.eterm.org/download/Eterm-%{version}.tar.gz
Source1:       http://www.eterm.org/download/Eterm-bg-%{version}.tar.gz
Source2:       eterm.png
Patch0:        eterm-0.9.6-gcc10.patch
Patch1:        eterm-0.9.6-gcc14.patch
Patch2:        https://sources.debian.org/data/main/e/eterm/0.9.6-7.1/debian/patches/fix-fail-to-build-with-imlib2.patch
Patch3:        eterm-0.9.6-query-graphics.patch
Patch4:        eterm-configure-c99.patch
Patch5:        eterm-c99-headers.patch
URL:           http://www.eterm.org/
Requires:      xorg-x11-fonts-misc
Requires:      xorg-x11-fonts-ISO8859-1-75dpi
Requires:      xorg-x11-fonts-ISO8859-1-100dpi
BuildRequires: desktop-file-utils
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: glibc-common
BuildRequires: imlib2-devel
BuildRequires: libXmu-devel
BuildRequires: libast-devel
BuildRequires: sed
BuildRequires: make
Provides:      Eterm = %{version}-%{release}
Obsoletes:     Eterm <= 0.9.2
%description
Eterm is a color vt102 terminal emulator with enhanced graphical
capabilities.  Eterm is intended to be a replacement for xterm for
Enlightenment window manager users, but it can also be used as a
replacement for xterm by users without Enlightenment.  Eterm supports
various themes and is very configurable, in keeping with the
philosophy of Enlightenment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a 1 -n Eterm-%{version}
for f in ChangeLog ; do
    mv $f $f.iso88591
    iconv -o $f -f iso88591 -t utf8 $f.iso88591
    rm -f $f.iso88591
done

%build
export PERL=%{__perl}
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
export CFLAGS="%{optflags} -std=gnu17"
%endif
%configure --enable-multi-charset \
           --enable-escreen       \
           --enable-auto-encoding \
           --enable-trans         \
           --disable-etwin        \
           --disable-mmx          \
           --disable-rpath
sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

echo -e "[Desktop Entry]
Encoding=UTF-8
Name=Eterm
TryExec=Eterm
Exec=Eterm
Icon=eterm
Type=Application
Categories=Utility;TerminalEmulator;System;" > eterm.desktop

install -D -m 0644 eterm.desktop             \
  %{buildroot}%{_datadir}/applications/eterm.desktop
desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/eterm.desktop
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/eterm.png
rm -f %{buildroot}/%{_libdir}/libEterm.{a,la,so}

%files
%license LICENSE
%doc doc/Eterm_reference.html doc/Eterm.tcap 
%doc doc/Eterm.ti doc/README.Escreen
%doc README ReleaseNotes ReleaseNotes.1 ChangeLog
%{_bindir}/Esetroot
%{_bindir}/Etbg
%{_bindir}/Etbg_update_list
%{_bindir}/Etcolors
%{_bindir}/Eterm
%{_bindir}/Etsearch
%{_bindir}/Ettable
%{_bindir}/kEsetroot
%{_libdir}/libEterm-%{version}.so
%{_mandir}/man1/Eterm.1*
%{_datadir}/Eterm
%{_datadir}/applications/eterm.desktop
%{_datadir}/pixmaps/eterm.png

%changelog
%autochangelog
