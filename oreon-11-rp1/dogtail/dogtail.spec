%global source0_hash cc46bd4c05aed0210ba594e7a1d356c7fa50455d249dc919ef9ec5cd48af823d
Summary:        GUI test tool and automation framework
Name: dogtail
Version: 2.1.0
Release:        1%{?dist}
License: GPL-2.0-only
URL: https://gitlab.com/dogtail/dogtail/
Source0:        https://files.pythonhosted.org/packages/source/d/dogtail/dogtail-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

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
Requires: python3-dogtail >= 2.1.0
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
%oreon_autofiles python3-dogtail usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-dogtail-scripts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-dogtail -f %{oreon_filedir}/python3-dogtail.list
%files -n python3-dogtail-scripts -f %{oreon_filedir}/python3-dogtail-scripts.list

%changelog

%autochangelog
