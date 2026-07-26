%global source0_hash 844cf83f703fa6e2949c287f84a6665e947dbfa69b152a96e5c5171255fad9ce

%define _hardened_build 1
Summary: GUI for several command-line debuggers
Name: ddd
Version: 3.4.1
Release: 7%{?dist}
License: GPL-2.0-or-later
URL: http://www.gnu.org/software/ddd/
Source0: https://ftp.gnu.org/gnu/ddd/ddd-%{version}.tar.gz
#For rc:
#Source0: https://alpha.gnu.org/gnu/ddd/ddd-%%{version}.tar.gz
#Source1: ddd.desktop
Source2: ddd.png
Source3: org.gnu.ddd.metainfo.xml
Patch0: ddd-3.3.12-debuginfo.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Requires: gdb, xterm, gnuplot, xdg-utils, xorg-x11-fonts-ISO8859-1-75dpi, xorg-x11-fonts-ISO8859-1-100dpi, xclipboard, xfontsel
BuildRequires:  gcc-c++
BuildRequires: motif-devel, ncurses-devel, libXaw-devel
BuildRequires: elfutils-libelf-devel, xterm 
BuildRequires: desktop-file-utils, gdb, readline-devel, texinfo, autoconf, automake
BuildRequires: make, libtool

%description
The Data Display Debugger (DDD) is a popular GUI for command-line
debuggers like GDB, DBX, JDB, WDB, XDB, the Perl debugger, and the
Python debugger. DDD allows you to view source texts and provides an
interactive graphical data display, in which data structures are
displayed as graphs. You can use your mouse to dereference pointers
or view structure contents, which are updated every time the program
stops. DDD can debug programs written in Ada, C, C++, Chill, Fortran,
Java, Modula, Pascal, Perl, and Python. DDD provides machine-level
debugging; hypertext source navigation and lookup; breakpoint,
watchpoint, backtrace, and history editors; array plots; undo and
redo; preferences and settings editors; program execution in the
terminal emulation window, debugging on a remote host, an on-line
manual, extensive help on the Motif user interface, and a command-line
interface with full editing, history and completion capabilities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1

%build
autoreconf -fi
export CXXFLAGS="${RPM_OPT_FLAGS} -fpermissive"
%configure --with-readline --disable-dependency-tracking
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT/%{_infodir}/dir*

mkdir -p $RPM_BUILD_ROOT/%{_infodir}
mv $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{version}/info/ddd* $RPM_BUILD_ROOT/%{_infodir}/
rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{version}/info/
rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{version}/doc/

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category X-Fedora \
        ddd/ddd.desktop

install -D -m 0644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/ddd.png

install -D -m 0644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_metainfodir}/org.gnu.ddd.metainfo.xml

%files
%license doc/COPYING*
%doc doc/
%{_bindir}/ddd
%{_datadir}/applications/*.desktop
#%%config(noreplace) %%{_datadir}/%%{name}-%%{version}/ddd/Ddd
%{_datadir}/%{name}-%{version}/themes/
#%%{_datadir}/%%{name}-%%{version}/vsllib/
%{_datadir}/icons/hicolor/128x128/apps/ddd.png
%{_metainfodir}/org.gnu.ddd.metainfo.xml
%{_infodir}/ddd*
%{_mandir}/man1/ddd.1*

%changelog
%autochangelog
