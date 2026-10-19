%global source0_hash 67f1f2648b027dde622c341bf19ea689ccc4af0be550249abbf6254cfa9c295b
%global gap_pkgname cvec
%global giturl      https://github.com/gap-packages/cvec
Name:           gap-pkg-%{gap_pkgname}
Version:        2.8.5
Release:        1%{?dist}
Summary:        Compact vectors over finite fields
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/cvec/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.bz2
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin example gap local test tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-orb-doc
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The CVEC package provides an implementation of compact vectors over finite
fields.  Contrary to earlier implementations no table lookups are used but
only word-based processor arithmetic.  This allows for bigger finite fields
and higher speed.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        CVEC documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-orb-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build

./configure --with-gaproot=%{gap_archdir}
%make_build V=1
make doc
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-cvec-doc -f %{oreon_filedir}/gap-pkg-cvec-doc.list

%changelog

%autochangelog
