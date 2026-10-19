%global source0_hash 547274fa6b0a561ccf549cc9524b999a578e737d015d8709d021f9d0d13bea47
Name:           python-typing-inspection
Version:        0.4.4
Release:        1%{?dist}
Summary:        Runtime typing introspection tools
License:        MIT
URL:            https://github.com/pydantic/typing-inspection
Source0:        https://files.pythonhosted.org/packages/source/t/typing_inspection/typing_inspection-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-typing-inspection = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-typing-inspection
Summary:        Runtime typing introspection tools
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.15.0
# /oreon:reqs
%description -n python3-typing-inspection

%prep
%global oreon_srcdir typing_inspection-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-typing-inspection usr/lib/python3*/site-packages/typing_inspection* usr/lib64/python3*/site-packages/typing_inspection* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/typing_inspection* usr/lib64/python3*/site-packages/typing_inspection* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-typing-inspection -f %{oreon_filedir}/python3-typing-inspection.list

%changelog

%autochangelog
