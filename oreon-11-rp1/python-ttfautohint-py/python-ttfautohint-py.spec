%global source0_hash 6f786db75d543716a8331ba3a6deeae19cf17701bd165aac05ff13b64e6614a3
%bcond tests 1
Name:           python-ttfautohint-py
Version:        0.6.1
Release:        1%{?dist}
Summary:        Python wrapper for ttfautohint, a free auto-hinter for TrueType fonts
License:        MIT
SourceLicense:  %{license} AND OFL-1.1
URL:            https://github.com/fonttools/ttfautohint-py
Source0:        https://github.com/fonttools/ttfautohint-py/archive/v%{version}/ttfautohint-py-%{version}.tar.gz
BuildArch: noarch
%if %{with tests}
%endif
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  /usr/bin/ttfautohint
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description %{common_description}

%package -n python3-ttfautohint-py
Summary:        Python wrapper for ttfautohint, a free auto-hinter for TrueType fonts
Requires:       /usr/bin/ttfautohint
%py_provides python3-ttfautohint
%description -n python3-ttfautohint-py %{common_description}

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%prep
%oreon_prep
%install
%pyproject_install
%oreon_autofiles python3-ttfautohint-py usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%pytest -v
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-ttfautohint-py -f %{oreon_filedir}/python3-ttfautohint-py.list

%changelog

%autochangelog
