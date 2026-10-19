%global source0_hash 555d5d83539d29d75cf655d1fb5077fe86204ce784cc5704ac8d475c71fd61b3
%global sum Standalone version of Django's feedgenerator module
Name:       python-feedgenerator
Version:    2.2.1
Release:        1%{?dist}
Summary:        Standalone version of Django's feedgenerator module
License:    BSD-3-Clause
URL:        https://github.com/getpelican/feedgenerator
Source0:        https://github.com/getpelican/feedgenerator/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:  noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-feedgenerator = %{version}-%{release}
# /oreon:deps
%description
FeedGenerator is a standalone version of Django’s feedgenerator module. It has
evolved over time, including an update for Py3K and numerous other
enhancements.

%package -n python3-feedgenerator
Summary:        %{sum}
%description -n python3-feedgenerator
FeedGenerator is a standalone version of Django’s feedgenerator module. It has
evolved over time, including an update for Py3K and numerous other
enhancements.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n feedgenerator-%{version}
# remove coverage related bits for pytest
sed -i.backup -e '/--cov/ d' -e '/pytest-cov/ d' pyproject.toml

rm -rf feedgenerator/django/utils/six.py

for f in feedgenerator/django/utils/*py;
do
    sed -i -e 's/from . import six/import six/' -e 's/from .six \(import .*$\)/from six \1/'  $f
done

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-feedgenerator usr/lib/python3*/site-packages/feedgenerator* usr/lib64/python3*/site-packages/feedgenerator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/feedgenerator* usr/lib64/python3*/site-packages/feedgenerator* usr/bin/*

%check

%pytest
%files
%files -n python3-feedgenerator -f %{oreon_filedir}/python3-feedgenerator.list

%changelog

%autochangelog
