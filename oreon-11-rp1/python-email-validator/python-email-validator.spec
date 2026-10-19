%global source0_hash 578564e92e66874bfb6c7506b4b33e7abd79f0e9b99dedd979d03fcd5fc4f039
Name:           python-email-validator
Version:        2.3.0
Release:        1%{?dist}
Summary:        A robust email syntax and deliverability validation library
License:        Unlicense
URL:            https://github.com/JoshData/python-email-validator
Source0:        https://github.com/JoshData/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        email_validator.1
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-email-validator = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-email-validator
Summary:        A robust email syntax and deliverability validation library
%description -n python3-email-validator

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'
%oreon_autofiles python3-email-validator usr/lib/python3*/site-packages/email_validator* usr/lib64/python3*/site-packages/email_validator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/email_validator* usr/lib64/python3*/site-packages/email_validator* usr/bin/*

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%pytest -v tests -m 'not network'
%files
%files -n python3-email-validator -f %{oreon_filedir}/python3-email-validator.list

%changelog

%autochangelog
