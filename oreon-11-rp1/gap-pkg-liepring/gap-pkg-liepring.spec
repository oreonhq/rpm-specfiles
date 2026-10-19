%global source0_hash c531dac70f3eab78f36e801c924dc0044dff999eca301729048cfcc25fa7d044
%global gap_pkgname liepring
%global giturl      https://github.com/gap-packages/liepring
Name:           gap-pkg-%{gap_pkgname}
Version:        2.9.3
Release:        1%{?dist}
Summary:        Database and algorithms for Lie p-rings
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/liepring/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap htm lib tst VERSION
BuildOption(check): tst/testall.g
Requires:       gap-pkg-liering
Recommends:     gap-pkg-singular
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-liering
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-singular
BuildRequires:  tth
# /oreon:deps
%description
The main object of the LiePRing package is to provide access to the nilpotent
Lie rings of order p^n for p>2 and n<=7.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        LiePRing documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Fix paths
sed -i 's,\.\./\.\./\.\./,%{gap_libdir}/,' doc/make_doc

%build

ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-liepring-doc -f %{oreon_filedir}/gap-pkg-liepring-doc.list

%changelog

%autochangelog
