%global source0_hash a9c92234d23cab8e38cb13f40279d78cf70a15c25a7b00fc3aa25e77fd77d45b
Name:           python-xstatic-json2yaml
Version:        0.1.1.1
Release:        1%{?dist}
Summary:        Json2yaml 0.1.1 _XStatic packaging standard_
License:        MIT
URL:            https://github.com/jeffsu/json2yaml
Source0:        https://files.pythonhosted.org/packages/source/x/xstatic_json2yaml/xstatic_json2yaml-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xstatic-json2yaml = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xstatic-json2yaml
Summary:        Json2yaml 0.1.1 _XStatic packaging standard_
%description -n python3-xstatic-json2yaml

%prep
%global oreon_srcdir xstatic_json2yaml-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xstatic-json2yaml usr/lib/python3*/site-packages/xstatic_json2yaml* usr/lib64/python3*/site-packages/xstatic_json2yaml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xstatic_json2yaml* usr/lib64/python3*/site-packages/xstatic_json2yaml* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xstatic-json2yaml -f %{oreon_filedir}/python3-xstatic-json2yaml.list

%changelog

%autochangelog
