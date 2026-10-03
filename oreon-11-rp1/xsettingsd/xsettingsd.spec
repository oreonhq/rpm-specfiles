%global source0_hash 69b5d1987608d1b5f2a0085f2f88cc55936a99b92279118e655d665ebb5e50d3

Name:           xsettingsd
Version:        1.0.2
Release:        13%{?dist}
Summary:        Provides settings to X11 clients via the XSETTINGS specification

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/derat/xsettingsd

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libX11-devel
BuildRequires:  systemd-rpm-macros

%description
xsettingsd is a daemon that implements the XSETTINGS specification.

It is intended to be small, fast, and minimally dependent on other libraries.
It can serve as an alternative to gnome-settings-daemon for users who are not
using the GNOME desktop environment but who still run GTK+ applications and
want to configure things such as themes, font anti-aliasing/hinting, and UI
sound effects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/dump_xsettings
%{_bindir}/xsettingsd
%{_mandir}/man1/dump_xsettings.1*
%{_mandir}/man1/xsettingsd.1*
%{_userunitdir}/xsettingsd.service

%changelog
%autochangelog
