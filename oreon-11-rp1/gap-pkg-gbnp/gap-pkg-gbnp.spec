%global source0_hash b01859fe938aa57b029bbbf2b3bac648e2793be8f2e9635e8cf7bf49d72177c4
%global gap_pkgname gbnp
%global giturl      https://github.com/gap-packages/gbnp
Name:           gap-pkg-%{gap_pkgname}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Computing Gröbner bases of noncommutative polynomials
License:        LGPL-2.1-or-later
URL:            https://gap-packages.github.io/gbnp/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/GBNP-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  make
BuildRequires:  tex-urlbst
# /oreon:deps
%description
GBNP provides GAP algorithms for computing Gröbner bases of non-commutative
polynomials with coefficients from a field implemented in GAP, and some
variations, such as a weighted and truncated version and a tracing facility.

The word algorithm is interpreted loosely: in general one cannot expect such
an algorithm to terminate, as it would imply solvability of the word problem
for finitely presented (semi)groups.

%package doc
License:        LGPL-2.1-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND LPPL-1.3a AND AGPL-3.0-only
Summary:        GBNP documentation and examples
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{gap_upname}-%{version}

%conf
# Help GAP find its files
sed -i "s,-r,-l '%{_builddir}/%{gap_upname}-%{version}/build;' &,;s/eval //" \
    etc/gapscript

%build

%make_build doc
%install -a
cp -a doc/{articles,examples} %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/doc
rm %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/lib/{gbnp-uses.sed,OPTIONS,STRUCTURE,TODO}
rm %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/tst/{.depend,GNUmakefile,txt2xml.sed}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-gbnp-doc -f %{oreon_filedir}/gap-pkg-gbnp-doc.list

%changelog

%autochangelog
