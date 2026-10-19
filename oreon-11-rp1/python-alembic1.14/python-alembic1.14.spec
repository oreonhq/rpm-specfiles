%global source0_hash db505480647bc60386c5369402f4a57a506b7539c9e9ef5e270d45cbbe4939bf
Name:             python-alembic1.14
Version:          1.20.0
Release:        1%{?dist}
Summary:        Database migration tool for SQLAlchemy
License:          MIT
URL:              https://pypi.io/project/alembic
Source0:        https://files.pythonhosted.org/packages/source/a/alembic/alembic-%{version}.tar.gz
Patch:            python-alembic1.14-1.14.1-no-tzdata-pkg.patch
BuildArch:        noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-alembic1.14 = %{version}-%{release}
# /oreon:deps
%package -n       python3-alembic1.14+tz
Summary:        Metapackage for python3-alembic1.14 tz extras
Requires:       python3-alembic1.14 = %{version}-%{release}
Provides:       python3dist(alembic1.14[tz]) = %{version}-%{release}

%description -n python3-alembic1.14+tz
Metapackage for python3-alembic1.14 tz extras.

%description

%package -n python3-alembic1.14
Summary:          %summary
Conflicts:        python3-alembic >= 1.15
Provides:         python3-alembic = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:reqs
Requires:       python3dist(sqlalchemy) >= 2.0
Requires:       python3dist(typing-extensions) >= 4.12
# /oreon:reqs
%description -n python3-alembic1.14

# Don’t use the %%pyproject_extras_subpkg macro, we want it to depend on the
# main tzdata package, not python3dist(tzdata) (which we don’t have).

%package -n python3-alembic1.14+tz
Summary: Metapackage for python3-alembic1.14: tz extra
Requires: python3-alembic1.14 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: tzdata
%description -n python3-alembic1.14+tz
This is a metapackage bringing in tz extra requires for python3-alembic1.14.
It contains no code, just makes sure the dependencies are installed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n alembic-%{version}
# HTML documentation has bundled and pre-compiled/pre-minified JavaScript; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/.
rm -rvf docs/_static
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*(black|zimports))\b/# &/' tox.ini
# Don't treat DeprecationWarnings as errors in tests
sed -i '/"error", category=DeprecationWarning/d' alembic/testing/warnings.py

%build

%pyproject_wheel
mkdir -p bin
echo '%{python3} -c "import alembic.config; alembic.config.main()" $*' > bin/alembic
chmod 0755 bin/alembic
help2man --version-string %{version} --no-info -s 1 bin/alembic > alembic.1
%install
install -d -m 0755 %{buildroot}%{_mandir}/man1
%pyproject_install
mv %{buildroot}/%{_bindir}/alembic %{buildroot}/%{_bindir}/alembic-3
ln -s alembic-3 %{buildroot}/%{_bindir}/alembic-%{python3_version}
install -m 0644 alembic.1 %{buildroot}%{_mandir}/man1/alembic-3.1
ln -s alembic-3.1 %{buildroot}%{_mandir}/man1/alembic-%{python3_version}.1
ln -s alembic-%{python3_version} %{buildroot}/%{_bindir}/alembic
ln -s alembic-%{python3_version}.1 %{buildroot}%{_mandir}/man1/alembic.1
%oreon_autofiles python3-alembic1.14 usr/lib/python3*/site-packages/alembic1.14* usr/lib64/python3*/site-packages/alembic1.14* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/alembic1.14* usr/lib64/python3*/site-packages/alembic1.14* usr/bin/*

%check

%pytest %{?!rhel:-n auto}
%files
%files -n python3-alembic1.14 -f %{oreon_filedir}/python3-alembic1.14.list

%changelog

%autochangelog
