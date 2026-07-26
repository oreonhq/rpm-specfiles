%global source0_hash 7bee104afa0f81ce6ca7ce2205f65943b5e3650105507363f1a628bbca3a075b

Name:           xrotor
Version:        7.55
Release:        30%{?dist}
Summary:        Design and analysis tools for propellers and windmills

# Plotlib is LGPLv2+, the rest is GPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://web.mit.edu/drela/Public/web/xrotor/
Source0:        http://web.mit.edu/drela/Public/web/xrotor/Xrotor%{version}.tar.tgz
# The package does not ship a license file
Source1:        LICENSE.GPL
Source2:        LICENSE.LGPL
# Makefile variables and flags
Patch0:         Xrotor7.55-makefile.patch

BuildRequires: make
BuildRequires:  gcc-gfortran libX11-devel
Requires:       xorg-x11-fonts-misc

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

%files
%doc version_notes.txt xrotor_doc.txt
%license LICENSE.GPL LICENSE.LGPL
%{_bindir}/xrotor
%{_bindir}/jplot
%{_bindir}/jplote

%changelog
%autochangelog
