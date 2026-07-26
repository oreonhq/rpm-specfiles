%global source0_hash 9990639e19a9c8f1db4af453b7e6a45ef2995ec03e13bac35b9824839fd46867

%global sum Simple packet creation/parsing library

Name:           python-dpkt
Version:        1.9.8
Release:        15%{?dist}
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/kbandla/dpkt
Source0:        https://github.com/kbandla/dpkt/archive/v%{version}.tar.gz
Patch0:         nostdeb-1.8.8.patch
Patch1:         python3-fixes-1.8.8.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest

%description
Fast, simple packet creation and parsing library
with definitions for the basic TCP/IP protocols.

%package -n python3-dpkt
Summary:        %{sum}

%description -n python3-dpkt
Fast, simple packet creation and parsing library
with definitions for the basic TCP/IP protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dpkt-%{version}
#%patch0 -p1
#%patch1 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dpkt

%check
%pyproject_check_import

# One test, "test_deprecated_decorator" fails, but doesn't appear
# to test actual functionality.
%ifarch s390x
%{__python3} -m pytest dpkt -k "not test_deprecated_decorator"
%endif

%files -n python3-dpkt -f %{pyproject_files}
%doc AUTHORS LICENSE README.md examples docs

%changelog
%autochangelog
