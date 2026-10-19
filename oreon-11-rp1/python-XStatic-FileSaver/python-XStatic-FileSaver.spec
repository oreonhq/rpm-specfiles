%global source0_hash 106f3f034659473e5427849866e3cab548f7c4aefe95f121512e039463254846
Name:           python-xstatic-filesaver
Version:        1.3.2.1
Release:        1%{?dist}
Summary:        FileSaver 1.3.2 _XStatic packaging standard_
License:        MIT
URL:            https://github.com/eligrey/FileSaver.js
Source0:        https://files.pythonhosted.org/packages/source/x/xstatic_filesaver/xstatic_filesaver-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xstatic-filesaver = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xstatic-filesaver
Summary:        FileSaver 1.3.2 _XStatic packaging standard_
%description -n python3-xstatic-filesaver

%prep
%global oreon_srcdir xstatic_filesaver-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xstatic-filesaver usr/lib/python3*/site-packages/xstatic_filesaver* usr/lib64/python3*/site-packages/xstatic_filesaver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xstatic_filesaver* usr/lib64/python3*/site-packages/xstatic_filesaver* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xstatic-filesaver -f %{oreon_filedir}/python3-xstatic-filesaver.list

%changelog

%autochangelog
