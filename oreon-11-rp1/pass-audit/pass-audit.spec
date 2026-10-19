%global source0_hash 570d93841346d94190bf93239783068db668f2f3228c982f746a9fa351e084af
Name: pass-audit
Version: 1.2
Release:        1%{?dist}
Summary:        A pass extension for auditing your password repository
%global pypkg pass_audit
%global common_name pass-audit
License: GPL-3.0-or-later
URL: https://github.com/roddhjav/%{name}
Source0:        https://github.com/roddhjav/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch: 0001-Install-data-files-from-the-Makefile.patch
Patch: 0001-remove-shebang-from-non-executable-__main__.py-file.patch
Requires: python3-%{name} = %{version}-%{release}
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pass-audit = %{version}-%{release}
# /oreon:deps
%description
`pass audit` is a password-store extension for auditing your password
repository. Passwords will be checked against the Python implementation of
Dropbox' zxcvbn algorithm and Troy Hunt's Have I Been Pwned Service. It supports
safe breached password detection from haveibeenpwned.com using a K-anonymity
method. Using this method, you do not need to (fully) trust the server that
stores the breached password. You should read the security consideration section
for more information.

%package -n python3-%{name}
Summary:        A pass extension for auditing your password repository
Requires: pass
%description -n python3-%{name}
`pass audit` python package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version} -p1

%build

%pyproject_wheel
%check

%pytest tests
%install
%pyproject_install
%make_install PYTHON=no
%oreon_autofiles main usr/lib/python3*/site-packages/pass_audit* usr/lib64/python3*/site-packages/pass_audit* usr/bin/*

%files
%files -n python3-pass-audit -f %{oreon_filedir}/python3-pass-audit.list

%changelog

%autochangelog
