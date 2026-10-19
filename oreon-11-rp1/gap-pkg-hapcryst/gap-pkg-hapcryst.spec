%global source0_hash dda392457ecc9fcffd7d86b3633da455e9fe65118d7bcf4039cc5d4d05edfc94
%global gap_pkgname hapcryst
%global giturl      https://github.com/gap-packages/hapcryst
Name:           gap-pkg-%{gap_pkgname}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Integral cohomology computations of Bieberbach groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/hapcryst/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
Patch:          %{name}-doc.patch
Patch:          %{name}-carat.patch
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): examples lib tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-aclib
Requires:       gap-pkg-cryst
Requires:       gap-pkg-hap
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-polymaking
Recommends:     gap-pkg-caratinterface
Recommends:     gap-pkg-crystcat
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-caratinterface
BuildRequires:  gap-pkg-cryst
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-hap
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-polymaking-doc
# /oreon:deps
%description
This package is an add-on for Graham Ellis' HAP package.  HAPcryst implements
some functions for crystallographic groups (namely OrbitStabilizer-type
methods).  It is also capable of calculating free resolutions for Bieberbach
groups.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        HAPcryst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{gap_upname}-%{version}

%build -a

sed -i 's,\./lib,.&,g' doc/*.html
%install -a
rm -fr %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/doc
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/doc
%gap_copy_docs -d lib/datatypes/doc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check -p

polymake --reconfigure - <<< exit;
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-hapcryst-doc -f %{oreon_filedir}/gap-pkg-hapcryst-doc.list

%changelog

%autochangelog
