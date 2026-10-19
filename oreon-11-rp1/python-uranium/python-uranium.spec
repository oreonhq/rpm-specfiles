%global source0_hash 1c50ddb3469ad01e7edade548991699d0762b61523ce3d5564ae6f8a3763ef9a
Name:           python-uranium
Version:        5.13.0
Release:        1%{?dist}
Summary:        A Python framework for building desktop applications
License:        LGPL-3.0-or-later
URL:            https://github.com/Ultimaker/Uranium
Source0:        https://github.com/Ultimaker/Uranium/archive/%{version}.tar.gz#/Uranium-%{version}.tar.gz
Patch:          Uranium-5.3.0-qt-try-ints-then-bytes-for-gl-mask-functions.patch
Patch:          https://github.com/Ultimaker/Uranium/pull/885.patch#/Uranium-5.3.0-python3.12.patch
Patch:          Uranium-5.6.0-pytest8.patch
Patch:          https://github.com/Ultimaker/Uranium/pull/997.patch
Source2:        mod_bundled_packages_json.py
Source3:        UraniumPluginInstall.cmake
Source4:        UraniumTests.cmake
Source5:        UraniumTranslationTools.cmake
Source6:        CMakeLists.txt
Source7:        CPackConfig.cmake
Source8:        Doxyfile
BuildArch:      noarch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  (python3-zombie-imp if python3 >= 3.12)
BuildRequires:  /usr/bin/doxygen
BuildRequires:  /usr/bin/msgmerge
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  python3-arcus
BuildRequires:  python3-cryptography
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pip
BuildRequires:  python3-pyclipper
BuildRequires:  python3-pyqt6-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-scipy
BuildRequires:  python3-shapely
BuildRequires:  python3-twisted
# /oreon:deps
%description
Uranium is a Python framework for building 3D printing related applications.

%package -n python3-uranium
Summary:        A Python framework for building desktop applications
Provides:       uranium = %{version}-%{release}
Requires:       python3-arcus >= 5.3.0
Requires:       python3-cryptography
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-shapely
Requires:       python3-pyclipper
Requires:       python3-pyqt6
Requires:       (python3-zombie-imp if python3 >= 3.12)
Recommends:     python3-numpy-stl
%description -n python3-uranium
Uranium is a Python framework for building 3D printing related applications.

%package doc
Summary: Documentation for %{name} package
%description doc
Documentation for Uranium, a Python framework for building 3D printing
related applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Uranium-%{version} -p1 -S git

mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} cmake/
rm -rf CMakeLists.txt
cp -a %{SOURCE6} %{SOURCE7} %{SOURCE8} .

# fix compile-shaders
sed -i 's|qsb |qsb-qt6 |g' scripts/compile-shaders

%build

%cmake -DLIB_SUFFIX:STR=
%cmake_build
%cmake_build -- doc
%check

%{python3} -m pip freeze
%{python3} -m pytest -v -k "not (TestSettingFunction and test_init_bad) and not TestHttpRequestManager"
%install
%cmake_install
mv %{buildroot}%{_datadir}/cmake* %{buildroot}%{_datadir}/cmake
pushd %{buildroot}%{_datadir}
mv uranium/resources/i18n locale
ln -s ../../locale uranium/resources/i18n
rm locale/uranium.pot
rm locale/*/uranium.po
popd
%py_byte_compile %{python3} %{buildroot}%{_prefix}/lib/uranium
%find_lang uranium
%oreon_autofiles python3-uranium usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-uranium -f %{oreon_filedir}/python3-uranium.list
%files -n python-uranium-doc -f %{oreon_filedir}/python-uranium-doc.list

%changelog

%autochangelog
