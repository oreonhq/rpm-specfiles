%global source0_hash d118c41340d10f6dacf58477dbb3e726824a71f7b79e6228f13f349bfa48365e
%global gap_pkgname sl2reps
%global giturl      https://github.com/snw-0/sl2-reps
Name:           gap-pkg-%{gap_pkgname}
Version:        1.1
Release:        1%{?dist}
Summary:        Construct representations of SL(2,Z)
License:        GPL-2.0-or-later
URL:            https://snw-0.github.io/sl2-reps/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/sl2-reps-%{version}.tar.gz
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
This package provides methods for constructing and testing matrix
presentations of the representations of SL(2,Z) whose kernels are congruence
subgroups of SL(2,Z).

Irreducible representations of prime-power level are constructed individually
by using the Weil representations of quadratic modules, and from these a list
of all representations of a given degree or level can be produced.  The format
is designed for the study of modular tensor categories in particular,
providing symmetric matrix presentations of each representation.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SL2Reps documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sl2-reps-%{version}
%oreon_prep
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-sl2reps-doc -f %{oreon_filedir}/gap-pkg-sl2reps-doc.list

%changelog

%autochangelog
