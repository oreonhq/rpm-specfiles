%global source0_hash 74552d1afcf779a84ca63527a1eaee9995c429ff422db15492bad0c3599cab4b
Name:           python-adafruit-platformdetect
Version:        3.89.1
Release:        1%{?dist}
Summary:        Platform detection for use by libraries like Adafruit-Blinka.
License:        MIT
URL:            https://github.com/adafruit/Adafruit_Python_PlatformDetect
Source0:        https://files.pythonhosted.org/packages/source/a/adafruit_platformdetect/adafruit_platformdetect-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-adafruit-platformdetect = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-adafruit-platformdetect
Summary:        Platform detection for use by libraries like Adafruit-Blinka.
%description -n python3-adafruit-platformdetect

%prep
%global oreon_srcdir adafruit_platformdetect-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-adafruit-platformdetect usr/lib/python3*/site-packages/adafruit_platformdetect* usr/lib64/python3*/site-packages/adafruit_platformdetect* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/adafruit_platformdetect* usr/lib64/python3*/site-packages/adafruit_platformdetect* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-adafruit-platformdetect -f %{oreon_filedir}/python3-adafruit-platformdetect.list

%changelog

%autochangelog
