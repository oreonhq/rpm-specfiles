%global source0_hash e30ca878e42021ec51f317496a330f8ff345f12c5c14de4c9c87670e64c8aba6
%global gap_pkgname datastructures
%global giturl      https://github.com/gap-packages/datastructures
Name:           gap-pkg-%{gap_pkgname}
Version:        0.4.3
Release:        1%{?dist}
Summary:        Standard data structures for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/datastructures/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The datastructures package aims at providing standard datastructures,
consolidating existing code and improving on it, in particular in view of
HPC-GAP.

The following data structures are provided:
- queues
- doubly linked lists
- heaps
- priority queues
- hashtables
- dictionaries

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Data structures documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build -p

export CFLAGS='%{build_cflags} -fwrapv'
export CXXFLAGS='%{build_cxxflags} -fwrapv'
./configure %{gap_archdir}
%make_build
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-datastructures-doc -f %{oreon_filedir}/gap-pkg-datastructures-doc.list

%changelog

%autochangelog
