%global source0_hash ea5a62f9c6a3127a6191901fa0cc32e23b05caf2034d7062193bd4c0539c7888
Name:           python-apkinspector
Version:        1.3.7
Release:        1%{?dist}
Summary:        apkInspector is a tool designed to provide detailed insights into the zip structure of APK files, offering the capability to extract content and decode the AndroidManifest.xml file.
License:        Apache-2.0
URL:            https://github.com/erev0s/apkInspector
Source0:        https://files.pythonhosted.org/packages/source/a/apkinspector/apkinspector-%{version}.tar.gz
BuildArch:      noarch
Patch:          doc.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-apkinspector = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-apkinspector
Summary:        apkInspector is a tool designed to provide detailed insights into the zip structure of APK files, offering the capability to extract content and decode the AndroidManifest.xml file.
%description -n python3-apkinspector

%prep
%global oreon_srcdir apkinspector-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-apkinspector usr/lib/python3*/site-packages/apkinspector* usr/lib64/python3*/site-packages/apkinspector* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/apkinspector* usr/lib64/python3*/site-packages/apkinspector* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-apkinspector -f %{oreon_filedir}/python3-apkinspector.list

%changelog

%autochangelog
