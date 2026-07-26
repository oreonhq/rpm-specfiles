%global source0_hash 8b5d02ec33a812425c9d6b95bb6798fe9a78f68bf2146bf10185f0ade5ede7ec

# Testsuite needs human interaction.
%bcond_with test

%global common_sum Provides system tray integration
%global common_desc This library allows you to create a system tray icon.

%global upname pystray

Name:		python-%{upname}
Version:	0.17.3
Release:	20%{?dist}
Summary:	%{common_sum}

License:	LGPL-3.0-or-later
URL:		https://github.com/moses-palmer/%{upname}
Source0:	%{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildArch:	noarch

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

%if %{with test}
%check
%{__python3} setup.py test
%endif # with test

%files -n python3-%{upname}
%license COPYING*
%doc README.rst
%{python3_sitelib}/%{upname}
%{python3_sitelib}/%{upname}-%{version}-py%{python3_version}.egg-info

%files -n python3-%{upname}-doc
%doc CHANGES.rst docs/build-%{python3_version}/html

%changelog
%autochangelog
