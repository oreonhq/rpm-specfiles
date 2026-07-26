%global source0_hash a860269540e5e646951ca4aafb732ac91680c48467ede5130683c4e30075b656

# Support a digital simulation with FreeHDL
%bcond_with qucs_enables_freehdl

Summary: Circuit simulator
Name:    qucs
Version: 0.0.20
Release: 4%{?dist}
License: GPL-1.0-or-later
URL:     http://qucs.sourceforge.net/
Source0: https://github.com/Qucs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: coreutils
BuildRequires: desktop-file-utils
BuildRequires: qt-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: gperf
BuildRequires: mot-adms >= 2.3.4
BuildRequires: octave-devel
BuildRequires: doxygen
BuildRequires: transfig
BuildRequires: latex2html
BuildRequires: texlive
BuildRequires: texlive-SIunits
BuildRequires: texlive-relsize
BuildRequires: texlive-IEEEtran
BuildRequires: texlive-savesym
BuildRequires: texlive-subfigure
BuildRequires: texlive-keystroke
BuildRequires: texlive-epstopdf
BuildRequires: texlive-stmaryrd
%if %{with qucs_enables_freehdl}
Requires: freehdl
%endif
Requires: perl-interpreter, iverilog
Requires: electronics-menu
Requires: mot-adms >= 2.3.4
Requires: hicolor-icon-theme

%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -fi
%configure --enable-debug=yes
# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' ./libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' ./libtool

# drop rpath from the LDFLAGS
# parallel build not working
%make_build -j1 qucsconv_LDFLAGS= qucsator_LDFLAGS=

%install
%make_install
install -d %{buildroot}%{_datadir}/applications

%if !%{with qucs_enables_freehdl}
rm -f %{buildroot}/%{_bindir}/qucsdigi*
rm -f %{buildroot}/%{_mandir}/man1/qucsdigi*
rm -f %{buildroot}/%{_datadir}/qucs/docs/*/{qucsdigi.png,start_digi.html}
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/qucs*
%{_bindir}/ps2sp*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/icons/*/*/*

%changelog
%autochangelog
