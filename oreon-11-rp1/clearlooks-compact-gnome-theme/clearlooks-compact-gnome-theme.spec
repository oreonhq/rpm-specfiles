%global source0_hash 7886129ae74ad1ecd1b5b8f1a864181baa9b724eb242228ff1895672a71635c2

Name:           clearlooks-compact-gnome-theme
Version:        1.5
Release:        34%{?dist}
Summary:        GNOME Desktop theme optimized for small displays

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://martin.ankerl.com/2007/11/04/clearlooks-compact-gnome-theme/
Source0:        http://martin.ankerl.com/files/ClearlooksCompact-%{version}.tar.bz2
BuildArch:      noarch

Requires:       gtk2-engines
# Just for convenience
Provides:       clearlooks-compact = %{version}-%{release}

%description
Compact version of Clearlooks theme, especially great on small screens like
the Eee PC, or for intense applications like Eclipse.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
# Backup file, apparently forgotten there by upstream
rm Clearlooks\ Compact/gtk-2.0/gtkrc~

%build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/themes
cp -ap Clearlooks\ Compact $RPM_BUILD_ROOT%{_datadir}/themes/
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/Clearlooks\ Compact/COPYING

%files
%{_datadir}/themes/*
# This only works with rpm >= 4.11
%doc "Clearlooks Compact/COPYING"

%changelog
%autochangelog
