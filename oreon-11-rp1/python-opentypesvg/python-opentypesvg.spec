%global source0_hash 21afa214d9a6c33743aa544f0a844779de99f9562f6990e4d3af8108adcd1b27
Name:           python-opentypesvg
Version:        1.1.5
Release:        1%{?dist}
Summary:        Tools for making OpenType-SVG fonts
License:        MIT
URL:            https://github.com/adobe-type-tools/opentype-svg
Source0:        https://files.pythonhosted.org/packages/source/o/opentypesvg/opentypesvg-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-opentypesvg = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-opentypesvg
Summary:        Tools for making OpenType-SVG fonts
%description -n python3-opentypesvg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir opentypesvg-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-opentypesvg usr/lib/python3*/site-packages/opentypesvg* usr/lib64/python3*/site-packages/opentypesvg* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/opentypesvg* usr/lib64/python3*/site-packages/opentypesvg* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-opentypesvg -f %{oreon_filedir}/python3-opentypesvg.list

%changelog

%autochangelog
