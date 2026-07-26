%global source0_hash d8d3efac1396e61d8a3a5e8b39b2015c8742fddd96b76689ab898062022d72b0

Version:        0.8.1

%global forgeurl https://github.com/OpenTTD/nml
%global tag      %{version}
%forgemeta

Name:           nml
Release:        %autorelease
Summary:        NewGRF Meta Language compiler

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc
BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description
A tool to compile nml files to grf or nfo files, making newgrf coding easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
# fixup version info
echo 'version = "%{version}"' > nml/__version__.py
rm nml/version_update.py

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nml nml_lz77

gzip docs/nmlc.1
install -Dpm 644 docs/nmlc.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/nmlc.1.gz
rm docs/nmlc.1.gz

 
%files -f %{pyproject_files}
%doc docs/changelog.txt
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1.gz

%changelog
%autochangelog
