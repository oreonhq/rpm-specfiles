%global source0_hash 85c6e15d1cc3a03996725419645d9de2c4d2c37057e7ecc4907b8e4b5ee24b4b
Name:           fastapi-cloud-cli
Version:        0.26.0
Release:        1%{?dist}
Summary:        Deploy and manage FastAPI Cloud apps from the command line
License:        MIT
URL:            https://github.com/fastapilabs/fastapi-cloud-cli
Source0:        https://github.com/fastapilabs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source100:      fastapi-cloud.1
Source110:      fastapi-cloud-deploy.1
Source120:      fastapi-cloud-link.1
Source130:      fastapi-cloud-login.1
Source140:      fastapi-cloud-logs.1
Source150:      fastapi-cloud-logout.1
Source160:      fastapi-cloud-whoami.1
Source170:      fastapi-cloud-unlink.1
Source180:      fastapi-cloud-setup-ci.1
Source190:      fastapi-cloud-env.1
Source191:      fastapi-cloud-env-list.1
Source192:      fastapi-cloud-env-set.1
Source193:      fastapi-cloud-env-delete.1
Patch:          0001-Downstream-only-patch-out-coverage-from-script-test.patch
BuildArch:      noarch
%py_provides python3-fastapi-cloud-cli
Requires:       gh
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fastapi-cloud-cli = %{version}-%{release}
# /oreon:deps
%package -n       python3-fastapi-cloud-cli+standard
Summary:        Metapackage for python3-fastapi-cloud-cli standard extras
Requires:       python3-fastapi-cloud-cli = %{version}-%{release}
Requires:       python3dist(uvicorn[standard]) >= 0.15.0
Provides:       python3dist(fastapi-cloud-cli[standard]) = %{version}-%{release}

%description -n python3-fastapi-cloud-cli+standard
Metapackage for python3-fastapi-cloud-cli standard extras.

%description
%{summary}.

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE100}' '%{SOURCE110}' '%{SOURCE120}' '%{SOURCE130}' \
    '%{SOURCE140}' '%{SOURCE150}' '%{SOURCE160}' '%{SOURCE170}' \
    '%{SOURCE180}' '%{SOURCE190}' '%{SOURCE191}' '%{SOURCE192}' \
    '%{SOURCE193}'
%oreon_autofiles main

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%pytest -v
%files

%changelog

%autochangelog
