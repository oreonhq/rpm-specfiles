%global source0_hash 5e4efc8c9ef2a50220fb627066e4b698482643070ab2a51e020bd85957595271

%global srcname zxcvbn-python

Name: python-zxcvbn
Summary: Realistic password strength estimator python module
Version: 4.5.0
Release: %autorelease
License: MIT
URL: https://github.com/dwolfhub/zxcvbn-python
Source: https://github.com/dwolfhub/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel

%global _description %{expand:
A realistic password strength estimator.

This is a Python implementation of the library created by the team at Dropbox.
The original library was written for JavaScript.

Accepts user data to be added to the dictionaries that are tested against
(name, birthdate, etc).  Gives a score to the password, from 0 (terrible)
to 4 (great). It provides feedback on the password and ways to improve it
and returns time estimates on how long it would take to guess the password
in different situations.}
%description %_description

%package -n python3-zxcvbn
Summary: Realistic password strength estimator python3 module

%description -n python3-zxcvbn %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zxcvbn

%check
%tox

%files -n python3-zxcvbn  -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/zxcvbn

%changelog
%autochangelog
