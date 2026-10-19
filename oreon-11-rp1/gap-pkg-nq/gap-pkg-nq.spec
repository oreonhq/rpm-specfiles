%global source0_hash 74b16c3a7cf87c5e628a1691defef783a639c6f8ecdd722816c847a8a88ce5eb
%global gap_pkgname nq
%global giturl      https://github.com/gap-packages/nq
Name:           gap-pkg-%{gap_pkgname}
Version:        2.6.1
Release:        1%{?dist}
Summary:        Nilpotent Quotients of finitely presented groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/nq/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_pkgname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin examples gap tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
Requires:       gap-pkg-polycyclic
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gmp)
# /oreon:deps
%description
This package provides access from within GAP to the ANU nilpotent quotient
program for computing nilpotent factor groups of finitely presented groups.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        NQ documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
./autogen.sh

%build -p

%configure --with-gaproot=%{gap_archdir} --disable-silent-rules
%make_build
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-nq-doc -f %{oreon_filedir}/gap-pkg-nq-doc.list

%changelog

%autochangelog
