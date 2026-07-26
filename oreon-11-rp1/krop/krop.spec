%global source0_hash 6a8e164ae3b1ddf5a656d0847cb21737f019c1a4c4f5ae4db9f00640643a394a

%global osname  %(cat /etc/redhat-release | awk '{sub(/ release.*/,""); print}')
%global pkgmgr  dnf

%bcond_without  python3

Name:           krop
Version:        0.5.1
Release:        29%{?dist}
Summary:        Tool to crop PDF files with an eye towards eReaders
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://arminstraub.com/software/krop
Source0:        http://arminstraub.com/downloads/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# upstreamable patch, see also
# https://bugzilla.redhat.com/show_bug.cgi?id=1707034
# https://github.com/arminstraub/krop/issues/23
Patch1: krop-0.5.1-sip_namespace.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%if %without python3
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-%{name} = %{version}-%{release}
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-%{name} = %{version}-%{release}
%endif

%description
Krop is a simple graphical tool to crop the pages of PDF files. A unique feature
of krop is its ability to automatically split pages into subpages to fit the
limited screen size of devices such as eReaders. This is particularly useful, if
your eReader does not support convenient scrolling.

%if %without python3
%package -n python2-%{name}
Summary:    Python2 module for %{name}
Requires:   python-PyPDF2 PyQt5 python-poppler-qt5
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
%else
%package -n python3-%{name}
Summary:    Python3 module for %{name}
Requires:   python3-PyPDF2 python3-PyQt5 python3-poppler-qt5
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%endif
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# In terms of OS available on Koji. "of" is needed since Ubuntu appears as font.
find . -type f -name '*.py' -exec sed -i -e 's/of ubuntu/of %{osname}/Ig' \
 -e 's|apt-get|%{pkgmgr}|g' -e 's|python-pypdf|pyPdf|g' '{}' +

%patch -P1 -p1 -b .sip_namespace

%build
%if %without python3
%py2_build
%else
%py3_build
%endif

%install
%if %without python3
%py2_install
%else
%py3_install
%endif
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
DESTDIR="%{buildroot}" appstream-util install %{name}.appdata.xml

%check
%if %without python3
%{__python2} setup.py check
%else
%{__python3} setup.py check
%endif
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%if %without python3
%files -n python2-%{name}
%{python2_sitelib}/%{name}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{name}/
%else
%files -n python3-%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}/
%endif
%license LICENSE

%changelog
%autochangelog
