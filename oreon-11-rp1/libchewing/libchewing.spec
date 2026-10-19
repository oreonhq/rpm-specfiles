%global source2_hash 5bb2f1a372c841621d2269ba4a3f5d9ddd3c2804523fdcf41ea65c4e9a65a63e
%global source1_hash 2e90858df5d385d5bdfc91e2ff03a093a388f70b91458a6dd5c2160f75f2cd0a
%global source0_hash c897a5d0aadfdeb07784e1411ceac0efef2c97bea8143fb3b1dcde8274e14fc0
%bcond check 0
%global libchewing_python_dir %{python3_sitelib}
%global im_name_zh_TW 新酷音輸入法
%global name_zh_TW %{im_name_zh_TW}函式庫
Name:           libchewing
Version:        0.13.1
Release:        1%{?dist}
Summary:        Intelligent phonetic input method library for Traditional Chinese
Summary(zh_TW): %{name_zh_TW}
License:        LGPL-2.1-or-later AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND MPL-2.0
URL:            https://chewing.im
Source0:        https://codeberg.org/chewing/%{name}/releases/download/v%{version}/libchewing-%{version}.tar.zst
Source1:        https://codeberg.org/chewing/%{name}/releases/download/v%{version}/libchewing-%{version}.tar.zst.asc
Source2:        https://chewing.im/.well-known/openpgpkey/hu/y84sdmnksfqswe7fxf5mzjg53tbdz8f5?l=release#/libchewing.pgp
Patch0:         0001-delete-sqlite-bundled-feature.patch
Patch1:         libchewing-0.13.1-clap_mangen0.13.patch
Obsoletes:      python2-libchewing < 0.5.1-13
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  cmake(Corrosion)
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  python3-devel
BuildRequires:  texinfo
# /oreon:deps
%description
libchewing is an intelligent phonetic input method library for Chinese.

It provides the core algorithm and logic that can be used by various
input methods. The Chewing input method is a smart bopomofo phonetics
input method that is useful for inputting Mandarin Chinese.

%description -l zh_TW
%{name_zh_TW}提供實做了核心選字演算法，以便輸入法程式調用。

%{im_name_zh_TW}是一種智慧型注音/拼音猜字輸入法，透過智慧型的字庫分析、習慣記錄學習與預測分析，
使拼字輸入的人為選字機率降至最低，進而提升中文輸入、打字的效率。

%package -n %{name}-devel
Summary:        Development files for libchewing
Summary(zh_TW): %{name_zh_TW}開發者套件
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n %{name}-devel
Headers and other files needed to develop applications using the %{name}
library.

%description -l zh_TW  -n %{name}-devel
%{name_zh_TW}開發者套件提供了開發%{im_name_zh_TW}相關程式所需的檔案，
像是標頭檔(header files)，以及函式庫。

%package -n python3-%{name}
Summary:        Python binding for libchewing
BuildArch:      noarch
Summary(zh_TW): %{name_zh_TW} python 綁定
Requires:       %{name} = %{version}-%{release}
%description -n python3-%{name}
Python binding of libchewing.

%description -l zh_TW -n python3-%{name}
%{name_zh_TW} python 綁定

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n libchewing-%{version}

%build

%cmake --preset default
%cmake_build
%{cargo_license_summary -f sqlite}
%{cargo_license -f sqlite} > LICENSE.dependencies
%install
%cmake_install
mkdir -p %{buildroot}%{libchewing_python_dir}
cp -p contrib/python/chewing.py %{buildroot}%{libchewing_python_dir}
rm -f %{buildroot}/%{_infodir}/dir
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%ctest -j1
%endif
%files -f %{oreon_filedir}/main.list
%files -n libchewing-devel -f %{oreon_filedir}/libchewing-devel.list
%files -n python3-libchewing -f %{oreon_filedir}/python3-libchewing.list

%changelog

%autochangelog
