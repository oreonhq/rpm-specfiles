%global source0_hash 0225ebe9089be8d5becd36cf7af60433b067e5e6cf5741753ad4dfd61d0965f9
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global gap_pkgname    autodoc
%global gap_upname     AutoDoc
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/AutoDoc
Name:           gap-pkg-%{gap_pkgname}
Version:        2026.09.09
Release:        1%{?dist}
Summary:        Generate documentation from GAP source code
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/AutoDoc/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs .. --bare -c 'LoadPackage("GAPDoc");'
BuildOption(install): gap tst
BuildOption(check): --bare -c 'LoadPackage("GAPDoc");' tst/testall.g
%if %{without bootstrap}
%endif
Requires:       coreutils
Requires:       gap-core
Requires:       GAPDoc-latex
# oreon:deps
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-io
BuildRequires:  tex(a4wide.sty)
# /oreon:deps
%description
This package is an add-on to GAPDoc that enables generating documentation from
GAP source code.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        AutoDoc documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%install -a
cp -p doc/*.xml %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/doc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-autodoc-doc -f %{oreon_filedir}/gap-pkg-autodoc-doc.list

%changelog

%autochangelog
