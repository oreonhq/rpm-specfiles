%global source0_hash 24929305fe4983626ce06ea1c9e3370048c7010c37de67670a0719835130d3f6

# Copyright 2011, Red Hat
%global oname configshell-fb

Name:           python-configshell
License:        Apache-2.0
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        2.0.3
Release:        1%{?dist}
URL:            https://github.com/open-iscsi/configshell-fb
Source:        https://github.com/open-iscsi/configshell-fb/archive/refs/tags/v2.0.2.tar.gz#/configshell-fb-2.0.2.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
A framework to implement simple but nice configuration-oriented\
command-line interfaces.

%description %_description

%package -n python3-configshell
Summary:        A framework to implement simple but nice CLIs

%description -n python3-configshell %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{oname}-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l 'configshell*'

%check
%pyproject_check_import

%files -n python3-configshell -f %{pyproject_files}
%doc COPYING README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.2-5
- Prepare for Oreon 11 (RP1)
