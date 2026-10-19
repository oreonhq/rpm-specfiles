%global source0_hash 4c042a3d39c9af4fa24497da76697fb4fff7abe6af04bcf55f099e0c23bc2c67
Name:           python-persist-queue
Version:        1.1.0
Release:        1%{?dist}
Summary:        A thread-safe disk based persistent queue in Python.
License:        ...
URL:            http://github.com/peter-wangxu/persist-queue
Source0:        https://files.pythonhosted.org/packages/source/p/persist_queue/persist_queue-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-persist-queue = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-persist-queue
Summary:        A thread-safe disk based persistent queue in Python.
%description -n python3-persist-queue

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir persist_queue-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-persist-queue usr/lib/python3*/site-packages/persist_queue* usr/lib64/python3*/site-packages/persist_queue* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/persist_queue* usr/lib64/python3*/site-packages/persist_queue* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-persist-queue -f %{oreon_filedir}/python3-persist-queue.list

%changelog

%autochangelog
