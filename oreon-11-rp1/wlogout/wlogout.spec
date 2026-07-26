%global source0_hash 4c9204bfa19c73f51176c94c67711f54f3e393301c0809c61ae379054060fa46

# -*-Mode: rpm-spec -*-

Name: wlogout
Version: 1.2.2
Release: 5%{?dist}
Summary: Wayland based logout menu
License: MIT
URL:     https://github.com/ArtsyMacaw/wlogout
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: gnupg2

%description
A wayland based logout menu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/zsh/
%{_datadir}/fish/
%{_datadir}/bash-completion/
%dir %{_sysconfdir}/%{name}

%license LICENSE

%doc README.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}.5.*

%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
%autochangelog
