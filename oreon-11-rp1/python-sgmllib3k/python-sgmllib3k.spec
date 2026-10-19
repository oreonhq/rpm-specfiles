%global source0_hash 7868fb1c8bfa764c1ac563d3cf369c381d1325d36124933a726f29fcdaa812e9
%{?!python3_pkgversion:%global python3_pkgversion 3}
%global pypi_name sgmllib3k
Name:           python-sgmllib3k
Version:        1.0.0
Release:        1%{?dist}
Summary:        python3 copy of sgmllib
License:        PSF-2.0
URL:            https://pypi.org/project/sgmllib3k/
Source0:        https://files.pythonhosted.org/packages/source/p/python-sgmllib3k/python-sgmllib3k-%{version}.tar.gz
BuildArch:      noarch
%{?python_enable_dependency_generator}
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
sgmllib was dropped in Python 3. For those depending on it,
that’s somewhat unfortunate. This is a quick and dirty
port of this old module. I just ran 2to3 on it and published it.
I don’t intend to maintain it, so it might be a good idea to
eventually think about finding another module to use.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        python3 copy of sgmllib
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python%{python3_pkgversion}-%{pypi_name}
sgmllib was dropped in Python 3. For those depending on it,
that’s somewhat unfortunate. This is a quick and dirty
port of this old module. I just ran 2to3 on it and published it.
I don’t intend to maintain it, so it might be a good idea to
eventually think about finding another module to use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-sgmllib3k -f %{oreon_filedir}/python3-sgmllib3k.list

%changelog

%autochangelog
