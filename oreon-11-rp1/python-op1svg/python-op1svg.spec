%global source0_hash 8f13084f491b8c9de9e69afd717dc4681d52fe13739ec44485e1171c6d4d73e8
%global pypi_name op1svg
%global forgeurl https://github.com/op1hacks/op1svg
%global commit 50a3b01ebb74fd07b33d91c08b1e59e11494801d
%forgemeta
%global common_description %{expand:
op1svg normalizes SVG files so that the OP-1 understands them:
- Remove unsupported tags and attributes
- Remove comments
- Convert styles to attributes, and drop unsupported styles
- Fix decimals; a maximum of 4 decimals is supported by the OP-1
- Reformat the path data in paths}
Name:           python-%{pypi_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Normalize SVG files so that the OP-1 understands them
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{pypi_name}-%{commit}.tar.gz
Source1:        op1svg.1
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  sed
# /oreon:deps
%description
%{common_description}

%package -n     %{pypi_name}
Summary:        Normalize SVG files so that the OP-1 understands them
%description -n %{pypi_name}
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python3|d" -i %{pypi_name}/*.py

%build

%py3_build
%install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -P %{SOURCE1} %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n op1svg -f %{oreon_filedir}/op1svg.list

%changelog

%autochangelog
