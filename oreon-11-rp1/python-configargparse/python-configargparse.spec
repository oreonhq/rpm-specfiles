%global source0_hash 6a865cee66285d5a3a325e273b6164adca5c014d80ce1f07b809a45a7ef7000f
Name:           python-configargparse
Version:        1.7.7
Release:        1%{?dist}
Summary:        Replacement for argparse that allows options to be set via config files
License:        MIT
URL:            https://github.com/bw2/ConfigArgParse
Source0:        https://github.com/bw2/ConfigArgParse/archive/v%{version}/ConfigArgParse-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A drop-in replacement for argparse that allows options to also be set via
config files and/or environment variables.
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard-coded
defaults, and in some cases, environment variables.
Python’s command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.}
# oreon:deps
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-subtests)
# /oreon:deps
%description %{common_description}

%package -n python3-configargparse
Summary:        Replacement for argparse that allows options to be set via config files
%description -n python3-configargparse %{common_description}

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%prep
%oreon_prep
%install
%pyproject_install
%oreon_autofiles python3-configargparse usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v -rs
%files -f %{oreon_filedir}/main.list
%files -n python3-configargparse -f %{oreon_filedir}/python3-configargparse.list

%changelog

%autochangelog
