%global source0_hash 6d4fe287766166a98ca7bc6f6312daf04a0481b1eda43e7173484051c0ab4366
Name:           python-colorclass
Version:        2.2.2
Release:        1%{?dist}
Summary:        Yet another ANSI color text library for Python
%global srcname colorclass
License:        MIT
URL:            https://pypi.python.org/pypi/colorclass
VCS:            git:https://github.com/matthewdeanmartin/colorclass
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Colorful worry-free console applications for Linux, Mac OS X, and Windows.
Yet another ANSI color text library for Python. Provides "auto colors" for
dark/light terminals. Works on Linux, OS X, and Windows.

%package -n python3-%{srcname}
Summary:        Yet another ANSI color text library for Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
Colorful worry-free console applications for Linux, Mac OS X, and Windows.
Yet another ANSI color text library for Python. Provides "auto colors" for
dark/light terminals. Works on Linux, OS X, and Windows.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
# cp %%{SOURCE1} .
rm -rf colorclass.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_check_import colorclass
%files -f %{oreon_filedir}/main.list
%files -n python3-colorclass -f %{oreon_filedir}/python3-colorclass.list

%changelog

%autochangelog
