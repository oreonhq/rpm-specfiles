%global source0_hash 4465e0deb891aa712cb48e72cfb971994f2270525cea6d9c3c6ef39c97476d9e

%global _mintlibdir %{_prefix}/lib/linuxmint/

Name:           mintlocale
Version:        1.4.7
Release:        21%{?dist}
Summary:        Language selection tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Revert https://github.com/linuxmint/mintlocale/commit/0206bbf7c12058999e701bb11f9012be54da2cbb
# Using non utf8 breaks gnome apps
Patch0:         show_utf8_only.patch
Patch1:         %{url}/pull/56.patch#/add_apt_checking.patch
Patch2:         %{url}/commit/7041982b69fa9fea065098e7b33f306df1dcac91.patch#/fix_signal_name.patch
Patch3:         fix_gdk_import.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils

Requires:       accountsservice
Requires:       %{name}-set-default-locale = %{version}-%{release}
Requires:       xapps

%description
Language selection tool for Cinnamon.

%package set-default-locale
Summary:        Language selection tool

%description set-default-locale
Language selection tool for Cinnamon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
echo 'nothing to build'

%install
%{__cp} -pr .%{_prefix} %{buildroot}
%{__rm} %{buildroot}%{_bindir}/add-remove-locales \
  %{buildroot}%{_datadir}/applications/%{name}-im.desktop \
  %{buildroot}%{_mintlibdir}/mintlocale/add.py \
  %{buildroot}%{_mintlibdir}/mintlocale/install_remove.py
%{__chmod} -c 0755 %{buildroot}%{_mintlibdir}/mintlocale/mintlocale.py

echo 'LANG=$locale' > %{buildroot}%{_datadir}/linuxmint/mintlocale/templates/default_locale.template

%{_bindir}/desktop-file-install \
  --add-only-show-in=X-Cinnamon \
  --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc debian/changelog
%license COPYING debian/copyright
%{_bindir}/%{name}
%{_mintlibdir}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/linuxmint
%{_datadir}/polkit-1/actions/com.linuxmint.mintlocale.policy

%files set-default-locale
%{_bindir}/set-default-locale

%changelog
%autochangelog
