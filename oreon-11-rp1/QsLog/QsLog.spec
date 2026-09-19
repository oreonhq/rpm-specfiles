%global source0_hash 705de180fcf9524712a93afb4156e5d8a77644a2874a4f550cc89d71112a4f24

%global commit 2959cec27825e53d1554a32668f1f7892ca351c7
%global medcommit %(c=%{commit}; echo ${c:0:12})
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           QsLog
Version:        0
Release:        33.%{shortcommit}git%{?dist}
Summary:        An easy to use logger that is based on Qt's QDebug class
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://bitbucket.org/razvanpetru/qslog

Source0:        https://bitbucket.org/razvanpetru/qslog/get/%{shortcommit}.tar.gz

# Don't install docs
Patch0:         QsLog-nodoc.patch
# Install libraries in correct directory
Patch1:         QsLog-libdir.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel

%description
QsLog is an easy to use logger that is based on Qt's QDebug class.
Features:
* Six logging levels (from trace to fatal)
* Logging level threshold configurable at runtime.
* Minimum overhead when logging is turned off.
* Supports multiple destinations, comes with file and debug destinations.
* Thread-safe
* Supports logging of common Qt types out of the box.
 
%package devel
Summary:         Development headers and library for QsLog
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and libraries necessary
for compiling against QsLog.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n razvanpetru-qslog-%{medcommit}
%patch -P0 -p1 -b .nodoc
%patch -P1 -p1 -b .libdir
# Prepare LICENSE
head -n 25 QsLog.cpp | sed "s|// ||g" > LICENSE
touch -r QsLog.cpp LICENSE

# Fix EOL encoding
for f in QsLog.h QsLogDestConsole.h QsLogLevel.h QsLogDest.h LICENSE; do
    sed 's|\r||g' $f > $f.new && \
    touch -r $f $f.new && \
    mv $f.new $f
done

%build
%qmake_qt4 QsLogSharedLibrary.pro
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%doc LICENSE QsLogReadme.txt
%{_libdir}/libQsLog.so.*

%files devel
%{_includedir}/QsLog/
%{_libdir}/libQsLog.so

%changelog
%autochangelog
