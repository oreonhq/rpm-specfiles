%global source0_hash 78ce070a0c7b89824eef97ee79773681832bfc1b2eb7737845d7eb0d97dec730
Name:           python-noggin-messages
Version:        1.1.0
Release:        1%{?dist}
Summary:        Fedora Messaging message schemas for Noggin.
License:        MIT
URL:            https://github.com/fedora-infra/noggin-messages
Source0:        https://files.pythonhosted.org/packages/source/n/noggin_messages/noggin_messages-%{version}.tar.gz
BuildArch:      noarch
Patch1001:      0001-Revert-Include-additional-files-in-the-sdist.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-noggin-messages = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-noggin-messages
Summary:        Fedora Messaging message schemas for Noggin.
%description -n python3-noggin-messages

%prep
%global oreon_srcdir noggin_messages-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-noggin-messages usr/lib/python3*/site-packages/noggin_messages* usr/lib64/python3*/site-packages/noggin_messages* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/noggin_messages* usr/lib64/python3*/site-packages/noggin_messages* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-noggin-messages -f %{oreon_filedir}/python3-noggin-messages.list

%changelog

%autochangelog
