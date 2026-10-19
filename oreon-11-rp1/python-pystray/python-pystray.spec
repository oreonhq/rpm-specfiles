%global source0_hash 2ab6bd15c14b400c9e8271a82c9de8adc0f1a0cacfc14080bdd4fb42bb88ec92
%bcond_with test
%global common_sum Provides system tray integration
%global common_desc This library allows you to create a system tray icon.
%global upname pystray
Name:		python-%{upname}
Version:	0.19.5
Release:        1%{?dist}
Summary:        Provides system tray integration
License:	LGPL-3.0-or-later
URL:		https://github.com/moses-palmer/%{upname}
Source0:        https://github.com/moses-palmer/%{upname}/archive/v%{version}/%{upname}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-pillow
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
BuildRequires:  python3-xlib
# /oreon:deps
%description
%{common_desc}

%package -n python3-%{upname}
Summary:	%{common_sum}
BuildRequires:	python3-devel >= 3.4
BuildRequires:	python3-pillow
BuildRequires:	python3-setuptools
BuildRequires:	python3-six
BuildRequires:	python3-xlib >= 0.17
Requires:	libappindicator-gtk3
Requires:	python3-pillow
Requires:	python3-six
Requires:	python3-xlib		>= 0.17
%{?python_provide:%python_provide python3-%{upname}}
%description -n python3-%{upname}
%{common_desc}

%package -n python3-%{upname}-doc
Summary:	Documentation-files for python3-%{upname}
BuildRequires:	fdupes
BuildRequires:	python3-sphinx >= 1.3.1
%description -n python3-%{upname}-doc
This package contains the Documentation-files for python3-%{upname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upname}-%{version}

# Remove pre-built and bundled crap.
%{__rm} -fr *.egg*

%build

%py3_build
sphinx-build-3 docs docs/build-%{python3_version}/html
%fdupes -s docs/build-%{python3_version}
for f in .buildinfo .doctrees .inv ; do
	%{_bindir}/find docs/ -name "*${f}*" -print0 |			\
		%{_bindir}/xargs -0 %{__rm} -frv
done
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with test}
%check

%{__python3} setup.py test
%endif # with test
%files -f %{oreon_filedir}/main.list
%files -n python3-pystray -f %{oreon_filedir}/python3-pystray.list
%files -n python3-pystray-doc -f %{oreon_filedir}/python3-pystray-doc.list

%changelog

%autochangelog
