%global source0_hash 47114348fc005b505abf7db52f8574035b4af56157a2a2eb821dc8eabe0d2aec

Name:           anaconda-webui
Version:        86
Release:        1%{?dist}
Summary:        Anaconda installer Web interface
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/rhinstaller/%{name}

Source0:        https://github.com/rhinstaller/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  gettext
# Needed for the unitdir macro
BuildRequires: systemd-rpm-macros

%global anacondacorever 0

%if 0%{?fedora} > 41
%global anacondacorever 42.5
%endif

%global cockpitver 275

%define _unitdir /usr/lib/systemd/system

%if 0%{?rhel}
Recommends: cockpit-storaged
Recommends: cockpit-networkmanager
Recommends: cockpit-bridge >= %{cockpitver}
Recommends: cockpit-ws >= %{cockpitver}
Recommends: python3-bugzilla
%else
Requires: cockpit-storaged
Requires: cockpit-networkmanager
Requires: cockpit-bridge >= %{cockpitver}
Requires: cockpit-ws >= %{cockpitver}
Requires: python3-bugzilla
%endif
Requires: anaconda-core  >= %{anacondacorever}
# Firefox dependency needs to be specified there as cockpit web-view does not have a hard dependency on Firefox as
# it can often fall back to a diferent browser. This does not work in the limited installer
# environment, so we need to make sure Firefox is available. Exclude on RHEL, only Flatpak version will be there.
%if ! 0%{?rhel}
Requires: (firefox if fedora-release-workstation)
%endif
%if 0%{?fedora}
Requires: system-logos
%endif
BuildRequires: desktop-file-utils

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

%description
Anaconda installer Web interface

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install PREFIX=/usr

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/extlinks.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/anaconda-gnome-control-center.desktop

%check
exit 0
# We have some integration tests, but those require running a VM, so that would
# be an overkill for RPM check script.

%files
%dir %{_datadir}/cockpit/anaconda-webui
%doc README.rst
%license LICENSE dist/index.js.LEGAL.txt
%{_datadir}/cockpit/anaconda-webui/qr-code-feedback.svg
%{_datadir}/cockpit/anaconda-webui/index.js.LEGAL.txt
%{_datadir}/cockpit/anaconda-webui/index.html
%{_datadir}/cockpit/anaconda-webui/index.js.gz
%{_datadir}/cockpit/anaconda-webui/index.js.map
%{_datadir}/cockpit/anaconda-webui/index.css.gz
%{_datadir}/cockpit/anaconda-webui/index.css.map
%{_datadir}/cockpit/anaconda-webui/manifest.json
%{_datadir}/cockpit/anaconda-webui/po.*.js.gz
%{_datadir}/cockpit/anaconda-webui/VERSION.txt
%{_libexecdir}/anaconda/cockpit-coproc-wrapper.sh
%dir %{_datadir}/anaconda/firefox-theme
%dir %{_datadir}/anaconda/firefox-theme/default
%dir %{_datadir}/anaconda/firefox-theme/default/chrome
%{_datadir}/anaconda/firefox-theme/default/user.js
%{_datadir}/anaconda/firefox-theme/default/chrome/userChrome.css
%dir %{_datadir}/anaconda/firefox-theme/live
%dir %{_datadir}/anaconda/firefox-theme/live/chrome
%{_datadir}/anaconda/firefox-theme/live/user.js
%{_datadir}/anaconda/firefox-theme/live/chrome/userChrome.css
%dir %{_datadir}/anaconda/firefox-theme/extlink
%{_datadir}/anaconda/firefox-theme/extlink/user.js
%{_libexecdir}/anaconda/webui-desktop
%{_libexecdir}/anaconda/browser-ext
%{_libexecdir}/anaconda/gnome-control-center-ext
%{_datadir}/applications/extlinks.desktop
%{_datadir}/applications/anaconda-gnome-control-center.desktop
%{_unitdir}/webui-cockpit-ws.service


# The changelog is automatically generated and merged
%changelog
%autochangelog
