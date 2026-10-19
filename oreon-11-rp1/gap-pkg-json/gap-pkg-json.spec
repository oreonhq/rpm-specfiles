%global source0_hash 8be90851eaa3e294fec988214ed45f49ba60877db92c14a982c703c274a686ac
%global gap_pkgname json
%global giturl      https://github.com/gap-packages/json
Name:           gap-pkg-%{gap_pkgname}
Version:        3.0.0
Release:        1%{?dist}
Summary:        JSON reading and writing for GAP
License:        BSD-2-Clause
URL:            https://gap-packages.github.io/json/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
Provides:       bundled(picojson-devel) = 1.1.1
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package defines a mapping between the JSON markup language and GAP.  The
built-in datatypes of GAP provide an easy mapping to and from JSON.  This
package uses the following mapping between GAP and JSON.

- JSON lists are mapped to GAP lists
- JSON dictionaries are mapped to GAP records
- JSON strings are mapped to GAP strings
- Integers are mapped to GAP integers, non-integer numbers are mapped to
  Floats
- true, false and null are mapped to true, false and fail respectively

Note that this library will not map any other GAP types, such as groups,
permutations, to or from JSON.  If you wish to map between more complex types,
look at the gap-pkg-openmath package, or IO_Pickle in the gap-pkg-io package.

%package doc
License:        BSD-2-CLause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        JSON documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build -p

./configure %{gap_archdir}
%make_build
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-json-doc -f %{oreon_filedir}/gap-pkg-json-doc.list

%changelog

%autochangelog
