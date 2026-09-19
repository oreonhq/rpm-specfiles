%global source0_hash 5c0250643f52ce0e75d7338ae2504ce7907f2d49a30f921826717b8ac12ebe40

Name:           xfoil
Version:        6.99
Release:        25%{?dist}
Summary:        Subsonic Airfoil Development System

# Plotlib is LGPLv2+, the rest is GPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://web.mit.edu/drela/Public/web/xfoil/
Source0:        http://web.mit.edu/drela/Public/web/xfoil/%{name}%{version}.tgz
# The package does not ship a license file
Source1:        LICENSE.GPL
Source2:        LICENSE.LGPL
# Makefile variables and flags
Patch0:         xfoil-6.99-makefile.patch
# Code fixes (from debian package)
Patch1:         xfoil-6.99-xfoil-fixes.patch
Patch2:         xfoil-6.99-fix-write-after-end.patch
Patch3:         xfoil-6.99-pxplot-args.patch
# Set osmap file location
Patch4:         xfoil-6.99-default-osfile.patch

BuildRequires: make
BuildRequires:  gcc-gfortran libX11-devel
Requires:       xorg-x11-fonts-misc

%description
XFOIL is an interactive program for the design and analysis of subsonic
isolated airfoils.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Xfoil
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
export FFLAGS="-fallow-argument-mismatch %{optflags}"
export CFLAGS="%{optflags} -DDEFAULT_OSFILE=\\\"%{_datadir}/%{name}/osmap.dat\\\""

%make_build -C orrs/bin osgen
pushd orrs
./bin/osgen osmaps_ns.lst
popd
%make_build -C plotlib
%make_build -C bin

%install
%make_install -C bin BINDIR=%{_bindir}
install -Dpm 0644 orrs/osmap.dat %{buildroot}/%{_datadir}/%{name}/osmap.dat

%files
%license LICENSE.GPL LICENSE.LGPL
%doc sessions.txt version_notes.txt xfoil_doc.txt
%{_datadir}/%{name}/
%{_bindir}/xfoil
%{_bindir}/pplot
%{_bindir}/pxplot

%changelog
%autochangelog
