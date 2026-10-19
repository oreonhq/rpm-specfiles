%global source0_hash 2c5a5de6813566aeec9449be61e1a8cd8ef85979a9e234d420f2882efcfde382
%bcond_without  tests
%undefine       _cmake_shared_libs
%global test_compositor cage
Name:           neovim-qt
Version:        0.2.19
Release:        3%{?dist}
Summary:        Qt GUI for Neovim
License:        ISC AND HPND-Markus-Kuhn
URL:            https://github.com/equalsraf/neovim-qt
Source0:        https://github.com/equalsraf/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with tests}
%endif
Requires:       hicolor-icon-theme
Requires:       neovim
# oreon:deps
BuildRequires:  cage
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(msgpack)
BuildRequires:  desktop-file-utils
BuildRequires:  font(dejavusansmono)
BuildRequires:  gcc-c++
BuildRequires:  neovim
BuildRequires:  xwfb-run
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -DWITH_QT:STRING=Qt6 \
    -DUSE_SYSTEM_MSGPACK:BOOL=ON  \
    -DENABLE_TESTS:BOOL=%{?with_tests:ON}%{!?with_tests:OFF}
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/nvim-qt.desktop
%if %{with tests}
%global __ctest xwfb-run -c %{test_compositor} -- %{__ctest}
%ctest
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
