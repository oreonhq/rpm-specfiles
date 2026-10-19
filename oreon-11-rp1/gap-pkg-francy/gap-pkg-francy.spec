%global source0_hash fc3b5a8c6a56144228e243e6ca540105975a666b7aed14c68ec11eced50492ce
%global gap_pkgname francy
%global giturl      https://github.com/gap-packages/francy
Name:           gap-pkg-%{gap_pkgname}
Version:        2.0.3
Release:        1%{?dist}
Summary:        Framework for interactive discrete mathematics
License:        MIT
URL:            https://gap-packages.github.io/francy/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples gap notebooks schema tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-json
Requires:       gap-pkg-jupyterkernel
Requires:       gap-pkg-uuid
Requires:       xdg-utils
# oreon:deps
BuildRequires:  elinks
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-json
BuildRequires:  gap-pkg-jupyterkernel
BuildRequires:  gap-pkg-uuid
BuildRequires:  xdg-utils
# /oreon:deps
%description
Francy is a package for GAP and provides a framework for Interactive Discrete
Mathematics.

Unlike xgap, Francy is not linked with any GUI framework and instead, this
package generates a semantic model that can be used to produce a graphical
representation using any other framework / language.

There is a JavaScript implementation of the graphical representation that
works on Jupyter, embedded in a Web page or as a Desktop Application (e.g.
using electron).

%package doc
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Francy documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%conf
# Call xdg-open instead of open
sed -i.orig 's/"open "/"xdg-open "/' gap/canvas.gi
touch -r gap/canvas.gi.orig gap/canvas.gi
rm gap/canvas.gi.orig

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-francy-doc -f %{oreon_filedir}/gap-pkg-francy-doc.list

%changelog

%autochangelog
