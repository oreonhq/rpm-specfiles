%global source0_hash ae9fa477e5df51e4da024b96ac16a6f17c3b8715aa953dabb9a4004da782820f
%global gap_pkgname liering
%global giturl      https://github.com/gap-packages/liering
Name:           gap-pkg-%{gap_pkgname}
Version:        2.4.2
Release:        1%{?dist}
Summary:        Computing with finitely presented Lie rings
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/liering/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
This package provides functions for constructing and working with Lie rings.
There are functions for dealing with finitely-presented Lie rings, and for
performing the Lazard correspondence.  The package also contains a small
database of finitely-generated Lie rings satisfying an Engel condition.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        LieRing documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-liering-doc -f %{oreon_filedir}/gap-pkg-liering-doc.list

%changelog

%autochangelog
