%global source0_hash d7c24ac421d42db55fb25345f077e7fd223167ee7b82d35e48cefbfb5bd2921d

%global pkg_name ua-parser
%global uap_core_version d668d6c6157db7737edfc0280adc6610c1b88029
%global run_unittests 0

Name:           python-%{pkg_name}
Version:        1.0.1
Release:        6%{?dist}
Summary:        Python port of Browserscope's user agent parser

License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-python
BuildArch:      noarch
Source0:        %{pypi_source ua_parser}
%if 0%{?run_unittests}
Source1:        https://github.com/ua-parser/uap-core/archive/%{uap_core_version}/uap-core-%{uap_core_version}.tar.gz
%endif

# ua_parser_rs resolver is currently not packaged for Fedora
Patch0:         ua_parser-no-ua_parse_rs.patch

Suggests:       python3-re2

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-re2

%description
Python port of Browserscope's user agent parser.

%package -n python3-%{pkg_name}
Summary:        Python port of Browserscope's user agent parser

%description -n python3-%{pkg_name}
Python port of Browserscope's user agent parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ua_parser-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ua_parser

%check
%pyproject_check_import
%if 0%{?run_unittests}
tar xf %{SOURCE1} --transform 's|uap-core-%{uap_core_version}|uap-core|'
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} ua_parser/user_agent_parser_test.py
%endif

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
