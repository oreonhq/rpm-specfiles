%global source0_hash 50cc069e3256197cecbab0044aabff985eca0eb92be431bd3c0d5e41feb3f509

# xschem Package description for Fedora/Free Electronic Lab
#
%global rpm_has_recommends    %(rpm --version | awk -e '{print ($3 > 4.12)}')
#
Name:           xschem
Version:        3.1.0
Release:        6%{?dist}
Summary:        Schematic capture and Netlisting EDA tool

License:        GPL-2.0-or-later
URL:            http://repo.hu/projects/xschem
Source0:        http://repo.hu/projects/xschem/releases/xschem-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gawk
BuildRequires:  flex, bison
#BuildRequires:  flex-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(cairo-xcb)
#BuildRequires:  cairo-devel
#BuildRequires:  xcb-util-devel

%if %rpm_has_recommends
Recommends:     %{name}-doc = %{version}-%{release}
%endif

#Requires:   tcl, tk

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

%autosetup

%build
./"configure" --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}" \
    --prefix=%{_prefix} --symbols
%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS Changelog README
%{_bindir}/%{name}
%{_bindir}/rawtovcd
%{_datadir}/%{name}
%{_mandir}/man1/xschem.1*

%files doc
%{_docdir}/%{name}

%changelog
%autochangelog
