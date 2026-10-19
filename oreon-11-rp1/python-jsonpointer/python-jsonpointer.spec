%global source0_hash 0b801c7db33a904024f6004d526dcc53bbb8a4a0f4e32bfd10beadf60adf1900
Name:           python-jsonpointer
Version:        3.1.1
Release:        1%{?dist}
Summary:        Identify specific nodes in a JSON document _RFC 6901_
License:        ...
URL:            https://github.com/stefankoegl/python-json-pointer
Source0:        https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jsonpointer = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jsonpointer
Summary:        Identify specific nodes in a JSON document _RFC 6901_
%description -n python3-jsonpointer

%prep
%global oreon_srcdir jsonpointer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jsonpointer usr/lib/python3*/site-packages/jsonpointer* usr/lib64/python3*/site-packages/jsonpointer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jsonpointer* usr/lib64/python3*/site-packages/jsonpointer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jsonpointer -f %{oreon_filedir}/python3-jsonpointer.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4-9
- Prepare for Oreon 11 (RP1)
