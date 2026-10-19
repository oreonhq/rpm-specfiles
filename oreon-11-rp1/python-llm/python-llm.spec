%global source0_hash 2ee0955b2e372408813ce966f3d03ad2c7419b85a547880c53797d31d3a3fdb6
Name:           python-llm
Version:        0.35
Release:        1%{?dist}
Summary:        CLI utility and Python library for interacting with Large Language Models from organizations like OpenAI, Anthropic and Gemini plus local models installed on your own machine.
License:        Apache-2.0
URL:            https://github.com/simonw/llm
Source0:        https://files.pythonhosted.org/packages/source/l/llm/llm-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-llm-0.28-relax-click.patch
Patch:          python-llm-0.27.1-disable-tests.patch
Patch:          python-llm-0.27.1-sqlite-3.51.patch
Patch:          https://github.com/simonw/llm/pull/1333.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-llm = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-llm
Summary:        CLI utility and Python library for interacting with Large Language Models from organizations like OpenAI, Anthropic and Gemini plus local models installed on your own machine.
# oreon:reqs
Requires:       python3dist(click-default-group) >= 1.2.3
Requires:       python3dist(condense-json) >= 1.1
Requires:       python3dist(openai) > 3
Requires:       python3dist(pydantic) >= 2.0.0
Requires:       python3dist(sqlite-utils) >= 4.0
# /oreon:reqs
%description -n python3-llm

%prep
%global oreon_srcdir llm-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-llm usr/lib/python3*/site-packages/llm* usr/lib64/python3*/site-packages/llm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/llm* usr/lib64/python3*/site-packages/llm* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-llm -f %{oreon_filedir}/python3-llm.list

%changelog

%autochangelog
