%global source0_hash f44ded591f68969019ae5a21fddc6c233b73d8f2497d126b3d4cccbe9b8b149d
Name:           python-jenkins-job-builder
Version:        6.5.0
Release:        1%{?dist}
Summary:        Manage Jenkins jobs with YAML
License:        ...
URL:            https://jenkins-job-builder.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/j/jenkins_job_builder/jenkins_job_builder-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 1.8
BuildRequires:  python3dist(setuptools) < 81
Requires:       python3-jenkins-job-builder = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jenkins-job-builder
Summary:        Manage Jenkins jobs with YAML
%description -n python3-jenkins-job-builder

%prep
%global oreon_srcdir jenkins_job_builder-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jenkins-job-builder usr/lib/python3*/site-packages/jenkins_job_builder* usr/lib64/python3*/site-packages/jenkins_job_builder* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jenkins_job_builder* usr/lib64/python3*/site-packages/jenkins_job_builder* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jenkins-job-builder -f %{oreon_filedir}/python3-jenkins-job-builder.list

%changelog

%autochangelog
