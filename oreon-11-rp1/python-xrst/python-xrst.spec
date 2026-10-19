%global source0_hash 720e254fe6e7195f0e5057ee5a1062d1806ac816e43f7604a11e4020b8d9e806
Name:           python-xrst
Version:        2026.0.0
Release:        1%{?dist}
Summary:        Extract Sphinx RST Files
License:        GPL-3.0-or-later
URL:            https://github.com/bradbell/xrst
Source0:        https://github.com/bradbell/xrst/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xrst = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-xrst
Summary:        Extract Sphinx RST Files
%description -n python3-xrst

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n xrst-%{version}
#
# Suppress spelling warnings during tox because this system
# may use a different dictionary than is used for xrst development.
cat << EOF > temp.sed
s|'sphinx_rtd_theme'|&, '--suppress_spell_warnings'|
EOF
sed -i pytest/test_rst.py -f temp.sed 
#
%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}/%{_mandir}/man1
%{python3} -m xrst \
   --rst_only --group_list default user --suppress_spell_warnings
%{python3} bin/rst2man.py \
   build/rst/run_xrst.rst %{buildroot}/%{_mandir}/man1/xrst.1
%oreon_autofiles python3-xrst usr/lib/python3*/site-packages/xrst* usr/lib64/python3*/site-packages/xrst* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xrst* usr/lib64/python3*/site-packages/xrst* usr/bin/*

%check

%tox
%files
%files -n python3-xrst -f %{oreon_filedir}/python3-xrst.list

%changelog

%autochangelog
