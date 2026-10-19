%global source0_hash 9e7800f500eb9ac89b7e3d503cb499fd01eaa45c8b547417ff1a36ada5a7d48c
%bcond_without  nm_icons
Name:           mint-x-icons
Version:        1.7.7
Release:        1%{?dist}
Summary:        Icon theme for Linux Mint
License:        GPL-3.0-or-later
URL:            http://linuxmint.com
Source0:        http://packages.linuxmint.com/pool/main/m/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch
Requires:       filesystem
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  fdupes
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with nm_icons}
%{_bindir}/find %{name}%{_prefix} -name "nm-*" -type f -delete
%{_bindir}/find %{name}%{_prefix} -name "nm-*" -xtype l			\
  -exec %{_bindir}/unlink {} \;
%{_bindir}/find %{name}%{_prefix} -name 'gnome-netstatus*' -xtype l	\
  -exec %{__file} {} \; | %{__grep} 'broken' |			\
  %{__sed} -e 's!:[ \t]\+.*$!!g' |				\
  %{_bindir}/xargs --max-args=1 %{_bindir}/unlink
%endif
%install
%{__cp} -pr %{name}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}
%transfiletriggerin -- %{_datadir}/icons/Mint-X
for _dir in %{_datadir}/icons/Mint-X*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done
%transfiletriggerpostun -- %{_datadir}/icons/Mint-X
for _dir in %{_datadir}/icons/Mint-X*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
