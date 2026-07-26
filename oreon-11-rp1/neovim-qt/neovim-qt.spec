%global source0_hash 2c5a5de6813566aeec9449be61e1a8cd8ef85979a9e234d420f2882efcfde382

%bcond_without  tests
# disable shared libraries to avoid building libneovim-qt-gui.so
# it's only needed for devel package which we're not providing
%undefine       _cmake_shared_libs

# Qt does not support QClipboard::Selection under Weston, causing tests to crash
%global test_compositor cage

Name:           neovim-qt
Version:        0.2.19
Release:        3%{?dist}
Summary:        Qt GUI for Neovim

# src/gui/shellwidget/konsole_wcwidth.cpp: HPND-Markus-Kuhn
# third_party/DejaVuSans*: Bitstream-Vera AND LicenseRef-Fedora-Public-Domain
License:        ISC AND HPND-Markus-Kuhn
URL:            https://github.com/equalsraf/neovim-qt
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(msgpack)
BuildRequires:  neovim
%if %{with tests}
BuildRequires:  font(dejavusansmono)
BuildRequires:  xwfb-run
BuildRequires:  %{test_compositor}
%endif

Requires:       hicolor-icon-theme
Requires:       neovim

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake \
    -DWITH_QT:STRING=Qt6 \
    -DUSE_SYSTEM_MSGPACK:BOOL=ON  \
    -DENABLE_TESTS:BOOL=%{?with_tests:ON}%{!?with_tests:OFF}
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/nvim-qt.desktop
%if %{with tests}
# UI component tests require running display server
%global __ctest xwfb-run -c %{test_compositor} -- %{__ctest}
%ctest
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/nvim-qt
%{_datadir}/applications/nvim-qt.desktop
%{_datadir}/icons/hicolor/192x192/apps/nvim-qt.png
%{_datadir}/icons/hicolor/scalable/apps/nvim-qt.svg
%{_datadir}/nvim-qt/

%changelog
%autochangelog
