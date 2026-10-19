%global source0_hash 47114348fc005b505abf7db52f8574035b4af56157a2a2eb821dc8eabe0d2aec
Name:           anaconda-webui
Version:        86
Release:        1%{?dist}
Summary:        Anaconda installer Web interface
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/rhinstaller/%{name}
Source0:        https://github.com/rhinstaller/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
%global anacondacorever 0
%global cockpitver 275
%define _unitdir /usr/lib/systemd/system
Requires: cockpit-storaged
Requires: cockpit-networkmanager
Requires: cockpit-bridge >= %{cockpitver}
Requires: cockpit-ws >= %{cockpitver}
Requires: python3-bugzilla
Requires: anaconda-core  >= %{anacondacorever}
Provides: bundled(npm(@patternfly/patternfly)) = 6.4.0
Provides: bundled(npm(@patternfly/react-core)) = 6.4.1
Provides: bundled(npm(@patternfly/react-icons)) = 6.4.0
Provides: bundled(npm(@patternfly/react-log-viewer)) = 6.3.0
Provides: bundled(npm(@patternfly/react-styles)) = 6.4.0
Provides: bundled(npm(@patternfly/react-table)) = 6.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 6.4.0
Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(dequal)) = 2.0.3
Provides: bundled(npm(error-stack-parser)) = 2.1.4
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.23
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(luxon)) = 3.7.2
Provides: bundled(npm(memoize-one)) = 5.2.1
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(react-dropzone)) = 14.4.1
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(source-map)) = 0.5.6
Provides: bundled(npm(stack-generator)) = 2.0.10
Provides: bundled(npm(stackframe)) = 1.3.4
Provides: bundled(npm(stacktrace-gps)) = 3.1.2
Provides: bundled(npm(stacktrace-js)) = 2.0.2
Provides: bundled(npm(tabbable)) = 6.4.0
Provides: bundled(npm(throttle-debounce)) = 5.0.2
Provides: bundled(npm(tslib)) = 2.8.1
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Anaconda installer Web interface

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}

%build

%install
%make_install PREFIX=/usr
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/extlinks.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/anaconda-gnome-control-center.desktop
%oreon_autofiles main

%check

exit 0
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
