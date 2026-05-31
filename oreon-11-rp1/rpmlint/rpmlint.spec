%global source0_hash 69884a3b80438698e41dc4b39658fae611b45ad6cfb31e38db76279bfb4288b1

# pass --without tests to skip the test suite
%bcond_without tests

Name:           rpmlint
Version:        2.8.0
Release:        3%{?dist}
Summary:        Tool for checking common errors in RPM packages
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/rpmlint
Source0:        https://github.com/rpm-software-management/rpmlint/archive/2.8.0/rpmlint-2.8.0.tar.gz

# Taken from https://github.com/rpm-software-management/rpmlint/tree/main/configs/Fedora
Source1:        fedora.toml
Source3:        scoring.toml
Source4:        users-groups.toml
Source5:        warn-on-functions.toml

BuildArch:      noarch

# use git to apply patches; it handles binary diffs
BuildRequires:  git-core
BuildRequires:  python3-devel
# tests
%if %{with tests}
%if ! 0%{?rhel}
BuildRequires:  dash
%endif
BuildRequires:  devscripts-checkbashisms
BuildRequires:  hunspell-cs
BuildRequires:  hunspell-en-US
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
%endif
%if ! 0%{?rhel}
Requires:       dash
%endif
Requires:       devscripts-checkbashisms
Requires:       rpm-build
Requires:       /usr/bin/appstream-util
Requires:       /usr/bin/desktop-file-validate
Requires:       rpmlint-fedora-license-data

%description
rpmlint is a tool for checking common errors in RPM packages. Binary
and source packages as well as spec files can be checked.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -Sgit_am

# Replace python-magic dep with file-magic (rhbz#1899279)
sed -i 's/python-magic/file-magic/g' pyproject.toml

%if 0%{?rhel}
# Avoid extra dependencies for checks not needed in RHEL
# pybeam: ErlangCheck
sed -i -e '/pybeam/d' pyproject.toml
sed -i -e '/ErlangCheck/d' rpmlint/configdefaults.toml test/test_lint.py
%endif

# Don't lint the code or measure coverage in %%check
sed -i -e '/^ *--cov=rpmlint$/d' pytest.ini

# Avoid warnings about pytest.mark.no_cover marker
sed -i '/^@pytest.mark.no_cover/d' test/test_lint.py

if ! which dash checkbashisms >/dev/null; then
    # Disable bashisms check if dash or checkbashisms is unavailable.
    sed -i -e '/BashismsCheck/d' %{SOURCE1}
fi

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

mkdir -p %{buildroot}%{_sysconfdir}/xdg/rpmlint/
cp -a %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}%{_sysconfdir}/xdg/rpmlint/

%check
%if %{with tests}
%pytest %{?rhel:--ignore test/test_erlang.py}
%endif

%files -f %{pyproject_files}
%doc README.md
%dir %{_sysconfdir}/xdg/rpmlint
%config(noreplace) %{_sysconfdir}/xdg/rpmlint/*.toml
%{_bindir}/rpmdiff
%{_bindir}/rpmlint

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.0-3
- Prepare for Oreon 11 (RP1)
