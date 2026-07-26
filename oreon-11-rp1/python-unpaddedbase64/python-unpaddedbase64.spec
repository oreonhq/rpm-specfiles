%global source0_hash 8f3aeae62aad49ee385c15c37bb64b625c96bb85a820aeab149c21970843ba68

%bcond check 0

%global modname unpaddedbase64

Name:           python-%{modname}
Version:        2.1.0
Release:        18%{?dist}
Summary:        Encode and decode Base64 without "=" padding

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/matrix-org/python-unpaddedbase64
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes\
using "=" characters. However this conveys no benefit so many protocols\
choose to use Base64 without the "=" padding.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with check}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%if %{with check}
%check
# https://github.com/matrix-org/python-unpaddedbase64/blob/master/.github/workflows/continuous-integration.yml#L48
%{python3} -m unittest
%endif

%files -n python3-%{modname}  -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
