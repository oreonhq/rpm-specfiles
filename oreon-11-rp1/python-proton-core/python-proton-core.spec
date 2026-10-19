%global source0_hash 9837199b8fa35e1b29260f863e5bc8718f18eebab580a9ff1707319151ae51e7
%define unmangled_name proton-core
%define github_repo_name python-proton-core
Name: python-%{unmangled_name}
Version: 0.3.3
Release:        1%{?dist}
Summary:        proton-core library
License: GPL-3.0-or-later
URL:     https://github.com/ProtonVPN/%{github_repo_name}
Source0:        https://github.com/ProtonVPN/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-proton-core = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{unmangled_name}
Summary:        proton-core library
Conflicts: python3-proton-client
%description -n python3-%{unmangled_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{github_repo_name}-%{version}
# Do not measure test coverage
sed -i '/addopts = --cov=proton --cov-report html --cov-report term/d' setup.cfg 

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/proton_core* usr/lib64/python3*/site-packages/proton_core* usr/bin/*

%check

%pyproject_check_import
k="${k-}${k+ and }not (TestAlternativeRouting and test_alternative_routing_works_on_prod)"
k="${k-}${k+ and }not (TestAuto and test_auto_works_on_prod)"
k="${k-}${k+ and }not (TestProtonSSO and test_broken_data)"
k="${k-}${k+ and }not (TestProtonSSO and test_broken_index)"
k="${k-}${k+ and }not (TestProtonSSO and test_sessions)"
k="${k-}${k+ and }not (TestSession and test_ping)"
k="${k-}${k+ and }not (TestTLSValidation and test_successful)"
k="${k-}${k+ and }not (TestTLSValidation and test_without_pinning)"
k="${k-}${k+ and }not (TestTLSValidation and test_bad_pinning_fingerprint_changed)"
k="${k-}${k+ and }not (TestTLSValidation and test_bad_pinning_url_changed)"
%pytest -k "${k-}"
%files
%files -n python3-proton-core -f %{oreon_filedir}/python3-proton-core.list

%changelog

%autochangelog
