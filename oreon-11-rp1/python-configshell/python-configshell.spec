# Copyright 2011, Red Hat
%global oname configshell-fb

Name:           python-configshell
License:        Apache-2.0
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        2.0.2
Release:        5%{?dist}
URL:            https://github.com/open-iscsi/configshell-fb
Source:        https://github.com/open-iscsi/configshell-fb/archive/v2.0.2/configshell-fb-2.0.2.tar.gz
# oreon url source checksums begin
%global source0_sha256 24929305fe4983626ce06ea1c9e3370048c7010c37de67670a0719835130d3f6
%global source0_file configshell-fb-2.0.2.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/configshell-fb-2.0.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "24929305fe4983626ce06ea1c9e3370048c7010c37de67670a0719835130d3f6" || { echo "oreon: Source0 SHA256 mismatch for configshell-fb-2.0.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
