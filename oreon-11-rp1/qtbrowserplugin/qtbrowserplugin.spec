%global source0_hash dc3bc11d65844d19119eec2d8d2b48e7a067a320588e0a63882f577ac39cefb5

%global commit 80592b0e7145fb876ea0e84a6e3dadfd5f7481b6

Name:           qtbrowserplugin
Version:        2.4
Release:        30%{?dist}
Summary:        Qt Solutions Component: Browser Plugin

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://qt.gitorious.org/qt-solutions/qt-solutions
# git archive --prefix=qtbrowserplugin-2.4/ 80592b0e7145fb876ea0e84a6e3dadfd5f7481b6:qtbrowserplugin/ | gzip > ../qtbrowserplugin-2.4-80592b0e7145fb876ea0e84a6e3dadfd5f7481b6.tar.gz
Source0:        qtbrowserplugin-%{version}-%{commit}.tar.gz
# Patch to build as a library
Patch0:         qtbrowserplugin-lib.patch

BuildRequires: make
BuildRequires:  qt-devel

# -debuginfo useless for (only) static libs
%global debug_package   %{nil}

%description
The QtBrowserPlugin solution is useful for implementing plugins
for web browser.

%package        devel
Summary:        Development files for %{name}
Requires:       qt-devel%{?_isa}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The QtBrowserPlugin solution is useful for implementing plugins
for web browser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .lib

%build
%{qmake_qt4}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}
cp -p libqtbrowserplugin.* %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cp -p src/*.h %{buildroot}%{_includedir}

%files devel
%doc doc examples README.TXT
%{_includedir}/*
%{_libdir}/lib%{name}.a

%changelog
%autochangelog
