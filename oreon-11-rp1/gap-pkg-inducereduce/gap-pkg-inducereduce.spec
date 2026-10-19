%global source0_hash 19ae3d4e16d62735daccc8215c90d72ca210c35420a3b8aa414ab4504c24093b
%global gap_pkgname inducereduce
%global gap_upname  InduceReduce
%global giturl      https://github.com/gap-packages/InduceReduce
Name:           gap-pkg-%{gap_pkgname}
Version:        1.4
Release:        1%{?dist}
Summary:        Compute the character table of a finite group
License:        GPL-3.0-or-later
URL:            https://gap-packages.github.io/InduceReduce/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
The InduceReduce package provides an implementation of Unger's algorithm for
computing the table of ordinary irreducible characters of a finite group.  The
algorithm works by inducing characters from suitably chosen elementary
subgroups and finding an orthogonal basis of the resulting lattice of
characters by LLL lattice reduction.

%package doc
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        InduceReduce documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-inducereduce-doc -f %{oreon_filedir}/gap-pkg-inducereduce-doc.list

%changelog

%autochangelog
