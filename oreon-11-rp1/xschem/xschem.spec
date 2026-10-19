%global source0_hash e6e15555e68f66f113f0d1ae3dd983184031b22f649be7be7ab530e2d862c751
%global rpm_has_recommends    %(rpm --version | awk -e '{print ($3 > 4.12)}')
Name:           xschem
Version:        3.4.7
Release:        1%{?dist}
Summary:        Schematic capture and Netlisting EDA tool
License:        GPL-2.0-or-later
URL:            http://repo.hu/projects/xschem
Source0:        http://repo.hu/projects/xschem/releases/xschem-%{version}.tar.gz
%if %rpm_has_recommends
Recommends:     %{name}-doc = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
# /oreon:deps
%description
%{name} is a schematic capture program, it allows creation of hierarchical
representation of circuits with a top down approach. By focusing on
interfaces, hierarchy and instance properties, a complex system can be
described in terms of simpler building blocks. A VHDL or Verilog or Spice
netlist can be generated from the drawn schematic, allowing the simulation
of the circuit. Key feature of the program is its drawing engine written in C
and using directly the Xlib drawing primitives; this gives very good
speed performance, even on very big circuits. The user interface is
built with the Tcl-Tk toolkit, Tcl is also the extension language used.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./"configure" --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}" \
    --prefix=%{_prefix} --symbols
%make_build
%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xschem-doc -f %{oreon_filedir}/xschem-doc.list

%changelog

%autochangelog
