%global source0_hash 509d6faa0d3c9cfc42ee0f2dd796900571877761f93621a80dce66b7e9a8a0ae
%global gap_pkgname standardff
%global gap_upname  StandardFF
%global gap_makedoc makedocrel.g
%global giturl      https://github.com/frankluebeck/StandardFF
Name:           gap-pkg-%{gap_pkgname}
Version:        1.0
Release:        1%{?dist}
Summary:        Standardized generation of finite fields and cyclic subgroups
License:        GPL-3.0-or-later
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/gap/StandardFF/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs .. -r pathtoroot
BuildOption(install): data lib tst VERSION
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
Recommends:     gap-pkg-ctbllib
Recommends:     gap-pkg-factint
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-spinsym
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(ntl)
# /oreon:deps
%description
The StandardFF package contains an implementation of *standard* generators of
finite fields and of cyclic subgroups in the multiplicative groups of finite
fields, as described in https://arxiv.org/abs/2107.02257.

%package doc
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
BuildArch:      noarch
Summary:        StandardFF documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build -p

cd ntl
for fil in *.cc; do
  g++ %{build_cxxflags} $fil -o $(basename $fil .cc) %{build_ldflags} -lntl
done
cd -
cat > pathtoroot << EOF
pathtoroot := "%{gap_libdir}";
EOF
%install -a
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/ntl
cp -p ntl/{factors,findirr,findstdirrGF{2,p},isirrGF{p,q}} \
   %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/ntl
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-standardff-doc -f %{oreon_filedir}/gap-pkg-standardff-doc.list

%changelog

%autochangelog
