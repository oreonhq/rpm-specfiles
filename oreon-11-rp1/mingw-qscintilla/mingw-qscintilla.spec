%global source0_hash dfe13c6acc9d85dfcba76ccc8061e71a223957a6c02f3c343b30a9d43a4cdd4d

%{?mingw_package_header}

%global pkgname qscintilla
%global scintilla_ver 3.5.4

Name:          mingw-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Version:       2.14.1
Release:       9%{?dist}
BuildArch:     noarch

License:       GPL-3.0-only
Url:           http://www.riverbankcomputing.com/software/qscintilla/
Source0:       https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_src-%{version}.tar.gz

BuildRequires: make

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-python3
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qtscript
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-python3-PyQt-builder
BuildRequires: mingw32-python3-qt5
BuildRequires: mingw32-sip

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-python3
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qtscript
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-python3-PyQt-builder
BuildRequires: mingw64-python3-qt5
BuildRequires: mingw64-sip

Provides: bundled(scintilla) = %{scintilla_ver}

%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 library

%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 library.

%package -n mingw32-python3-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 Python 3 bindings
Requires:      mingw32-%{pkgname}-qt5 = %{version}-%{release}
Requires:      mingw32-python3-qt5

%description -n mingw32-python3-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 Python 3 bindings.

%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 library

%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 library.

%package -n mingw64-python3-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 Python 3 bindings
Requires:      mingw64-%{pkgname}-qt5 = %{version}-%{release}
Requires:      mingw64-python3-qt5

%description -n mingw64-python3-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 Python 3 bindings.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n QScintilla_src-%{version}

%build
pushd src
%mingw_qmake_qt5 ../qscintilla.pro
%mingw_make_build
popd

pushd Python
ln -s pyproject-qt5.toml pyproject.toml
mingw32-sip-build --build-dir=build_win32 --no-make --qmake=%{_bindir}/mingw32-qmake-qt5 --verbose \
    --qsci-include-dir=../src --qsci-library-dir=../src/build_win32/release --qsci-features-dir=../src/features
mingw64-sip-build --build-dir=build_win64 --no-make --qmake=%{_bindir}/mingw64-qmake-qt5 --verbose \
    --qsci-include-dir=../src --qsci-library-dir=../src/build_win64/release --qsci-features-dir=../src/features
%mingw_make_build
popd

%install
pushd src
%mingw_make_install INSTALL_ROOT=%{buildroot}
popd
pushd Python
%mingw_make_install INSTALL_ROOT=%{buildroot}
popd

%find_lang qscintilla --with-qt
grep "%{mingw32_datadir}/qt5/translations" qscintilla.lang > mingw32-qscintilla-qt5.lang
grep "%{mingw64_datadir}/qt5/translations" qscintilla.lang > mingw64-qscintilla-qt5.lang

# Fix library names and installation folders
mkdir -p %{buildroot}%{mingw32_bindir}
mkdir -p %{buildroot}%{mingw64_bindir}
mv %{buildroot}%{mingw32_libdir}/qscintilla2_qt5.dll %{buildroot}%{mingw32_bindir}/qscintilla2_qt5.dll
mv %{buildroot}%{mingw64_libdir}/qscintilla2_qt5.dll %{buildroot}%{mingw64_bindir}/qscintilla2_qt5.dll

%files -n mingw32-%{pkgname}-qt5 -f mingw32-qscintilla-qt5.lang
%license LICENSE
%{mingw32_bindir}/qscintilla2_qt5.dll
%{mingw32_libdir}/libqscintilla2_qt5.dll.a
%{mingw32_includedir}/qt5/Qsci/
%{mingw32_datadir}/qt5/mkspecs/features/qscintilla2.prf

%files -n mingw32-python3-%{pkgname}-qt5
%{mingw32_python3_sitearch}/PyQt5/bindings/Qsci/
%{mingw32_python3_sitearch}/PyQt5/Qsci.pyd
%{mingw32_python3_sitearch}/qscintilla-%{version}.dist-info/
%{mingw32_datadir}/qt5/qsci/

%files -n mingw64-%{pkgname}-qt5 -f mingw64-qscintilla-qt5.lang
%license LICENSE
%{mingw64_bindir}/qscintilla2_qt5.dll
%{mingw64_libdir}/libqscintilla2_qt5.dll.a
%{mingw64_includedir}/qt5/Qsci/
%{mingw64_datadir}/qt5/mkspecs/features/qscintilla2.prf

%files -n mingw64-python3-%{pkgname}-qt5
%{mingw64_python3_sitearch}/PyQt5/bindings/Qsci/
%{mingw64_python3_sitearch}/PyQt5/Qsci.pyd
%{mingw64_python3_sitearch}/qscintilla-%{version}.dist-info/
%{mingw64_datadir}/qt5/qsci/

%changelog
%autochangelog
