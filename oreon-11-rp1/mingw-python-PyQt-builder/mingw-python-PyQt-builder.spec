%global source0_hash 6af6646ba29668751b039bfdced51642cb510e300796b58a4d68b7f956a024d8
%{?mingw_package_header}
%global pkg_name PyQt-builder
%global pypi_name pyqt-builder
Name:           mingw-python-%{pkg_name}
Summary:        MinGW Python PyQt-builder
Version:        1.19.1
Release:        1%{?dist}
BuildArch:      noarch
License:        BSD-2-Clause
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt_builder/pyqt_builder-%{version}.tar.gz
Patch0:         PyQt-builder_mingw.patch
Patch1:         pyqt_builder_nosetuptoolsscm.patch
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
# /oreon:deps
%description
MinGW Python %{pkg_name}.

%package -n mingw32-python3-%{pkg_name}
Summary:       MinGW Python 3 %{pkg_name}
Requires:      mingw32-sip >= 6.0.0
%description -n mingw32-python3-%{pkg_name}
MinGW Python 3 %{pkg_name}.

%package -n mingw64-python3-%{pkg_name}
Summary:       MinGW Python 3 %{pkg_name}
Requires:      mingw64-sip >= 6.0.0
%description -n mingw64-python3-%{pkg_name}
MinGW Python 3 %{pkg_name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyqt_builder-%{version}
# Set version (see pyqt_builder_nosetuptoolsscm.patch)
sed -i 's|@version@|%version|' pyproject.toml
# Remove bundled egg-info
rm -rf PyQt_builder.egg-info
# Delete precompiled dlls
rm -rf pyqtbuild/bundle/dlls/

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-PyQt-builder -f %{oreon_filedir}/mingw32-python3-PyQt-builder.list
%files -n mingw64-python3-PyQt-builder -f %{oreon_filedir}/mingw64-python3-PyQt-builder.list

%changelog

%autochangelog
