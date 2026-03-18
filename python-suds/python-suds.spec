Name:           python-suds
Version:        1.2.0
Release:        7%{?dist}
Summary:        A python SOAP client

License:        LGPL-3.0-or-later
URL:            https://github.com/suds-community/suds
Source:         %{url}/archive/v%{version}.tar.gz#/suds-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
The suds project is a python soap web services client lib.  Suds leverages
python meta programming to provide an intuitive API for consuming web
services.  Objectification of types defined in the WSDL is provided
without class generation.  Programmers rarely need to read the WSDL since
services and WSDL based objects can be easily inspected.}

%description %_description

%package -n python3-suds
Summary:        %{summary}
%description -n python3-suds %_description

%prep
%autosetup -p1 -n suds-%{version}

%build
export SUDS_PACKAGE=suds
%pyproject_wheel

%generate_buildrequires
%pyproject_buildrequires

%install
%pyproject_install
%pyproject_save_files suds

%check
%pytest

%files -n python3-suds -f %{pyproject_files}
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-7
- Prepare for Oreon 11 (RP1)
