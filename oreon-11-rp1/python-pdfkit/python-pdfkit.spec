%global source0_hash 992f821e1e18fc8a0e701ecae24b51a2d598296a180caee0a24c0af181da02a9
Name:           python-pdfkit
Version:        1.0.0
Release:        1%{?dist}
Summary:        Wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt
License:        MIT
URL:            UNKNOWN
Source0:        https://files.pythonhosted.org/packages/source/p/pdfkit/pdfkit-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pdfkit = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pdfkit
Summary:        Wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt
%description -n python3-pdfkit

%prep
%global oreon_srcdir pdfkit-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pdfkit usr/lib/python3*/site-packages/pdfkit* usr/lib64/python3*/site-packages/pdfkit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pdfkit* usr/lib64/python3*/site-packages/pdfkit* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pdfkit -f %{oreon_filedir}/python3-pdfkit.list

%changelog

%autochangelog
