%global source0_hash 22e5eb9a940bf407bcf30410ecc3708f3c56cc44b29c34e1726fe85006935f41

%{?python_enable_dependency_generator}
%global pkg_name flask-mail
%global mod_name Flask-Mail

Name:       python-%{pkg_name}
Version:    0.9.1
Release:    32%{?dist}
Summary:    Flask extension for sending email
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://github.com/mattupstate/%{pkg_name}/
Source0:    %{pypi_source %{mod_name}}
BuildArch:  noarch

%description
A Flask extension for sending email messages.

%package -n python3-%{pkg_name}
Summary:    Flask extension for sending email
BuildRequires:   python3-devel
BuildRequires:   python3-setuptools
BuildRequires:   python3-flask

%description -n python3-%{pkg_name}
A Flask extension for sending email messages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{mod_name}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/flask_mail.py
%{python3_sitelib}/__pycache__/flask_mail*.py*
%{python3_sitelib}/Flask_Mail*.egg-info/

%changelog
%autochangelog
