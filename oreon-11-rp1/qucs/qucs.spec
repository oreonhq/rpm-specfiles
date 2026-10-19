%global source0_hash a860269540e5e646951ca4aafb732ac91680c48467ede5130683c4e30075b656
%bcond_with qucs_enables_freehdl
Summary:        Circuit simulator
Name:    qucs
Version: 0.0.20
Release:        1%{?dist}
License: GPL-1.0-or-later
URL:     http://qucs.sourceforge.net/
Source0:        https://github.com/Qucs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with qucs_enables_freehdl}
Requires: freehdl
%endif
Requires: perl-interpreter, iverilog
Requires: electronics-menu
Requires: mot-adms >= 2.3.4
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  latex2html
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mot-adms
BuildRequires:  octave-devel
BuildRequires:  qt-devel
BuildRequires:  texlive
BuildRequires:  texlive-IEEEtran
BuildRequires:  texlive-SIunits
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-keystroke
BuildRequires:  texlive-relsize
BuildRequires:  texlive-savesym
BuildRequires:  texlive-stmaryrd
BuildRequires:  texlive-subfigure
BuildRequires:  transfig
# /oreon:deps
%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure --enable-debug=yes
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' ./libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' ./libtool
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
