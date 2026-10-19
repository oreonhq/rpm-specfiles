%global source1_hash 535cb795da5d1672783d0c6e43649880e9b2be4d79456a743d4711029ede00d8
%global source0_hash b987f60fa44ae1a2374d162ba22b496ace1fd7af49d95df46335eeff6a99bf84
%global desc %{expand: \
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.}
Name:           pyflakes
Version:        3.4.0
Release:        1%{?dist}
Summary:        A simple program which checks Python source files for errors
License:        MIT
URL:            https://github.com/PyCQA/pyflakes
Source0:        https://github.com/PyCQA/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://cdn.debian.net/debian/pool/main/p/pyflakes/pyflakes_2.5.0-1.debian.tar.xz
BuildArch:      noarch
%py_provides python3-%{name}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyflakes = %{version}-%{release}
# /oreon:deps
%description %{desc}

%package -n python%{python3_pkgversion}-%{name}
Summary:        A simple program which checks Python source files for errors
%description -n python%{python3_pkgversion}-%{name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mv %{buildroot}%{_bindir}/pyflakes %{buildroot}%{_bindir}/pyflakes-%{python3_version}
ln -s pyflakes-%{python3_version} %{buildroot}%{_bindir}/pyflakes-3
ln -s pyflakes-3 %{buildroot}%{_bindir}/pyflakes
install -Dpm 644 debian/pyflakes3.1 %{buildroot}%{_mandir}/man1/pyflakes-%{python3_version}.1
ln -s pyflakes-%{python3_version}.1 %{buildroot}%{_mandir}/man1/pyflakes-3.1
ln -s pyflakes-3.1 %{buildroot}%{_mandir}/man1/pyflakes.1
%oreon_autofiles main usr/lib/python3*/site-packages/pyflakes* usr/lib64/python3*/site-packages/pyflakes* usr/bin/*

%check

%pytest -v -k "not test_errors_syntax"
%files
%files -n python3-pyflakes -f %{oreon_filedir}/python3-pyflakes.list

%changelog

%autochangelog
