%global source0_hash bc8bb0839ee400915df1c809ba9ba131c34bd022d194db4d4828115d7dbf8e99
%global gap_pkgname profiling
%global giturl      https://github.com/gap-packages/profiling
Name:           gap-pkg-%{gap_pkgname}
Version:        2.6.3
Release:        1%{?dist}
Summary:        Line by line profiling and code coverage for GAP
License:        MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://gap-packages.github.io/profiling/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
Patch:          %{name}-rapidjson.patch
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin data gap tst
BuildOption(check): tst/testall.g
Requires:       flamegraph
Requires:       flamegraph-stackcollapse
Requires:       gap-pkg-io%{?_isa}
Requires:       which
Requires:       xdg-utils
Provides:       bundled(md5-plumb)
# oreon:deps
BuildRequires:  elinks
BuildRequires:  flamegraph
BuildRequires:  flamegraph-stackcollapse
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  which
BuildRequires:  xdg-utils
# /oreon:deps
%description
This package provides line-by-line profiling of GAP, allowing both discovering
which lines of code take the most time, and which lines of code are even
executed.

The main function provided by this package is
OutputAnnotatedCodeCoverageFiles, which takes a previously generated profile
(using ProfileLineByLine or CoverageLineByLine, both provided by the GAP
library), and outputs human-readable HTML files.

There is also OutputFlameGraph, which outputs a graphical diagram showing
which functions took the most time during execution.

%package doc
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Profiling documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{gap_upname}-%{version}

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not use the bundled rapidjson
rm -fr src/rapidjson
sed -i.orig 's,"\(rapidjson/.*h\)",<\1>,' src/json_parse_rapidjson.h
fixtimestamp src/json_parse_rapidjson.h

# Do not use the bundled FlameGraph
rm -fr FlameGraph
sed -i.orig '/Flame/s,DirectoriesPackageLibrary([^)]*),Directory("%{_bindir}"),' gap/profiling.gi
fixtimestamp gap/profiling.gi

%build -p

./configure %{gap_archdir}
%make_build V=1
%check -p

export BROWSER=elinks
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-profiling-doc -f %{oreon_filedir}/gap-pkg-profiling-doc.list

%changelog

%autochangelog
