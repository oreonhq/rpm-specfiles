%global source0_hash c83e73c581427af92a0a67da0178386c91cfb93706f1a3f3e3cd41ee03435d80
Name:           python-sport-activities-features
Version:        0.5.4
Release:        1%{?dist}
Summary:        A minimalistic toolbox for extracting features from sport activity files
License:        MIT
URL:            https://github.com/firefly-cpp/sport-activities-features
Source0:        https://files.pythonhosted.org/packages/source/s/sport_activities_features/sport_activities_features-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-sport-activities-features = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sport-activities-features
Summary:        A minimalistic toolbox for extracting features from sport activity files
%description -n python3-sport-activities-features

%prep
%global oreon_srcdir sport_activities_features-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sport-activities-features usr/lib/python3*/site-packages/sport_activities_features* usr/lib64/python3*/site-packages/sport_activities_features* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sport_activities_features* usr/lib64/python3*/site-packages/sport_activities_features* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sport-activities-features -f %{oreon_filedir}/python3-sport-activities-features.list

%changelog

%autochangelog
