%global source0_hash 97f5ba6d74eab23ef47823c4f1bff6c607cee9a92ab605411b77ff4703474370

%global commit 94677dc52fe1c2ea6fe42bd5acdbddab755eeb0b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner croscato

Name:           QMsgBox
Version:        0
Release:        32.20130830git%{shortcommit}%{?dist}
Summary:        Solves a problem that prevents qt message icons from being displayed
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.qtcentre.org/wiki/index.php?title=QMsgBox_%28Solves_the_QMessageBox_icon_problem%29
Source0:        https://github.com/croscato/QMsgBox/tarball/%{commit}/%{owner}-%{name}-%{shortcommit}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel

%description
QMsgBox is a class that inherits QMessageBox to replace the static
functions:
* QMessageBox::warning
* QMessageBox::information
* QMessageBox::critical
* QMessageBox::question 

All other functions remain the same. The usage of the replaced
function also remains the same.

The objective of this class is to solve a problem that prevents the
message icon from being displayed in some platforms with some Qt
styles.

%package devel
Summary:        Development libraries for QMsgBox
Provides:       %{name}(devel) =  %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-headers = %{version}-%{release}

%description devel
This package contains the development libraries necessary
for compiling code against QMsgBox.

%package headers
Summary:        Development headers for QMsgBox
Requires:       %{name}(devel) = %{version}-%{release}
BuildArch:      noarch

%description headers
This package contains the development headers necessary
for compiling code against QMsgBox.

%package        qt5
Summary:        Qt5 version of %{name}
Requires:       qt5-qtbase%{?_isa}

%description    qt5
QMsgBox is a class that inherits QMessageBox to replace the static
functions:
* QMessageBox::warning
* QMessageBox::information
* QMessageBox::critical
* QMessageBox::question 

All other functions remain the same. The usage of the replaced
function also remains the same.

The objective of this class is to solve a problem that prevents the
message icon from being displayed in some platforms with some Qt
styles.

%package        qt5-devel
Summary:        Development files for %{name} using Qt5
Provides:       %{name}(devel) =  %{version}-%{release}
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       %{name}-headers = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    qt5-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} and Qt5.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{owner}-%{name}-%{shortcommit}
# Plug in correct install path
sed -i "s|target.path = .*|target.path = %{buildroot}%{_libdir}|g" src/src.pro
# Fix EOL encoding
for f in LICENSE.GPL3; do
    sed 's|\r||g' $f > $f.new && \
        touch -r $f $f.new && \
        mv $f.new $f
done
# Fix file permissions
find . -type f -exec chmod 644 {} \;

# Create Qt5 dir
rm -rf ../%{owner}-%{name}-%{shortcommit}-qt5
cp -a ../%{owner}-%{name}-%{shortcommit} ../%{owner}-%{name}-%{shortcommit}-qt5
sed -i -e 's/TARGET = QMsgBox/TARGET = QMsgBox-qt5/' ../%{owner}-%{name}-%{shortcommit}-qt5/src/src.pro

%build
%{qmake_qt4}
make %{?_smp_mflags}

cd ../%{owner}-%{name}-%{shortcommit}-qt5
%{qmake_qt5}
make %{?_smp_mflags}

%install
make install
make -C ../%{owner}-%{name}-%{shortcommit}-qt5 install

# Install header file
install -D -p -m 644 src/qmsgbox.h %{buildroot}%{_includedir}/qmsgbox.h
# and symlink
ln -s %{_includedir}/qmsgbox.h %{buildroot}%{_includedir}/QMsgBox.h

%ldconfig_scriptlets

%files
%doc LICENSE.GPL3
%{_libdir}/libQMsgBox.so.*

%files devel
%{_libdir}/libQMsgBox.so

%files headers
%{_includedir}/QMsgBox.h
%{_includedir}/qmsgbox.h

%files qt5
%doc LICENSE.GPL3
%{_libdir}/libQMsgBox-qt5.so.*

%files qt5-devel
%{_libdir}/libQMsgBox-qt5.so

%changelog
%autochangelog
