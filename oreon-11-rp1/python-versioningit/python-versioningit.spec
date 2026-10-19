%global source0_hash b91ad7d73e73d21220e69540f20213f2b729a1f9b35c04e9e137eaf28d2214da
%bcond tests 1
%bcond pydantic_tests 1
Name:           python-versioningit
Version:        3.3.0
Release:        1%{?dist}
Summary:        Versioning It with your Version In Git
License:        MIT
URL:            https://pypi.org/pypi/versioningit
Source0:        https://files.pythonhosted.org/packages/source/v/versioningit/versioningit-%{version}.tar.gz
Source1:        versioningit.1
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-versioningit = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-versioningit
Summary:        Versioning It with your Version In Git
Recommends:     git-core
Recommends:     mercurial
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  git-core
BuildRequires:  mercurial
%endif
# oreon:reqs
Requires:       python3dist(importlib-metadata) >= 3.6
Requires:       python3dist(packaging) >= 17.1
Requires:       python3dist(tomli) < 3.0
Requires:       python3dist(tomli) >= 1.2
# /oreon:reqs
%description -n python3-versioningit

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n versioningit-%{version}

# Tweak build requirements to use what we have in Fedora. For test
# dependencies, we change all semver pins to minimum versions.
sed -r -i 's/~=/>=/g' tox.ini
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*)(pytest-cov|.*--(.*-)?cov)/\1# \2/g' tox.ini
sed -r -i 's/^([[:blank:]]*)(ignore:.*coverage)/\1# \2/g' tox.ini
%if %{without pydantic_tests}
sed -r -i 's/^([[:blank:]]*)(pydantic\b)/\1# \2/g' tox.ini
%endif
# Do not error on DeprecationWarning; this makes sense for upstream CI, but is
# too strict for downstream builds.
sed -r -i 's/^(filterwarnings = )error/\1default/' tox.ini

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build

%pyproject_wheel
%install
%pyproject_install
install -p -m 0644 -Dt %{buildroot}%{_mandir}/man1/ %{SOURCE1}
%oreon_autofiles python3-versioningit usr/lib/python3*/site-packages/versioningit* usr/lib64/python3*/site-packages/versioningit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/versioningit* usr/lib64/python3*/site-packages/versioningit* usr/bin/*

%check

%if %{with tests}
k="${k-}${k+ and }not test_editable_mode"
k="${k-}${k+ and }not test_install_from_git_url"
k="${k-}${k+ and }not test_install_from_zip_url"
%if %{without pydantic_tests}
ignore="${ignore-} --ignore=test/test_methods/test_hg.py"
ignore="${ignore-} --ignore=test/test_methods/test_git.py"
ignore="${ignore-} --ignore=test/test_end2end.py"
%endif
%pytest -k "${k-}" ${ignore-}
%endif
%files
%files -n python3-versioningit -f %{oreon_filedir}/python3-versioningit.list

%changelog

%autochangelog
