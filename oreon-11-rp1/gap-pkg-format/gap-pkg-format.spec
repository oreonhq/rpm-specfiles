%global source0_hash 443804dc4cb11c23f496508378bce4940a9b748812e62c03ecacdc538afca477
%global gap_pkgname format
%global giturl      https://github.com/gap-packages/format
Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.5
Release:        1%{?dist}
Summary:        Formations of finite solvable groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/format/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): grp htm lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  tth
# /oreon:deps
%description
The package contains programs for computing with formations of finite solvable
groups and with various formation-theoretic subgroups.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        Format documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-format-doc -f %{oreon_filedir}/gap-pkg-format-doc.list

%changelog

%autochangelog
