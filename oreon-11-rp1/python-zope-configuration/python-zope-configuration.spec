%global source0_hash 46c8ed338ff8b7fa3e9f218d65652a786d696f702b974c91cb7c12b872d7f004

%global modname zope.configuration

Name:           python-zope-configuration
Version:        5.0.1
Release:        10%{?dist}
Summary:        Zope Configuration Markup Language (ZCML)

License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.configuration
Source:         %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
The zope configuration system provides an extensible system for supporting
various kinds of configurations.

It is based on the idea of configuration directives. Users of the configuration
system provide configuration directives in some language that express
configuration choices. The intent is that the language be pluggable. An XML
language is provided by default.}
 
%description %_description

%package -n python3-zope-configuration
Summary:        %{summary}

%description -n python3-zope-configuration %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x docs,test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zope

%check
%{py3_test_envvars} zope-testrunner --test-path=src

%files -n python3-zope-configuration -f %{pyproject_files}
%license COPYRIGHT.txt
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{modname}-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
