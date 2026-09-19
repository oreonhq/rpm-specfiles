%global source0_hash 820bd9e32be5b1a4422744c19b371616ace70f48f00768b8afe373f9ded1516b

Name:           gnucap
Version:        0.35
Release:        45%{?dist}
Summary:        The Gnu Circuit Analysis Package
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.gnu.org/software/gnucap/
Source0:        http://www.gnucap.org/devel/gnucap-%{version}.tar.gz
Patch0:         gnucap-0.34-debian.patch
Patch1:         gnucap-0.35-gcc43.patch
Patch2:         gnucap-0.35-gcc6.patch
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires: make

%description
The primary component is a general purpose circuit simulator. It performs
nonlinear dc and transient analyses, fourier analysis, and ac analysis. Spice
compatible models for the MOSFET (level 1-7), BJT, and diode are included in
this release. Gnucap is not based on Spice, but some of the models have been
derived from the Berkeley models. Unlike Spice, the engine is designed to do
true mixed-mode simulation. Most of the code is in place for future support of
event driven analog simulation, and true multi-rate simulation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# use ncurses instead of termcap (bz 226771)
sed -i 's/-ltermcap/-lncurses/g' configure

%build
%configure
make %{?_smp_mflags}

%install
%make_install

# for %%doc
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}
mv doc/acs-tutorial doc/gnucap-tutorial
rm examples/Makefile*

%files
%doc doc/history doc/relnotes.* doc/gnucap-tutorial doc/whatisit
%doc man/gnucap-man.pdf examples
%license doc/COPYING
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
