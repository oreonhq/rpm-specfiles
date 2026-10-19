%global source0_hash 1b028a8d5d4572c972fb4a2186b03818a372e66a5c81a2b65fa4a94aabe66036
%global gap_pkgname liealgdb
%global giturl      https://github.com/gap-packages/liealgdb
Name:           gap-pkg-%{gap_pkgname}
Version:        2.3.1
Release:        1%{?dist}
Summary:        Database of Lie algebras
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/liealgdb/
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
The package LieAlgDB provides access to several classifications of Lie
algebras.  In the mathematics literature many classifications of Lie algebras
of various types have been published (refer to the bibliography of the manual
for a few examples).  However, working with these classifications from paper
is not always easy.  This package aims at making a few classifications of
small dimensional Lie algebras that have appeared in recent years more
accessible.  For each classification that is contained in the package,
functions are provided that construct Lie algebras from that classification
inside GAP.  This allows the user to obtain easy access to the often rather
complicated data contained in a classification, and to directly interface the
Lie algebras to the functionality for Lie algebras which is already contained
in GAP.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        LieAlgDB documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-liealgdb-doc -f %{oreon_filedir}/gap-pkg-liealgdb-doc.list

%changelog

%autochangelog
