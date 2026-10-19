%global source0_hash d7fa88855515769d8ece8f6715c407a61963336a1c682d9765c99bfc4367a187
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global gap_pkgname openmath
%global gap_upname  OpenMath
%global giturl      https://github.com/gap-packages/openmath
Name:           gap-pkg-%{gap_pkgname}
Version:        11.5.6
Release:        1%{?dist}
Summary:        Import and export of OpenMath objects for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/openmath/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
%global _docdir_fmt %{name}
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): cds gap hasse private tst
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
Requires:       gap-pkg-io
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-scscp-doc
# /oreon:deps
%description
This package provides an OpenMath phrasebook for GAP.  It allows GAP users to
import and export mathematical objects encoded in OpenMath, for the purpose of
exchanging them with other OpenMath-enabled applications.  For details about
the OpenMath encoding, see https://openmath.org/.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        OpenMath documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%if %{without bootstrap}
Requires:       gap-pkg-scscp-doc
%endif
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build -p

ln -s %{gap_libdir}/doc ../../doc
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-openmath-doc -f %{oreon_filedir}/gap-pkg-openmath-doc.list

%changelog

%autochangelog
