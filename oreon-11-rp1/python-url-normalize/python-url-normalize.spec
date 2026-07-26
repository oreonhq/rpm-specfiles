%global source0_hash 9803deb16a6ecd88075686c4445ff6c78986d3ae676a4cc6cc3e4d324bc45c56

%global srcname url-normalize

Name: python-%{srcname}
Version: 1.4.3
Release: 11%{?dist}
Summary: Python URI normalizator

License: MIT
Url: https://github.com/niksite/url-normalize
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/niksite/url-normalize/pull/28
Patch0:         https://github.com/niksite/url-normalize/pull/28.patch#/python-url-normalize-poetry-core.patch

BuildArch: noarch
BuildRequires: python3-devel
# needed for check
BuildRequires: python3dist(pytest)

%global _description %{expand:

URI Normalization function
 * Take care of IDN domains.
 * Always provide the URI scheme in lowercase characters.
 * Always provide the host, if any, in lowercase characters.
 * Only perform percent-encoding where it is essential.
 * Always use uppercase A-through-F characters when percent-encoding.
 * Prevent dot-segments appearing in non-relative URI paths.
 * For schemes that define a default authority, use an empty authority if the
   default is desired.
 * For schemes that define an empty path to be equivalent to a path of "/",
   use "/".
 * For schemes that define a port, use an empty port if the default is desired
 * All portions of the URI must be utf-8 encoded NFC from Unicode strings

Inspired by Sam Ruby's urlnorm.py:
    http://intertwingly.net/blog/2004/08/04/Urlnorm
This fork author: Nikolay Panov (<pythonista@npanov.com>)
}

%description %_description

%generate_buildrequires
%pyproject_buildrequires

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{srcname}-%{version}

# supplied tox.ini causes check to fail, will use pytest instead
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files url_normalize

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
