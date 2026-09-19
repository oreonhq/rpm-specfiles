%global source0_hash d5ad9eb6bbc9c2a3ae2ded11986ec9e7972529aac16d917abb0fbd53afc0d184

%global commit 88c53cd44a626ede3b07dab0b548f8bcfda42867
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          pycanberra
Summary:       A very basic (and incomplete) wrapper for libcanberra
URL:           https://github.com/psykoyiko/pycanberra/
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2

# There's no versioning upstream, it's all about the Git hash
Version:       0
Release:       0.45.git%{shortcommit}%{?dist}

# There aren't any release yet, I'm downloading straight from the last commit
Source0:       https://github.com/psykoyiko/pycanberra/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:     noarch

BuildRequires: python3-devel

# This will break at run time when libcanberra bumps its soname :(
Requires:      libcanberra

%description
A very basic (and incomplete) wrapper of libcanberra for Python 2.

%package -n python3-canberra
Summary:       A very basic (and incomplete) wrapper for libcanberra

%description -n python3-canberra
A very basic (and incomplete) wrapper of libcanberra for Python 3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pycanberra-%{commit}

%build
# Nothing to build

%install
install -D -p -m 0644 pycanberra.py -t %{buildroot}%{python3_sitelib}/

%files -n python3-canberra
%doc COPYING README
%{python3_sitelib}/pycanberra.py
%{python3_sitelib}/__pycache__/*

%changelog
%autochangelog
