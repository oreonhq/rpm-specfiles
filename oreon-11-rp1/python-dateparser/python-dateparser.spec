%global source0_hash bab8c43a746266e68142f4926e69438ce551441aa88e54e78bb6410bf3ee7000
Name:           python-dateparser
Version:        1.4.3
Release:        1%{?dist}
Summary:        Date parsing library designed to parse dates from HTML pages
License:        BSD-3-Clause
URL:            https://github.com/scrapinghub/dateparser
Source0:        https://files.pythonhosted.org/packages/source/d/dateparser/dateparser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-dateparser = %{version}-%{release}
# /oreon:deps
%package -n       python3-dateparser+calendars
Summary:        Metapackage for python3-dateparser calendars extras
Requires:       python3-dateparser = %{version}-%{release}
Requires:       python3dist(convertdate) >= 2.2.1
Provides:       python3dist(dateparser[calendars]) = %{version}-%{release}

%description -n python3-dateparser+calendars
Metapackage for python3-dateparser calendars extras.

%package -n       python3-dateparser+langdetect
Summary:        Metapackage for python3-dateparser langdetect extras
Requires:       python3-dateparser = %{version}-%{release}
Requires:       python3dist(langdetect) >= 1.0.0
Provides:       python3dist(dateparser[langdetect]) = %{version}-%{release}

%description -n python3-dateparser+langdetect
Metapackage for python3-dateparser langdetect extras.

%description

%package -n     python3-dateparser
Summary:        Date parsing library designed to parse dates from HTML pages
# oreon:reqs
Requires:       python3dist(python-dateutil) >= 2.7.0
Requires:       python3dist(pytz) >= 2024.2
Requires:       python3dist(regex) >= 2024.9.11
Requires:       python3dist(tzlocal) >= 0.2
# /oreon:reqs
%description -n python3-dateparser

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir dateparser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dateparser usr/lib/python3*/site-packages/dateparser* usr/lib64/python3*/site-packages/dateparser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dateparser* usr/lib64/python3*/site-packages/dateparser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dateparser -f %{oreon_filedir}/python3-dateparser.list

%changelog

%autochangelog
