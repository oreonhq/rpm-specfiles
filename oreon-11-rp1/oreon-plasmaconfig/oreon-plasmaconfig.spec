%global source0_hash none

Name:           oreon-plasmaconfig
Version:        11
Release:        1%{?dist}
Summary:        Oreon Plasma look-and-feel package

License:        GPLv2+
URL:            https://oreonproject.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        kdeglobals
BuildArch:      noarch

Requires:       plasma-workspace

%description
Oreon look-and-feel package for KDE Plasma.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel
cp -a org.oreonproject.oreon.desktop %{buildroot}%{_datadir}/plasma/look-and-feel/
install -D -m 0644 kdeglobals %{buildroot}%{_sysconfdir}/xdg/kdeglobals

%files
%{_datadir}/plasma/look-and-feel/org.oreonproject.oreon.desktop
%config(noreplace) %{_sysconfdir}/xdg/kdeglobals

%changelog
* Wed Feb 04 2026 Brandon Lester <blester@oreonhq.com> - 11-1
- Initial package
