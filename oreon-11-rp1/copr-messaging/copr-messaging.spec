%global source0_hash 521ae86daad640cce659d42d99d2c2a40011a06ff33ee05db545fecc24e011b2

%global _description\
Schemas for messages sent by Copr project, as described on \
fedora-messaging documentation page \
https://fedora-messaging.readthedocs.io/en/latest/messages.html#schema \
\
Package also provides several convenience methods for working with \
copr messages.

Name:       copr-messaging
Version:    1.2
Release:    4%{?dist}
Summary:    Abstraction for Copr messaging listeners/publishers

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch:  noarch

Requires:      wget

BuildRequires: asciidoc
BuildRequires: libxslt
BuildRequires: util-linux

BuildRequires: python3-copr-common
BuildRequires: python3-devel
BuildRequires: python3-fedora-messaging
BuildRequires: python3-pytest
%if 0%{?rhel} == 8
BuildRequires: python3-setuptools
%endif
BuildRequires: python3-sphinx

%description %_description

%package -n python3-%name
Summary: %summary
Provides: %name = %version

Requires: python3-copr-common
Requires: python3-fedora-messaging

%description -n python3-%name %_description

%package -n python3-%name-doc
Summary: Code documentation for copr messaging

%description -n python3-%name-doc %_description

This package contains documentation for copr-messaging.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%if 0%{?rhel} != 8
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?rhel} == 8
%py3_build
%else
%pyproject_wheel
%endif
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?rhel} == 8
%py3_install
%else
%pyproject_install
%pyproject_save_files -l copr_messaging
%endif

%check
./run_tests.sh -vv

%if 0%{?rhel} == 8
%files -n python3-%name
%else
%files -n python3-%name -f %{pyproject_files}
%endif
%doc README.md
%if 0%{?rhel} == 8
%license LICENSE
%doc README.md
%python3_sitelib/copr_messaging
%python3_sitelib/copr_messaging*egg-info
%endif

%files -n python3-%name-doc
%license LICENSE
%doc html

%changelog
%autochangelog
