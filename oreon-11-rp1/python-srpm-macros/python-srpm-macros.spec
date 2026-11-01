%global source0_hash 62195cc0cf614d540d2dff813dab14d2a2cede9ac69e1cbc4aa2a764980fc09c
%global debug_package %{nil}

Name: python-srpm-macros
Version: 3.15
Release: 2%{?dist}
Summary: SRPM macros for Python packages
License: MIT
URL: https://www.python.org/
BuildArch: noarch
Source0: macros.python-srpm
Source1: compileall2.py
Source2: clamp_source_mtime.py
Source3: brp-python-bytecompile
Source4: brp-python-hardlink
Source5: brp-python-rpm-in-distinfo
Source6: brp-fix-pyc-reproducibility
Source7: python.lua
Requires: oreon-rpm-config
Provides: bundled(python3dist(compileall2)) = 0.8.0

BuildRequires: oreon-rpm-macros

%description
SRPM macros and the bytecompile scripts Python source packages use.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}
mkdir -p %{buildroot}%{_rpmluadir}/oreon/srpm
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.python-srpm
install -m 644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/compileall2.py
install -m 644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/clamp_source_mtime.py
install -m 755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/brp-python-bytecompile
install -m 755 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/brp-python-hardlink
install -m 755 %{SOURCE5} %{buildroot}%{_rpmconfigdir}/brp-python-rpm-in-distinfo
install -m 755 %{SOURCE6} %{buildroot}%{_rpmconfigdir}/brp-fix-pyc-reproducibility
install -m 644 %{SOURCE7} %{buildroot}%{_rpmluadir}/oreon/srpm/python.lua

%files
%{_rpmmacrodir}/macros.python-srpm
%{_rpmconfigdir}/compileall2.py
%{_rpmconfigdir}/clamp_source_mtime.py
%{_rpmconfigdir}/brp-python-bytecompile
%{_rpmconfigdir}/brp-python-hardlink
%{_rpmconfigdir}/brp-python-rpm-in-distinfo
%{_rpmconfigdir}/brp-fix-pyc-reproducibility
%{_rpmluadir}/oreon/srpm/python.lua
