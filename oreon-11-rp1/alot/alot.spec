%global source0_hash 4227913ee8acef847ac9a9c14312c878310ab6574ccd0bef178a209c606036ec
Name:           alot
Version:        0.12
Release:        1%{?dist}
Summary:        Experimental terminal MUA based on notmuch mail
License:        GPL-3.0-or-later
URL:            https://github.com/pazz/alot
Source0:        https://github.com/pazz/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch:          0001-replace-python-magic-with-file-magic.patch
BuildArch:      noarch
Requires:       python3-standard-mailcap
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-alot = %{version}-%{release}
# /oreon:deps
%package -n       python3-alot+docs
Summary:        Metapackage for python3-alot docs extras
Requires:       python3-alot = %{version}-%{release}
Provides:       python3dist(alot[docs]) = %{version}-%{release}

%description -n python3-alot+docs
Metapackage for python3-alot docs extras.

%package -n       python3-alot+tests
Summary:        Metapackage for python3-alot tests extras
Requires:       python3-alot = %{version}-%{release}
Provides:       python3dist(alot[tests]) = %{version}-%{release}

%description -n python3-alot+tests
Metapackage for python3-alot tests extras.

%package -n       python3-alot+typing
Summary:        Metapackage for python3-alot typing extras
Requires:       python3-alot = %{version}-%{release}
Provides:       python3dist(alot[typing]) = %{version}-%{release}

%description -n python3-alot+typing
Metapackage for python3-alot typing extras.

%description
alot makes use of existing solutions where possible: It does not fetch, send or
edit mails; it lets notmuch handle your mailindex and uses a toolkit to render
its display. You are responsible for automatic initial tagging.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%make_build man PYTHONPATH=${PYTHONPATH}:$RPM_BUILD_DIR/alot-%{version} SPHINX_BUILD=sphinx-build-3 PYTHON=python3 -C docs
%install
%pyproject_install
install -Dpm0644 docs/build/man/alot.1* -t %{buildroot}%{_mandir}/man1/
install -Dpm0644 alot/defaults/* -t %{buildroot}/%{python3_sitelib}/alot/defaults/
%oreon_autofiles main

%check

%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest
%files

%changelog

%autochangelog
