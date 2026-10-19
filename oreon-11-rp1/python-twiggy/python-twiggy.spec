%global source0_hash 7938840275972f6ce89994a5bdfb0b84f0386301a043a960af6364952e78ffe4
%{!?_licensedir: %global license %%doc}
%global modname twiggy
%global distname Twiggy
%global pypi_name Twiggy
Name:               python-twiggy
Version:            0.5.1
Release:        20%{?dist}
Summary:        A Pythonic logger
License:            LicenseRef-Callaway-BSD
URL:                http://pypi.python.org/pypi/Twiggy
Source0:        https://files.pythonhosted.org/packages/source/p/python-twiggy/python-twiggy-%{version}.tar.gz
BuildArch:          noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description
Twiggy is a Pythonic logger.

You should use Twiggy because it is awesome. For more information, read the
`documentation <http://twiggy.wearpants.org>`_ or `see this blog post
<http://blog.wearpants.org/meet-twiggy>`_.

%package -n python3-%{modname}
Summary:            A Pythonic logger
%{?python_provide:%python_provide python3-%{modname}}
%description -n python3-%{modname}
Twiggy is a Pythonic logger.

You should use Twiggy because it is awesome. For more information, read the
`documentation <http://twiggy.wearpants.org>`_ or `see this blog post
<http://blog.wearpants.org/meet-twiggy>`_.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{distname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-twiggy -f %{oreon_filedir}/python3-twiggy.list

%changelog

%autochangelog
