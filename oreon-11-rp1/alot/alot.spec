%global source0_hash 4227913ee8acef847ac9a9c14312c878310ab6574ccd0bef178a209c606036ec

Name:           alot
Version:        0.12
Release:        3%{?dist}
Summary:        Experimental terminal MUA based on notmuch mail

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/pazz/alot
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Patch:          0001-replace-python-magic-with-file-magic.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# needed to generate manpages
BuildRequires:  python3-sphinx
BuildRequires:  python3-standard-mailcap
BuildRequires:  make
BuildRequires:  procps-ng
Requires:       python3-standard-mailcap

%description
alot makes use of existing solutions where possible: It does not fetch, send or
edit mails; it lets notmuch handle your mailindex and uses a toolkit to render
its display. You are responsible for automatic initial tagging.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%make_build man PYTHONPATH=${PYTHONPATH}:$RPM_BUILD_DIR/alot-%{version} SPHINX_BUILD=sphinx-build-3 PYTHON=python3 -C docs

%install
%pyproject_install
%pyproject_save_files -l alot
install -Dpm0644 docs/build/man/alot.1* -t %{buildroot}%{_mandir}/man1/
install -Dpm0644 alot/defaults/* -t %{buildroot}/%{python3_sitelib}/alot/defaults/

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest

%files -f %{pyproject_files}
%license COPYING
%doc NEWS README.md
%{_bindir}/alot
%{_mandir}/man1/alot.1*
%{python3_sitelib}/alot/defaults

%changelog
%autochangelog
