%global source0_hash 24e11b5e8b875ca6bb438a34e1181f53f82be23bdc5dad4b58aa4065644ccaad
Name:           shybrid
Version:        0.4.3
Release:        1%{?dist}
Summary:        GUI for generating hybrid ground-truth spiking data
License:        GPL-3.0-or-later
URL:            https://github.com/jwouters91/shybrid
Source0:        https://files.pythonhosted.org/packages/source/s/shybrid/shybrid-%{version}.tar.gz
Source1:        shybrid.desktop
Patch:          %{url}/pull/13.patch
BuildArch:      noarch 
Requires:       python3-matplotlib-qt5
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-shybrid = %{version}-%{release}
# /oreon:deps
%description
SHYBRID is a graphical user interface that allows for the easy creation of
hybrid ground truth extracellular recordings.

%prep

%autosetup -p1
# Do not pin an exact version of PyQt5
sed -r -i 's/(PyQt5)==/\1>=/' setup.py
# These also have unnecesary shebangs, and were not included in PR#13
find examples -type f -name '*.py' -exec sed -r -i '1{/^#!/d}' '{}' '+'

%install
%pyproject_install
desktop-file-install \
    --dir='%{buildroot}%{_datadir}/applications' \
    '%{SOURCE1}'
%oreon_autofiles main

%build

%pyproject_wheel
%files

%changelog

%autochangelog
