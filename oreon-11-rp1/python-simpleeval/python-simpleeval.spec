%global source0_hash b417f869c11f2de034eb919820a825f35d12ce99f63a43971947ce73679eb9ba
Name:           python-simpleeval
Version:        1.0.8
Release:        1%{?dist}
Summary:        A simple, safe single expression evaluator library.
License:        MIT
URL:            https://github.com/danthedeckie/simpleeval
Source0:        https://files.pythonhosted.org/packages/source/s/simpleeval/simpleeval-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-simpleeval = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-simpleeval
Summary:        A simple, safe single expression evaluator library.
%description -n python3-simpleeval

%prep
%global oreon_srcdir simpleeval-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-simpleeval usr/lib/python3*/site-packages/simpleeval* usr/lib64/python3*/site-packages/simpleeval* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/simpleeval* usr/lib64/python3*/site-packages/simpleeval* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-simpleeval -f %{oreon_filedir}/python3-simpleeval.list

%changelog

%autochangelog
