%global source0_hash 535cb795da5d1672783d0c6e43649880e9b2be4d79456a743d4711029ede00d8

%global desc %{expand: \
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.}

Name:           pyflakes
# WARNING: When updating pyflakes, check not to break flake8!
Version:        3.1.0
Release:        9%{?dist}
Summary:        A simple program which checks Python source files for errors

License:        MIT
URL:            https://github.com/PyCQA/pyflakes
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://cdn.debian.net/debian/pool/main/p/pyflakes/pyflakes_2.5.0-1.debian.tar.xz
# Support Python 3.14
Patch:          https://github.com/PyCQA/pyflakes/pull/842.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%py_provides python3-%{name}

%description %{desc}

%package -n python%{python3_pkgversion}-%{name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

mv %{buildroot}%{_bindir}/pyflakes %{buildroot}%{_bindir}/pyflakes-%{python3_version}
ln -s pyflakes-%{python3_version} %{buildroot}%{_bindir}/pyflakes-3
ln -s pyflakes-3 %{buildroot}%{_bindir}/pyflakes

install -Dpm 644 debian/pyflakes3.1 %{buildroot}%{_mandir}/man1/pyflakes-%{python3_version}.1
ln -s pyflakes-%{python3_version}.1 %{buildroot}%{_mandir}/man1/pyflakes-3.1
ln -s pyflakes-3.1 %{buildroot}%{_mandir}/man1/pyflakes.1

%check
# test_errors_syntax fails on Python 3.13 because of a changed error message
# https://github.com/PyCQA/pyflakes/issues/811
%pytest -v -k "not test_errors_syntax"

%files -n python%{python3_pkgversion}-%{name} -f %{pyproject_files}
%doc AUTHORS NEWS.rst README.rst
%{_bindir}/pyflakes-%{python3_version}
%{_bindir}/pyflakes-3
%{_bindir}/pyflakes
%{_mandir}/man1/pyflakes-%{python3_version}.1*
%{_mandir}/man1/%{name}-3.1.gz
%{_mandir}/man1/pyflakes.1*
%exclude %{python3_sitelib}/pyflakes/test

%changelog
%autochangelog
