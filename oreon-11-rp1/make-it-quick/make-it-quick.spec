%global source0_hash dd7181afe8f9babc68c85e852ef0909445b62840f27ba41deff36a159b3cc372

Name:           make-it-quick
Version:        0.3.3
Release:        1%{?dist}
Summary:        A make-only build system for C/C++ programs
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/tao-3D/%{name}
Source:         https://github.com/tao-3D/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  make >= 3.82
BuildRequires:  gcc >= 4.8
BuildRequires:  gcc-c++ >= 4.8
Requires:       sed
Requires:       make >= 3.82
BuildArch:      noarch

%description
A simple make-only build system with basic auto-configuration that
can be used to rapidly build C and C++ programs.

%package devel
Summary:        Development files for make-it-quick
%description devel
Development files for make-it-quick

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build COLORIZE= TARGET=release DESTDIR=%{buildroot}

%check
%make_build COLORIZE= TARGET=release check DESTDIR=%{buildroot}

%install
%make_install COLORIZE= TARGET=release PREFIX.license=/usr/share/licenses/ DESTDIR=%{buildroot}

%files
%doc README.md
%doc AUTHORS
%doc NEWS
%license COPYING

%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.mk

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/config
%{_datadir}/%{name}/config/*.c

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
