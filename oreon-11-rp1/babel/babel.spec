%global source0_hash b80b99a14bd085fcacfa15c9165f651fbb3406e66cc603abf11c5750937c992d
%bcond bootstrap 0
%bcond datetime_tests %{undefined rhel}
Name:           babel
Version:        2.18.0
Release:        1%{?dist}
Summary:        Tools for internationalizing Python applications
License:        BSD-3-Clause
URL:            https://babel.pocoo.org/
Source0:        https://files.pythonhosted.org/packages/source/b/babel/babel-2.18.0.tar.gz
BuildArch:      noarch
%if %{without bootstrap}
%if %{with datetime_tests}
%endif
%endif
Requires:       python3-babel = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-babel = %{version}-%{release}
# /oreon:deps
%description
Babel is composed of two major parts:

* tools to build and work with gettext message catalogs

* a Python interface to the CLDR (Common Locale Data Repository),
  providing access to various locale display names, localized number
  and date formatting, etc.

%package -n python3-babel
Summary:        Library for internationalizing Python applications
%description -n python3-babel
Babel is composed of two major parts:

* tools to build and work with gettext message catalogs

* a Python interface to the CLDR (Common Locale Data Repository),
  providing access to various locale display names, localized number
  and date formatting, etc.

%if %{without bootstrap}
%package doc
Summary:        Documentation for Babel
%py_provides    python3-babel-doc
%description doc
Documentation for Babel
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir babel-%{version}
%oreon_prep
%build

%pyproject_wheel
BUILDDIR="$PWD/built-docs"
rm -rf "$BUILDDIR"
%if %{without bootstrap}
pushd docs
make \
    SPHINXBUILD=sphinx-build-3 \
    BUILDDIR="$BUILDDIR" \
    html man
popd
rm -f "$BUILDDIR/html/.buildinfo"
%endif
%install
%pyproject_install
%if %{without bootstrap}
install -D -m 0644 built-docs/man/babel.1 %{buildroot}%{_mandir}/man1/pybabel.1
%oreon_autofiles python3-babel usr/lib/python3*/site-packages/babel* usr/lib64/python3*/site-packages/babel* usr/bin/*
%oreon_autofiles babel-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/babel* usr/lib64/python3*/site-packages/babel* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

export TZ=UTC
%pyproject_check_import
%if %{without bootstrap}
%pytest %{!?with_datetime_tests:\
  -k "not (babel.dates.format_time or babel.dates.get_timezone_name)" \
  --ignore tests/test_dates.py \
  --ignore tests/messages/frontend/test_cli.py \
  --ignore tests/messages/frontend/test_extract.py \
  --ignore tests/messages/frontend/test_init.py}
%endif
%files
%files -n python3-babel -f %{oreon_filedir}/python3-babel.list
%files -n babel-doc -f %{oreon_filedir}/babel-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.0-1
- Prepare for Oreon 11 (RP1)
