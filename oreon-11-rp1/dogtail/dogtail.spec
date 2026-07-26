%global source0_hash 801a15b183916df5adadd50338e82f76426b5b598477d2dc5e2258b1ce47236b

Summary: GUI test tool and automation framework
Name: dogtail
Version: 0.9.11
Release: 30%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://gitlab.com/dogtail/dogtail/
Source0: https://gitlab.com/dogtail/dogtail/raw/released/%{name}-%{version}.tar.gz
BuildArch: noarch

%global _description\
GUI test tool and automation framework that uses assistive technologies to\
communicate with desktop applications.

%description %_description

%package -n python3-dogtail
Summary: GUI test tool and automation framework - python3 installation
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3-pyatspi
Requires: python3-gobject
Requires: python3-cairo
Requires: xorg-x11-xinit
Requires: hicolor-icon-theme

%description -n python3-dogtail
GUI test tool and automation framework that uses assistive technologies to
communicate with desktop applications.

%package -n python3-dogtail-scripts
Summary: Sniff and other scripts for use with Dogtail framework
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: desktop-file-utils
Requires: python3-pyatspi
Requires: python3-gobject
Requires: python3-cairo
Requires: xorg-x11-xinit
Requires: hicolor-icon-theme
Requires: python3-dogtail >= 0.9.11

%description -n python3-dogtail-scripts
GUI test tool and automation framework that uses assistive technologies to
communicate with desktop applications. This subpackage contains Sniff,
the a11y exploration tool as well dogtail-run-headless scripts to start
session to run tests in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%{__python3} setup.py build

%install
%{__python3} ./setup.py install -O2 --root=$RPM_BUILD_ROOT --record=%{name}.files
rm -rf $RPM_BUILD_ROOT/%{_docdir}/dogtail
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

find examples -type f -exec chmod 0644 \{\} \;
desktop-file-install $RPM_BUILD_ROOT/%{_datadir}/applications/sniff.desktop \
  --dir=$RPM_BUILD_ROOT/%{_datadir}/applications \

%files -n python3-dogtail
%{python3_sitelib}/dogtail/
%{_datadir}/dogtail/
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%doc COPYING
%doc README
%doc NEWS

%files -n python3-dogtail-scripts
%{_bindir}/*
%{_datadir}/applications/*
%doc COPYING
%doc README
%doc NEWS

%changelog
%autochangelog
