%global source0_hash e9cb319ad599643259b8e8bb680a8a293fb29db2aff2b27cd8c358351b4d00f1
%global gap_pkgname jupyterviz
%global giturl      https://github.com/nathancarter/jupyterviz
Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.6
Release:        1%{?dist}
Summary:        Jupyter notebook visualization tools for GAP
License:        GPL-2.0-or-later
URL:            https://nathancarter.github.io/jupyterviz/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
Patch:          %{name}-python3.patch
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): *.ipynb examples lib tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-json
Requires:       gap-pkg-jupyterkernel
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-json
BuildRequires:  gap-pkg-jupyterkernel
BuildRequires:  python3-devel
# /oreon:deps
%description
This package adds visualization tools to GAP for use in Jupyter notebooks.
These include standard line and bar graphs, pie charts, scatter plots, and
graphs in the vertices-and-edges sense.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Jupyter visualization tools for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{gap_upname}-%{version}

%build -p

python3 extract_examples.py
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-jupyterviz-doc -f %{oreon_filedir}/gap-pkg-jupyterviz-doc.list

%changelog

%autochangelog
