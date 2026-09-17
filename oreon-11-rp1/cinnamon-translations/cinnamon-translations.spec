%global source0_hash 0350945058c19c588148090657135cef4bb248069c881bc336c9fb373945f934

%global _trans_version 2018.12.11

Name:           cinnamon-translations
Version:        6.6.2
Release:        3%{?dist}
Summary:        Translations for Cinnamon and Nemo

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%{_trans_version}.tar.xz
BuildRequires:  gettext
BuildRequires:  make

BuildArch:      noarch

%description
Translations for Cinnamon, Nemo and Mintlocale.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -a 1 -p 1

%build
%{make_build}
%{make_build} -C mint-translations

%install
# install mint translations for mintlocale
%{_bindir}/find mint-translations -not -name 'mintlocale.mo' -type f -delete
%{_bindir}/find . -name 'cinnamon-bluetooth.mo' -type f -delete
%{__cp} -pr mint-translations/%{_datadir}/linuxmint/locale .%{_datadir}
%{__cp} -pr .%{_prefix} %{buildroot}

%find_lang cinnamon
%find_lang mintlocale
%find_lang nemo
%find_lang nemo-extensions
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-settings-daemon

%files -f cinnamon.lang -f mintlocale.lang -f nemo.lang -f nemo-extensions.lang -f cinnamon-control-center.lang -f cinnamon-screensaver.lang -f cinnamon-session.lang -f cinnamon-settings-daemon.lang
%license COPYING

%changelog
%autochangelog
