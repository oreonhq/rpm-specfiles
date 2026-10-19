%global source0_hash 087d1d744354192697735b26c2553540daa3ffb2b6138664b3f829d31c408a78
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global gap_pkgname    orb
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/orb
Name:           gap-pkg-%{gap_pkgname}
Version:        5.1.0
Release:        1%{?dist}
Summary:        Methods to enumerate orbits in GAP
License:        GPL-3.0-or-later
URL:            https://gap-packages.github.io/orb/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
Source1:        %{name}-testdata.tar.xz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin examples gap tst
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
Requires:       gap-pkg-io%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-browse
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-cvec
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package enables enumerating orbits in various ways from within GAP.

%package doc
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        ORB documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -b 1

%conf
# Account for changed hash values on big endian architectures
# https://github.com/gap-packages/orb/issues/70
%ifarch s390x
sed -i 's/799/741/;s/573/237/' tst/bugfix.tst
%endif

%build -p

./configure --with-gaproot=%{gap_archdir}
%make_build V=1
%check -p

rm -f tst/orbitspeedtest.g
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-orb-doc -f %{oreon_filedir}/gap-pkg-orb-doc.list

%changelog

%autochangelog
