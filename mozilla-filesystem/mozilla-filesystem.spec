Name:           mozilla-filesystem
Version:        1.9
Release:        38%{?dist}
Summary:        Mozilla filesytem layout
License:        MPL-1.1

# Firefox/Thunderbird moved to XDG dirs (mzbz#259356)
Conflicts:      firefox < 147.0
Conflicts:      thunderbird < 147.0

%description
This package provides some directories required by packages which use
Mozilla technologies such as native messaging extensions.

%prep

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/{lib,%{_lib}}/mozilla/{plugins,extensions,native-messaging-hosts}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mozilla/extensions
mkdir -p $RPM_BUILD_ROOT/etc/skel/.config/mozilla/{plugins,extensions}

%files
/usr/lib*/mozilla
%{_datadir}/mozilla
/etc/skel/.config/mozilla

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9-38
- Prepare for Oreon 11 (RP1)
