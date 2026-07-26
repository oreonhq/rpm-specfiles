%global source0_hash 201bb83fe8fa09a271c4abc9f0c174effb0c59d0de7c84153847008535d5bedb

#global commit c54d99563414cd178abec7cf7d9663eb949a0f51
#global shortcommit %(c=%{commit}; echo ${c:0:7})

# Update to submodule revision as in https://github.com/apitrace/apitrace/tree/master/thirdparty when updating
%global libbacktrace_commit 8602fda64e78f1f46563220f2ee9f7e70819c51d
%global libbacktrace_shortcommit %(c=%{libbacktrace_commit}; echo ${c:0:7})

Name:           apitrace
Version:        13.0
Release:        6%{?commit:.git%{shortcommit}}%{?dist}
Summary:        Tools for tracing OpenGL

License:        MIT
URL:            http://apitrace.github.io/
%if 0%{?commit:1}
# git clone --recursive https://github.com/apitrace/apitrace.git
# cd apitrace
# git archive --prefix=apitrace-$commit/ -o ../apitrace-${commit:0:7}.tar $commit
# git submodule foreach --recursive "git archive --prefix=apitrace-$commit/\$path/ --output=\$sha1.tar HEAD && tar --concatenate --file=$(pwd)/../apitrace-${commit:0:7}.tar \$sha1.tar && rm \$sha1.tar"
# cd ..
# gzip apitrace-${commit:0:7}.tar
Source0:        apitrace-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/apitrace/apitrace/archive/%{version}/apitrace-%{version}.tar.gz
%endif
Source1:        https://github.com/ianlancetaylor/libbacktrace/archive/%{libbacktrace_commit}/libbacktrace-%{libbacktrace_shortcommit}.tar.gz
Source2:        qapitrace.desktop
Source3:        qapitrace.appdata.xml

# Don't require third-party submodules
Patch0:         apitrace_nosubmodules.patch
# Fix build with gcc15
Patch1:         apitrace-gcc15.patch
# Raise minimum cmake version, use GNUInstallDirs
Patch2:         https://github.com/apitrace/apitrace/commit/6f8527625ad5cf636e04a65b035228da96d7e228.patch

BuildRequires:  brotli-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libappstream-glib
BuildRequires:  libdwarf-devel
BuildRequires:  libpng-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  snappy-devel
BuildRequires:  python3-devel

Requires:       %{name}-libs%{_isa} = %{version}-%{release}
# scripts/snapdiff.py
Requires:       python3-pillow

# See http://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides:       bundled(md5-plumb)
# See https://fedorahosted.org/fpc/ticket/429
Provides:       bundled(libbacktrace)
# Modofied http://create.stephan-brumme.com/crc32/, see thirdparty/crc32c/README.md
Provides:       bundled(crc32c)

%description
apitrace consists of a set of tools to:
 * trace OpenGL and OpenGL ES  APIs calls to a file;
 * replay OpenGL and OpenGL ES calls from a file
 * inspect OpenGL state at any call while retracing
 * visualize and edit trace files

%package libs
Summary:        Libraries used by apitrace
Requires:       %{name} = %{version}-%{release}

%description libs
Libraries used by apitrace

%package gui
Summary:        Graphical frontend for apitrace
Requires:       %{name}%{_isa} = %{version}-%{release}

%description gui
This package contains qapitrace, the Graphical frontend for apitrace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit} -a1
%else
%autosetup -p1 -n %{name}-%{version} -a1
%endif

# Remove bundled libraries, except khronos headers
rm -rf `ls -1d thirdparty/* | grep -Ev "(khronos|md5|crc32c|libbacktrace.cmake|support|CMakeLists.txt)"`

# Add bundled libbacktrace
mv libbacktrace-%{libbacktrace_commit} thirdparty/libbacktrace

%build
%cmake -DENABLE_STATIC_SNAPPY=OFF -DENABLE_QT6=ON -DSCRIPTS_INSTALL_DIR=%{_libdir}/%{name}/scripts
%cmake_build

%install
%cmake_install

# Install doc through %%doc
rm -rf %{buildroot}%{_docdir}/

# Install desktop file and icon
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE2}
install -Dpm 0644 gui/resources/qapitrace.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qapitrace.png

# Install appdata file
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_datadir}/appdata/qapitrace.appdata.xml
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/qapitrace.appdata.xml

# highlight.py is not a script
chmod 0644 %{buildroot}%{_libdir}/%{name}/scripts/highlight.py

%check
%ctest

%files
%license LICENSE
%doc README.markdown docs/*
%{_bindir}/apitrace
%{_bindir}/eglretrace
%{_bindir}/glretrace
%{_bindir}/gltrim

%files libs
%{_libdir}/%{name}/

%files gui
%{_bindir}/qapitrace
%{_datadir}/applications/qapitrace.desktop
%{_datadir}/appdata/qapitrace.appdata.xml
%{_datadir}/icons/hicolor/128x128/apps/qapitrace.png

%changelog
%autochangelog
