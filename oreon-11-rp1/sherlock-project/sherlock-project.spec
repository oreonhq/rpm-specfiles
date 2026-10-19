%global source0_hash 5888c02c0fb79caf3e1612c8ee2deef59ca9797f6fffa8e597cf094af9e74b10
Name:           sherlock-project
Version:        0.16.2
Release:        1%{?dist}
Summary:        Hunt down social media accounts by username across social networks
License:        MIT
URL:            https://github.com/sherlock-project/sherlock
Source0:        https://github.com/%{name}/sherlock/archive/v%{version}/sherlock-%{version}.tar.gz
Patch0:         0001-Remove-tor.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.2.0
Requires:       python3-sherlock-project = %{version}-%{release}
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sherlock-%{version}
sed -i '/torrequest/d' 'pyproject.toml' # Pending upstream removal

%build

sherlock_version=$(sed -n 's/^__version__ *= *"\([0-9.]*\)"/\1/p' sherlock_project/__init__.py)
sed -r -i "s/^version *= .*?$/version = \"$sherlock_version\"/" pyproject.toml
%pyproject_wheel
%install
%pyproject_install
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/sherlock_project/__main__.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/sherlock_project/sherlock.py'
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info \
    --version-string='%{version}' \
    --name='%{summary}' \
    --output='%{buildroot}%{_mandir}/man1/sherlock.1' \
    '%{buildroot}%{_bindir}/sherlock'
%oreon_autofiles main

%check

%tox -e offline
%files

%changelog

%autochangelog
