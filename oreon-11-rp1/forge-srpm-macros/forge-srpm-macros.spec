%global source0_hash 467386263eb6f9140c9fcd88b7bb0b5709458133a17de9a584db21c1fdc15f00
%global debug_package %{nil}

Name: forge-srpm-macros
Version: 0.4.0
Release: 2%{?dist}
Summary: Macros for packaging code hosted on forges
License: GPL-1.0-or-later
URL: https://git.sr.ht/~gotmax23/forge-srpm-macros
BuildArch: noarch
Source0: macros.forge
Source1: forge.lua
Source2: _forge_util.lua
Source3: GPL-1.0-or-later.txt
Requires: oreon-rpm-config

BuildRequires: oreon-rpm-macros

%description
Macros that turn a forge tag into a source URL and an unpacked directory name.

%prep
%oreon_sha256
cp %{SOURCE3} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmluadir}/oreon/srpm
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.forge
install -m 644 %{SOURCE1} %{buildroot}%{_rpmluadir}/oreon/srpm/forge.lua
install -m 644 %{SOURCE2} %{buildroot}%{_rpmluadir}/oreon/srpm/_forge_util.lua

%files
%license GPL-1.0-or-later.txt
%{_rpmmacrodir}/macros.forge
%{_rpmluadir}/oreon/srpm/forge.lua
%{_rpmluadir}/oreon/srpm/_forge_util.lua
