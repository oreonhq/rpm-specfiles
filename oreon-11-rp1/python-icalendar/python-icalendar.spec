%global source0_hash 7bd001c8e648205e1bde5c6a5b77096598e8d0893dcf57755c6c597635620132
Name:           python-icalendar
Version:        7.3.0
Release:        1%{?dist}
Summary:        RFC 5545 compatible parser and generator of iCalendar files
License:        BSD-2-Clause
URL:            https://icalendar.readthedocs.io/en/stable/
Source0:        https://files.pythonhosted.org/packages/source/i/icalendar/icalendar-%{version}.tar.gz
BuildArch:      noarch
Patch0:         hatch.patch
Patch1:         tzdata.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-icalendar = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-icalendar
Summary:        RFC 5545 compatible parser and generator of iCalendar files
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.10
Requires:       python3dist(tzdata) >= 2025.3
# /oreon:reqs
%description -n python3-icalendar

%prep
%global oreon_srcdir icalendar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-icalendar usr/lib/python3*/site-packages/icalendar* usr/lib64/python3*/site-packages/icalendar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/icalendar* usr/lib64/python3*/site-packages/icalendar* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-icalendar -f %{oreon_filedir}/python3-icalendar.list

%changelog

%autochangelog
