%global source0_hash c68668a3047fe4910aa8dc971210a614e0373eb4e8f53f7d14b2d8271e463c47
Name:           python-pyqt-feedback-flow
Version:        0.3.6
Release:        1%{?dist}
Summary:        Show feedback in toast-like notifications
License:        ...
URL:            https://github.com/firefly-cpp/pyqt-feedback-flow
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt_feedback_flow/pyqt_feedback_flow-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-pyqt-feedback-flow = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyqt-feedback-flow
Summary:        Show feedback in toast-like notifications
%description -n python3-pyqt-feedback-flow

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyqt_feedback_flow-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyqt-feedback-flow usr/lib/python3*/site-packages/pyqt_feedback_flow* usr/lib64/python3*/site-packages/pyqt_feedback_flow* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyqt_feedback_flow* usr/lib64/python3*/site-packages/pyqt_feedback_flow* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyqt-feedback-flow -f %{oreon_filedir}/python3-pyqt-feedback-flow.list

%changelog

%autochangelog
