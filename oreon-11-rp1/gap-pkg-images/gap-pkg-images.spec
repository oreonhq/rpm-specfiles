%global source0_hash 69fc28df4be32613ec9b7af56fbf935148f6b500b21681f4ce8fe85400093276

%global gap_pkgname images
%global giturl      https://github.com/gap-packages/images

Name:           gap-pkg-%{gap_pkgname}
Version:        1.3.3
Release:        %autorelease
Summary:        Minimal and canonical images in permutation groups

License:        MPL-2.0
URL:            https://gap-packages.github.io/images/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-ferret
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-tomlib

Requires:       gap-core

Recommends:     gap-pkg-ferret

%description
This package provides functionality to compute canonical representatives under
group actions in GAP.

%package doc
# The content is MPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Images documentation
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Update the atlas package name
sed -i 's/atlas/atlasrep/' tst/test_functions.g

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
