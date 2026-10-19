%global source0_hash 2ae9c1691fe46950a44e2614ed4dcfe5dbb418c13cf3ebb4515f6aa59990ea9f
%global gap_pkgname digraphs
%global giturl      https://github.com/digraphs/Digraphs
Name:           gap-pkg-%{gap_pkgname}
Version:        1.15.0
Release:        1%{?dist}
Summary:        GAP package for digraphs and multidigraphs
License:        GPL-3.0-or-later AND LGPL-3.0-only
URL:            https://digraphs.github.io/Digraphs/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): bin data gap notebooks tst VERSIONS
BuildOption(check): tst/teststandard.g
Requires:       gap-pkg-datastructures%{?_isa}
Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}
Recommends:     gap-pkg-grape%{?_isa}
Recommends:     gap-pkg-nautytracesinterface%{?_isa}
Recommends:     graphviz
Provides:       bundled(bliss) = 0.73
# oreon:deps
BuildRequires:  GAPDoc-doc
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-datastructures
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-nautytracesinterface
BuildRequires:  gap-pkg-orb
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libplanarity)
BuildRequires:  tex(a4wide.sty)
BuildRequires:  xdg-utils
# /oreon:deps
%description
The Digraphs package is a GAP package containing methods for graphs, digraphs,
and multidigraphs.

%package doc
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Digraphs documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%conf
# Make sure the bundled planarity is not used
rm -fr extern/edge-addition-planarity-suite-Version_4.0.0.0

%build -p

%configure --with-gaproot=%{gap_archdir} --disable-silent-rules \
  --with-external-planarity
%make_build
%check -p

cp -p doc/*.xml %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/doc
%check -a

rm %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/doc/*.xml
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-digraphs-doc -f %{oreon_filedir}/gap-pkg-digraphs-doc.list

%changelog

%autochangelog
