%global source0_hash f71c841ca07f4824771c2079cafdc54c9bbfe67cbe14427d56b080e94b981751
%global gap_pkgname design
%global giturl      https://github.com/gap-packages/design
Name:           gap-pkg-%{gap_pkgname}
Version:        1.8.2
Release:        1%{?dist}
Summary:        Construct, classify, partition, and study block designs
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/design/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): htm lib tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-grape
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-grape
BuildRequires:  tth
# /oreon:deps
%description
DESIGN is a package for constructing, classifying, partitioning and studying
block designs.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        Block design documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%conf
# There is no longer an ext manual
sed -i '/UseReferences.*ext/d' doc/manual.tex

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-design-doc -f %{oreon_filedir}/gap-pkg-design-doc.list

%changelog

%autochangelog
