%global source0_hash 7bee104afa0f81ce6ca7ce2205f65943b5e3650105507363f1a628bbca3a075b
Name:           xrotor
Version:        7.57
Release:        1%{?dist}
Summary:        Design and analysis tools for propellers and windmills
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://web.mit.edu/drela/Public/web/xrotor/
Source0:        http://web.mit.edu/drela/Public/web/xrotor/Xrotor%{version}.tar.tgz
Source1:        LICENSE.GPL
Source2:        LICENSE.LGPL
Patch0:         Xrotor7.55-makefile.patch
Requires:       xorg-x11-fonts-misc
# oreon:deps
BuildRequires:  gcc-gfortran
BuildRequires:  libX11-devel
BuildRequires:  make
# /oreon:deps
%description
XROTOR is an interactive program for the design and analysis of propellers
and windmills. It includes
 1. Design of minimum induced loss rotor (propeller or windmill)
 2. Prompted input of an arbitrary rotor geometry
 3. Interactive modification of a rotor geometry
and many others.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Xrotor
cp %{SOURCE1} .
cp %{SOURCE2} .

%build

export FFLAGS="-fallow-argument-mismatch %{optflags}"
export CFLAGS="%{optflags}"
%make_build -C plotlib
%make_build -C bin
%install
%make_install -C bin BINDIR=%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
