%global source0_hash 85c2ab396cd9f514b20882fb2c68a102b892417a8de50a38610d0d0411e338f6

Summary:       A graphical interface for modifying the system language
Name:          system-config-language
Version:       3.5.1
Release:       2%{?dist}
URL:           https://pagure.io/system-config-language
Source0:       https://pagure.io/releases/%{name}/%{name}-%{version}.tar.xz
License:       GPL-2.0-or-later
Patch0:        %{name}-3.5.1-fallback-to-old-dnf-version.patch

BuildArch:     noarch
BuildRequires: make
BuildRequires: gcc
BuildRequires: desktop-file-utils
BuildRequires: gettext

# Requires both python lib and 'dnf' command directly, so express both
Requires:      python3-dnf
Requires:      polkit
Requires:      hicolor-icon-theme
Requires:      python3-gobject

# Need this for text execution
Requires:      python3-newt

%description
system-config-language is a graphical user interface that 
allows the user to change the default language of the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i '83ikk_KZ.UTF-8 utf8 latarcyrheb-sun16 Kazakh' src/locale-list

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

desktop-file-install --vendor system --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
  --add-category System \
  --add-category Settings \
  --add-category X-Red-Hat-Base                             \
  %{buildroot}%{_datadir}/applications/system-config-language.desktop

%find_lang %name

%files -f %{name}.lang
%license COPYING
%doc NEWS ChangeLog
%{_bindir}/system-config-language
%{_datadir}/system-config-language
%{_datadir}/applications/system-config-language.desktop
%{_datadir}/icons/hicolor/48x48/apps/system-config-language.png
%{_mandir}/man1/system-config-language.1.gz
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/polkit-1/actions/org.fedoraproject.config.language.policy

%changelog
%autochangelog
