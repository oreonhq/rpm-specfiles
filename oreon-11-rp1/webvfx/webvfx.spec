%global source0_hash ac75600222b46aa880632d569dce800e30f5a790a79cc3614a726dd7416334de

Name:           webvfx
Version:        1.2.0
Release:        16%{?dist}
Summary:        Video effects engine based on web technologies
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mltframework/webvfx
Source0:        https://github.com/mltframework/webvfx/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-libdir.patch

BuildRequires: make
#BuildRequires:  mlt-devel >= 6.20.0
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  doxygen
BuildRequires:  chrpath

%description
WebVfx is a video effects library that allows effects to be implemented using
WebKit HTML or Qt QML.

%package        devel
Summary:        Development library for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
Development library for %{name}

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} PREFIX=%{_prefix} LIB_SUFFIX=%{_lib} \
..
%make_build
popd

# update Doxyfile
doxygen -u doc/Doxyfile
# build docs
doxygen doc/Doxyfile

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/%{name}_viewer
chrpath --delete %{buildroot}%{_bindir}/%{name}_render
#chrpath --delete %{buildroot}%{_libdir}/mlt/libmltwebvfx.so

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE
%{_bindir}/webvfx_*
#%%{_libdir}/mlt/libmltwebvfx.so
%{_libdir}/libwebvfx.so.*

%files devel
%{_libdir}/libwebvfx.so

%files doc
%license LICENSE
%doc doxydoc

%changelog
%autochangelog
