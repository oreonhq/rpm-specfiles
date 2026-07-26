%global source0_hash 24e11b5e8b875ca6bb438a34e1181f53f82be23bdc5dad4b58aa4065644ccaad

Name:           shybrid
Version:        0.4.3
Release:        %autorelease
Summary:        GUI for generating hybrid ground-truth spiking data

License:        GPL-3.0-or-later
URL:            https://github.com/jwouters91/shybrid
Source0:        %{pypi_source shybrid}
Source1:        shybrid.desktop

# Remove useless or unused shebang lines
# https://github.com/jwouters91/shybrid/pull/13
Patch:          %{url}/pull/13.patch

BuildArch:      noarch 

BuildSystem:            pyproject
BuildOption(install):   -l hybridizer

BuildRequires:  python3-matplotlib-qt5
Requires:       python3-matplotlib-qt5

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
SHYBRID is a graphical user interface that allows for the easy creation of
hybrid ground truth extracellular recordings.

%prep -a
# Do not pin an exact version of PyQt5
sed -r -i 's/(PyQt5)==/\1>=/' setup.py
# These also have unnecesary shebangs, and were not included in PR#13
find examples -type f -name '*.py' -exec sed -r -i '1{/^#!/d}' '{}' '+'

%install -a
desktop-file-install \
    --dir='%{buildroot}%{_datadir}/applications' \
    '%{SOURCE1}'

%files -f %{pyproject_files}
%doc README.md
%doc examples/

%{_bindir}/shybrid
%{_datadir}/applications/shybrid.desktop

%changelog
%autochangelog
