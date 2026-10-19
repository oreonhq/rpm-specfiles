%global source0_hash f4017afb359e7c91824bd32b06a96426db88498dc43edfd5fe041599b2a30f19
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
Name:           texworks
Version:        0.6.11
Release:        1%{?dist}
Summary:        A simple IDE for authoring TeX documents
License:        GPL-2.0-or-later
URL:            https://tug.org/texworks/
Source0:        https://github.com/TeXworks/texworks/archive/release-%{version}/texworks-release-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  libappstream-glib
BuildRequires:  lua-devel
BuildRequires:  ninja-build
BuildRequires:  poppler-qt6-devel
BuildRequires:  python3-devel
BuildRequires:  urw-base35-fonts
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  zlib-devel
# /oreon:deps
%description
TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc) documents,
with a Unicode-based, TeX-aware editor, integrated PDF viewer, and a clean,
simple interface accessible to casual and non-technical users.

TeXworks is inspired by Dick Koch's award-winning TeXShop program for macOS,
which has made quality typesetting through TeX accessible to a wider community
of users, without a technical or intimidating face. The goal of TeXworks is to
deliver a similarly integrated, easy-to-use environment for users on all
platforms, especially GNU/Linux and Windows.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-release-%{version}
%oreon_prep
%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DWITH_PYTHON=ON \
    -DTW_BUILD_ID=Fedora \
    -DTeXworks_DIC_DIR=%{_datadir}/hunspell \
    -DTeXworks_PLUGIN_DIR=%{_libdir}/texworks \
    -DQT_DEFAULT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_docdir}/%{name}/COPYING
%oreon_autofiles main

%check

%ifarch s390x
xvfb-run -a bash -c "%ctest -E test_poppler-qt6"
%else
xvfb-run -a bash -c "%ctest"
%endif
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
