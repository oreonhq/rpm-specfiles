%global source0_hash 0c804c7e48dd17db24cb39121ade7171f684fb463c8aa01d0338cd11d254364a
%bcond tests 1
Name:           bindep
Version:        2.14.0
Release:        1%{?dist}
Summary:        Binary dependency utility
License:        Apache-2.0
URL:            https://docs.opendev.org/opendev/bindep
Source0:        https://files.pythonhosted.org/packages/source/b/bindep/bindep-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-bindep = %{version}-%{release}
# /oreon:deps
%package -n       python3-bindep+build-docs
Summary:        Metapackage for python3-bindep build-docs extras
Requires:       python3-bindep = %{version}-%{release}
Requires:       python3dist(fixtures) >= 0.3.12
Requires:       python3dist(reno) >= 2.8.0
Requires:       python3dist(sphinx)
Provides:       python3dist(bindep[build-docs]) = %{version}-%{release}

%description -n python3-bindep+build-docs
Metapackage for python3-bindep build-docs extras.

%package -n       python3-bindep+test-cover
Summary:        Metapackage for python3-bindep test-cover extras
Requires:       python3-bindep = %{version}-%{release}
Requires:       python3dist(coverage) >= 3.6
Provides:       python3dist(bindep[test-cover]) = %{version}-%{release}

%description -n python3-bindep+test-cover
Metapackage for python3-bindep test-cover extras.

%package -n       python3-bindep+test-linters
Summary:        Metapackage for python3-bindep test-linters extras
Requires:       python3-bindep = %{version}-%{release}
Requires:       python3dist(hacking) >= 7
Requires:       python3dist(hacking) < 8
Provides:       python3dist(bindep[test-linters]) = %{version}-%{release}

%description -n python3-bindep+test-linters
Metapackage for python3-bindep test-linters extras.

%package -n       python3-bindep+test-unit
Summary:        Metapackage for python3-bindep test-unit extras
Requires:       python3-bindep = %{version}-%{release}
Requires:       python3dist(fixtures) >= 0.3.12
Requires:       python3dist(stestr) >= 1
Requires:       python3dist(testtools) >= 0.9.27
Provides:       python3dist(bindep[test-unit]) = %{version}-%{release}

%description -n python3-bindep+test-unit
Metapackage for python3-bindep test-unit extras.

%description
Bindep is a tool for checking the presence of binary packages needed to use an
application / library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove dependencies unwanted in Fedora
sed -i -E '/(coverage|pytest-cov|mock)/d' test-requirements.txt
find -type f -name '*.py' | xargs -d'\n' sed -i \
    -e 's/^\( *\)import mock/\1from unittest import mock/' \
    -e 's/^\( *\)from mock import /\1from unittest.mock import /'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%if %{with tests}
%pytest \
    -s \
    -k 'not test_arch_implies_pacman and not test_manjaro_implies_pacman'
%endif
%files

%changelog

%autochangelog
