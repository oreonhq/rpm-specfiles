%global source0_hash c6630c5d5385caa3a0e470599759f8e42bd5f0147eebfee164ca808cec83371e
%global gap_pkgname crime
%global giturl      https://github.com/gap-packages/crime
Name:           gap-pkg-%{gap_pkgname}
Version:        1.6
Release:        1%{?dist}
Summary:        Group cohomology and Massey products
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/crime/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  perl-generators
# /oreon:deps
%description
This GAP package computes cohomology rings for finite p-groups using Jon
Carlson's method, both as GAP objects, and also in terms of generators and
relators.  It also computes induced homomorphisms on cohomology and Massey
products in the cohomology ring.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Group cohomology documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%check

gap -l '%{buildroot}%{gap_libdir};' << EOF
LoadPackage("crime");
GAP_EXIT_CODE(Test("tst/test.tst", rec(compareFunction := "uptowhitespace")));
EOF
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-crime-doc -f %{oreon_filedir}/gap-pkg-crime-doc.list

%changelog

%autochangelog
