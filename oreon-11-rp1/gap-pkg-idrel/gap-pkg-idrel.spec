%global source0_hash 3b3c2c7e781d702cd1c0e10e8af8d27c36777db7b2ecdb41967f6934b3fa8324
%global gap_pkgname idrel
%global giturl      https://github.com/gap-packages/idrel
Name:           gap-pkg-%{gap_pkgname}
Version:        2.51
Release:        1%{?dist}
Summary:        Identities among relations of a group presentation
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/idrel/
VCS :           git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
The IdRel package is designed for computing the identities among relations of
a group presentation using rewriting, logged rewriting, monoid polynomials,
module polynomials and Y-sequences.

%package doc
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP idrel package
Requires:       %{name} = %{version}-%{release}
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-idrel-doc -f %{oreon_filedir}/gap-pkg-idrel-doc.list

%changelog

%autochangelog
