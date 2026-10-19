%global source0_hash 4681d0561bf96599bf9bf5eb25103d07ee8f045f31576dc2e72b8529587a67c6
%define git g4717841
Name:	 qtchooser
Summary:        Wrapper to select between Qt development binary versions
Version: 39
Release:        35%{?dist}
License: LicenseRef-Callaway-LGPLv2 OR GPL-3.0-only
URL:	 http://macieira.org/qtchooser
Source0:        http://macieira.org/%{name}/%{name}-%{version}-%{git}.tar.gz
Recommends: qt5-assistant
Recommends: qt5-designer
Recommends: qt5-linguist
Recommends: qt5-qdbusviewer
Recommends: qt5-qtbase-devel
Recommends: qt5-qtdeclarative-devel
Recommends: qt5-qtquick1-devel
Recommends: qt5-qttools
Recommends: qt5-qtxmlpatterns-devel
SOURCE10: qtchooser.sh
SOURCE11: qtchooser.csh
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
# /oreon:deps
%description
Qt Chooser provides a wrapper to switch between versions of Qt development
binaries when multiple versions like 4 and 5 are installed or local Qt builds
are to be used.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n qtchooser-%{version}-%{git}

%build

%make_build \
  %{?optflags:CXXFLAGS="%{optflags}"} \
  %{?__global_ldflags:LFLAGS="%{__global_ldflags}"}
%install
make install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}/etc/xdg/qtchooser
install -D -p -m 0644 doc/qtchooser.1 %{buildroot}%{_mandir}/man1/qtchooser.1
mkdir -p %{buildroot}%{_prefix}/lib/qtchooser
mv %{buildroot}%{_bindir}/* %{buildroot}%{_prefix}/lib/qtchooser/
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m644 -p %{SOURCE10} %{SOURCE11} \
  %{buildroot}%{_sysconfdir}/profile.d/
%oreon_autofiles main

%check

PATH="%{_qt5_bindir}:$PATH" ; export PATH
make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
