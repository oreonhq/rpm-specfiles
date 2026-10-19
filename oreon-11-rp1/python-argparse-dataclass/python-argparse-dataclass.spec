%global source0_hash 4840dc5c793bfeea4864371f21a341dcf6592047755f558c1c2814c0724b4119
Name:           python-argparse-dataclass
Version:        2.0.0
Release:        1%{?dist}
Summary:        Declarative CLIs with argparse and dataclasses
License:        MIT
URL:            https://github.com/mivade/argparse_dataclass
Source0:        https://github.com/mivade/argparse_dataclass/archive/%{version}/argparse_dataclass-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-argparse-dataclass = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-argparse-dataclass
Summary:        Declarative CLIs with argparse and dataclasses
%description -n python3-argparse-dataclass %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-argparse-dataclass usr/lib/python3*/site-packages/argparse_dataclass* usr/lib64/python3*/site-packages/argparse_dataclass* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/argparse_dataclass* usr/lib64/python3*/site-packages/argparse_dataclass* usr/bin/*

%check

%pytest --doctest-modules -v
%files
%files -n python3-argparse-dataclass -f %{oreon_filedir}/python3-argparse-dataclass.list

%changelog

%autochangelog
