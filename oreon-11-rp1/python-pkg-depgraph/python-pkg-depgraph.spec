%global source0_hash de51cef8252fa1047345ce0d0ffb106fafc7d99878f26069659638d8661f998a
Name:           python-pkg-depgraph
Version:        0.0.1.post1
Release:        1%{?dist}
Summary:        Packaging-oriented dependency graph library
License:        GPL-2.0-or-later
URL:            https://pagure.io/michel-slm/pkg-depgraph
Source0:        https://files.pythonhosted.org/packages/source/p/pkg_depgraph/pkg_depgraph-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pkg-depgraph = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pkg-depgraph
Summary:        Packaging-oriented dependency graph library
%description -n python3-pkg-depgraph

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pkg_depgraph-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pkg-depgraph usr/lib/python3*/site-packages/pkg_depgraph* usr/lib64/python3*/site-packages/pkg_depgraph* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pkg_depgraph* usr/lib64/python3*/site-packages/pkg_depgraph* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-pkg-depgraph -f %{oreon_filedir}/python3-pkg-depgraph.list

%changelog

%autochangelog
