%global source0_hash 39fca8c8a6a95fd76419ace3ec5f0b7876044abc78b979c2632ab73b2da50b58

%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$

Name: qt-jdenticon
Version: 0.3.1
Release: %autorelease

License: MIT
Summary: Jdenticon Qt5 plugin
URL: https://github.com/Nheko-Reborn/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: qt6-qtbase-devel

%description
Special Qt/C++14 port of Jdenticon distributed as a Qt plugin.

The eventual plan for this is that it will be made into a Qt library that can
be used in other applications with a command-line application for use as a
standalone generator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%qmake_qt6 QtIdenticon.pro
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%if 0%{?flatpak}
# qtbase is part of runtime in /usr, this is built in /app
mv %{buildroot}/usr %{buildroot}/app
%endif

%files
%doc README.md
%license LICENSE
%{_qt6_plugindir}/libqtjdenticon.so

%changelog
%autochangelog
