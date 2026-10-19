%global source0_hash bab404ad42fb37f943107da2f6003ffc79724d11cc95076a7a539513371779da
Name:           python-ua-parser
Version:        1.0.2
Release:        1%{?dist}
Summary:        Python port of Browserscope_s user agent parser
License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-python
Source0:        https://files.pythonhosted.org/packages/source/u/ua_parser/ua_parser-%{version}.tar.gz
BuildArch:      noarch
Patch0:         ua_parser-no-ua_parse_rs.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ua-parser = %{version}-%{release}
# /oreon:deps
%package -n       python3-ua-parser+yaml
Summary:        Metapackage for python3-ua-parser yaml extras
Requires:       python3-ua-parser = %{version}-%{release}
Provides:       python3dist(ua-parser[yaml]) = %{version}-%{release}

%description -n python3-ua-parser+yaml
Metapackage for python3-ua-parser yaml extras.

%package -n       python3-ua-parser+re2
Summary:        Metapackage for python3-ua-parser re2 extras
Requires:       python3-ua-parser = %{version}-%{release}
Provides:       python3dist(ua-parser[re2]) = %{version}-%{release}

%description -n python3-ua-parser+re2
Metapackage for python3-ua-parser re2 extras.

%package -n       python3-ua-parser+regex
Summary:        Metapackage for python3-ua-parser regex extras
Requires:       python3-ua-parser = %{version}-%{release}
Provides:       python3dist(ua-parser[regex]) = %{version}-%{release}

%description -n python3-ua-parser+regex
Metapackage for python3-ua-parser regex extras.

%description

%package -n     python3-ua-parser
Summary:        Python port of Browserscope_s user agent parser
%description -n python3-ua-parser

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ua_parser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ua-parser usr/lib/python3*/site-packages/ua_parser* usr/lib64/python3*/site-packages/ua_parser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ua_parser* usr/lib64/python3*/site-packages/ua_parser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ua-parser -f %{oreon_filedir}/python3-ua-parser.list

%changelog

%autochangelog
