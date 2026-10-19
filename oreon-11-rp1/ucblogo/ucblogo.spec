%global source0_hash 668734c775d4f8eddb999094941572c55aaa1951b6936df2ba1f376427bedb3c
Name:           ucblogo
Version:        6.2.5
Release:        4%{?dist}
Summary:        An interpreter for the Logo programming language
License:        GPL-3.0-or-later
Source0:        https://github.com/jrincayc/ucblogo-code/archive/version_%{version}/ucblogo-%{version}.tar.gz
Patch1: compile-flags.patch
Patch2: termios.patch
URL:            https://people.eecs.berkeley.edu/~bh/logo.html
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libbsd-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  tetex-dvips
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
Berkeley Logo (ucblogo) is an interpreter for the Logo programming
language. Logo is a computer programming language designed for use by
learners, including children. This dialect of Logo features
random-access arrays, variable number of inputs to user-defined
procedures, various error handling improvements, comments and
continuation lines, first-class instruction and expression templates,
and macros.

%package doc
Summary: Documentation for ucblogo
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
This package includes HTML and PDF documentation for ucblogo
and the Program Logic Manual (plm)

%package x11
Summary: X11 version for ucblogo
Requires:       %{name} = %{version}-%{release}
%description x11
This package contains the x11 binary for ucblogo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -fi
autoconf
%configure --x-includes=%{_includedir} --x-libraries=%{_libdir} --enable-x11 --with-wx-config=no
%make_build ucblogo
mv ucblogo ucblogo-x11
make clean
%configure --with-wx-config=/usr/bin/wx-config-3.2
%make_build
make html
%install
%make_install
install -m0755 ucblogo-x11 ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/info
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 ucblogo.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 plm $RPM_BUILD_ROOT%{_datadir}/doc/ucblogo
rm -f ${RPM_BUILD_ROOT}%{_bindir}/install-logo-mode
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

/sbin/install-info %{_infodir}/ucblogo.info --entry="* UCBLogo: (ucblogo).     Berkeley Logo User Manual." --section="Programming Languages"  %{_infodir}/dir 2>/dev/null || :
%preun

if [ $1 = 0 ]; then
    /sbin/install-info --delete  %{_infodir}/ucblogo.info --entry="* UCBLogo: (ucblogo).        Berkeley Logo User Manual." --section="Programming Languages"  %{_infodir}/dir 2>/dev/null || :
fi
%files -f %{oreon_filedir}/main.list
%files -n ucblogo-doc -f %{oreon_filedir}/ucblogo-doc.list
%files -n ucblogo-x11 -f %{oreon_filedir}/ucblogo-x11.list

%changelog

%autochangelog
