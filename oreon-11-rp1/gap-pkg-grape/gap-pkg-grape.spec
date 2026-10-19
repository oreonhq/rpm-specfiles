%global source0_hash 911b7e181161a4935b5c36cd370a11b250769735ea2f10087bbd75a8de3a2fa1
%global gap_pkgname grape
%global giturl      https://github.com/gap-packages/grape
Name:           gap-pkg-%{gap_pkgname}
Version:        4.9.3
Release:        1%{?dist}
Summary:        GRaph Algorithms using PErmutation groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/grape/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
Patch:          %{name}-nauty.patch
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): grh htm lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
Requires:       nauty
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  nauty
BuildRequires:  tth
# /oreon:deps
%description
GRAPE is a package for computing with graphs and groups, and is primarily
designed for constructing and analyzing graphs related to groups, finite
geometries, and designs.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        GRAPE documentation and examples
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{gap_upname}-%{version}

%conf
# There is no ext manual anymore
sed -i '/UseReferences.*ext/d' doc/manual.tex

# Remove nauty sources so we use the system version
rm -fr nauty2_8_6

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-grape-doc -f %{oreon_filedir}/gap-pkg-grape-doc.list

%changelog

%autochangelog
