%global source0_hash bb700599c721f49a437bf6ee03b0f9cc729752646873985c94b4affaf88f113c
Name:           python-twilio
Version:        9.11.1
Release:        1%{?dist}
Summary:        Twilio API client and TwiML generator
License:        MIT
URL:            https://github.com/twilio/twilio-python/
Source0:        https://files.pythonhosted.org/packages/source/t/twilio/twilio-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-twilio-rm-python-mock-usage.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-twilio = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-twilio
Summary:        Twilio API client and TwiML generator
%description -n python3-twilio

%prep
%global oreon_srcdir twilio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-twilio usr/lib/python3*/site-packages/twilio* usr/lib64/python3*/site-packages/twilio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/twilio* usr/lib64/python3*/site-packages/twilio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-twilio -f %{oreon_filedir}/python3-twilio.list

%changelog

%autochangelog
