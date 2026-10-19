%global source0_hash 76ca6130f55e65ac7b2e32d8e24266022e34f71b0b7c4385c0f418340a111690
%bcond_without tests
Name:           rpmlint
Version:        2.10.0
Release:        1%{?dist}
Summary:        Tool for checking common errors in RPM packages
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/rpmlint
Source0:        https://github.com/rpm-software-management/rpmlint/archive/refs/tags/2.10.0.tar.gz#/rpmlint-2.8.0.tar.gz
Source1:        fedora.toml
Source3:        scoring.toml
Source4:        users-groups.toml
Source5:        warn-on-functions.toml
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       devscripts-checkbashisms
Requires:       rpm-build
Requires:       /usr/bin/appstream-util
Requires:       /usr/bin/desktop-file-validate
Requires:       rpmlint-fedora-license-data
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-rpmlint = %{version}-%{release}
# /oreon:deps
%package -n       python3-rpmlint+test
Summary:        Metapackage for python3-rpmlint test extras
Requires:       python3-rpmlint = %{version}-%{release}
Provides:       python3dist(rpmlint[test]) = %{version}-%{release}

%description -n python3-rpmlint+test
Metapackage for python3-rpmlint test extras.

%description
rpmlint is a tool for checking common errors in RPM packages. Binary
and source packages as well as spec files can be checked.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -Sgit_am

# Replace python-magic dep with file-magic (rhbz#1899279)
sed -i 's/python-magic/file-magic/g' pyproject.toml

# Don't lint the code or measure coverage in %%check
sed -i -e '/^ *--cov=rpmlint$/d' pytest.ini

# Avoid warnings about pytest.mark.no_cover marker
sed -i '/^@pytest.mark.no_cover/d' test/test_lint.py

if ! which dash checkbashisms >/dev/null; then
    # Disable bashisms check if dash or checkbashisms is unavailable.
    sed -i -e '/BashismsCheck/d' %{SOURCE1}
fi

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/rpmlint/
cp -a %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}%{_sysconfdir}/xdg/rpmlint/
%oreon_autofiles main

%check

%if %{with tests}
%pytest %{?rhel:--ignore test/test_erlang.py}
%endif
%files

%changelog

%autochangelog
