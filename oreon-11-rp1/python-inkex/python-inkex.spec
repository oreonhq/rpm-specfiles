%global source0_hash 301d5dddec0817b8890d0ca43e7e138ccc9e3fa3af3662b009953536b253a0de

%global         commit          89726a336658e2dd3986a64a26cffd67fd632afe
%global         shortcommit     %(c=%{commit}; echo ${c:0:8})
%global         commitdate      20250307
%global         reponame        extensions
%global         srcname         inkex
%global         forgeurl        https://gitlab.com/inkscape/extensions
Version:        1.4.0^%{commitdate}git%{shortcommit}
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        5%{?dist}
Summary:        Python extensions for Inkscape core

License:        GPL-2.0-or-later
URL:            %forgeurl
Source:         %{url}/-/archive/%{commit}/%{reponame}-%{shortcommit}.tar.gz
BuildRequires:  python3-devel
# Tests
BuildRequires:  gtk3-devel
BuildRequires:  gzip
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-base
BuildRequires:  python3-gobject-base-noarch
BuildRequires:  python3-gobject-devel
BuildRequires:  which
BuildArch: noarch

%global _description %{expand:
This package supports Inkscape extensions.

It provides
- a simplification layer for SVG manipulation through lxml
- base classes for common types of Inkscape extensions
- simplified testing of those extensions
- a user interface library based on GTK3

At its core, Inkscape extensions take in a file, and output a file.
- For effect extensions, those two files are SVG files.
- For input extensions, the input file may be any arbitrary
  file and the output is an SVG.
- For output extensions, the input is an SVG file while the
  output is an arbitrary file.
- Some extensions (e.g. the extensions manager) don't manipulate files.

This folder also contains the stock Inkscape extensions, i.e. the scripts
that implement some commands that you can use from within Inkscape.
Most of these commands are in the Extensions menu, or in the Open /
Save dialogs.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{reponame}-%{commit}
# Remove unneeded files
rm *.lock

rm tests/test_w*
rm tests/test_v*
rm tests/test_t*
rm tests/test_s*
rm tests/test_r*
rm tests/test_p*
rm tests/test_o*
rm tests/test_n*
rm tests/test_m*
rm tests/test_l*
rm tests/test_j*
rm tests/test_int*
rm tests/test_ins*
rm tests/test_inks*
rm tests/test_inkw*
rm tests/test_ink2*
rm tests/test_im*
rm tests/test_h*
rm tests/test_g*
rm tests/test_f*
rm tests/test_e*
rm tests/test_d*
rm tests/test_c*
rm tests/test_a*
rm tests/test_u*
rm tests/add_pylint.py

# Remove version limit from lxml
sed -i "s/lxml = .*/lxml = '\*'/" pyproject.toml
# Relax version limit for scour
sed -i 's/scour = "^0.37"/scour = ">=0.37"/' pyproject.toml
# Update version in configuration files
sed -i 's/cssselect = "^1.2.0"/cssselect = ">=1.1.0,<2.0.0"/' pyproject.toml
# Update python command
sed -i 's/call("python"/call("python3"/' tests/test_inkex_command.py
			     
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
# Executable fix
sed -i /env\ python/d %{buildroot}%{python3_sitelib}/inkex/tester/inx.py

%check
%pyproject_check_import
%pytest -k "not test_inkex_gui"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc package-readme.md
%license LICENSE.txt
 
%changelog
%autochangelog
