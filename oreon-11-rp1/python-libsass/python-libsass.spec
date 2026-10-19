%global source0_hash 4bff7819756f52f6e4592f03f205104d1ca431088d9452aed5042f89a36f9873
Name:           python-libsass
Version:        0.23.0
Release:        1%{?dist}
Summary:        Sass for Python: A straightforward binding of libsass for Python
License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source0:        https://github.com/dahlia/libsass-python/archive/%{version}/libsass-python-%{version}.tar.gz
%global common_description %{expand:
This package provides a simple Python extension module sass which is binding
LibSass (written in C/C++ by Hampton Catlin and Aaron Leung). It’s very
straightforward and there isn’t any headache related to Python
distribution/deployment. That means you can add just libsass into your
setup.py’s install_requires list or requirements.txt file. No need for Ruby nor
Node.js.}
# oreon:deps
BuildRequires:  (python3dist(werkzeug) with python3dist(werkzeug) >= 0.9)
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libsass-devel
BuildRequires:  make
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description %{common_description}

%package -n python3-libsass
Summary:        Sass for Python: A straightforward binding of libsass for Python
%py_provides python3-sass
%py_provides python3-pysassc
%py_provides python3-sasstests
%py_provides python3-sassutils
Obsoletes:      python-libsass-doc < 0.23.0-6
%description -n python3-libsass %{common_description}

%prep

%autosetup -p1
# While upstream has the executable bit set, we will install this in
# site-packages without executable permissions; therefore, the shebang becomes
# useless, and we should remove it downstream.
sed -r -i '1{/^#!/d}' pysassc.py

%build -p

export SYSTEM_SASS='1'
%install -p
export SYSTEM_SASS='1'
%oreon_autofiles python3-libsass usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%install
%pyproject_install
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitearch}' \
    help2man --no-info --output='%{buildroot}%{_mandir}/man1/pysassc.1' \
    '%{buildroot}%{_bindir}/pysassc'
%oreon_autofiles python3-libsass usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v sasstests.py
%files -f %{oreon_filedir}/main.list
%files -n python3-libsass -f %{oreon_filedir}/python3-libsass.list

%changelog

%autochangelog
