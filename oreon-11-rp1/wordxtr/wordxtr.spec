%global source0_hash d4b9af814639370dc862715bf3aea1475d8375ce5dfa45fe46e58c82347e6382

Name:           wordxtr
Version:        2.0.0
Release:        11%{?dist}
Summary:        Create hunspell dictionary from given plain text input data files

License:        GPL-2.0-or-later
URL:            https://pagure.io/wordxtr	
Source0:        http://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros

## we need wordlist2hunspell which is provided by hunspell-devel
Requires:       hunspell-devel

%description
This package will help you to create hunspell dictionary for given 
input language and plain text unicode data files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wordxtr

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/wordxtr

%changelog
%autochangelog
