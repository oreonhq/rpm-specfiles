Name:           python-varlink
Version:        31.0.0
Release:        18%{?dist}
Summary:        Python implementation of Varlink
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 3c1f0ef71d887717e890a195811569535991863fa21da0c23c176d58f1732ebe
%global source0_file python-varlink-31.0.0.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

%global _description \
An python module for Varlink with client and server support.

%description %_description

%package -n python3-varlink
Summary:       %summary
%{?python_provide:%python_provide python3-varlink}
# The varlink copr had this package under the "python-varlink"
# name. Add Obsoletes to make it easy to upgrade.
Obsoletes:     python-varlink <= 3-1.git.61.1bc637d.fc27

%description -n python3-varlink %_description

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/python-varlink-31.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3c1f0ef71d887717e890a195811569535991863fa21da0c23c176d58f1732ebe" || { echo "oreon: Source0 SHA256 mismatch for python-varlink-31.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n varlink-%{version}
# varlink also supports python-2.7 but python3 is required here
sed -i -e 's#env python#env python3#' varlink/tests/test_certification.py
# varlink also supports python-2.7 but python3 is required here
sed -i -e 's#env python#env python3#' varlink/tests/test_orgexamplemore.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
CFLAGS="%{optflags}" %{__python3} %{py_setup} %{?py_setup_args} check

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%files -n python3-varlink
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 31.0.0-18
- Import
